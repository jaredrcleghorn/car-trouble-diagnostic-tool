import json

class BayesNetNode:
    def __init__(self, variable):
        self.variable = variable['name']

        if 'parents' in variable:
            self.parents = variable['parents']
            self.cpt = {}

            for key, value in variable['probability'].items():
                self.cpt[tuple(True if c == 'T' else False for c in key)] = value
        else:
            self.parents = []
            self.cpt = {(): variable['probability']}

    def probability(self, value, event):
        probability_true = self.cpt[tuple([event[parent] for parent in self.parents])]
        return probability_true if value else 1 - probability_true

class BayesNet:
    def __init__(self, variables=[]):
        self.nodes = [BayesNetNode(variable) for variable in variables]

    def probability(self, event, index=0):
        if not self.nodes[index:]:
            return 1.0

        node = self.nodes[index]
        variable = node.variable

        if variable in event:
            return node.probability(event[variable], event) * self.probability(event, index + 1)
        else:
            return sum(node.probability(value, event) * self.probability({**event, variable: value}, index + 1) for value in [True, False])

with open('variables.json') as f:
    variables = json.load(f)

bayes_net = BayesNet(variables)
variable_map = {variable['abbreviation']: variable['name'] for variable in variables}
hypothesis = input('Hypothesis: ')
event = {}

for abbreviation_value_string in hypothesis.strip().split(','):
    abbreviation_value = abbreviation_value_string.split('=')

    if len(abbreviation_value) == 2:
        abbreviation, value = [s.strip() for s in abbreviation_value]

        if abbreviation in variable_map:
            variable = variable_map[abbreviation]
            value = True if value == 'true' else False if value == 'false' else None

            if isinstance(value, bool):
                event[variable] = value
                continue

    print('error: invalid hypothesis')
    exit()

print(bayes_net.probability(event))

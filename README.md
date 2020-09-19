# car-trouble-diagnostic-tool

A tool that uses a simple Bayes net to diagnose car trouble

## `variables.json`

The `variables.json` file describes the variables. Each variable's `probability` is specified according to the order of the variable's `parents`, so for `Starts`, whose parents are `["Ignition", "StarterMotor", "Gas"]`, the property `probability["TTF"]` is the probability that `Starts` is true given that `Ignition` is true, `StarterMotor` is true, and `Gas` is false, while `probability["TFT"]` is the probability that `Starts` is true given that `Ignition` is true, `StarterMotor` is false, and `Gas` is true.

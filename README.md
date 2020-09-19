# car-trouble-diagnostic-tool

A tool that uses a simple Bayes net to diagnose car trouble

## `variables.json`

The `variables.json` file describes the variables. Each variable's `probability` is specified according to the order of the variable's `parents`, so for `Starts`, whose parents are `["Ignition", "StarterMotor", "Gas"]`, the property `probability["TTF"]` is the probability that `Starts` is true given that `Ignition` is true, `StarterMotor` is true, and `Gas` is false, while `probability["TFT"]` is the probability that `Starts` is true given that `Ignition` is true, `StarterMotor` is false, and `Gas` is true.

## Usage

To start the script, run

```shell
python3 cartroublediagnostictool.py
```

## Sources

The Bayes net code in this repository is based on the Bayes net code in the [aimacode/aima-python](https://github.com/aimacode/aima-python/blob/master/probability4e.py) repository.

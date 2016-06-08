# correlationLocFeatures

A module to calculate correlations between lines of code per language and
features per language.

This is the readme file for our *main* module correlationLocFeatures.
We also implemented the following modules, which are used to distribute the
work necessary for this module. README files for these modules are also available:
* featuresPerContribution (https://github.com/alexsr/101worker/tree/master/modules/featuresPerContribution)
* locPerLanguagePerContribution (https://github.com/alexsr/101worker/tree/master/modules/locPerLanguagePerContribution)
* programmingLanguagePerContribution (https://github.com/alexsr/101worker/tree/master/modules/programmingLanguagePerContribution)

The motivation to distribute the work into different modules was both to create useful information for others to use in the future and to have a clearer structure in this main module.

## Details

The module generates a "correlationLocFeatures.json" dump, which consists
of all programming languages used in all contributions and a value which
represents the average lines of code per feature for each programming language.
```json
{
    "Haskell": 53.8,
    "Java": 105.0,
    "Python": 49.333333333333336
}```
This is a sample output of the module using just a few contributions. The value is
calculated by dividing the lines of code per language by the features per language in
the scope of the processed contributions.

## Dependencies

This module relies on the dump from the modules featuresPerContribution,
locPerLanguagePerContribution and programmingLanguagePerContribution and
their respective dependencies.

## Issues

None.

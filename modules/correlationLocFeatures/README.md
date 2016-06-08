This is the readme file for our *main* module correlationLocFeatures.
We also implemented the following modules, which are used to distribute the work necessary for this module:
featuresPerContribution (TODO: Link)
locPerLanguagePerContribution (TODO: Link)
programmingLanguagePerContribution (TODO: Link)



# Headline

A module to calculate correlations between locs per language and 
features per language.

# Details

The module generates a "correlationLocFeatures.json" dump which consists
of all programming languages used in all contributions, and a value wich 
represents the avarage loc per feature for each programming language.  
It relies on the modules featuresPerContribution, 
locPerLanguagePerContribution and programmingLanguagePerContribution.

# Dependencies

This module relies on the dump from the modules featuresPerContribution, 
locPerLanguagePerContribution and programmingLanguagePerContribution and
their respective dependencies.

# Issues

None.

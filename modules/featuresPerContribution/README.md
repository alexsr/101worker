# Readme 

This module implements a function that gets a list of all implemented features for each contribution.

# Details 
The module creates a dump called "featuresPerContribution.json" in which it derives a list of all contributions along with their implemented features. It reads the "pages" dump and therefore does not need the code of the contribution itself. 

# Dependencies 
It uses the "pages" dump, asssuming all features are tagged according to conventions ("Implements::Feature:...).

# Issues 
None.
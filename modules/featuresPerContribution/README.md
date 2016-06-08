# featuresPerContribution

This module implements a function that gets a list of all implemented features
for each contribution.

# Details
The module creates a dump called "featuresPerContribution.json" in which it
derives a list of all contributions along with their implemented features.

```json
{ 
    "haskellComposition": [
        "Closed serialization",
        "Cut",
        "Hierarchical company",
        "Total"
    ]
}
```
This is sample output for just one contribution. In reality all contributions in the
pages dump are present in the dictionary created.

# Dependencies
It uses the "pages.json" dump, assuming all features are tagged according to
conventions ("Implements::Feature:...).

# Issues
None.

# locPerLanguagePerContribution

A module to associate a contribution with the lines of code of each language
used in this contribution.

## Details

The module generates a "locPerLanguagePerContribution.json" dump, which consists
of all contributions associated with the used language(s) and the lines of code
of these languages respectively. The used derived resources are particularly useful
because they are available per file which makes the association trivial. While the
module is doing its work, the dump is read for every file processed to update the
information with every new file. Naturally, otherwise the last file processed would
define the whole content of the dump.
```json
{
    "haskellComposition": {
        "Plain Text": 11,
        "Haskell": 147,
        "unkown": 41
    }
}
```
This is a sample output of the module using just a the haskellComposition contribution.
## Dependencies

This module relies on the derived resources loc (simpleLOC) and lang
(matchLanguage).

## Issues

None.

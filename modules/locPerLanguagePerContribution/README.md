# Headline

A module to associate a contribution with the lines of code of each language
used in this contribution.

# Details

The module generates a "locPerLanguagePerContribution.json" dump which consists
of all contributions, associated with the used language(s) and the lines of code
of these languages respectively. It relies on the derived resources loc
(simpleLOC) and lang (matchLanguage), which are particularly useful because they
work per file making the association trivial. While the worker is doing its
work, the dump is read for every file processed to update the information with
every new file. Naturally, otherwise the last file processed would
define the whole content of the dump.

# Dependencies

This module relies on the derived resources loc (simpleLOC) and lang
(matchLanguage).

# Issues

None.

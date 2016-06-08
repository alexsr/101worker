# programmingLanguagePerContribution

A module to associate contributions with the used programming language (as
opposed to every used language)

## Details

The module generates a "programmingLanguagePerContribution.json" dump which
consists of all contributions associated with the used programming language(s).
```json
{
    "happstack": [
        "Haskell",
        "JavaScript"
    ]
}
```
This is sample output for just one contribution. In reality all contributions in the
pages dump are present in the dictionary created.

## Dependencies

This module uses the wiki ("pages") dump to extract programming languages,
contributions and the associations between the two. It assumes contributions are
properly tagged (with "Uses::Language:...") and programming languages are 
properly declared as such (e.g. "OO programming language", "programming 
language", "functional programming language"). We thought about implementing a little
hack where raw_content is scanned for the term "programming language" as well to include
a few more programming languages which are currently not tagged correctly, but refrained
form using it, because we consider it bad style.

## Issues

None.

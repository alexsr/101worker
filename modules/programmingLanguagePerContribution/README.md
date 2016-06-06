# Headline

A module to associate contributions with the used programming language (as
opposed to every used language)

# Details

The module generates a "programmingLanguagePerContribution.json" dump which
consists of all contributions, associated with the used programming language(s).
It only needs the wiki ("pages") dump and does not need the contributions
themselves or any other primary or derived resource.

# Dependencies

This module uses the wiki ("pages") dump to extract programming languages,
contributions and the associations between the two. It assumes contributions are
properly tagged (with "Uses::Language:...") and programming languages are 
properly declared as such (e.g. "OO programming language", "programming 
language", "functional programming language").

# Issues

None.

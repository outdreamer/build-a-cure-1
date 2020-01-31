
overall testing strategy:
- test for each source of variance that can hold embedded assumptions (inputs/outputs, conditions, function & stack metadata such as permissions/context)

concepts:
- concepts like relevance are important in security: is there a 'need to know'

integration test:
- calculating interaction of all objects in code requires analyzing not just classes & functions but:
  - system context (permissions, installed tools, browser settings, antivirus software, firewall configuration)
  - emergent properties
  - implicit assumptions
  - consecutive exploits using gaps in multiple chainable objects

other testing tools:
- code generation tools (generate API) to standardize code
- analyze dependencies & context

my testing tools:
- intent-matching
- test generation (parsing code & generating unit tests)

my code optimization tools:
- identifying code snippets with repeated logic (on various interfaces, not just raw code repetition) or too much variance
- identifying assumptions in code that can be exploited
- identfiying optimal logic order:
  - if variable exists condition should precede variable use
  - condition with return should usually precede conditions without return 
  - conditions with common assumption should be preceded by condition testing that assumption 
  - list metadata (location of an item) should be stored during list definition if possible to avoid iteration later
  - over-restrictive conditions that reduce later choices should be carefully examined for necessity
  - if conditions should be in an if/else block rather than consecutive if conditions, if they should never happen concurrently

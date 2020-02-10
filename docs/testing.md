# Testing

## Overall testing strategy

- test for each source of variance that can hold embedded assumptions (inputs/outputs, conditions, function & stack metadata such as permissions/context)

## Test concepts

- concepts like relevance are important in security: is there a 'need to know'

## Integration test

- calculating interaction of all objects in code requires analyzing not just classes & functions but:
  - system context (permissions, installed tools, browser settings, antivirus software, firewall configuration)
  - emergent properties
  - implicit assumptions
  - consecutive exploits using gaps in multiple chainable objects
  - agent actions/resources (info about stack being used)

## Standard test questions

  - 'how will program resolve selection between two alternative resources based on tech stack'
  - 'how can functionality/inputs be mimicked'
  - 'how will this user action interact with this user-exposed function'

## Non-standard test questions

  - 'how will this object1.function interact with object2.function under edge conditions'
  - 'can object1.function be tricked into interacting with object2.function'
  - 'how will tool design limits conflict with developer intents' 
      - can a query expose information because of how the query tool is designed
      - if there are assumptions embedded in tool design to account for specific priorities (latency, accuracy, latest data, resilience), will that produce unexpected query results under certain conditions
        - if so which conditions
      - do embedded assumptions carry hidden advantages for various agent positions
        - does prioritizing most recent data have un/intended advantages, and how could those be exploited

## Existing testing tools

  - code generation tools (generate API) to standardize code
  - analyze dependencies & context
    - 'if a third party tool makes this mistake, how will that impact our system'

## Custom testing tools

  - intent-matching
    - 'what is the possible & likely reasons for this action'
      - 'why would someone make a request to a third-party site with injected javascript - how could retrieved resource be exploited'
      - 'what previous/future user actions based on their intent/decision profile could make this resource a security hole'
  - test generation
    - parsing code assumptions & generating unit tests by variance/assumptions

## Code optimization tools

- identifying code snippets with repeated logic (on various interfaces, not just raw code repetition) or too much variance
- identifying assumptions in code that can be exploited
- identfiying optimal logic order:
  - if variable exists condition should precede variable use
  - condition with return should usually precede conditions without return 
  - conditions with common assumption should be preceded by condition testing that assumption 
  - list metadata (location of an item) should be stored during list definition if possible to avoid iteration later
  - over-restrictive conditions that reduce later choices should be carefully examined for necessity
  - if conditions should be in an if/else block rather than consecutive if conditions, if they should never happen concurrently

## Test Generation

    - unit testing:

      - assumptions
      - inputs/outputs
      - conditions
      - intents/use cases

    - integration testing: 
    
      - function chains
      - system context
      - user decision history (visited insecure website/cleared cache)

    - identify objects that need to be mocked bc of security/deployment constraints

    - generate assert statements, conditions, and mock objects as needed

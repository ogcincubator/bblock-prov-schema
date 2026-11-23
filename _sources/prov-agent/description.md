## Agent Object sub-schema

An **Agent** is something that bears some form of responsibility for an activity taking place, for
the existence of an entity, or for another agent's activity. Typical Agents are a person, an
organization, or a piece of software acting on someone's behalf.

Defines Agents and core subtypes (`Organization`, `Person`, `SoftwareAgent`, `SoftwareDescription`,
`DirectQueryService`), along with the `Association` object used to qualify an Activity's relation to
an Agent, and the `qualifiedDelegation` relation between Agents.

## Object typing

Object typing needs to be explicit to support effective semantic mapping to the PROV
vocabulary, and to support schema validation scope clarity (using the right sub-schema for
objects in a collection representing the directed graph model of PROV).  Sub-schemas
should also be efficiently identifiable without structural type inference or the need to
refer to the PROV-O hierarchy.

`provType` for an Agent must be `Agent`. The custom `agentType` field may be used to specify PROV
subclasses or additional types from external vocabularies (such as Schema.org or Wfprov).

The custom application object type is explicit (`agentType`) to support schema validation clarity.

An Agent object must be identified by either a `name` or an `id`.


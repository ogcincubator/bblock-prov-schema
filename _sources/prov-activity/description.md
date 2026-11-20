## Activity Object sub-schema

An **Activity** is something that occurs over a period of time and acts upon or with entities; it
may include consuming, processing, transforming, modifying, relocating, using, or generating
entities. An Activity typically starts and ends, and is associated with the Agents responsible for
carrying it out.

Defines Activities, and the qualified relation objects used to describe how an Activity relates to
Entities and Agents: `Usage`, `Generation`, `Invalidation`, `Communication`, `Derivation`,
`Delegation`, `Attribution`, `Start` and `End`.

## Object typing

Object typing needs to be explicit to support effective semantic mapping to the PROV
vocabulary, and to support schema validation scope clarity (using the right sub-schema for
objects in a collection representing the directed graph model of PROV).  Sub-schemas
should also be efficiently identifiable without structural type inference or the need to
refer to the PROV-O hierarchy.

`provType` for an Activity must be `Activity`. The custom `activityType` field may be used to
specify PROV subclasses (note that PROV-O defines no further Activity subclasses) or additional
types from external vocabularies (such as Schema.org or Wfprov)

The custom application object type is explicit (`activityType`) to support schema validation
clarity.

## Temporal properties

An Activity may declare `startedAtTime` and `endedAtTime` to record when it began and finished.
`used`, `generated` and `invalidated` reference the Entities it consumed, produced or invalidated;
`wasAssociatedWith` and `wasInformedBy` reference the Agents and prior Activities involved. The
`qualifiedStart` and `qualifiedEnd` relations may be used instead when the start/end needs to be
qualified further (e.g. attributed to a triggering Entity).

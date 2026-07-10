## Activity Object sub-schema

An **Activity** is something that occurs over a period of time and acts upon or with entities; it
may include consuming, processing, transforming, modifying, relocating, using, or generating
entities. An Activity typically starts and ends, and is associated with the Agents responsible for
carrying it out.

Defines Activities, and the qualified relation objects used to describe how an Activity relates to
Entities and Agents: `Usage`, `Generation`, `Invalidation`, `Communication`, `Derivation`,
`Delegation`, `Attribution`, `Start` and `End`.

## Object typing

Object typing needs to be explicit to support effective semantic mapping to the PROV vocabulary, and to support schema validation scope clarity (using the right sub-schema for objects in a collection representing the directed graph model of PROV).

`provType` may be used to map to the subClasses of the Provenance vocabulary (currently only `Activity`
itself; PROV-O defines no further Activity subclasses).

The custom application object type is explicit (`activityType`) to support schema validation clarity.

## Temporal properties

An Activity may declare `startedAtTime` and `endedAtTime` to record when it began and finished.
`used`, `generated` and `invalidated` reference the Entities it consumed, produced or invalidated;
`wasAssociatedWith` and `wasInformedBy` reference the Agents and prior Activities involved. The
`qualifiedStart` and `qualifiedEnd` relations may be used instead when the start/end needs to be
qualified further (e.g. attributed to a triggering Entity).
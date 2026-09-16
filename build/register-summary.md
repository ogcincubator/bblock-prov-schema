# JSON schemas for W3C PROV model

Defines a standardised JSON schema for PROV ontology elements - supporting a graph structure based on an array of objects implementing PROV defined classes with object cross references.

Provenance defined using the [W3C PROV-O model](https://www.w3.org/TR/prov-o/) is a DAG (non-cyclic graph) based on three main object types: Entity, Activity and Agent.

This repository defines a JSON schema and matching JSON-LD context using the [OGC Building Blocks](https://ogcincubator.github.io/bblocks-docs/) methodology, 
for W3C PROV-O model, using the canonical terminology used in the PROV ontology as element names.

This schema is made of mutually dependend sub schemas for the key elements of Prov - Entity, Activity and Agent.

It also defines a context for an optional schema property "has_provenance" that can be used to wrap a provenance graph as an array of such objects, to extend the property prov:wasGeneratedBy (whose range is one or more Entity objects) with an explicit schema.

![](https://www.w3.org/TR/prov-o/diagrams/starting-points.svg)

Note that the PROV working group originally defined a number of JSON serialisation options, however these have limited uptake and do no allow PROV-O to annotate other schemas. This implementation uses modern JSON schema and JSON-LD mechanisms to provide a complete mapping from JSON to PROV-O model.

Since the development of this schema another proposal has been submitted as a W3C memberr submission: 
[https://www.w3.org/submissions/prov-jsonld/](https://www.w3.org/submissions/prov-jsonld/)

The rationale for this is consistent with the design principles:

" the family of PROV specifications lacks a serialization capable of simultaneously addressing all of the following requirements:

  - **Lightweight** A serialization MUST support lightweight Web applications.
  - **Natural** A serialization MUST look natural to its targeted community of users.
  - **Semantic** A serialization MUST allow for semantic markup and integration with linked data applications.
  - **Efficient** A serialization MUST be efficiently processable.
In our view, none of the existing PROV serializations supports all these requirements simultaneously."

An activity to reconcile these approaches and explore formalisation is proposed. 


## Building Blocks

### `ogc.ogc-utils.prov-bundled` — Single Schema for PROV

**Type:** schema

The original version of a single Schema for a provenance chain based on PROV vocabulary semantics, Agents, Activities and Entities. This schema is designed as a mix-in that can be used to add properties to other objects in a polymorphic way.

### `ogc.ogc-utils.prov` — Provenance Chain

**Type:** schema

Schema for a provenance chain based on PROV vocabulary semantics, Agents, Activities and Entities. This schema is designed as a mix-in that can be used to add properties to other objects in a polymorphic way.

### `ogc.ogc-utils.prov-activity` — Prov Activity

**Type:** schema

Sub-schema for PROV Activities: something that occurs over a period of time and acts upon or with entities, and may involve one or more agents.

### `ogc.ogc-utils.prov-entity` — Prov Entity

**Type:** schema

Sub-schema for PROV Entities: physical, digital, conceptual, or other things with some fixed aspects that were generated, used, derived from or otherwise involved in provenance relations.

### `ogc.ogc-utils.prov-agent` — Prov Agent

**Type:** schema

Sub-schema for PROV Agents: something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.


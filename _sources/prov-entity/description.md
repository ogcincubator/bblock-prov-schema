## Entity Object sub-schema

An **Entity** is a physical, digital, conceptual, or other kind of thing with some fixed aspects;
entities may be real or imaginary. In PROV terms, an Entity is what was generated, used, derived
from, or otherwise involved in an Activity or attributed to an Agent — for example a dataset, a
document, a feature, or a plan.

Defines Entities and core subtypes (`Bundle`, `Plan`, `Collection`), along with the qualified
relations that may be attached to an Entity (`qualifiedGeneration`, `qualifiedInvalidation`,
`qualifiedDerivation`, `qualifiedAttribution`, `qualifiedPrimarySource`, `qualifiedQuotation`,
`qualifiedRevision`).

`generatedAtTime` and `invalidatedAtTime` record when the entity became available and when it
stopped being usable, respectively. `value` may hold a literal value carried directly by the entity.

## Object typing

Object typing needs to be explicit to support effective semantic mapping to the PROV
vocabulary, and to support schema validation scope clarity (using the right sub-schema for
objects in a collection representing the directed graph model of PROV).  Sub-schemas
should also be efficiently identifiable without structural type inference or the need to
refer to the PROV-O hierarchy.

`provType` for an Entity must be `Entity`. The custom `entityType` field may be used to specify PROV
subclasses or additional types from external vocabularies (such as Schema.org or Wfprov).

The custom application object type is explicit (`entityType`) to support schema validation clarity.

The properties `type` and `featureType` are deliberately avoided in order to allow compatibility
with [OGC Feature](https://docs.ogc.org/is/21-045r1/21-045r1.html#feature-types) and
[GeoJSON](https://www.rfc-editor.org/info/rfc7946/#section-3), which use them with constant string
values.

An Entity object requires an `id`. When `entityType` is set to `Collection`, `hadMember` (an array of
member Entities) is also required; when set to `EmptyCollection`, `hadMember` must be an empty array.


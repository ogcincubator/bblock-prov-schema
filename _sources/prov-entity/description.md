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

Object typing needs to be explicit to support effective semantic mapping to the PROV vocabulary, and to support schema validation scope clarity (using the right sub-schema for objects in a collection representing the directed graph model of PROV).

`provType` may be used to map to the subClasses of the Provenance vocabulary.

The custom application object type is explicit (`entityType`) to support schema validation clarity.

Note that `entityType` is optional and may be replaced by `featureType` for compatibility with the OGC Feature implementation (implicitly always an Entity)

likewise the use of the property `type` is not specified to allow compatibility with GeoJSON features that must have this property with a constant value ("Feature" or "FeatureCollection").

An Entity object requires an `id`. When `type` is set to `Collection`, `hadMember` (an array of
member Entities) is also required; when set to `EmptyCollection`, `hadMember` must be an empty array.


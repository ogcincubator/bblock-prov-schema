
# Provenance Chain (Schema)

`ogc.ogc-utils.prov` *v0.1*

Schema for a provenance chain based on PROV vocabulary semantics, Agents, Activities and Entities. This schema is designed as a mix-in that can be used to add properties to other objects in a polymorphic way.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Provenance chain

A schema defining objects that may be referenced or nested as a chain of activities.

This schema implements the PROV vocabulary semantics.


## Examples

### Example Entities with Provenance Chains
See panel to right - note that a more user friendly "collapsable" version is in development. 
#### json
```json
{
  "@context": {
    "@base": "https://example.org/",
    "agents": "https://someagentregister.eg/",
    "thing": "https://example.org/entities/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "survtypes": "https://example.org/surveytypes/",
    "surveyreg": "https://example.org/surveys/"
  },
  "id": "DP-1",
  "type": "Feature",
  "featureType": "Survey",
  "wasGeneratedBy": [
    "surveyreg:DP-1-S1",
    {
      "activity": "Registration",
      "id": "surveyreg:DP-1-S2",
      "endedAtTime": "2019-01-01T19:03:15+01:00",
      "wasAssociatedWith": "agents:bc-3",
      "used": {
        "id": "Example-Act",
        "wasAttributedTo": "agents:nz",
        "links": [
          {
            "href": "https://nze.gov/linktoact/Example1",
            "rel": "related"
          }
        ]
      }
    }
  ],
  "provenance": [
    {
      "id": "DP-2223",
      "type": "Entity",
      "wasGeneratedBy": "thing:DP-1-S1"
    },
    {
      "type": "Activity",
      "id": "thing:DP-1-S1",
      "endedAtTime": "2023-10-05T05:03:15+01:00",
      "wasAssociatedWith": "agents:ah-2344503",
      "used": {
        "id": "Act3",
        "type": "Entity",
        "wasAttributedTo": "agents:nz",
        "links": [
          {
            "href": "https://some.gov/linktoact/",
            "rel": "related"
          }
        ]
      }
    }
  ]
}




```

#### jsonld
```jsonld
{
  "@context": [
    "https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/context.jsonld",
    {
      "@base": "https://example.org/",
      "agents": "https://someagentregister.eg/",
      "thing": "https://example.org/entities/",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "survtypes": "https://example.org/surveytypes/",
      "surveyreg": "https://example.org/surveys/"
    }
  ],
  "id": "DP-1",
  "type": "Feature",
  "featureType": "Survey",
  "wasGeneratedBy": [
    "surveyreg:DP-1-S1",
    {
      "activity": "Registration",
      "id": "surveyreg:DP-1-S2",
      "endedAtTime": "2019-01-01T19:03:15+01:00",
      "wasAssociatedWith": "agents:bc-3",
      "used": {
        "id": "Example-Act",
        "wasAttributedTo": "agents:nz",
        "links": [
          {
            "href": "https://nze.gov/linktoact/Example1",
            "rel": "related"
          }
        ]
      }
    }
  ],
  "provenance": [
    {
      "id": "DP-2223",
      "type": "Entity",
      "wasGeneratedBy": "thing:DP-1-S1"
    },
    {
      "type": "Activity",
      "id": "thing:DP-1-S1",
      "endedAtTime": "2023-10-05T05:03:15+01:00",
      "wasAssociatedWith": "agents:ah-2344503",
      "used": {
        "id": "Act3",
        "type": "Entity",
        "wasAttributedTo": "agents:nz",
        "links": [
          {
            "href": "https://some.gov/linktoact/",
            "rel": "related"
          }
        ]
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix agents: <https://someagentregister.eg/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix surveyreg: <https://example.org/surveys/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/DP-1> prov:wasGeneratedBy surveyreg:DP-1-S1,
        surveyreg:DP-1-S2 .

<https://example.org/Example-Act> rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget "https://nze.gov/linktoact/Example1" ] ;
    prov:wasAttributedTo agents:nz .

surveyreg:DP-1-S2 prov:endedAtTime "2019-01-01T19:03:15+01:00"^^xsd:dateTime ;
    prov:used <https://example.org/Example-Act> ;
    prov:wasAssociatedWith agents:bc-3 .


```


### Example Activity
#### json
```json
{
  "type": "Activity",
  "id": "surveyreg-nz:DP-1-S2",
  "endedAtTime": "2029-01-01T22:05:19+02:00",
  "wasAssociatedWith": "linz-registered-surveyors:bc-3",
  "used": {
    "type": "Entity",
    "id": "Act3",
    "wasAttributedTo": "icsm-jurisdictions:nz",
    "links": [
      {
        "href": "https://some.gov/linktoact/",
        "rel": "related"
      }
    ]
  }
}





```

#### jsonld
```jsonld
{
  "type": "Activity",
  "id": "surveyreg-nz:DP-1-S2",
  "endedAtTime": "2029-01-01T22:05:19+02:00",
  "wasAssociatedWith": "linz-registered-surveyors:bc-3",
  "used": {
    "type": "Entity",
    "id": "Act3",
    "wasAttributedTo": "icsm-jurisdictions:nz",
    "links": [
      {
        "href": "https://some.gov/linktoact/",
        "rel": "related"
      }
    ]
  },
  "@context": "https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/context.jsonld"
}
```

#### ttl
```ttl
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<surveyreg-nz:DP-1-S2> prov:endedAtTime "2029-01-01T22:05:19+02:00"^^xsd:dateTime ;
    prov:used <http://www.example.com/exampleActivity/Act3> ;
    prov:wasAssociatedWith <linz-registered-surveyors:bc-3> .

<http://www.example.com/exampleActivity/Act3> rdfs:seeAlso [ ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget "https://some.gov/linktoact/" ] ;
    prov:wasAttributedTo <icsm-jurisdictions:nz> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: provenance chain
$defs:
  objectref:
    $anchor: objectref
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json
  oneOrMoreObjectref:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json#/$defs/MultipleOrObject
  curie:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json
  oneOrMoreActivitiesOrRefIds:
    oneOf:
    - $ref: '#/$defs/objectref'
    - $ref: '#/$defs/Activity'
    - type: array
      items:
        anyOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
  oneOrMoreEntitiesOrRefIds:
    oneOf:
    - $ref: '#/$defs/objectref'
    - $ref: '#/$defs/Entity'
    - type: array
      items:
        anyOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Entity'
  oneOrMoreAgentsOrRefIds:
    oneOf:
    - $ref: '#/$defs/objectref'
    - $ref: '#/$defs/externalLink'
    - $ref: '#/$defs/Agent'
    - type: array
      items:
        anyOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Agent'
  externalLink:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json
  influenced:
    type: object
    properties:
      wasInfluencedBy:
        anyOf:
        - $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        - $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        - $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
        x-jsonld-type: '@id'
      qualifiedInfluence:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Influence'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Influence'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
        x-jsonld-type: '@id'
  Entity:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      featureType:
        $ref: '#/$defs/objectref'
      provenance:
        $ref: '#/$defs/Prov'
      wasGeneratedBy:
        $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
        x-jsonld-type: '@id'
      wasAttributedTo:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
        x-jsonld-type: '@id'
      wasDerivedFrom:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
        x-jsonld-type: '@id'
      alternateOf:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
        x-jsonld-type: '@id'
      hadPrimarySource:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
        x-jsonld-type: '@id'
      specializationOf:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
        x-jsonld-type: '@id'
      wasInvalidatedBy:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
        x-jsonld-type: '@id'
      wasQuotedFrom:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
        x-jsonld-type: '@id'
      wasRevisionOf:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
        x-jsonld-type: '@id'
      mentionOf:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
        x-jsonld-type: '@id'
      atLocation:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#atLocation
        x-jsonld-type: '@id'
      links:
        type: array
        items:
          $ref: '#/$defs/externalLink'
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
      qualifiedGeneration:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Generation'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Generation'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
        x-jsonld-type: '@id'
      qualifiedInvalidation:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Invalidation'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Invalidation'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
        x-jsonld-type: '@id'
      qualifiedDerivation:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Derivation'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Derivation'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
        x-jsonld-type: '@id'
      qualifiedAttribution:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Attribution'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Attribution'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
        x-jsonld-type: '@id'
    required:
    - id
    anyOf:
    - properties:
        type:
          oneOf:
          - type: string
            enum:
            - Entity
            - Bundle
            - Plan
          - type: array
            contains:
              type: string
              enum:
              - Entity
              - Bundle
              - Plan
      required:
      - type
    - required:
      - featureType
    - required:
      - wasGeneratedBy
    - required:
      - wasAttributedTo
    - required:
      - wasDerivedFrom
    - required:
      - provenance
    - properties:
        type:
          type: string
          const: Collection
        hadMember:
          type: array
          items:
            $ref: '#/$defs/Entity'
          x-jsonld-id: http://www.w3.org/ns/prov#hadMember
          x-jsonld-type: '@id'
      required:
      - hadMember
      - type
    - properties:
        type:
          type: string
          const: EmptyCollection
        hadMember:
          type: array
          maxItems: 0
          x-jsonld-id: http://www.w3.org/ns/prov#hadMember
          x-jsonld-type: '@id'
      required:
      - hadMember
      - type
    allOf:
    - $ref: '#/$defs/influenced'
  dateTime:
    type: string
    format: date-time
    pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?$
  Activity:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        $ref: '#/$defs/oneOrMoreObjectref'
      endedAtTime:
        $ref: '#/$defs/dateTime'
        x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      wasAssociatedWith:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
        x-jsonld-type: '@id'
      wasInformedBy:
        $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
        x-jsonld-type: '@id'
      used:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#used
        x-jsonld-type: '@id'
      wasStartedBy:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
        x-jsonld-type: '@id'
      wasEndedBy:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
        x-jsonld-type: '@id'
      invalidated:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#invalidated
        x-jsonld-type: '@id'
      generated:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#generated
        x-jsonld-type: '@id'
      atLocation:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#atLocation
        x-jsonld-type: '@id'
      qualifiedUsage:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Usage'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Usage'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
        x-jsonld-type: '@id'
      qualifiedCommunication:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Communication'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Generation'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
        x-jsonld-type: '@id'
      qualifiedStart:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Start'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
        x-jsonld-type: '@id'
      qualifiedEnd:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/End'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
        x-jsonld-type: '@id'
      qualifiedAssociation:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Association'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Association'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
        x-jsonld-type: '@id'
    anyOf:
    - properties:
        type:
          oneOf:
          - type: string
            const: Activity
          - type: array
            contains:
              type: string
              const: Activity
            items:
              type: string
      required:
      - type
    - required:
      - activity
    - required:
      - used
    - required:
      - wasInformedBy
    - required:
      - endedAtTime
    - required:
      - startedAtTime
    - required:
      - wasAssociatedWith
    allOf:
    - $ref: '#/$defs/influenced'
  Agent:
    type: object
    properties:
      type:
        $ref: '#/$defs/oneOrMoreObjectref'
      name:
        type: string
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      actedOnBehalfOf:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
        x-jsonld-type: '@id'
      atLocation:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#atLocation
        x-jsonld-type: '@id'
      qualifiedDelegation:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Delegation'
        - type: array
          items:
            oneOf:
            - $ref: '#/$defs/objectref'
            - $ref: '#/$defs/Delegation'
        x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
        x-jsonld-type: '@id'
    required:
    - name
    anyOf:
    - properties:
        type:
          oneOf:
          - type: string
            enum:
            - Agent
            - Organization
            - Person
            - SoftwareAgent
            - SoftwareDescription
            - DirectQueryService
          - type: array
            contains:
              type: string
              enum:
              - Agent
              - Organization
              - Person
              - SoftwareAgent
              - SoftwareDescription
              - DirectQueryService
            items:
              type: string
      required:
      - type
    - required:
      - agentType
    - required:
      - actedOnBehalfOf
    allOf:
    - $ref: '#/$defs/influenced'
  Usage:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Usage
        - type: array
          contains:
            type: string
            const: Usage
          items:
            type: string
      atTime:
        $ref: '#/$defs/dateTime'
        x-jsonld-id: http://www.w3.org/ns/prov#atTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      entity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Entity'
        x-jsonld-id: http://www.w3.org/ns/prov#entity
        x-jsonld-type: '@id'
    required:
    - atTime
    - entity
  Generation:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Generation
        - type: array
          contains:
            type: string
            const: Generation
          items:
            type: string
      atTime:
        $ref: '#/$defs/dateTime'
        x-jsonld-id: http://www.w3.org/ns/prov#atTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      activity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#activity
        x-jsonld-type: '@id'
    required:
    - atTime
    - activity
  Invalidation:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Invalidation
        - type: array
          contains:
            type: string
            const: Invalidation
          items:
            type: string
      atTime:
        $ref: '#/$defs/dateTime'
        x-jsonld-id: http://www.w3.org/ns/prov#atTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      activity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#activity
        x-jsonld-type: '@id'
    required:
    - atTime
    - activity
  Communication:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Communication
        - type: array
          contains:
            type: string
            const: Communication
          items:
            type: string
      activity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#activity
        x-jsonld-type: '@id'
    required:
    - activity
  StartOrEnd:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
        - type: array
          items:
            type: string
      atTime:
        $ref: '#/$defs/dateTime'
        x-jsonld-id: http://www.w3.org/ns/prov#atTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      entity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Entity'
        x-jsonld-id: http://www.w3.org/ns/prov#entity
        x-jsonld-type: '@id'
      hadActivity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
        x-jsonld-type: '@id'
    required:
    - atTime
  Start:
    allOf:
    - $ref: '#/$defs/StartOrEnd'
    - properties:
        type:
          anyOf:
          - const: Start
          - contains:
              const: Start
  End:
    allOf:
    - $ref: '#/$defs/StartOrEnd'
    - properties:
        type:
          anyOf:
          - const: End
          - contains:
              const: End
  Derivation:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Derivation
        - type: array
          contains:
            type: string
            const: Derivation
          items:
            type: string
      hadGeneration:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Generation'
        x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
        x-jsonld-type: '@id'
      hadActivity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
        x-jsonld-type: '@id'
      hadUsage:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Usage'
        x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
        x-jsonld-type: '@id'
      entity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Entity'
        x-jsonld-id: http://www.w3.org/ns/prov#entity
        x-jsonld-type: '@id'
    required:
    - atTime
    - entity
  Delegation:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Delegation
        - type: array
          contains:
            type: string
            const: Delegation
          items:
            type: string
      agent:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Agent'
        x-jsonld-id: http://www.w3.org/ns/prov#agent
        x-jsonld-type: '@id'
      hadActivity:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Activity'
        x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
        x-jsonld-type: '@id'
  Attribution:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Attribution
        - type: array
          contains:
            type: string
            const: Attribution
          items:
            type: string
      agent:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Agent'
        x-jsonld-id: http://www.w3.org/ns/prov#agent
        x-jsonld-type: '@id'
  Association:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      type:
        oneOf:
        - type: string
          const: Association
        - type: array
          contains:
            type: string
            const: Association
          items:
            type: string
      agent:
        oneOf:
        - $ref: '#/$defs/objectref'
        - $ref: '#/$defs/Agent'
        x-jsonld-id: http://www.w3.org/ns/prov#agent
        x-jsonld-type: '@id'
      hadRole:
        $ref: '#/$defs/oneOrMoreObjectref'
        x-jsonld-id: http://www.w3.org/ns/prov#hadRole
        x-jsonld-type: '@id'
      hadPlan:
        $ref: '#/$defs/oneOrMoreObjectref'
        x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
        x-jsonld-type: '@id'
  Influence:
    type: object
    properties:
      id:
        $ref: '#/$defs/curie'
        x-jsonld-id: '@id'
      influencer:
        anyOf:
        - $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        - $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        - $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#influencer
        x-jsonld-type: '@id'
      entity:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#entity
        x-jsonld-type: '@id'
      activity:
        $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#activity
        x-jsonld-type: '@id'
      agent:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#agent
        x-jsonld-type: '@id'
    anyOf:
    - required:
      - influencer
    - required:
      - entity
    - required:
      - activity
    - required:
      - agent
  Prov:
    description: An list of provenance objects linked together to form a provenance
      chain for the current object. Objects may have nested objects as well, with
      or without referencable ids
    type: array
    items:
      oneOf:
      - $ref: '#/$defs/Entity'
      - $ref: '#/$defs/Activity'
      - $ref: '#/$defs/Agent'
anyOf:
- $ref: '#/$defs/Entity'
- $ref: '#/$defs/Activity'
x-jsonld-extra-terms:
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://www.w3.org/ns/prov#Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_provenance:
    x-jsonld-id: http://www.w3.org/ns/prov#has_provenance
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  prov: http://www.w3.org/ns/prov#
  xsd: http://www.w3.org/2001/XMLSchema#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id"
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id"
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id"
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id"
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id"
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasGeneratedBy": {
                  "@id": "prov:wasGeneratedBy",
                  "@type": "@id"
                },
                "wasAttributedTo": {
                  "@id": "prov:wasAttributedTo",
                  "@type": "@id"
                },
                "wasInvalidatedBy": {
                  "@id": "prov:wasInvalidatedBy",
                  "@type": "@id"
                },
                "wasQuotedFrom": {
                  "@id": "prov:wasQuotedFrom",
                  "@type": "@id"
                },
                "wasRevisionOf": {
                  "@id": "prov:wasRevisionOf",
                  "@type": "@id"
                },
                "mentionOf": {
                  "@id": "prov:mentionOf",
                  "@type": "@id"
                },
                "qualifiedGeneration": {
                  "@id": "prov:qualifiedGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedInvalidation": {
                  "@id": "prov:qualifiedInvalidation",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedDerivation": {
                  "@id": "prov:qualifiedDerivation",
                  "@type": "@id",
                  "@context": {
                    "hadGeneration": {
                      "@id": "prov:hadGeneration",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    },
                    "hadUsage": {
                      "@id": "prov:hadUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAttribution": {
                  "@id": "prov:qualifiedAttribution",
                  "@type": "@id",
                  "@context": {}
                },
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id",
                  "@context": {
                    "hadMember": {
                      "@id": "prov:hadMember",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id",
              "@context": {
                "wasGeneratedBy": {
                  "@id": "prov:wasGeneratedBy",
                  "@type": "@id"
                },
                "wasAttributedTo": {
                  "@id": "prov:wasAttributedTo",
                  "@type": "@id"
                },
                "wasInvalidatedBy": {
                  "@id": "prov:wasInvalidatedBy",
                  "@type": "@id"
                },
                "wasQuotedFrom": {
                  "@id": "prov:wasQuotedFrom",
                  "@type": "@id"
                },
                "wasRevisionOf": {
                  "@id": "prov:wasRevisionOf",
                  "@type": "@id"
                },
                "mentionOf": {
                  "@id": "prov:mentionOf",
                  "@type": "@id"
                },
                "qualifiedGeneration": {
                  "@id": "prov:qualifiedGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedInvalidation": {
                  "@id": "prov:qualifiedInvalidation",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedDerivation": {
                  "@id": "prov:qualifiedDerivation",
                  "@type": "@id",
                  "@context": {
                    "hadGeneration": {
                      "@id": "prov:hadGeneration",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    },
                    "hadUsage": {
                      "@id": "prov:hadUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAttribution": {
                  "@id": "prov:qualifiedAttribution",
                  "@type": "@id",
                  "@context": {}
                },
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id",
                  "@context": {
                    "hadMember": {
                      "@id": "prov:hadMember",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id",
      "@context": {
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id",
      "@context": {
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id",
      "@context": {
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id",
      "@context": {
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id",
      "@context": {
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@id": "prov:qualifiedUsage",
      "@type": "@id",
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        }
      }
    },
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id",
      "@context": {
        "activity": {
          "@id": "prov:activity",
          "@type": "@id"
        },
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        }
      }
    },
    "qualifiedStart": {
      "@id": "prov:qualifiedStart",
      "@type": "@id",
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id",
                  "@context": {}
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      }
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id",
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id",
                  "@context": {}
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      }
    },
    "qualifiedAssociation": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id",
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "wasGeneratedBy": {
                  "@id": "prov:wasGeneratedBy",
                  "@type": "@id"
                },
                "wasAttributedTo": {
                  "@id": "prov:wasAttributedTo",
                  "@type": "@id",
                  "@context": {}
                },
                "wasInvalidatedBy": {
                  "@id": "prov:wasInvalidatedBy",
                  "@type": "@id",
                  "@context": {}
                },
                "wasQuotedFrom": {
                  "@id": "prov:wasQuotedFrom",
                  "@type": "@id",
                  "@context": {}
                },
                "wasRevisionOf": {
                  "@id": "prov:wasRevisionOf",
                  "@type": "@id",
                  "@context": {}
                },
                "mentionOf": {
                  "@id": "prov:mentionOf",
                  "@type": "@id",
                  "@context": {}
                },
                "qualifiedGeneration": {
                  "@id": "prov:qualifiedGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedInvalidation": {
                  "@id": "prov:qualifiedInvalidation",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedDerivation": {
                  "@id": "prov:qualifiedDerivation",
                  "@type": "@id",
                  "@context": {
                    "hadGeneration": {
                      "@id": "prov:hadGeneration",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    },
                    "hadUsage": {
                      "@id": "prov:hadUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAttribution": {
                  "@id": "prov:qualifiedAttribution",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                },
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id",
                  "@context": {
                    "hadMember": {
                      "@id": "prov:hadMember",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "wasGeneratedBy": {
                      "@id": "prov:wasGeneratedBy",
                      "@type": "@id"
                    },
                    "wasAttributedTo": {
                      "@id": "prov:wasAttributedTo",
                      "@type": "@id",
                      "@context": {}
                    },
                    "wasInvalidatedBy": {
                      "@id": "prov:wasInvalidatedBy",
                      "@type": "@id",
                      "@context": {}
                    },
                    "wasQuotedFrom": {
                      "@id": "prov:wasQuotedFrom",
                      "@type": "@id",
                      "@context": {}
                    },
                    "wasRevisionOf": {
                      "@id": "prov:wasRevisionOf",
                      "@type": "@id",
                      "@context": {}
                    },
                    "mentionOf": {
                      "@id": "prov:mentionOf",
                      "@type": "@id",
                      "@context": {}
                    },
                    "qualifiedGeneration": {
                      "@id": "prov:qualifiedGeneration",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedInvalidation": {
                      "@id": "prov:qualifiedInvalidation",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedDerivation": {
                      "@id": "prov:qualifiedDerivation",
                      "@type": "@id",
                      "@context": {
                        "hadGeneration": {
                          "@id": "prov:hadGeneration",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        },
                        "hadUsage": {
                          "@id": "prov:hadUsage",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAttribution": {
                      "@id": "prov:qualifiedAttribution",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        }
                      }
                    },
                    "hadMember": {
                      "@id": "prov:hadMember",
                      "@type": "@id",
                      "@context": {
                        "hadMember": {
                          "@id": "prov:hadMember",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id",
                  "@context": {
                    "wasGeneratedBy": {
                      "@id": "prov:wasGeneratedBy",
                      "@type": "@id"
                    },
                    "wasAttributedTo": {
                      "@id": "prov:wasAttributedTo",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "wasInvalidatedBy": {
                      "@id": "prov:wasInvalidatedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "wasQuotedFrom": {
                      "@id": "prov:wasQuotedFrom",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "wasRevisionOf": {
                      "@id": "prov:wasRevisionOf",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "mentionOf": {
                      "@id": "prov:mentionOf",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedGeneration": {
                      "@id": "prov:qualifiedGeneration",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedInvalidation": {
                      "@id": "prov:qualifiedInvalidation",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedDerivation": {
                      "@id": "prov:qualifiedDerivation",
                      "@type": "@id",
                      "@context": {
                        "hadGeneration": {
                          "@id": "prov:hadGeneration",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        },
                        "hadUsage": {
                          "@id": "prov:hadUsage",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAttribution": {
                      "@id": "prov:qualifiedAttribution",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        }
                      }
                    },
                    "hadMember": {
                      "@id": "prov:hadMember",
                      "@type": "@id",
                      "@context": {
                        "hadMember": {
                          "@id": "prov:hadMember",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              }
            }
          }
        },
        "hadRole": {
          "@id": "prov:hadRole",
          "@type": "@id"
        },
        "hadPlan": {
          "@id": "prov:hadPlan",
          "@type": "@id"
        }
      }
    },
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasAssociatedWith": {
          "@id": "prov:wasAssociatedWith",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@id": "prov:qualifiedUsage",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedStart": {
          "@id": "prov:qualifiedStart",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedEnd": {
          "@id": "prov:qualifiedEnd",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAssociation": {
          "@id": "prov:qualifiedAssociation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id"
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {}
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id"
            }
          }
        }
      }
    },
    "qualifiedInfluence": {
      "@id": "prov:qualifiedInfluence",
      "@type": "@id",
      "@context": {
        "influencer": {
          "@id": "prov:influencer",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasAttributedTo": {
                  "@id": "prov:wasAttributedTo",
                  "@type": "@id",
                  "@context": {
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "wasInvalidatedBy": {
                  "@id": "prov:wasInvalidatedBy",
                  "@type": "@id",
                  "@context": {
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "wasQuotedFrom": {
                  "@id": "prov:wasQuotedFrom",
                  "@type": "@id",
                  "@context": {
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "wasRevisionOf": {
                  "@id": "prov:wasRevisionOf",
                  "@type": "@id",
                  "@context": {
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "mentionOf": {
                  "@id": "prov:mentionOf",
                  "@type": "@id",
                  "@context": {
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAttribution": {
                  "@id": "prov:qualifiedAttribution",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {}
                    }
                  }
                },
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id",
          "@context": {
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasGeneratedBy": {
              "@id": "prov:wasGeneratedBy",
              "@type": "@id"
            },
            "wasAttributedTo": {
              "@id": "prov:wasAttributedTo",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasInvalidatedBy": {
              "@id": "prov:wasInvalidatedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasQuotedFrom": {
              "@id": "prov:wasQuotedFrom",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "wasRevisionOf": {
              "@id": "prov:wasRevisionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "mentionOf": {
              "@id": "prov:mentionOf",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                }
              }
            },
            "qualifiedGeneration": {
              "@id": "prov:qualifiedGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedInvalidation": {
              "@id": "prov:qualifiedInvalidation",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedDerivation": {
              "@id": "prov:qualifiedDerivation",
              "@type": "@id",
              "@context": {
                "hadGeneration": {
                  "@id": "prov:hadGeneration",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                },
                "hadUsage": {
                  "@id": "prov:hadUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAttribution": {
              "@id": "prov:qualifiedAttribution",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {}
                }
              }
            },
            "hadMember": {
              "@id": "prov:hadMember",
              "@type": "@id",
              "@context": {
                "hadMember": {
                  "@id": "prov:hadMember",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "agent": {
          "@id": "prov:agent",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "used": {
                      "@id": "prov:used",
                      "@type": "@id"
                    },
                    "wasStartedBy": {
                      "@id": "prov:wasStartedBy",
                      "@type": "@id"
                    },
                    "wasEndedBy": {
                      "@id": "prov:wasEndedBy",
                      "@type": "@id"
                    },
                    "invalidated": {
                      "@id": "prov:invalidated",
                      "@type": "@id"
                    },
                    "generated": {
                      "@id": "prov:generated",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "name": "rdfs:label",
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      }
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id",
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id"
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              }
            }
          }
        }
      }
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id",
      "@context": {
        "wasAssociatedWith": {
          "@id": "prov:wasAssociatedWith",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@id": "prov:qualifiedUsage",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedStart": {
          "@id": "prov:qualifiedStart",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedEnd": {
          "@id": "prov:qualifiedEnd",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAssociation": {
          "@id": "prov:qualifiedAssociation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id"
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@type": "@id"
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                }
              }
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            }
          }
        }
      }
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      }
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id",
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id",
      "@context": {
        "atTime": {
          "@id": "prov:atTime",
          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "activity": {
          "@id": "prov:activity",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedCommunication": {
              "@id": "prov:qualifiedCommunication",
              "@type": "@id",
              "@context": {
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "qualifiedDerivation": {
      "@id": "prov:qualifiedDerivation",
      "@type": "@id",
      "@context": {
        "hadGeneration": {
          "@id": "prov:hadGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {}
                },
                "qualifiedCommunication": {
                  "@id": "prov:qualifiedCommunication",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "wasInfluencedBy": {
                          "@id": "prov:wasInfluencedBy",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "qualifiedInfluence": {
                          "@id": "prov:qualifiedInfluence",
                          "@type": "@id",
                          "@context": {
                            "influencer": {
                              "@id": "prov:influencer",
                              "@type": "@id",
                              "@context": {
                                "href": "oa:hasTarget",
                                "rel": {
                                  "@id": "http://www.iana.org/assignments/relation",
                                  "@type": "@id",
                                  "@context": {
                                    "@base": "http://www.iana.org/assignments/relation/"
                                  }
                                },
                                "type": "dct:type",
                                "hreflang": "dct:language",
                                "title": "rdfs:label",
                                "length": "dct:extent"
                              }
                            },
                            "activity": {
                              "@id": "prov:activity",
                              "@type": "@id"
                            },
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id",
                              "@context": {
                                "href": "oa:hasTarget",
                                "rel": {
                                  "@id": "http://www.iana.org/assignments/relation",
                                  "@type": "@id",
                                  "@context": {
                                    "@base": "http://www.iana.org/assignments/relation/"
                                  }
                                },
                                "type": "dct:type",
                                "hreflang": "dct:language",
                                "title": "rdfs:label",
                                "length": "dct:extent"
                              }
                            }
                          }
                        }
                      }
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadActivity": {
          "@id": "prov:hadActivity",
          "@type": "@id",
          "@context": {
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id"
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "used": {
              "@id": "prov:used",
              "@type": "@id"
            },
            "wasStartedBy": {
              "@id": "prov:wasStartedBy",
              "@type": "@id"
            },
            "wasEndedBy": {
              "@id": "prov:wasEndedBy",
              "@type": "@id"
            },
            "invalidated": {
              "@id": "prov:invalidated",
              "@type": "@id"
            },
            "generated": {
              "@id": "prov:generated",
              "@type": "@id"
            },
            "qualifiedUsage": {
              "@id": "prov:qualifiedUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "qualifiedStart": {
              "@id": "prov:qualifiedStart",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedEnd": {
              "@id": "prov:qualifiedEnd",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadUsage": {
          "@id": "prov:hadUsage",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            }
          }
        },
        "entity": {
          "@id": "prov:entity",
          "@type": "@id"
        }
      }
    },
    "qualifiedAttribution": {
      "@id": "prov:qualifiedAttribution",
      "@type": "@id",
      "@context": {
        "agent": {
          "@id": "prov:agent",
          "@type": "@id",
          "@context": {
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {}
                },
                "used": {
                  "@id": "prov:used",
                  "@type": "@id"
                },
                "wasStartedBy": {
                  "@id": "prov:wasStartedBy",
                  "@type": "@id"
                },
                "wasEndedBy": {
                  "@id": "prov:wasEndedBy",
                  "@type": "@id"
                },
                "invalidated": {
                  "@id": "prov:invalidated",
                  "@type": "@id"
                },
                "generated": {
                  "@id": "prov:generated",
                  "@type": "@id"
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent"
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id",
                      "@context": {}
                    },
                    "used": {
                      "@id": "prov:used",
                      "@type": "@id"
                    },
                    "wasStartedBy": {
                      "@id": "prov:wasStartedBy",
                      "@type": "@id"
                    },
                    "wasEndedBy": {
                      "@id": "prov:wasEndedBy",
                      "@type": "@id"
                    },
                    "invalidated": {
                      "@id": "prov:invalidated",
                      "@type": "@id"
                    },
                    "generated": {
                      "@id": "prov:generated",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "used": {
                      "@id": "prov:used",
                      "@type": "@id"
                    },
                    "wasStartedBy": {
                      "@id": "prov:wasStartedBy",
                      "@type": "@id"
                    },
                    "wasEndedBy": {
                      "@id": "prov:wasEndedBy",
                      "@type": "@id"
                    },
                    "invalidated": {
                      "@id": "prov:invalidated",
                      "@type": "@id"
                    },
                    "generated": {
                      "@id": "prov:generated",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                }
              }
            }
          }
        }
      }
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id",
      "@context": {
        "wasAssociatedWith": {
          "@id": "prov:wasAssociatedWith",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id"
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id"
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id"
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "used": {
          "@id": "prov:used",
          "@type": "@id"
        },
        "wasStartedBy": {
          "@id": "prov:wasStartedBy",
          "@type": "@id"
        },
        "wasEndedBy": {
          "@id": "prov:wasEndedBy",
          "@type": "@id"
        },
        "invalidated": {
          "@id": "prov:invalidated",
          "@type": "@id"
        },
        "generated": {
          "@id": "prov:generated",
          "@type": "@id"
        },
        "qualifiedUsage": {
          "@id": "prov:qualifiedUsage",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedStart": {
          "@id": "prov:qualifiedStart",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedEnd": {
          "@id": "prov:qualifiedEnd",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAssociation": {
          "@id": "prov:qualifiedAssociation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            },
            "hadRole": {
              "@id": "prov:hadRole",
              "@type": "@id"
            },
            "hadPlan": {
              "@id": "prov:hadPlan",
              "@type": "@id"
            }
          }
        },
        "wasInfluencedBy": {
          "@id": "prov:wasInfluencedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasAssociatedWith": {
              "@id": "prov:wasAssociatedWith",
              "@type": "@id",
              "@context": {
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedAssociation": {
              "@id": "prov:qualifiedAssociation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "hadRole": {
                  "@id": "prov:hadRole",
                  "@type": "@id"
                },
                "hadPlan": {
                  "@id": "prov:hadPlan",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedInfluence": {
          "@id": "prov:qualifiedInfluence",
          "@type": "@id",
          "@context": {
            "influencer": {
              "@id": "prov:influencer",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id",
                      "@context": {
                        "wasAssociatedWith": {
                          "@id": "prov:wasAssociatedWith",
                          "@type": "@id"
                        },
                        "qualifiedAssociation": {
                          "@id": "prov:qualifiedAssociation",
                          "@type": "@id",
                          "@context": {
                            "hadRole": {
                              "@id": "prov:hadRole",
                              "@type": "@id"
                            },
                            "hadPlan": {
                              "@id": "prov:hadPlan",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id",
                      "@context": {
                        "wasAssociatedWith": {
                          "@id": "prov:wasAssociatedWith",
                          "@type": "@id"
                        },
                        "qualifiedUsage": {
                          "@id": "prov:qualifiedUsage",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "qualifiedStart": {
                          "@id": "prov:qualifiedStart",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedEnd": {
                          "@id": "prov:qualifiedEnd",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedAssociation": {
                          "@id": "prov:qualifiedAssociation",
                          "@type": "@id",
                          "@context": {
                            "hadRole": {
                              "@id": "prov:hadRole",
                              "@type": "@id"
                            },
                            "hadPlan": {
                              "@id": "prov:hadPlan",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "qualifiedDelegation": {
          "@id": "prov:qualifiedDelegation",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id"
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@id": "prov:wasGeneratedBy",
          "@type": "@id",
          "@context": {
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "href": "oa:hasTarget",
                "rel": {
                  "@id": "http://www.iana.org/assignments/relation",
                  "@type": "@id",
                  "@context": {
                    "@base": "http://www.iana.org/assignments/relation/"
                  }
                },
                "type": "dct:type",
                "hreflang": "dct:language",
                "title": "rdfs:label",
                "length": "dct:extent",
                "actedOnBehalfOf": {
                  "@id": "prov:actedOnBehalfOf",
                  "@type": "@id"
                },
                "qualifiedDelegation": {
                  "@id": "prov:qualifiedDelegation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id"
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "wasAttributedTo": {
          "@id": "prov:wasAttributedTo",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasInvalidatedBy": {
          "@id": "prov:wasInvalidatedBy",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasQuotedFrom": {
          "@id": "prov:wasQuotedFrom",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "wasRevisionOf": {
          "@id": "prov:wasRevisionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "mentionOf": {
          "@id": "prov:mentionOf",
          "@type": "@id",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@type": "@id"
            },
            "qualifiedDelegation": {
              "@id": "prov:qualifiedDelegation",
              "@type": "@id",
              "@context": {
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                },
                "hadActivity": {
                  "@id": "prov:hadActivity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "entity": {
                          "@id": "prov:entity",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                }
              }
            },
            "wasInfluencedBy": {
              "@id": "prov:wasInfluencedBy",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id"
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id"
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                }
              }
            },
            "qualifiedInfluence": {
              "@id": "prov:qualifiedInfluence",
              "@type": "@id",
              "@context": {
                "influencer": {
                  "@id": "prov:influencer",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "entity": {
                  "@id": "prov:entity",
                  "@type": "@id"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id"
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "atTime": {
                          "@id": "prov:atTime",
                          "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "agent": {
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              }
            }
          }
        },
        "qualifiedGeneration": {
          "@id": "prov:qualifiedGeneration",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedCommunication": {
                  "@id": "prov:qualifiedCommunication",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "qualifiedInvalidation": {
          "@id": "prov:qualifiedInvalidation",
          "@type": "@id",
          "@context": {
            "atTime": {
              "@id": "prov:atTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "activity": {
              "@id": "prov:activity",
              "@type": "@id",
              "@context": {
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedCommunication": {
                  "@id": "prov:qualifiedCommunication",
                  "@type": "@id",
                  "@context": {
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "qualifiedDerivation": {
          "@id": "prov:qualifiedDerivation",
          "@type": "@id",
          "@context": {
            "hadGeneration": {
              "@id": "prov:hadGeneration",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "activity": {
                  "@id": "prov:activity",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "wasInfluencedBy": {
                          "@id": "prov:wasInfluencedBy",
                          "@type": "@id"
                        },
                        "qualifiedInfluence": {
                          "@id": "prov:qualifiedInfluence",
                          "@type": "@id",
                          "@context": {
                            "influencer": {
                              "@id": "prov:influencer",
                              "@type": "@id"
                            },
                            "activity": {
                              "@id": "prov:activity",
                              "@type": "@id"
                            },
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "qualifiedUsage": {
                      "@id": "prov:qualifiedUsage",
                      "@type": "@id",
                      "@context": {}
                    },
                    "qualifiedCommunication": {
                      "@id": "prov:qualifiedCommunication",
                      "@type": "@id",
                      "@context": {
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedStart": {
                      "@id": "prov:qualifiedStart",
                      "@type": "@id",
                      "@context": {
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedEnd": {
                      "@id": "prov:qualifiedEnd",
                      "@type": "@id",
                      "@context": {
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "qualifiedDelegation": {
                              "@id": "prov:qualifiedDelegation",
                              "@type": "@id",
                              "@context": {
                                "agent": {
                                  "@id": "prov:agent",
                                  "@type": "@id"
                                },
                                "hadActivity": {
                                  "@id": "prov:hadActivity",
                                  "@type": "@id"
                                }
                              }
                            },
                            "wasInfluencedBy": {
                              "@id": "prov:wasInfluencedBy",
                              "@type": "@id",
                              "@context": {
                                "href": "oa:hasTarget",
                                "rel": {
                                  "@id": "http://www.iana.org/assignments/relation",
                                  "@type": "@id",
                                  "@context": {
                                    "@base": "http://www.iana.org/assignments/relation/"
                                  }
                                },
                                "type": "dct:type",
                                "hreflang": "dct:language",
                                "title": "rdfs:label",
                                "length": "dct:extent"
                              }
                            },
                            "qualifiedInfluence": {
                              "@id": "prov:qualifiedInfluence",
                              "@type": "@id",
                              "@context": {
                                "influencer": {
                                  "@id": "prov:influencer",
                                  "@type": "@id",
                                  "@context": {
                                    "href": "oa:hasTarget",
                                    "rel": {
                                      "@id": "http://www.iana.org/assignments/relation",
                                      "@type": "@id",
                                      "@context": {
                                        "@base": "http://www.iana.org/assignments/relation/"
                                      }
                                    },
                                    "type": "dct:type",
                                    "hreflang": "dct:language",
                                    "title": "rdfs:label",
                                    "length": "dct:extent"
                                  }
                                },
                                "activity": {
                                  "@id": "prov:activity",
                                  "@type": "@id"
                                },
                                "agent": {
                                  "@id": "prov:agent",
                                  "@type": "@id",
                                  "@context": {
                                    "href": "oa:hasTarget",
                                    "rel": {
                                      "@id": "http://www.iana.org/assignments/relation",
                                      "@type": "@id",
                                      "@context": {
                                        "@base": "http://www.iana.org/assignments/relation/"
                                      }
                                    },
                                    "type": "dct:type",
                                    "hreflang": "dct:language",
                                    "title": "rdfs:label",
                                    "length": "dct:extent"
                                  }
                                }
                              }
                            }
                          }
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent",
                            "actedOnBehalfOf": {
                              "@id": "prov:actedOnBehalfOf",
                              "@type": "@id"
                            },
                            "qualifiedDelegation": {
                              "@id": "prov:qualifiedDelegation",
                              "@type": "@id",
                              "@context": {
                                "agent": {
                                  "@id": "prov:agent",
                                  "@type": "@id"
                                },
                                "hadActivity": {
                                  "@id": "prov:hadActivity",
                                  "@type": "@id"
                                }
                              }
                            }
                          }
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent",
                            "actedOnBehalfOf": {
                              "@id": "prov:actedOnBehalfOf",
                              "@type": "@id"
                            },
                            "qualifiedDelegation": {
                              "@id": "prov:qualifiedDelegation",
                              "@type": "@id",
                              "@context": {
                                "agent": {
                                  "@id": "prov:agent",
                                  "@type": "@id"
                                },
                                "hadActivity": {
                                  "@id": "prov:hadActivity",
                                  "@type": "@id"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadActivity": {
              "@id": "prov:hadActivity",
              "@type": "@id",
              "@context": {
                "wasAssociatedWith": {
                  "@id": "prov:wasAssociatedWith",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    },
                    "wasInfluencedBy": {
                      "@id": "prov:wasInfluencedBy",
                      "@type": "@id"
                    },
                    "qualifiedInfluence": {
                      "@id": "prov:qualifiedInfluence",
                      "@type": "@id",
                      "@context": {
                        "influencer": {
                          "@id": "prov:influencer",
                          "@type": "@id"
                        },
                        "activity": {
                          "@id": "prov:activity",
                          "@type": "@id"
                        },
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedUsage": {
                  "@id": "prov:qualifiedUsage",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                  }
                },
                "qualifiedStart": {
                  "@id": "prov:qualifiedStart",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedEnd": {
                  "@id": "prov:qualifiedEnd",
                  "@type": "@id",
                  "@context": {
                    "atTime": {
                      "@id": "prov:atTime",
                      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "hadActivity": {
                      "@id": "prov:hadActivity",
                      "@type": "@id"
                    }
                  }
                },
                "qualifiedAssociation": {
                  "@id": "prov:qualifiedAssociation",
                  "@type": "@id",
                  "@context": {
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "wasInfluencedBy": {
                          "@id": "prov:wasInfluencedBy",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "qualifiedInfluence": {
                          "@id": "prov:qualifiedInfluence",
                          "@type": "@id",
                          "@context": {
                            "influencer": {
                              "@id": "prov:influencer",
                              "@type": "@id",
                              "@context": {
                                "href": "oa:hasTarget",
                                "rel": {
                                  "@id": "http://www.iana.org/assignments/relation",
                                  "@type": "@id",
                                  "@context": {
                                    "@base": "http://www.iana.org/assignments/relation/"
                                  }
                                },
                                "type": "dct:type",
                                "hreflang": "dct:language",
                                "title": "rdfs:label",
                                "length": "dct:extent"
                              }
                            },
                            "activity": {
                              "@id": "prov:activity",
                              "@type": "@id"
                            },
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id",
                              "@context": {
                                "href": "oa:hasTarget",
                                "rel": {
                                  "@id": "http://www.iana.org/assignments/relation",
                                  "@type": "@id",
                                  "@context": {
                                    "@base": "http://www.iana.org/assignments/relation/"
                                  }
                                },
                                "type": "dct:type",
                                "hreflang": "dct:language",
                                "title": "rdfs:label",
                                "length": "dct:extent"
                              }
                            }
                          }
                        }
                      }
                    },
                    "hadRole": {
                      "@id": "prov:hadRole",
                      "@type": "@id"
                    },
                    "hadPlan": {
                      "@id": "prov:hadPlan",
                      "@type": "@id"
                    }
                  }
                },
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent",
                    "actedOnBehalfOf": {
                      "@id": "prov:actedOnBehalfOf",
                      "@type": "@id"
                    },
                    "qualifiedDelegation": {
                      "@id": "prov:qualifiedDelegation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadActivity": {
                          "@id": "prov:hadActivity",
                          "@type": "@id"
                        }
                      }
                    }
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id"
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent",
                        "actedOnBehalfOf": {
                          "@id": "prov:actedOnBehalfOf",
                          "@type": "@id"
                        },
                        "qualifiedDelegation": {
                          "@id": "prov:qualifiedDelegation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "hadUsage": {
              "@id": "prov:hadUsage",
              "@type": "@id",
              "@context": {
                "atTime": {
                  "@id": "prov:atTime",
                  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                }
              }
            },
            "entity": {
              "@id": "prov:entity",
              "@type": "@id"
            }
          }
        },
        "qualifiedAttribution": {
          "@id": "prov:qualifiedAttribution",
          "@type": "@id",
          "@context": {
            "agent": {
              "@id": "prov:agent",
              "@type": "@id",
              "@context": {
                "wasInfluencedBy": {
                  "@id": "prov:wasInfluencedBy",
                  "@type": "@id",
                  "@context": {
                    "wasAssociatedWith": {
                      "@id": "prov:wasAssociatedWith",
                      "@type": "@id",
                      "@context": {}
                    },
                    "qualifiedAssociation": {
                      "@id": "prov:qualifiedAssociation",
                      "@type": "@id",
                      "@context": {
                        "agent": {
                          "@id": "prov:agent",
                          "@type": "@id"
                        },
                        "hadRole": {
                          "@id": "prov:hadRole",
                          "@type": "@id"
                        },
                        "hadPlan": {
                          "@id": "prov:hadPlan",
                          "@type": "@id"
                        }
                      }
                    },
                    "href": "oa:hasTarget",
                    "rel": {
                      "@id": "http://www.iana.org/assignments/relation",
                      "@type": "@id",
                      "@context": {
                        "@base": "http://www.iana.org/assignments/relation/"
                      }
                    },
                    "type": "dct:type",
                    "hreflang": "dct:language",
                    "title": "rdfs:label",
                    "length": "dct:extent"
                  }
                },
                "qualifiedInfluence": {
                  "@id": "prov:qualifiedInfluence",
                  "@type": "@id",
                  "@context": {
                    "influencer": {
                      "@id": "prov:influencer",
                      "@type": "@id",
                      "@context": {
                        "wasAssociatedWith": {
                          "@id": "prov:wasAssociatedWith",
                          "@type": "@id",
                          "@context": {}
                        },
                        "qualifiedUsage": {
                          "@id": "prov:qualifiedUsage",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "qualifiedStart": {
                          "@id": "prov:qualifiedStart",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedEnd": {
                          "@id": "prov:qualifiedEnd",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedAssociation": {
                          "@id": "prov:qualifiedAssociation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadRole": {
                              "@id": "prov:hadRole",
                              "@type": "@id"
                            },
                            "hadPlan": {
                              "@id": "prov:hadPlan",
                              "@type": "@id"
                            }
                          }
                        },
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    },
                    "entity": {
                      "@id": "prov:entity",
                      "@type": "@id"
                    },
                    "activity": {
                      "@id": "prov:activity",
                      "@type": "@id",
                      "@context": {
                        "wasAssociatedWith": {
                          "@id": "prov:wasAssociatedWith",
                          "@type": "@id",
                          "@context": {
                            "href": "oa:hasTarget",
                            "rel": {
                              "@id": "http://www.iana.org/assignments/relation",
                              "@type": "@id",
                              "@context": {
                                "@base": "http://www.iana.org/assignments/relation/"
                              }
                            },
                            "type": "dct:type",
                            "hreflang": "dct:language",
                            "title": "rdfs:label",
                            "length": "dct:extent"
                          }
                        },
                        "qualifiedUsage": {
                          "@id": "prov:qualifiedUsage",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            }
                          }
                        },
                        "qualifiedStart": {
                          "@id": "prov:qualifiedStart",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedEnd": {
                          "@id": "prov:qualifiedEnd",
                          "@type": "@id",
                          "@context": {
                            "atTime": {
                              "@id": "prov:atTime",
                              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                            },
                            "hadActivity": {
                              "@id": "prov:hadActivity",
                              "@type": "@id"
                            }
                          }
                        },
                        "qualifiedAssociation": {
                          "@id": "prov:qualifiedAssociation",
                          "@type": "@id",
                          "@context": {
                            "agent": {
                              "@id": "prov:agent",
                              "@type": "@id"
                            },
                            "hadRole": {
                              "@id": "prov:hadRole",
                              "@type": "@id"
                            },
                            "hadPlan": {
                              "@id": "prov:hadPlan",
                              "@type": "@id"
                            }
                          }
                        }
                      }
                    },
                    "agent": {
                      "@id": "prov:agent",
                      "@type": "@id",
                      "@context": {
                        "href": "oa:hasTarget",
                        "rel": {
                          "@id": "http://www.iana.org/assignments/relation",
                          "@type": "@id",
                          "@context": {
                            "@base": "http://www.iana.org/assignments/relation/"
                          }
                        },
                        "type": "dct:type",
                        "hreflang": "dct:language",
                        "title": "rdfs:label",
                        "length": "dct:extent"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "hadMember": {
          "@id": "prov:hadMember",
          "@type": "@id"
        }
      }
    },
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "value": "prov:value",
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "http://www.w3.org/2000/01/rdf-schema#Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "http://www.w3.org/2000/01/rdf-schema#Literal"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_provenance": {
      "@id": "prov:has_provenance",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/context.jsonld)

## Sources

* [The PROV-O vocabulary](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblock-prov-schema](https://github.com/ogcincubator/bblock-prov-schema)
* Path: `_sources`


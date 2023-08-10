---
title: Provenance Chain (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - ttl: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>Provenance Chain</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Provenance Chain (Schema)
---


# Provenance Chain `ogc.ogc-utils.prov`

Schema for a provenance chain based on PROV vocabulary semantics, Agents, Activities and Entities. This schema is designed as a mix-in that can be used to add properties to other objects in a polymorphic way.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/bblock-prov-schema/blob/master/build/tests/ogc-utils/prov/" target="_blank">valid</a></strong>
</aside>

# Description

## Provenance chain

A schema defining objects that may be referenced or nested as a chain of activities.

This schema implements the PROV vocabulary semantics.


# Examples

## Example Entities with Provenance Chains

See panel to right - note that a more user friendly "collapsable" version is in development. 

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
      "endedAtTime": "2029-01-01",
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
      "endedAtTime": "2023-10-05",
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
      "endedAtTime": "2029-01-01",
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
      "endedAtTime": "2023-10-05",
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

```ttl
@prefix agents: <https://someagentregister.eg/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix prov-x: <http://www.w3.org/ns/prov-x#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix surveyreg: <https://example.org/surveys/> .
@prefix thing: <https://example.org/entities/> .

<https://example.org/DP-1> a <https://example.org/Feature> ;
    prov:featureType "Survey" ;
    prov:wasGeneratedBy surveyreg:DP-1-S1,
        surveyreg:DP-1-S2 ;
    prov-x:provenance <https://example.org/DP-2223>,
        thing:DP-1-S1 .

<https://example.org/Act3> a prov:Entity ;
    rdfs:seeAlso <https://some.gov/linktoact/> ;
    prov:wasAttributedTo agents:nz .

<https://example.org/DP-2223> a prov:Entity ;
    prov:wasGeneratedBy thing:DP-1-S1 .

<https://example.org/Example-Act> rdfs:seeAlso <https://nze.gov/linktoact/Example1> ;
    prov:wasAttributedTo agents:nz .

surveyreg:DP-1-S2 prov:activity "Registration" ;
    prov:endedAtTime "2029-01-01" ;
    prov:used <https://example.org/Example-Act> ;
    prov:wasAssociatedWith agents:bc-3 .

thing:DP-1-S1 a prov:Activity ;
    prov:endedAtTime "2023-10-05" ;
    prov:used <https://example.org/Act3> ;
    prov:wasAssociatedWith agents:ah-2344503 .


```


## Example Activity

```json
{
  "type": "Activity",
  "id": "surveyreg-nz:DP-1-S2",
  "endedAtTime": "2029-01-01",
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

```jsonld
{
  "type": "Activity",
  "id": "surveyreg-nz:DP-1-S2",
  "endedAtTime": "2029-01-01",
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

```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<surveyreg-nz:DP-1-S2> a prov:Activity ;
    prov:endedAtTime "2029-01-01" ;
    prov:used <http://www.example.com/exampleActivity/Act3> ;
    prov:wasAssociatedWith <linz-registered-surveyors:bc-3> .

<http://www.example.com/exampleActivity/Act3> a prov:Entity ;
    rdfs:seeAlso <https://some.gov/linktoact/> ;
    prov:wasAttributedTo <icsm-jurisdictions:nz> .


```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: provenance chain
$defs:
  objectref:
    $anchor: objectref
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
  Entity:
    type: object
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      featureType:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#featureType
      provenance:
        $ref: '#/$defs/Prov'
        x-jsonld-id: http://www.w3.org/ns/prov-x#provenance
        x-jsonld-type: '@id'
        x-jsonld-container: '@set'
      wasGeneratedBy:
        $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
      wasAttributedTo:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
      wasDerivedFrom:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
      links:
        type: array
        items:
          $ref: '#/$defs/externalLink'
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    required:
    - id
    anyOf:
    - properties:
        type:
          type: string
          const: Entity
          x-jsonld-id: '@type'
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
  dateOrTime:
    oneOf:
    - type: string
      format: date
      pattern: ^\d{4}-\d{2}-\d{2}$
    - type: string
      format: date-time
      pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?$
  Activity:
    type: object
    properties:
      activity:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#activity
      endedAtTime:
        $ref: '#/$defs/dateOrTime'
        x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
      wasAssociatedWith:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
      wasInformedBy:
        $ref: '#/$defs/oneOrMoreActivitiesOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
      used:
        $ref: '#/$defs/oneOrMoreEntitiesOrRefIds'
        x-jsonld-type: '@id'
        x-jsonld-id: http://www.w3.org/ns/prov#used
    anyOf:
    - properties:
        type:
          type: string
          const: Activity
          x-jsonld-id: '@type'
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
  Agent:
    type: object
    properties:
      agentType:
        $ref: '#/$defs/objectref'
        x-jsonld-id: http://www.w3.org/ns/prov#agentType
      name:
        type: string
        x-jsonld-id: foaf:name
      id:
        type: string
        format: uri
        x-jsonld-id: '@id'
      actedOnBehalfOf:
        $ref: '#/$defs/oneOrMoreAgentsOrRefIds'
        x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    required:
    - name
    anyOf:
    - properties:
        type:
          type: string
          const: Agent
          x-jsonld-id: '@type'
      required:
      - type
    - required:
      - agentType
    - required:
      - actedOnBehalfOf
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
  Entity:
    x-jsonld-id: http://www.w3.org/ns/prov#Entity
  Activity:
    x-jsonld-id: http://www.w3.org/ns/prov#Activity
  Agent:
    x-jsonld-id: http://www.w3.org/ns/prov#Agent
x-jsonld-prefixes:
  prov: http://www.w3.org/ns/prov#
  prov-x: http://www.w3.org/ns/prov-x#

```

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml" target="_blank">https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.json" target="_blank">https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "id": "@id",
    "featureType": "prov:featureType",
    "provenance": {
      "@id": "prov-x:provenance",
      "@type": "@id",
      "@container": "@set",
      "@context": {
        "used": {
          "@type": "@id",
          "@id": "prov:used"
        },
        "agentType": "prov:agentType",
        "name": "foaf:name",
        "actedOnBehalfOf": {
          "@id": "prov:actedOnBehalfOf",
          "@context": {
            "href": "@id",
            "title": "rdfs:label"
          }
        }
      }
    },
    "wasGeneratedBy": {
      "@type": "@id",
      "@id": "prov:wasGeneratedBy",
      "@context": {
        "used": {
          "@type": "@id",
          "@id": "prov:used"
        }
      }
    },
    "wasAttributedTo": {
      "@type": "@id",
      "@id": "prov:wasAttributedTo",
      "@context": {
        "href": "@id",
        "title": "rdfs:label",
        "agentType": "prov:agentType",
        "name": "foaf:name",
        "actedOnBehalfOf": "prov:actedOnBehalfOf"
      }
    },
    "wasDerivedFrom": {
      "@type": "@id",
      "@id": "prov:wasDerivedFrom"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "type": "@type",
    "activity": "prov:activity",
    "endedAtTime": "prov:endedAtTime",
    "wasAssociatedWith": {
      "@type": "@id",
      "@id": "prov:wasAssociatedWith",
      "@context": {
        "href": "@id",
        "title": "rdfs:label",
        "agentType": "prov:agentType",
        "name": "foaf:name",
        "actedOnBehalfOf": "prov:actedOnBehalfOf"
      }
    },
    "wasInformedBy": "prov:wasInformedBy",
    "used": {
      "@type": "@id",
      "@id": "prov:used",
      "@context": {
        "provenance": {
          "@id": "prov-x:provenance",
          "@type": "@id",
          "@container": "@set",
          "@context": {
            "agentType": "prov:agentType",
            "name": "foaf:name",
            "actedOnBehalfOf": {
              "@id": "prov:actedOnBehalfOf",
              "@context": {
                "href": "@id",
                "title": "rdfs:label"
              }
            }
          }
        },
        "wasGeneratedBy": {
          "@type": "@id",
          "@id": "prov:wasGeneratedBy"
        }
      }
    },
    "Entity": "prov:Entity",
    "Activity": "prov:Activity",
    "Agent": "prov:Agent",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "prov-x": "http://www.w3.org/ns/prov-x#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/context.jsonld" target="_blank">https://ogcincubator.github.io/bblock-prov-schema/build/annotated/ogc-utils/prov/context.jsonld</a>

# References

* [The PROV-O vocabulary](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/bblock-prov-schema" target="_blank">https://github.com/ogcincubator/bblock-prov-schema</a>
* Path: `_sources`


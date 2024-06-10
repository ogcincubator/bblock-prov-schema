# OGC Building Block template

This repository defines a "building block" for use of [PROV-O Vocabulary](https://www.w3.org/TR/prov-o/) in a JSON or JSON-LD implementation.

The "ready-to-use" form is generated [here:](https://ogcincubator.github.io/bblock-prov-schema/build/generateddocs/slate-build/ogc-utils/prov/index.html)

The **JSON schema** allows for either nested instances of PROV classes, or for arrays of objects linked by identifiers, and the use of external URI identifiers for PROV objects.

Such a schema is complex, and the purpose of this building block is to provide a canonical implementation supported by validation and examples.

The **JSON-LD** context binds these structures to the PROV-O vocabulary.

The **SHACL** rules perform consistency checking above and beyond schema validation.


[OGC Building Blocks](https://opengeospatial.github.io/bblocks) are defined by the Open Geospatial Consortium to support implementation of customised applications consistent with OGC specifications.

Building Blocks are supported by git actions to post-process the components, testing the structure, examples and test-case data.
This post-processing handles the complex task of integrating references to other building blocks into a ready-to use form, allowing building blocks to be composed into complete applications.  

Many such BuildingBlocks define bindings to the object structures supported by APIs (such as GeoJSON Features). 

The PROV building block defines a **"datatype"** - i.e. a sub-schema that can be used to annotate such features or *any other schema*.

## Build (local) shortcut

docker run --rm --workdir /workspace -v "$(pwd):/workspace" --pull=always ghcr.io/opengeospatial/bblocks-postprocess   --clean true --base-url https://test.org/ --generated-docs-path build-local/generateddocs --annotated-path build-local/annotated --register-file build-local/register.json --test-outputs build-local/tests

## OGC Building Block structure

Building Blocks can be reused by either:

- cut and paste "ready to use" forms from the "build/" directory

- directly reference the artefacts in the "build" directory using the URL pattern specified in the building block description

- including as source using `git submodule add {building block repository}` and referencing reused components directly. (in which case the build/ resources of the submodule will referenced in the build/ outputs, but the source definitions will be used for consistency checking and optimisation)

# Building Block development

You can find information how Building Blocks are constructed in [USAGE.md](USAGE.md).

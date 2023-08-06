# Dataset maker

The Dataset maker is responsible for:
- Loading and harmonizing data from different sources
- Keeping track of Datastory's ontology (canonical entities and concepts)
- Creating validated DDF dataset folders (with datapackage.json and csv files)
- Creating the datastory-core dataset. (A special subset of data with more custom meta data and support for translations.)

## Creating a new DDF from a source

[ to be described ]

### Adding new canonical entities and concepts

[ to be described ]


## Creating datastory-core

[ to be described ]


## Datastory Ontology

[ to be described ]


## DDF Organization

[ to be described ]


## datapackage.json

This is the format of the datapackage.json.

```
"name": "world-bank" // used as ID and SLUG. Should follow format 'my-source'
"title": "World Bank" // title of data source
"tags" : "education, sweden, swedish-education" //comma-separated tag IDs
"language": {
   "id": "en" //use same locales as Datastory, 2 letter codes or specific code if we need to support a very custom language
},
"default-indicator" : "life_expectancy", //optional helper for users who browse
"default-primary-key" : "country-year", //optional helper to show nice data default
"translations": [
    {
        "id": "ar",
    },
    {
        "id": "es"
    },
    {
        "id": "fr"
    }
],  
"license": "", 
"author": "Datastory", (or original if simply copy / paste)
"source" : "Skolverket" // shorthand if all indicators in dataset come from same source
"created": "2018-11-04T08:25:30.708697+00:00", //gets added automatically
resources : [] //gets added automatically
ddfSchema : [] //gets added automatically
```


If a source has many subcollections, we can allow this but should ideally be avoided: (another option is as meta data in concepts.csv)

```
"name": "world-bank-wdi" // 
"title": "World Bank – World development indicators" // title of collection
```

## /lang folder

[tbd]

## ddf--concepts--*.csv

A concept row has to include:
- concept
- concept_type
- name 

In addition, concept rows can define:
- collections ("World Development Indicators, Partisympatiundersölningen" etc.)
- tags ("agriculture, politics")
- description
- name_datastory (will override name)
- slug (will be used as slug, otherwise default to concept)
- source
- source_url
- updated
- unit
- scales [linear, log] (if there's a preferred default)


## ddf--entities--*.csv

An entitity row has to include:
- country (or whatever is the primary key, examples: school, region, organization)
- name 


In addition, an entity row can define:
- entity-domain columns (country belongs to region etc.) 
- string-type columns (for example capital name)
```

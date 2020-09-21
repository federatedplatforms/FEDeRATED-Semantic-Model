
`Logistics Ontologies - Ontology of Logistics concepts`
_____________________________________________________________________________________

This repository is a work in progress and it contains materials related FEDeRated project:
- Schema Registry 
-  Input materials as a reference of existing resources to create the ontology
-  Images of the structure of the ontology 

`Owner and maintenance` -- For any questions related to the ontolgoy, please contact us dena.tahvildari@tno.nl , Maaike (Add email address), and Cornlies (Add email address) 
_____________________________________________________________________________________

The Logistics Ontology (LO) 1.0 models concepts and relations important to real physical objects, event and business knowlege in logistics domain. 
It has a focus on  three main concepts Digital Twin, Business Service Overview and Event. 
LO is modelled in OWL-RDF.
Constrainsts for specific use case is modeled with Shape language. 
_____________________________________________________________________________________

LO is developed in a modular manner and is a network of three main ontologies. 

Catalaouge of the LO: 

[DigitalTwin](https://ci.tno.nl/gitlab/federated/federated/-/blob/master/Ontologies/schema-registry/DigitalTwin.ttl)

Namespace:DT
 
[Event](https://ci.tno.nl/gitlab/federated/federated/-/blob/master/Ontologies/schema-registry/Event.ttl)

Namespace:event

[businessService](https://ci.tno.nl/gitlab/federated/federated/-/blob/master/Ontologies/schema-registry/Event.ttl)

Namespace:businessService

[Classifications](https://ci.tno.nl/gitlab/federated/federated/-/blob/master/Ontologies/schema-registry/Event.ttl)

Namespace:classifications

**For practical usecases, only the Event Ontology gets populated. **


`OverView`

**Digital Twin** 
Digital twin is an generic ontology that includes representations of a real work physical object. Digital Twin Ontology has a strong focus on logistics real physical objects. 

for example: Cargo is a physical component of Digital Twin

Some of the concepts in DT ontology are: 

- Cargo
- Equipment
- Package
- Product
- Location
- transportMeans

For each of these concepts we have indentified few number of subclasses, and data attribtues. [possible to extend]


[[ Digital twin is an old term, which was coined 20 years ago, surfacing now as our society becomes more interconnected. Several studies refer to a DT as a “cyber-physical integration", with the term “Digital Twin” representing the ultimate, unachievable goal, as no model abstraction can mirror real world things with identical fidelity. For the purposes of this project we created a namespace Digtial Twin in which we model the physical component of the logistics domain. The virtual component and the relation between physical and virtual component of DT are out of the the scope of this reporsitory [Reference: https://www.sciencedirect.com/science/article/pii/S0926580519314785]]]. 


**Event**
An event reflects any physical activity in the real world, creating, updating, or 'deleting' an association between physical objects or entities. There are many synomyms based on combinations of entities, date/time, and physical activities. First, the commone data properties are given. Secondly, the specific ones are provided.
In event ontology we identify and encode common data attributes of an event. Also we identify and encode the specific event patterns. 
For example: All the event are recognisable by their Milestones. Some known vocabualries of Milestone is "start"and "end". 
every logistics event combines elements from digital twin and business service. 

Event imports DT and BusinessService. 

**businessService**
This ontology modeles the knwoledge about types of logsitics service and business side of the logistics event.  

For example:
- Transport Service is class and logistics service is a subclass of taransportService.
- Logistic Service provider is a class which it is indeitfiable by LSP name and lap website. 

Business Service is related to DT via the proeprty Role. 
Business service knowledge is used for populating Event. 

**Classifications**

Classifications ontology models knowledge about additional classifications for physical objects in DT. 

For example:
 
The nature of Cargo is modeled in Classifications ontology. 
The vocabulary list for such representation is extracted from community and standrdisation insititue (Dangerous, Excise and etc). 

Mode of transport is modeled in classifications Ontology. Mode of transport are: Road, Air, Sea and etc. 

Classifications Imports DT. 



[**Ontology Architecture**](https://365tno-my.sharepoint.com/:u:/g/personal/dena_tahvildari_tno_nl/Edwlw3OkmalMoSlG7gSnbw0BFrfZJXhFAjMeq_80hwa9Zw?email=dena.tahvildari%40tno.nl&e=5XqJhM)`

[[to add Figure 1. The UML diagram below shows the class structure of the Event ontology.]]


The inventory of all terms and their semantic roles for the first usecase is [documented here](https://365tno-my.sharepoint.com/:x:/g/personal/dena_tahvildari_tno_nl/EYHLvuukdyhDi0FxA9ZhJ3cBc7XrYixH0FH1l3RiiIXRew?email=dena.tahvildari%40tno.nl&e=Q9sk5S). 
____________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________

**Usecase: Tranposrt service **

**Application : Search and Find**

We modeled the requried cosntrainsts using shacl language.  

@prefix searchFind: http://tno.io/searchFind# . 

The constrainsts are identified based the requriemetns of the application search and find. 

The collection of [constrainsts](https://365tno-my.sharepoint.com/:x:/g/personal/dena_tahvildari_tno_nl/EYHLvuukdyhDi0FxA9ZhJ3cBc7XrYixH0FH1l3RiiIXRew?email=dena.tahvildari%40tno.nl&e=Q9sk5S) in common language can be found here: 


________________________________________________________________________________________________________________________________________

Test: [IN PROGRESS] 

Piepline test. 

Data must be mapped to ontology = dataGraph.ttl
DataGraph must be checked against the searchFind.ttl

We use Pyshacl library https://github.com/RDFLib/pySHAC for validating the searchFind.ttl 

For basic use of this module, you can just call the validate function of the pyshacl module like this:


``from pyshacl import validate``

```
r = validate(data_graph, shacl_graph=sg, ont_graph=og, inference='rdfs', abort_on_error=False, meta_shacl=False, advanced=False, debug=False)
conforms, results_graph, results_text = r
```



















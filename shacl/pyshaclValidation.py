### Imports ###
from pyshacl import validate
import rdflib

path = '../'

### Load data graph ###
data_graph = rdflib.Graph()
data_graph.parse(path + 'individuals/eventSample.ttl', format= "ttl")

### Load shacl graph ###
shapes_graph = rdflib.Graph()
shapes_graph.parse('[Incident]EFTIRetrieval.shapes.ttl', format="ttl")

### Load all ontology graphs in one ###
ont_graph = rdflib.Graph()
ont_graph.parse(path + 'DigitalTwin.ttl', format="ttl")
ont_graph.parse(path + 'BusinessService.ttl', format="ttl")
ont_graph.parse(path + 'Event.ttl', format="ttl")
ont_graph.parse(path + 'Classifications.ttl', format="ttl")

### Validation ###
r = validate(data_graph = data_graph, shacl_graph = shapes_graph, ont_graph = ont_graph, inference='rdfs', abort_on_error=False, meta_shacl=False, advanced=False, debug=False)

conforms, results_graph, results_text = r

print(results_text)
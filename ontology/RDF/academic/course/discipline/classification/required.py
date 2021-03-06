from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class Required(object):
    """
    Required
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Required'),
            subClassOf,
            URIRef(pp + 'Classification'),
        ))
        graph.add((
            URIRef(pp + 'Required'),
            title,
            Literal('Required', lang='en')
        ))

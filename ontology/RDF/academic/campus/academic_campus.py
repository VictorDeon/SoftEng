from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .FGA import FGA


class AcademicCampus(object):
    """
    Academic Campus
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Academic_Campus'),
            subClassOf,
            URIRef(pp + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Academic_Campus'),
            title,
            Literal('Academic Campus', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        FGA(self.graph)

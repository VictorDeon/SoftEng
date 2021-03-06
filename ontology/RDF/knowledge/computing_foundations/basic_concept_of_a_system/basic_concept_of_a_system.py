from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge
from .emergent_system_properties import EmergentSystemProperties
from .overview_of_a_computer_system import OverviewOfAComputerSystem
from .systems_engineering import SystemsEngineering

text = """
Ian Sommerville writes, “a system is a purposeful collection of interrelated components that work together to achieve some objective”.  A system can be very simple and include only a few components, like an ink pen, or rather complex, like an aircraft. Depending on whether humans are part of the system, systems can be divided into technical computer-based systems and sociotechnical systems.  A technical computer-based system functions without human involvement, such as televisions, mobile phones, thermostat, and some software; a sociotechnical system will not function without human involvement.  Examples of such system include manned space vehicles, chips embedded inside a human, and so forth.
"""


class BasicConceptOfASystem(object):
    """
    Topic: Basic Concept of a System
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
            typeOf,
            URIRef(knowledge + 'Topic'),
        ))
        graph.add((
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
            title,
            Literal('Basic Concept of a System', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        EmergentSystemProperties(self.graph)
        OverviewOfAComputerSystem(self.graph)
        SystemsEngineering(self.graph)

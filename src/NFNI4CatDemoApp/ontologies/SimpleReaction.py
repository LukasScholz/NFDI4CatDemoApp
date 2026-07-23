from owlready2 import *
from NFNI4CatDemoApp.Exceptions.InformationException import MissingDataException

onto = get_ontology("http://test.org/onto.owl")


with onto:

    class Metabolites(Thing):
        def __repr__(self):
            return self.name

    class Reagents(Metabolites):
        pass

    class Products(Metabolites):
        pass


    class Reaction(Thing):
        def react(self):
            raise MissingDataException("The Reaction is missing key components", 404)


    class has_reagents_setup(Reaction >> Reagents):
        python_name = "reagents"

    class has_products_setup(Reaction >> Products):
        python_name = "products"


    class ReactionAssociation(Reaction):
        equivalent_to = [Reaction & has_reagents_setup.some(Reagents) & has_products_setup.some(Products)]
        def react(self):
            print(f"The metabolites {self.reagents} reactet to {self.products}" )
            return True  # Exit Code

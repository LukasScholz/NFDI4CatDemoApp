
import unittest

from NFNI4CatDemoApp.ontologies.SimpleReaction import *

TRIPLESTORE_FOLDER = "./test/triplestores/"

class TestTriplestore(unittest.TestCase):
    def test_alanin_transaminase(self):
        # Reagents
        alanin = Reagents("l-alanin")
        oxoglutarate = Reagents("2-oxoglutarate")

        # Products
        pyruvate = Products("pyruvate")
        glutamate = Products("L-glutamate")

        # Reaction
        AllDifferent([alanin, oxoglutarate, pyruvate, glutamate])
        reaction = Reaction(reagents=[alanin, oxoglutarate], products=[pyruvate, glutamate])


        close_world(Reaction)
        sync_reasoner_pellet()

        reaction.react()
        graph = default_world.as_rdflib_graph()

        with open(TRIPLESTORE_FOLDER+"alanin_transaminase.txt", "w") as file:
            for subject, predicate, object in graph:
                file.write(f"{subject}, {predicate}, {object}\n")


    def test_cysteine_transaminase(self):
        # Reagents
        cystein = Reagents("l-cysteine")
        oxoglutarate = Reagents("2-oxoglutarate")

        # Products
        sulfanylpropanoate = Products("2-oxo-3-sulfanylpropanoate")
        glutamate = Products("L-glutamate")

        # Reaction
        AllDifferent([cystein, oxoglutarate, sulfanylpropanoate, glutamate])
        reaction = Reaction(reagents=[cystein, oxoglutarate], products=[sulfanylpropanoate, glutamate])

        close_world(Reaction)
        sync_reasoner_pellet()

        reaction.react()
        graph = default_world.as_rdflib_graph()

        with open(TRIPLESTORE_FOLDER + "cysteine_transaminase.txt", "w") as file:
            for subject, predicate, object in graph:
                file.write(f"{subject}, {predicate}, {object}\n")


    def test_aspartate_transaminase(self):
        # Reagents
        aspartate = Reagents("L-aspartate")
        oxoglutarate = Reagents("2-oxoglutarate")

        # Products
        oxaloacetate = Products("oxaloacetate")
        glutamate = Products("L-glutamate")

        # Reaction
        AllDifferent([aspartate, oxoglutarate, oxaloacetate, glutamate])
        reaction = Reaction(reagents=[aspartate, oxoglutarate], products=[oxaloacetate, glutamate])

        close_world(Reaction)
        sync_reasoner_pellet()

        reaction.react()
        graph = default_world.as_rdflib_graph()

        with open(TRIPLESTORE_FOLDER + "aspartate_transaminase.txt", "w") as file:
            for subject, predicate, object in graph:
                file.write(f"{subject}, {predicate}, {object}\n")


if __name__ == "__main__":
    unittest.main()
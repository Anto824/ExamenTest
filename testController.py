from Tache import Tache
from Controller import TacheController
from Projet import Projet
from GestionTaches import GestionTaches


import unittest
from io import StringIO
import sys

class TestTacheController(unittest.TestCase):
    def test_afficher_taches(self):
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        output = StringIO()
        sys.stdout = output
        controller.afficher_taches()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Tache 1\nTache 2\n")

    def test_afficher_tache_par_titre(self):
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        output = StringIO()
        sys.stdout = output
        controller.afficher_tache_par_titre("Tache 1")
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Tache 1\n")
        
    def test_afficher_tache_par_titre_not_found(self):
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        output = StringIO()
        sys.stdout = output
        controller.afficher_tache_par_titre("Tache 3")
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Tache not found\n")
        
if __name__ == '__main__':
    unittest.main()
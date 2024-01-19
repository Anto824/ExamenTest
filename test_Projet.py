import unittest
from GestionTaches import GestionTaches
from Tache import Tache
from Projet import Projet

class TestProjet(unittest.TestCase):
    def setUp(self):
        self.taches = [Tache("Tache 1", "Description de la tache")]

    def test_ajouter_tache(self):
        projet = Projet("Projet 1", self.taches)
        projet.ajouter_tache("Nouvelle Tache", "Description de la nouvelle tache")
        self.assertEqual(len(projet.taches), 2)

    def test_completer_tache(self):
        projet = Projet("Projet 1", self.taches)
        projet.completer_tache("Tache 1")
        self.assertTrue(projet.taches[0].complet)

    def test_verifier_tache(self):
        projet = Projet("Projet 1", self.taches)
        self.assertFalse(projet.verifier_tache("Tache 1"))

if __name__ == '__main__':
    unittest.main()

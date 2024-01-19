import unittest
from GestionTaches import GestionTaches
from Tache import Tache

class TestGestionTaches(unittest.TestCase):
    def test_completer_tache(self):
        tache = Tache("Tache 1", "Description de la tache")
        GestionTaches.completer_tache("Tache 1", [tache])
        self.assertTrue(tache.complet)

    def test_verifier_tache(self):
        tache = Tache("Tache 1", "Description de la tache")
        self.assertFalse(GestionTaches.verifier_tache("Tache 1", [tache]))

if __name__ == '__main__':
    unittest.main()

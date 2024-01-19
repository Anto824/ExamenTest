import unittest
from GestionTaches import GestionTaches
from Tache import Tache
from Projet import Projet

class TestProjet(unittest.TestCase):
    def setUp(self):
        # Initialisation avec une tâche pour les tests
        self.taches = [Tache("Tache 1", "Description de la tache")]

    def test_ajouter_tache(self):
        # Teste l'ajout d'une nouvelle tâche au projet
        projet = Projet("Projet 1", self.taches)
        projet.ajouter_tache("Nouvelle Tache", "Description de la nouvelle tache")
        self.assertEqual(len(projet.taches), 2)

    def test_completer_tache(self):
        # Teste la complétion d'une tâche dans le projet
        projet = Projet("Projet 1", self.taches)
        projet.completer_tache("Tache 1")
        self.assertTrue(projet.taches[0].complet)

    def test_verifier_tache(self):
        # Teste la vérification de l'état (complet ou non) d'une tâche dans le projet
        projet = Projet("Projet 1", self.taches)
        self.assertFalse(projet.verifier_tache("Tache 1"))

    def test_duree_totale(self):
        # Teste le calcul de la durée totale des tâches dans le projet
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache1.ajouter_duree(5)
        tache2 = Tache("Tache 2", "Description de la tache 2")
        tache2.ajouter_duree(5)
        tache3 = Tache("Tache 3", "Description de la tache 3")
        tache3.ajouter_duree(2)
        taches = [tache1, tache2, tache3]
        projet = Projet("Projet 1", taches)
        self.assertEqual(projet.calculer_duree_totale(), 12)

    def test_duree_totale_vide(self):
        # Teste le calcul de la durée totale pour un projet sans tâches
        taches = []
        projet = Projet("Projet 1", taches)
        self.assertFalse(projet.calculer_duree_totale())

if __name__ == '__main__':
    unittest.main()

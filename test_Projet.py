import unittest
from GestionTaches import GestionTaches
from Projet import Projet


class TestProjet(unittest.TestCase):

    def test_ajouter_tache_au_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Projet 1", gestion_taches)
        projet.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertEqual(len(projet.taches), 1)
        self.assertEqual(projet.taches[0]["titre"], "Tâche 1")
        self.assertEqual(projet.taches[0]["complet"], False)
        self.assertEqual(len(gestion_taches.taches), 1)
        self.assertEqual(gestion_taches.taches[0]["titre"], "Tâche 1")
        self.assertEqual(gestion_taches.taches[0]["complet"], False)

    def test_completer_tache_du_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Projet 1", gestion_taches)
        projet.ajouter_tache("Tâche 1", "Description de la tâche 1")
        projet.completer_tache("Tâche 1")
        self.assertTrue(projet.verifier_tache("Tâche 1"))
        self.assertTrue(gestion_taches.verifier_tache("Tâche 1"))

    def test_verifier_tache_non_completee_du_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Projet 1", gestion_taches)
        projet.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertFalse(projet.verifier_tache("Tâche 1"))
        self.assertFalse(gestion_taches.verifier_tache("Tâche 1"))

    def test_verifier_tache_completee_du_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Projet 1", gestion_taches)
        projet.ajouter_tache("Tâche 1", "Description de la tâche 1")
        projet.completer_tache("Tâche 1")
        self.assertTrue(projet.verifier_tache("Tâche 1"))
        self.assertTrue(gestion_taches.verifier_tache("Tâche 1"))

    def test_completer_tache_inexistante_du_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Projet 1", gestion_taches)
        projet.ajouter_tache("Tâche 1", "Description de la tâche 1")
        projet.completer_tache("Tâche 2")
        self.assertFalse(projet.verifier_tache("Tâche 2"))
        self.assertFalse(gestion_taches.verifier_tache("Tâche 2"))


if __name__ == '__main__':
    unittest.main()

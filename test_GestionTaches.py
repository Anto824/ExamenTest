import unittest
import GestionTaches

class TestGestionTaches(unittest.TestCase):

    def test_ajouter_tache(self):
        gestion_taches = GestionTaches()
        gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertEqual(len(gestion_taches.taches), 1)
        self.assertEqual(gestion_taches.taches[0]["titre"], "Tâche 1")
        self.assertEqual(gestion_taches.taches[0]["complet"], False)
        gestion_taches.ajouter_tache("Tâche 2", "Description de la tâche 2")
        self.assertEqual(len(gestion_taches.taches), 2)
        self.assertEqual(gestion_taches.taches[1]["titre"], "Tâche 2")
        self.assertEqual(gestion_taches.taches[1]["complet"], False)
        

    def test_completer_tache(self):
        gestion_taches = GestionTaches()
        gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        gestion_taches.completer_tache("Tâche 1")
        self.assertTrue(gestion_taches.verifier_tache("Tâche 1"))

    def test_verifier_tache_non_completee(self):
        gestion_taches = GestionTaches()
        gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertFalse(gestion_taches.verifier_tache("Tâche 1"))

    def test_verifier_tache_completee(self):
        gestion_taches = GestionTaches()
        gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        gestion_taches.completer_tache("Tâche 1")
        self.assertTrue(gestion_taches.verifier_tache("Tâche 1"))
        
    def test_completer_tache_inexistante(self):
        gestion_taches = GestionTaches()
        gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        gestion_taches.completer_tache("Tâche 2")
        self.assertFalse(gestion_taches.verifier_tache("Tâche 2"))

if __name__ == '__main__':
    unittest.main()

# Importation des modules requis
import unittest
from GestionTaches import GestionTaches
from Tache import Tache

# Début de la classe de test
class TestGestionTaches(unittest.TestCase):
    def test_completer_tache(self):
        # Création d'une instance de la classe Tache
        tache = Tache("Tache 1", "Description de la tache")
        # Appel de la méthode completer_tache de la classe GestionTaches
        GestionTaches.completer_tache("Tache 1", [tache])
        # Vérification que la tâche est complétée
        self.assertTrue(tache.complet)

    def test_verifier_tache(self):
        # Création d'une instance de la classe Tache
        tache = Tache("Tache 1", "Description de la tache")
        # Appel de la méthode verifier_tache de la classe GestionTaches
        # Vérification que la tâche n'est pas complétée
        self.assertFalse(GestionTaches.verifier_tache("Tache 1", [tache]))

# Point d'entrée du programme
if __name__ == '__main__':
    # Exécution des tests
    unittest.main()

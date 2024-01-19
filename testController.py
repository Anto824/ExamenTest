from Tache import Tache
from Controller import TacheController
from Projet import Projet
from GestionTaches import GestionTaches

import unittest
from io import StringIO
import sys

class TestTacheController(unittest.TestCase):
    def test_afficher_taches(self):
        # Crée des tâches, un contrôleur et teste l'affichage des tâches
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        # Redirige la sortie standard vers un objet StringIO pour la capture
        output = StringIO()
        sys.stdout = output
        controller.afficher_taches()
        sys.stdout = sys.__stdout__  # Restaure la sortie standard
        self.assertEqual(output.getvalue(), "Tache 1\nTache 2\n")

    def test_afficher_tache_par_titre(self):
        # Crée des tâches, un contrôleur et teste l'affichage d'une tâche spécifique par titre
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        # Redirige la sortie standard vers un objet StringIO pour la capture
        output = StringIO()
        sys.stdout = output
        controller.afficher_tache_par_titre("Tache 1")
        sys.stdout = sys.__stdout__  # Restaure la sortie standard
        self.assertEqual(output.getvalue(), "Tache 1\n")
        
    def test_afficher_tache_par_titre_not_found(self):
        # Crée des tâches, un contrôleur et teste l'affichage d'un message pour une tâche non trouvée
        tache1 = Tache("Tache 1", "Description de la tache 1")
        tache2 = Tache("Tache 2", "Description de la tache 2")
        taches = [tache1, tache2]
        controller = TacheController(taches)

        # Redirige la sortie standard vers un objet StringIO pour la capture
        output = StringIO()
        sys.stdout = output
        controller.afficher_tache_par_titre("Tache 3")
        sys.stdout = sys.__stdout__  # Restaure la sortie standard
        self.assertEqual(output.getvalue(), "Tache not found\n")

if __name__ == '__main__':
    unittest.main()

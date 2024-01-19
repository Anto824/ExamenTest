import Projet


class GestionTaches:
    def __init__(self, Projet):
        self.taches = []
        self.Projet = Projet()

    def completer_tache(self, titre):
        """Marque une tâche comme complétée."""
        for tache in self.Projet.taches:
            if tache["titre"] == titre:
                tache["complet"] = True
                return
        print(f"Tâche avec le titre '{titre}' non trouvée.")

    def verifier_tache(self, titre):
        """Vérifie si une tâche est complétée."""
        for tache in self.Projet.taches:
            if tache["titre"] == titre:
                return tache["complet"]
        print(f"Tâche avec le titre '{titre}' non trouvée.")
        return False

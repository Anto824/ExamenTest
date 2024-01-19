class GestionTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, titre, description):
        """Ajoute une nouvelle tâche au projet."""
        for tache in self.taches:
            if tache["titre"] == titre:
                print(f"Tâche avec le titre '{titre}' déjà existante.")
                return

        nouvelle_tache = {"titre": titre, "description": description, "complet": False}
        self.taches.append(nouvelle_tache)

    def completer_tache(self, titre):
        """Marque une tâche comme complétée."""
        for tache in self.taches:
            if tache["titre"] == titre:
                tache["complet"] = True
                return
        print(f"Tâche avec le titre '{titre}' non trouvée.")

    def verifier_tache(self, titre):
        """Vérifie si une tâche est complétée."""
        for tache in self.taches:
            if tache["titre"] == titre:
                return tache["complet"]
        print(f"Tâche avec le titre '{titre}' non trouvée.")
        return False

# Exemple d'utilisation
gestion_taches = GestionTaches()
gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
gestion_taches.ajouter_tache("Tâche 2", "Description de la tâche 2")

gestion_taches.completer_tache("Tâche 1")
print(gestion_taches.verifier_tache("Tâche 1"))  # True
print(gestion_taches.verifier_tache("Tâche 2"))  # False (non complétée)

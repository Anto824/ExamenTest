class Projet:
    def __init__(self, nom, taches):
        self.nom = nom
        self.taches = taches

    def ajouter_tache(self, titre, description):
        """Ajoute une nouvelle tâche au projet."""
        for tache in self.taches:
            if tache["titre"] == titre:
                print(f"Tâche avec le titre '{titre}' déjà existante.")
                return
        nouvelle_tache = {"titre": titre, "description": description, "complet": False}
        self.taches.append(nouvelle_tache)
        
        



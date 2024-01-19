from GestionTaches import GestionTaches
from Tache import Tache


class Projet:
    def __init__(self, nom, taches):
        self.nom = nom
        self.taches = taches

    def ajouter_tache(self, titre, description):
        """Ajoute une nouvelle tâche au projet."""
        for tache in self.taches:
            if tache.titre == titre:
                print(f"Tâche avec le titre '{titre}' déjà existante.")
                return
        nouvelle_tache = Tache(titre, description, complet=False)
        self.taches.append(nouvelle_tache)

    def completer_tache(self, titre):
        return GestionTaches.completer_tache(titre, self.taches)

    def verifier_tache(self, titre):
        return GestionTaches.verifier_tache(titre, self.taches)
    
    def calculer_duree_totale(self):
        """Calcule la durée totale nécessaire pour toutes les tâches d'un projet."""
        if len(self.taches) == 0:
            return False
        duree_totale = 0
        for tache in self.taches:
            duree_totale += tache.duree
        return duree_totale

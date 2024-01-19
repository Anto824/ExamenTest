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

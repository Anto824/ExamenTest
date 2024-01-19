class Tache:
    def __init__(self, titre, description, complet=False):
        self.titre = titre
        self.description = description
        self.complet = complet

class GestionTaches:
    taches = []

    @classmethod
    def completer_tache(cls, titre):
        """Marque une tâche comme complétée."""
        for tache in cls.taches:
            if tache.titre == titre:
                tache.complet = True
                return
        raise Exception(f"Tâche avec le titre '{titre}' non trouvée.")

    @classmethod
    def verifier_tache(cls, titre):
        """Vérifie si une tâche est complétée."""
        for tache in cls.taches:
            if tache.titre == titre:
                return tache.complet
        raise Exception(f"Tâche avec le titre '{titre}' non trouvée.")

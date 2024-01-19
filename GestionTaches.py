class GestionTaches:
    @classmethod
    def completer_tache(cls, titre, taches):
        """Marque une tâche comme complétée."""
        for tache in taches:
            if tache.titre == titre:
                tache.complet = True
                return
        raise Exception(f"Tâche avec le titre '{titre}' non trouvée.")

    @classmethod
    def verifier_tache(cls, titre, taches):
        """Vérifie si une tâche est complétée."""
        for tache in taches:
            if tache.titre == titre:
                return tache.complet
        raise Exception(f"Tâche avec le titre '{titre}' non trouvée.")

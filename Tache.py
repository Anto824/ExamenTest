class Tache:
    def __init__(self, titre, description, complet=False):
        self.titre = titre
        self.description = description
        self.complet = complet
        self.duree = 0  # Initialize duration to 0
    def ajouter_duree(self, duree):
        if duree >= 0:  # Add condition to ensure duration is greater than or equal to 0
            self.duree = duree

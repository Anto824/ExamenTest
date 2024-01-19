# Definition de la classe Tache
class Tache:
    def __init__(self, titre, description, complet=False):
        self.titre = titre
        self.description = description
        self.complet = complet
        self.duree = 0  # initialisation de la durée à 0

    # methode pour ajouter une durée à une tache
    def ajouter_duree(self, duree):
        if duree >= 0:  # Ajoute la durée si et seulement si elle est positive
            self.duree = duree

from Tache import Tache

class TacheController:
    def __init__(self, taches):
        self.taches = taches

    def afficher_taches(self):
        # Affiche les titres de toutes les tâches
        for tache in self.taches:
            print(tache.titre)

    def afficher_tache_par_titre(self, titre):
        # Affiche le titre de la tâche correspondant au titre donné en paramètre
        for tache in self.taches:
            if tache.titre == titre:
                print(tache.titre)
                return
        print("Tache not found")
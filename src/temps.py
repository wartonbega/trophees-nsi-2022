from utils.Date import Date
from Gestion import Gestion

class Temps:
    LIMITE = 120
    actuel = Date.get_date()
    date_ig = "00/00"
    ajout = 0

    def avancement(self, ajouter:int) -> str:
        self.ajout += ajouter
        self.date_ig = Date.ajouter_mois(self.ajout)
        self.verification()
        return self.date_ig

    def verification(self) -> bool:
        if self.ajout == self.LIMITE:
            Gestion.fin_jeu(1)

def filter_farben(liste):
    farben = ["rot", "grün", "blau", "gelb", "schwarz", "weiß"]
    return [farbe for farbe in liste if len(farbe) > 3]
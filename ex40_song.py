class Song(object):
    def __init__(self, canzone):
        self.canzone = canzone

    def cantare(self):
        for line in self.canzone:
            print line

inno_italia = Song(["Fratelli di Italia",
                "Siamo messi un pochino male",
                "Dobbiamo lavorare per ricominciare!"])

inno_italia.cantare()

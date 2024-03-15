class festivals:
    def celebrate(self):
        print("Festivals enhance cultural and social relations.")
class diwali(festivals):
    def celebrate(self):
        super().celebrate()
        print("with crackers")
class holi(festivals):
    def celebrate(self):
        super().celebrate()
        print("with colors")
d = diwali()
d.celebrate()
h = holi()
h.celebrate()
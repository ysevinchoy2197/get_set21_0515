class Train:
    company = "Uzbekiston Temir Yollari"

    def __init__(self, name, wagons):
        self.name = name
        self.wagons = wagons

    def show_info(self):
        print(f"Poyezd: {self.name}")
        print(f"Vagonlar: {self.wagons}")


t1 = Train("Afrosiyob", 12)
t2 = Train("Sharq", 10)

t1.show_info()
print("----------")
t2.show_info()

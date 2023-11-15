class TRAIN:
    def __init__(self, NAZN, NUMR, TIME):
        self.NAZN = NAZN
        self.NUMR = NUMR
        self.TIME = TIME

# introducerea in baza de date
def input_trains():
    RASР = []
    for i in range(8):
        print(f"Informatia despre tren {i + 1}:")
        NAZN = input("Punct final: ")
        NUMR = input("Nr de tren: ")
        TIME = input("Timpuul plecarii: ")
        train = TRAIN(NAZN, NUMR, TIME)
        RASР.append(train)
    return RASР

# sortare
def sort_trains_by_destination(trains):
    return sorted(trains, key=lambda x: x.NAZN)

# afisare sortare dupa timp
def print_trains_after_time(trains, input_time):
    found_trains = False
    for train in trains:
        if train.TIME > input_time:
            found_trains = True
            print(f"DEN: {train.NAZN}, NUMR: {train.NUMR}, TIME: {train.TIME}")
    if not found_trains:
        print("Nu a fost gasit nici un tren dupa timp.")

#main
if __name__ == "__main__":
    RASР = input_trains()
    RASР = sort_trains_by_destination(RASР)

    input_time = input("INtroduceti timpul  (in format HH:MM): ")

    print("Informatia despre tren:")
    print_trains_after_time(RASР, input_time)

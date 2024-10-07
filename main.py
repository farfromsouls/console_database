from baseClass import carBase

class Car(carBase):
    
    def polling():
        task = input("read(r), create(c), delete(d)\n")

        if task == "r":
            Car.read()

        elif task == "c":
            name = input("Enter name: ")
            try:
                year = int(input("Enter year: "))
                cost = int(input("Enter cost: "))
                color = input("Enter color: ")
                description = input("Description (optional): ")
                Car(name, year, cost, color, description)
            except:
                print("Некорректный ввод")


    # infinit polling
if __name__ == "__main__":
    while True:
        Car.polling()
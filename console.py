import json
import os


class Car:
    def __init__(self, model, year, cost, prob, color, dtp):
        self.model = model
        self.year = year
        self.cost = cost
        self.prob = prob
        self.color = color
        self.dtp = dtp

    def to_dict(self):
        return {
            "model": self.model,
            "year": self.year,
            "cost": self.cost,
            "prob": self.prob,
            "color": self.color,
            "dtp": self.dtp
        }

    def __str__(self):
        return (f"Model: {self.model}, Year: {self.year}, Cost: {self.cost}, "
                f"Mileage: {self.prob}, Color: {self.color}, DTPs: {self.dtp}")


class CarDatabase:
    def __init__(self, filename="cars.json"):
        self.filename = filename
        self.cars = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.cars = [Car(**car) for car in data]

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump([car.to_dict() for car in self.cars], file, indent=2)

    def add_car(self, car):
        self.cars.append(car)
        self.save_data()

    def remove_car(self, index):
        if 0 <= index < len(self.cars):
            del self.cars[index]
            self.save_data()
            return True
        return False

    def find_car(self, attribute, value):
        return [car for car in self.cars if getattr(car, attribute) == value]

    def update_car(self, index, attribute, value):
        if 0 <= index < len(self.cars):
            setattr(self.cars[index], attribute, value)
            self.save_data()
            return True
        return False

    def display_cars(self):
        for i, car in enumerate(self.cars):
            print(f"{i}: {str(car)}")


def main():
    db = CarDatabase()

    while True:
        print("\n1. Найти автомобиль")
        print("2. удалить автомобиль")
        print("3. найти автомобиль")
        print("4. обновить автомобиль")
        print("5. отобразить все автомобили")
        print("6. выход")

        choice = input("Enter your choice: ")

        if choice == "1":
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            cost = float(input("Enter cost: "))
            prob = float(input("Enter prob (mileage): "))
            color = input("Enter color: ")
            dtp = int(input("Enter number of DTPs: "))
            car = Car(model, year, cost, prob, color, dtp)
            db.add_car(car)
            print("Car added successfully.")

        elif choice == "2":
            index = int(input("Enter the index of the car to remove: "))
            if db.remove_car(index):
                print("Car removed successfully.")
            else:
                print("Invalid index.")

        elif choice == "3":
            attribute = input(
                "Enter element to search by (model/year/cost/prob/color/dtp): ")
            value = input("Enter value to search: ")
            if attribute in ["year", "dtp"]:
                value = int(value)
            elif attribute in ["cost", "prob"]:
                value = float(value)
            results = db.find_car(attribute, value)
            if results:
                for car in results:
                    print(str(car))
            else:
                print("No cars found.")

        elif choice == "4":
            index = int(input("Enter the index of the car to update: "))
            attribute = input(
                "Enter attribute to update (model/year/cost/prob/color/dtp): ")
            value = input("Enter new value: ")
            if attribute in ["year", "dtp"]:
                value = int(value)
            elif attribute in ["cost", "prob"]:
                value = float(value)
            if db.update_car(index, attribute, value):
                print("Car updated successfully.")
            else:
                print("Invalid index.")

        elif choice == "5":
            db.display_cars()

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

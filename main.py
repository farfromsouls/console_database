#  Реализация CRUD
class AutoCRUD():

    def getLastId(base):
        return base.count("\n")

    def create(name, year, cost):
        id = AutoCRUD.getLastId("\n".join(AutoCRUD.read()))
        with open("base.txt", "a") as f:
            f.write(f'{id} {name} {year} {cost}\n')

    def read():
        with open("base.txt") as f:
            base = f.read().split("\n")
            return base

    def delete(id):
        base = AutoCRUD.read()
        with open("base.txt", "w") as f:
            for line in base:
                if line.split(" ")[0] != id:
                    f.write(line + "\n")

    def update(id, name, year, cost):
        base = AutoCRUD.read()
        with open("base.txt", "w") as f:
            for line in base:
                if line.split(" ")[0] != id:
                    f.write(line + "\n")
                else:
                    f.write(f"{id} {name} {year} {cost}\n")


#  Пользовательский интерфейс
if __name__ == "__main__":
    while True:

        task = input("\nВозможные запросы: create, read, update, delete\n")

        if task == "create":
            try:
                data = input(
                    "Ведите название, год, цену (через пробел)\n").split()
                AutoCRUD.create(name=data[0], year=data[1], cost=data[2])
            except:
                print("Некорректный ввод")

        elif task == "read":
            print(AutoCRUD.read())

        elif task == "update":
            data = input(
                "Введите id элементаn и новые значения название, год, цену (через пробел)\n"
            ).split()
            AutoCRUD.update(id=data[0],
                            name=data[1],
                            year=data[2],
                            cost=data[3])

        elif task == "delete":
            AutoCRUD.delete(input("Введите id элемента\n"))

        else:
            print("Некорректный ввод")

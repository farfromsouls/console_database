class carBase:
    def __init__(self, name: str,
                 year: int,
                 cost: int,
                 color: str,
                 description=None):
        self.id = carBase.__getLastId__(self)
        self.name = name
        self.year = year
        self.cost = cost
        self.color = color
        self.description = description
        carBase.__addToBase__(self)

    def read():
        with open("base.txt", "r") as f:
            print("\nid|name|year|cost|color|description")
            print("----------------------")
            for i in f.read().replace("|", " ").split("\n")[:-1]:
                print(i)
            print("----------------------\n")

    def delete(id):
        with open("base.txt", "r") as r:
            lines = r.readlines()
            with open("base.txt", "w") as d:
                for line in lines:
                    if line.split("|")[0] != str(id):
                        d.write(line)

    def __getLastId__(self):
        with open("base.txt", "r") as f:
            return f.read().count("\n")

    def __addToBase__(self):
        with open("base.txt", "a") as f:
            f.write(f"{self.id}|{self.name}|{self.year}|"
            + f"{self.cost}|{self.color}|{self.description}\n")
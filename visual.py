import tkinter as tk
from tkinter import ttk, messagebox
import json

class CarApp:
    def __init__(self, root, filename="cars.json"):
        self.root = root
        self.root.title("Car Database")
        self.filename = filename

        self.tree = ttk.Treeview(root, columns=('model', 'year', 'cost', 'prob', 'color', 'dtp'), show='headings')
        self.tree.heading('model', text='Model')
        self.tree.heading('year', text='Year')
        self.tree.heading('cost', text='Cost')
        self.tree.heading('prob', text='Mileage')
        self.tree.heading('color', text='Color')
        self.tree.heading('dtp', text='DTPs')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_data()
        self.add_buttons()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                cars = json.load(file)
                for car in cars:
                    self.tree.insert('', tk.END, values=(car['model'], car['year'], car['cost'], car['prob'], car['color'], car['dtp']))
        except FileNotFoundError:
            print(f"File {self.filename} not found.")

    def add_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)

        add_button = tk.Button(frame, text="Add Car", command=self.add_car)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        delete_button = tk.Button(frame, text="Delete Car", command=self.delete_car)
        delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        update_button = tk.Button(frame, text="Update Car", command=self.update_car)
        update_button.pack(side=tk.LEFT, padx=5, pady=5)

        search_button = tk.Button(frame, text="Search Car", command=self.search_car)
        search_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_car(self):
        car = {}
        car['model'] = tk.StringVar()
        car['year'] = tk.StringVar()
        car['cost'] = tk.StringVar()
        car['prob'] = tk.StringVar()
        car['color'] = tk.StringVar()
        car['dtp'] = tk.StringVar()

        def submit():
            car['model'] = model_entry.get()
            car['year'] = year_entry.get()
            car['cost'] = cost_entry.get()
            car['prob'] = prob_entry.get()
            car['color'] = color_entry.get()
            car['dtp'] = dtp_entry.get()

            self.tree.insert('', tk.END, values=(car['model'], car['year'], car['cost'], car['prob'], car['color'], car['dtp']))

            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.get_all_cars(), file)

            window.destroy()

        window = tk.Toplevel(self.root)
        window.title("Add Car")

        model_label = tk.Label(window, text="Model:")
        model_label.grid(row=0, column=0, padx=5, pady=5)
        model_entry = tk.Entry(window, textvariable=car['model'])
        model_entry.grid(row=0, column=1, padx=5, pady=5)

        model_label.grid(row=0, column=0, padx=5, pady=5)
        model_entry = tk.Entry(window, textvariable=car['model'])
        model_entry.grid(row=0, column=1, padx=5, pady=5)

        year_entry = tk.Entry(window, textvariable=car['year'])
        year_entry.grid(row=0, column=2, padx=5, pady=5)

        cost_entry = tk.Entry(window, textvariable=car['cost'])
        cost_entry.grid(row=0, column=3, padx=5, pady=5)

        prob_entry = tk.Entry(window, textvariable=car['prob'])
        prob_entry.grid(row=0, column=4, padx=5, pady=5)

        color_entry = tk.Entry(window, textvariable=car['color'])
        color_entry.grid(row=0, column=5, padx=5, pady=5)
            
        dtp_entry = tk.Entry(window, textvariable=car['dtp'])
        dtp_entry.grid(row=0, column=6, padx=5, pady=5)

        submit_button = tk.Button(window, text="Submit", command=submit)
        submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def delete_car(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.get_all_cars(), file)
        else:
            messagebox.showwarning("Delete Car", "No car selected.")

    def update_car(self):
        selected_item = self.tree.selection()
        if selected_item:
            car = self.get_car_by_id(selected_item[0])

            car['model'] = tk.StringVar(value=car['model'])
            car['year'] = tk.StringVar(value=car['year'])
            car['cost'] = tk.StringVar(value=car['cost'])
            car['prob'] = tk.StringVar(value=car['prob'])
            car['color'] = tk.StringVar(value=car['color'])
            car['dtp'] = tk.StringVar(value=car['dtp'])

            def submit():
                car['model'] = model_entry.get()
                car['year'] = year_entry.get()
                car['cost'] = cost_entry.get()
                car['prob'] = prob_entry.get()
                car['color'] = color_entry.get()
                car['dtp'] = dtp_entry.get()

                self.tree.set(selected_item[0], column='model', value=car['model'])
                self.tree.set(selected_item[0], column='year', value=car['year'])
                self.tree.set(selected_item[0], column='cost', value=car['cost'])
                self.tree.set(selected_item[0], column='prob', value=car['prob'])
                self.tree.set(selected_item[0], column='color', value=car['color'])
                self.tree.set(selected_item[0], column='dtp', value=car['dtp'])

                with open(self.filename, "w", encoding="utf-8") as file:
                    json.dump(self.get_all_cars(), file)

                window.destroy()

            window = tk.Toplevel(self.root)
            window.title("Update Car")

            model_label = tk.Label(window, text="Model:")
            model_label.grid(row=0, column=0, padx=5, pady=5)
            model_entry = tk.Entry(window, textvariable=car['model'])
            model_entry.grid(row=0, column=1, padx=5, pady=5)

            year_entry = tk.Entry(window, textvariable=car['year'])
            year_entry.grid(row=0, column=2, padx=5, pady=5)

            cost_entry = tk.Entry(window, textvariable=car['cost'])
            cost_entry.grid(row=0, column=3, padx=5, pady=5)

            prob_entry = tk.Entry(window, textvariable=car['prob'])
            prob_entry.grid(row=0, column=4, padx=5, pady=5)

            color_entry = tk.Entry(window, textvariable=car['color'])
            color_entry.grid(row=0, column=5, padx=5, pady=5)

            dtp_entry = tk.Entry(window, textvariable=car['dtp'])
            dtp_entry.grid(row=0, column=6, padx=5, pady=5)

            # Add similar entries for year, cost, prob, color, and dtp

            submit_button = tk.Button(window, text="Submit", command=submit)
            submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        else:
            messagebox.showwarning("Update Car", "No car selected.")

    def search_car(self):
        search_query = tk.StringVar()

        def search():
            search_result = []
            for car in self.get_all_cars():
                if search_query.get().lower() in str(car.values()).lower():
                    search_result.append(car)

            self.clear_tree()
            for car in search_result:
                self.tree.insert('', tk.END, values=(car['model'], car['year'], car['cost'], car['prob'], car['color'], car['dtp']))

        window = tk.Toplevel(self.root)
        window.title("Search Car")

        search_label = tk.Label(window, text="Search Query:")
        search_label.grid(row=0, column=0, padx=5, pady=5)
        search_entry = tk.Entry(window, textvariable=search_query)
        search_entry.grid(row=0, column=1, padx=5, pady=5)

        search_button = tk.Button(window, text="Search", command=search)
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def get_all_cars(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def get_car_by_id(self, item_id):
        cars = self.get_all_cars()
        for car in cars:
            if car['model'] == self.tree.item(item_id)['values'][0]:
                return car
        return None

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

if __name__ == "__main__":
    root = tk.Tk()
    app = CarApp(root)
    root.mainloop()
from tkinter import ttk
import tkinter as tk
import configparser


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x80")
        self.title('Tkinter OptionMenu Widget')

        # initialize data
        self.stations = ('AIS', 'CCD', 'CRZF',
                        'DRV', 'PAF', 'WEL')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Choix de la config de station à charger:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.stations[0],
            *self.stations,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
    
    def commenter_config(self, ligne):
        # Lit la config actuelle dans le fichier config.txt
        with open("config.txt", "r") as file:
            lignes = file.readlines()
        
        # Commente toutes les lignes de config des stations
        for i in range(30):
            if lignes[1 + i].startswith('#'):
                pass
            else:
                lignes[1 + i] = "#" + lignes[1 + i]
        
        # Décommente la station choisie
        for i in range(5):
            lignes[ligne + i] = lignes[ligne + i][1:] 
        
        
        # Ecrit la nouvelle config dans le fichier config.txt
        with open("config.txt", "w") as file:
            file.writelines(lignes)
    
    def option_changed(self, *args):
        print("Changement de station")
        # Lit la config actuelle dans le fichier config.txt
        with open("config.txt", "r") as file:
            lignes = file.readlines()
        
        if(self.option_var.get() == 'AIS'):
            print("Nouvelle station = Amsterdam")
            self.commenter_config(1)
        
        if(self.option_var.get() == 'CCD'):
            print("Nouvelle station = Concordia")
            self.commenter_config(7)
        
        if(self.option_var.get() == 'CRZF'):
            print("Nouvelle station = Crozet")
            self.commenter_config(13)
        
        if(self.option_var.get() == 'DRV'):
            print("Nouvelle station = Dumont D'Urville")
            self.commenter_config(19)
        
        if(self.option_var.get() == 'PAF'):
            print("Nouvelle station = Kerguelen")
            self.commenter_config(25)
        
        if(self.option_var.get() == 'WEL'):
            print("Nouvelle station = Welschbruch")
            self.commenter_config(31)
                
        self.output_label['text'] = f'Config chargée pour la station: {self.option_var.get()}'
        
    



if __name__ == "__main__":
    app = App()
    app.mainloop()

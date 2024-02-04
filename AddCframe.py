import tkinter as tk 
from tkinter import messagebox
import mainProject as mp

class AddCframe(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Aggiungi Categoria")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.grid()
        
        self.font = ("Helvetica", 15)
        self.fileCategories = []
        self.buildSubFrame()
    
    #Funzione di lettura del file: 
    def ReadFile(self):
        self.path = mp.MainFrame.LoadFile()
        with open(f"{self.path}", "r") as f: 
            self.fileCategories = f.readlines()
        f.close()
    
    #Funzione di salvataggio del file: 
    def SaveData(self):
        with open(f"{self.path}", "w") as f: 
            self.content = str(self.etrCategoryName.get())
            if not self.content: 
                messagebox.showerror("Errore", "Inserisci un nome")
            else: 
                f.write(self.content)
        f.close()
        
    def buildSubFrame(self):
    #Inserimento nome: 
        self.lblCategoryName = tk.Label(self, text = "Nome della Categoria", font = self.font)
        self.lblCategoryName.grid(row = 0, column = 0, padx = 5, pady = 10)

        self.etrCategoryName = tk.Entry(self, font = self.font)
        self.etrCategoryName.grid(row = 0, column = 1)
    
    #Bottone di salvataggio: 
        self.btnSave = tk.Button(self, text = "Salva", command = None, font = self.font)
        self.btnSave.grid(row = 1, column = 0, padx = 10, pady = 100)

def main():
    if __name__ == "__main__":
        f = AddCframe()
        f.mainloop()
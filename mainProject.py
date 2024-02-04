import tkinter as tk 
from tkinter import messagebox, filedialog 
import AddCframe as acf

global categoryName

class MainFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Gestione inventario")
        self.master.geometry("600x600")
        self.master.resizable(False, False)
        self.grid()
        
        #Variabile di controllo della apertura del file 
        self.fileLoaded = False
        
        self.font = ("Helvetica", 15)
        self.BuildMainFrame()
        
        
    #Funzioni per il controllo del file e attivazione dei widget  
    def FrameEnabling(self):
        self.btnAddCategory.config(state = "active")
        self.btnDeleteCategory.config(state = "active")
        self.btnEditCategory.config(state = "active")
        
    def EnableFrames(self, controllo):
        if controllo == True:
            self.FrameEnabling()
        else:
            messagebox.showerror("Errore", "Inserisci un file!")
        
    def LoadFile(self):
        #Richiesta di apertura del file 
        self.filePath = filedialog.askopenfilename()
        
        #Controllo dell'estensione del file 
        if self.filePath:
            if self.filePath != None:
                self.fileExtension = self.filePath.split(".")[-1]
                if self.fileExtension == "txt":
                    self.LoadFile = True
                else: 
                    self.LoadFile = False
        
        self.EnableFrames(self.LoadFile)
        return self.filePath
    
    #Funzioni per i pulsanti 
    def AddCategory(self):
        acf.main()

    #Funzione di costruzione principale
    def BuildMainFrame(self):
        #Frame per il loading del file 
        self.frmLoadFile = tk.Frame(self, width = 550, height = 100)
        self.frmLoadFile.grid(row = 0, column = 0)
        
        #Bottone per il loading di un file 
        self.btnLoadFile = tk.Button(self.frmLoadFile, text = "Carica File", command = self.LoadFile, font = self.font)
        self.btnLoadFile.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        #Widget disabilitati prima del controllo 
        
        #Frame dei controlli delle categorie 
        self.frmCategorySettings = tk.Frame(self, width = 550, height = 100)
        self.frmCategorySettings.grid(row = 1, column = 0, padx = 5)
        
        #Widget per aggiungere una categoria
        self.btnAddCategory = tk.Button(self.frmCategorySettings, text = "Aggiungi Categoria", command = self.AddCategory, font = self.font)
        self.btnAddCategory.grid(row = 1, column = 0)
        self.btnAddCategory.config(state = "disabled")
        
        #Widget per modificare una categoria
        self.btnEditCategory = tk.Button(self.frmCategorySettings, text = "Modifica Categoria", command = None, font = self.font)
        self.btnEditCategory.grid(row = 1, column = 1, padx = 10)
        self.btnEditCategory.config(state = "disabled")
        
        #Widget per eliminare una categoria 
        self.btnDeleteCategory = tk.Button(self.frmCategorySettings, text = "Elimina Categoria", command = None, font = self.font)
        self.btnDeleteCategory.grid(row = 1, column = 2)
        self.btnDeleteCategory.config(state = "disabled")
        
        #Widget per la visualizzazione delle categorie
        self.frmCategoryShow = tk.Frame(self, width = 550, height = 400)
        self.frmCategoryShow.grid(row = 2, column = 0)
        

#Esecuzione dello script 
if __name__ == "__main__":
    f = MainFrame()
    f.mainloop()
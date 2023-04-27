import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x400")
        self.master.title("Plotagem de Gráficos")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self)
        self.load_button["text"] = "Carregar CSV"
        self.load_button["command"] = self.load_csv
        self.load_button.pack(side="top")

        self.plot_type = tk.StringVar(self)
        self.plot_type.set("Gráfico de Linha")

        self.plot_menu = tk.OptionMenu(self, self.plot_type, "Gráfico de Linha", "Gráfico de Área", "Gráfico de Barra", "Gráfico de Pizza")
        self.plot_menu.pack(side="top")

        self.plot_button = tk.Button(self)
        self.plot_button["text"] = "Plotar Gráfico"
        self.plot_button["state"] = "disabled"
        self.plot_button["command"] = self.plot_graph
        self.plot_button.pack(side="top")

        self.info_label = tk.Label(self, text="")
        self.info_label.pack(side="top")

        self.quit_button = tk.Button(self, text="Fechar", fg="red",
                            command=self.master.destroy)
        self.quit_button.pack(side="bottom")


    def load_csv(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.df = pd.read_csv(file_path)
            self.column_names = list(self.df.columns)
            self.info_label.config(text=f"Arquivo {self.file_path} carregado com sucesso!")
            self.plot_button["state"] = "normal"


    
    def plot_graph(self):
        if self.plot_type.get() == "Gráfico de Linha":
            self.plot_line_graph(self.df)
        elif self.plot_type.get() == "Gráfico de Área":
            self.plot_area_graph(self.df)
        elif self.plot_type.get() == "Gráfico de Barra":
            self.plot_bar_graph(self.df)
        elif self.plot_type.get() == "Gráfico de Pizza":
            self.plot_pie_graph(self.df)
        
    def plot_line_graph(self, df):
        plt.plot(df.iloc[:, 0], df.iloc[:, 1:])
        plt.xlabel(df.columns[0])
        plt.ylabel("Valores")
        plt.title("Gráfico de Linha")
        plt.show()

    def plot_area_graph(self, df):
        plt.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:])
        plt.xlabel(df.columns[0])
        plt.ylabel("Valores")
        plt.title("Gráfico de Área")
        plt.legend(loc='upper left')
        plt.show()

    def plot_bar_graph(self, df):
        if len(df.columns) == 2:
            x = df.iloc[:, 0]
            y = df.iloc[:, 1]
            plt.bar(x, y)
            plt.xlabel(df.columns[0])
            plt.ylabel("Valores")
            plt.title("Gráfico de Barra")
            plt.show()
        else:
            df.plot.bar(x=df.columns[0], y=df.columns[1:])
            plt.xlabel(df.columns[0])
            plt.ylabel("Valores")
            plt.title("Gráfico de Barra")
            plt.show()

    def plot_pie_graph(self, df):
        plt.pie(df.iloc[:, 1], labels=df.iloc[:, 0], autopct='%1.1f%%')
        plt.title("Gráfico de Pizza")
        plt.show()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

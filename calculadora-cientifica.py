import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora Científica")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.create_widgets()
        
    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=5, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, pady=10)
        self.display.bind("<Key>", self.clear_error)

        buttons = [
            "7", "8", "9", "/", "C",
            "4", "5", "6", "*", "√",
            "1", "2", "3", "-", "^",
            "0", ".", "=", "+", "π",
            "sin", "cos", "tan", "log", "ln"
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            ttk.Button(self, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1
        
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        
        for i in range(1, 7):
            self.grid_rowconfigure(i, weight=1)
    
    def clear_error(self, event):
        if self.display.get() == "Erro":
            self.display.delete(0, tk.END)

    def on_button_click(self, char):
        if char == "C":
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                expression = self.display.get()
                expression = expression.replace("√", "math.sqrt")
                expression = expression.replace("^", "**")
                expression = expression.replace("π", "math.pi")
                expression = expression.replace("sin", "math.sin")
                expression = expression.replace("cos", "math.cos")
                expression = expression.replace("tan", "math.tan")
                expression = expression.replace("log", "math.log10")
                expression = expression.replace("ln", "math.log")
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            if self.display.get() == "Erro":
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
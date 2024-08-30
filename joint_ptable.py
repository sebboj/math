# allow user to input dimensions and then values of a joint ptable thru a basic UI
# calculate probability values and E[x], E[y], E[XY], COV(X,Y), and correlation of X, Y

import tkinter as tk
import math

precision = 4 # round to 4 decimal places

class TableInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Joint Probability Table Input')

        # table dimension input
        self.row_label = tk.Label(root, text='Enter # of rows:')
        self.row_label.grid(row=0, column=0)

        self.row_entry = tk.Entry(root)
        self.row_entry.grid(row=0, column=1)

        self.col_label = tk.Label(root, text='Enter # of columns:')
        self.col_label.grid(row=1, column=0)

        self.col_entry = tk.Entry(root)
        self.col_entry.grid(row=1, column=1)

        self.generate_button = tk.Button(root, text='Generate Table', command=self.generate_table)
        self.generate_button.grid(row=2, column=0, columnspan=1)

        # restart button to clear table
        self.restart_button = tk.Button(self.root, text='Restart', command=self.restart)
        self.restart_button.grid(row=2, column=1, columnspan=1, padx=8)

        self.label = None
        self.X_values = []
        self.Y_values = []
        self.table_entries = []
        self.probabilities = []

    def restart(self):
        # clear all widgets
        if self.label:
            self.label.destroy()
        if self.X_values:
            for x in self.X_values:
                x.destroy()
        if self.Y_values:
            for y in self.Y_values:
                y.destroy()
        if self.table_entries:
            for row in self.table_entries:
                for entry in row:
                    entry.destroy()
        if self.submit_button:
            self.submit_button.destroy()

        # clear all table and dimension entries
        self.table_entries = []
        self.probabilities = []
        self.X_values = []
        self.Y_values = []
        self.row_entry.delete(0, tk.END)
        self.col_entry.delete(0, tk.END)

    def generate_table(self):
        # clear existing input fields
        for entry_row in self.table_entries:
            for entry in entry_row:
                entry.destroy()
        self.table_entries.clear()

        rows = int(self.row_entry.get())
        cols = int(self.col_entry.get())

        # generate table input fields
        for r in range(rows + 1):
            row_entries = []
            for c in range(cols + 1):
                if r == 0 and c == 0:
                    self.label = tk.Label(root, text='Y values ↓\\ X values →')
                    self.label.grid(row=3,column=0)
                else:
                    entry = tk.Entry(self.root)
                    entry.grid(row=r+3, column=c) # 3 offset to prevent overlap w dimension inputs
                    if r == 0:
                        self.X_values.append(entry)
                        entry.grid(pady=4)
                    elif c == 0:
                        self.Y_values.append(entry)
                        entry.grid(padx=4)
                    else:
                        row_entries.append(entry)
            if r > 0:
                self.table_entries.append(row_entries)

        # submit inputs to calculate probabilities
        self.submit_button = tk.Button(self.root, text='Submit Entries', command=self.submit_table)
        self.submit_button.grid(row=rows+4, column=0, columnspan=cols)

    def submit_table(self):
        table = []
        total = 0
        rows = len(self.Y_values)
        cols = len(self.X_values)

        for row_entries in self.table_entries:
            row = [float(entry.get()) for entry in row_entries]
            total += sum(row)
            table.append(row)
        print('Table:', table)

        for row in table:
            probs = [round(entry / total, precision) for entry in row]
            self.probabilities.append(probs)
        print('Probabilities:', self.probabilities)

        P_X = [0] * cols
        P_Y = [0] * rows
        for row in range(rows):
            for col in range(cols):
                P_X[col] += self.probabilities[row][col]
                P_Y[row] += self.probabilities[row][col]

        # process the table data
        E_X = round(sum([P_X[x] * float(self.X_values[x].get())  for x in range(cols)]), precision)
        E_Y = round(sum([P_Y[y] * float(self.Y_values[y].get())  for y in range(rows)]), precision)
        E_XY = 0
        for row in range(rows):
            for col in range(cols):
                E_XY += round(float(self.X_values[col].get()) * float(self.Y_values[row].get()) * self.probabilities[row][col], precision)
        COV_XY = round(E_XY - E_X * E_Y, precision)
        sigma_X = round(sum([float(self.X_values[x].get()) ** 2  * P_X[x] for x in range(cols)]) - E_X ** 2, precision)
        sigma_Y = round(sum([float(self.Y_values[y].get()) ** 2  * P_Y[y] for y in range(rows)]) - E_Y ** 2, precision)
        CORR_XY = COV_XY/math.sqrt(sigma_X * sigma_Y)

        # print results
        print('Expected Value of X:', E_X)
        print('Expected Value of Y:', E_Y)
        print('Expected Value of XY:', E_XY)
        print('Covariance of X,Y:', COV_XY)
        print('Correlation of X,Y:', CORR_XY)

if __name__ == '__main__':
    root = tk.Tk()
    app = TableInputApp(root)
    root.mainloop()

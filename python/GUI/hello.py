import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#import numpy as np


class HelloApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello, Tkinter!")
        self.geometry("800x600")
        self.button_click()
    
    def button_click(self):
        print("Hello, Tkinter!")
        # st谱
        stspectrumButton = tk.Button(
            text="st谱", fg="black",
            command=lambda : [self.matplot()])
        stspectrumButton.config(height = 1, width = 2)
        stspectrumButton.grid(row=1, column=8, sticky='nsew',rowspan=1)

    def matplot(self):
        
        newroot = tk.Tk(); newroot.columnconfigure(1, weight=1); newroot.rowconfigure(1, weight=1); newroot.title('坐标 ' + '单道图')
        fig = Figure(figsize=(12, 10)); fig.clear(); 

        a = fig.add_subplot(111); a.clear()
        a.plot([1, 2, 3, 4], [0, 3, 4, 1])
        a.set_xlabel("Time [ns]"); a.set_ylabel("Amplitude"); a.set_title("Single-channel signal diagram")

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=newroot)
        canvas.get_tk_widget().grid(row=1, column=1, columnspan=10, rowspan=8, sticky='nsew')
        canvas.draw()




if __name__ == "__main__":
    app = HelloApp()
    app.mainloop()
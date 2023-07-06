
import sys
import tkinter as tk


def main(args=None):
		rightcol=9
		figrowsp=19+1

		root = tk.Tk()

		for col in range(rightcol):
			root.columnconfigure(col, weight=1)
		for row in range(figrowsp):    
			root.rowconfigure(row, weight=1)
			

		root.mainloop()

if __name__ == "__main__":
	main()
###
#Jhamni Young-Shinnick
#10.25.17
#RisingSun.py
#Interactive Animation w/rising Sun
###
import Tkinter as tk #names TKinter to be used as tk
root = tk.Tk() #Creates root window
canvas = tk.Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, bg="white")
canvas.grid() #Fills background white and creates a larger Canvas
#format (x0, y0, x1, y1), all are poits for the circle's box
canvas.create_oval(0,300, 0, 300, width=2, fill='red')
root.mainloop()# Event loop
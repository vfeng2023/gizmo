from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Gizmo")


# add radio buttons
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/
button_frame = tk.Frame(root)
button_frame.grid(row=0)
containertype = tk.Label(button_frame, text="Container Type: ")
containertype.grid(row=0, column=0, sticky="E")
containercombo = ttk.Combobox(button_frame, values=["Glass", "Plastic", "Steel"])
containercombo.grid(row=0, column=1,sticky="E")

liquidtype = tk.Label(button_frame, text = "Liquid Type: ")
liquidtype.grid(row=1, column=0, sticky='E')
liquidselect = ttk.Combobox(button_frame, values = ["Water", "Ice", "Oil"])
liquidselect.grid(row=1, column=1, sticky='E')

thicknes = tk.Label(button_frame, text="Thickness: ")
thicknes.grid(row=2, column=0)
slider = tk.Scale(button_frame, from_ = 1, to=4, orient="horizontal")
slider.grid(row=2, column=1)

liquidtemp = tk.Label(button_frame, text = "Liquid Temperature: ")
liquidtemp.grid(row=3, column=0)
ltempentry = tk.Entry(button_frame, width=10)
ltempentry.grid(row=3, column=1)


outsidetemp = tk.Label(button_frame, text = "Outside Temperature: ")
outsidetemp.grid(row=4, column=0)
otempentry = tk.Entry(button_frame, width=10)
otempentry.grid(row=4, column=1)

# add insulator image
insulator = tk.Canvas(root)
insulator.configure(height=400, width=400)
insulator.configure(bg="red")
insulator.grid(row=1)
# add temperature graph

tempgraph = tk.Canvas(root)
tempgraph.configure(height=400, width=400,bg="blue")
tempgraph.grid(row=0,column=1)
root.mainloop()
import tkinter as tk
from tkinter import *
from Utils import sort, generate

window = tk.Tk()
window.title("Sort Visualiser")
window.geometry("800x700+10+10")
OPTIONS = ["Quicksort", "Merge Sort"]
RECTANGLE_X = 20
RECTANGLE_Y = 350
rectangle_list = []
generate.generate_list(rectangle_list)

"""
CANVAS
"""

canvas = tk.Canvas(window, width=700, height=600)
canvas.grid(row=1, column=0, padx=10, pady=5)

"""
DROPDOWN MENU
"""
current_option = StringVar(window)
current_option.set(OPTIONS[0])
option_dropdown = OptionMenu(window, current_option, *OPTIONS)
option_dropdown.grid()
option_dropdown.place(x=250, y=40)
"""
BUTTON FOR DROPDOWN
"""


def get_sort():  # Function to get selected sort function
    if current_option.get() == OPTIONS[0]:
        canvas.delete("all")
        rectangle_list = []
        generate.generate_list(rectangle_list)
        sort.sort(rectangle_list, 0, len(rectangle_list) - 1, window, 0.08, canvas)
    elif current_option.get() == OPTIONS[1]:
        canvas.delete("all")
        rectangle_list = []
        generate.generate_list(rectangle_list)
        sort.merge_sort(rectangle_list, window, canvas, 0.1)


button = Button(window, text="Start Sort", command=get_sort)
button.grid()
button.place(x=250, y=10)

window.mainloop()

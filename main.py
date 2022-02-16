import tkinter as tk
from tkinter import *
from Utils import sort, generate

window = tk.Tk()
window.title("Sort Visualiser")
window.geometry("700x600+10+10")
OPTIONS_SORT = ["Quick Sort", "Merge Sort", "Bubble Sort"]
OPTIONS_SPEED = ["Slow", "Medium", "Fast"]
RECTANGLE_X = 20
RECTANGLE_Y = 350
SPEED = 0.3

"""
CANVAS
"""

canvas = tk.Canvas(window, width=700, height=600)
canvas.grid(row=1, column=0, padx=10, pady=5)

"""
DROPDOWN MENU (SORT AND SPEED)
"""
current_option_sort = StringVar(window)
current_option_sort.set(OPTIONS_SORT[0])
option_dropdown_sort = OptionMenu(window, current_option_sort, *OPTIONS_SORT)
option_dropdown_sort.grid()
option_dropdown_sort.place(x=30, y=40)

current_option_speed = StringVar(window)
current_option_speed.set(OPTIONS_SPEED[0])
option_dropdown_speed = OptionMenu(window, current_option_speed, *OPTIONS_SPEED)
option_dropdown_speed.grid()
option_dropdown_speed.place(x=140, y=40)

"""
BUTTON FOR DROPDOWN (SORT AND SPEED)
"""


def set_speed():
    global SPEED
    if current_option_speed.get() == 'Slow':
        SPEED = 0.3
    elif current_option_speed.get() == 'Medium':
        SPEED = 0.1
    else:
        SPEED = 0.001


def set_sort():  # Function to get selected sort function
    if current_option_sort.get() == OPTIONS_SORT[0]:
        canvas.delete("all")
        rectangle_list = []
        generate.generate_list(rectangle_list)
        sort.sort(rectangle_list, 0, len(rectangle_list) - 1, window, SPEED, canvas)

    elif current_option_sort.get() == OPTIONS_SORT[1]:
        canvas.delete("all")
        rectangle_list = []
        generate.generate_list(rectangle_list)
        sort.merge_sort(rectangle_list, window, canvas, SPEED)

    elif current_option_sort.get() == OPTIONS_SORT[2]:
        canvas.delete("all")
        rectangle_list = []
        generate.generate_list(rectangle_list)
        sort.bubble_sort(rectangle_list, window, canvas, SPEED)


button_sort = Button(window, text="Start Sort", command=set_sort)
button_sort.grid()
button_sort.place(x=30, y=10)

button_speed = Button(window, text="Set Speed", command=set_speed)
button_speed.grid()
button_speed.place(x=140, y=10)

window.mainloop()

import tkinter as tk
from Utils import sort, generate

RECTANGLE_X = 20
RECTANGLE_Y = 450
rectangle_list = []
generate.generate_list(rectangle_list)


window = tk.Tk()
canvas = tk.Canvas(window, width=700, height=600)
canvas.grid(row=1, column=0, padx=10, pady=5)
window.title("Sort Visualiser")
window.geometry("700x600+10+10")
sort.sort(rectangle_list, 0, len(rectangle_list) - 1, window, 0.08, canvas)
#sort.merge_sort(rectangle_list, window, canvas, 0.1)
window.mainloop()

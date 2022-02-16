from Utils import colors


def draw_current_rectangles(list_of_rectangles, screen, canvas, lower, upper):
    i = 1
    canvas.delete("all")
    for index, rectangle_height in enumerate(list_of_rectangles):
        if index == lower or index == upper:
            canvas.create_rectangle(15 * i, 600, 15 * i + 15, 600 - rectangle_height, outline=colors.BLACK,
                                    fill=colors.RED)
        else:
            canvas.create_rectangle(15 * i, 600, 15 * i + 15, 600 - rectangle_height, outline=colors.BLACK,
                                    fill=colors.BLUE)
        canvas.update()
        i += 1
    screen.update_idletasks()

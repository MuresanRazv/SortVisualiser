import time
from Utils import draw

"""
QUICKSORT
"""


def partition(a_list, low, high, window, timetick, canvas):
    pivot = a_list[low]
    i = low
    j = high
    draw.draw_current_rectangles(a_list, window, canvas, i, j)
    time.sleep(timetick)
    while i != j:
        while pivot <= a_list[j] and i < j:
            j -= 1
            draw.draw_current_rectangles(a_list, window, canvas, i, j)
            time.sleep(timetick)
        a_list[i] = a_list[j]
        draw.draw_current_rectangles(a_list, window, canvas, i, j)
        while a_list[i] <= pivot and i < j:
            i += 1
            draw.draw_current_rectangles(a_list, window, canvas, i, j)
            time.sleep(timetick)
        a_list[j] = a_list[i]
        a_list[i] = pivot
        draw.draw_current_rectangles(a_list, window, canvas, i, j)
    draw.draw_current_rectangles(a_list, window, canvas, i, j)
    return i


def quickSortRec(a_list, low, high, window, timetick, canvas):
    pivotPos = partition(a_list, low, high, window, timetick, canvas)
    if low < pivotPos - 1:
        quickSortRec(a_list, low, pivotPos - 1, window, timetick, canvas)
    if pivotPos + 1 < high:
        quickSortRec(a_list, pivotPos + 1, high, window, timetick, canvas)


def sort(a_list, low, high, timetick, window, canvas):
    quickSortRec(a_list, low, high, timetick, window, canvas)
    return a_list


"""
MERGE SORT
"""


def merge_sort(a_list, window, canvas, timetick):
    if len(a_list) > 1:
        middle = len(a_list) // 2
        left = a_list[:middle]
        right = a_list[middle:]

        merge_sort(left, window, canvas, timetick)
        merge_sort(right, window, canvas, timetick)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a_list[k] = left[i]
                i += 1
                draw.draw_current_rectangles(a_list, window, canvas, i, j)
                window.update_idletasks()
            else:
                a_list[k] = right[j]
                j += 1
                draw.draw_current_rectangles(a_list, window, canvas, i, j)
                window.update_idletasks()
            k += 1

        while i < len(left):
            a_list[k] = left[i]
            i += 1
            k += 1
            draw.draw_current_rectangles(a_list, window, canvas, i, j)
            window.update_idletasks()

        while j < len(right):
            a_list[k] = right[j]
            j += 1
            k += 1
            draw.draw_current_rectangles(a_list, window, canvas, i, j)
            window.update_idletasks()

        canvas.update()
        time.sleep(timetick)


"""
BUBBLE SORT
"""


def bubble_sort(a_list, window, canvas, timetick):
    for i in range(0, len(a_list)):
        for j in range(i, len(a_list)):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]
            time.sleep(timetick)
            draw.draw_current_rectangles(a_list, window, canvas, i, j)
        time.sleep(timetick)
        draw.draw_current_rectangles(a_list, window, canvas, i, j)


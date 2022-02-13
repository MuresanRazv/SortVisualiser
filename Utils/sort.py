import time
from Utils import draw

"""
QUICKSORT
"""


def partition(a_list, low, high, window, timeTick, canvas):
    pivot = a_list[low]
    i = low
    j = high
    draw.draw_current_rectangles(a_list, window, canvas, i, j)
    canvas.update()
    time.sleep(timeTick)
    while i != j:
        while pivot <= a_list[j] and i < j:
            j -= 1
        a_list[i] = a_list[j]
        while a_list[i] <= pivot and i < j:
            i += 1
        a_list[j] = a_list[i]
        a_list[i] = pivot
    draw.draw_current_rectangles(a_list, window, canvas, i, j)
    window.update_idletasks()
    return i


def quickSortRec(a_list, low, high, window, timeTick, canvas):
    pivotPos = partition(a_list, low, high, window, timeTick, canvas)
    if low < pivotPos - 1:
        quickSortRec(a_list, low, pivotPos - 1, window, timeTick, canvas)
    if pivotPos + 1 < high:
        quickSortRec(a_list, pivotPos + 1, high, window, timeTick, canvas)


def sort(a_list, low, high, timeTick, window, canvas):
    quickSortRec(a_list, low, high, timeTick, window, canvas)
    return a_list


"""
MERGE SORT
"""


def merge_sort(a_list, window, canvas, timeTick):
    if len(a_list) > 1:
        middle = len(a_list) // 2
        left = a_list[:middle]
        right = a_list[middle:]

        merge_sort(left, window, canvas, timeTick)
        merge_sort(right, window, canvas, timeTick)

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
        time.sleep(timeTick)

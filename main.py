from asciimatics.screen import Screen
from time import sleep

def draw_array(screen, arr, highlight_indexes=[], highlight_color=Screen.COLOUR_GREEN):
    screen.clear()
    for i, val in enumerate(arr):
        color = highlight_color if i in highlight_indexes else Screen.COLOUR_WHITE
        screen.print_at(f"{val}", i * 4 + 10, 3, colour=color)
    screen.refresh()
    sleep(0.5)

def bubble_sort_visualization(screen, arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_array(screen, arr, [j, j+1])

def binary_search_visualization(screen, arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        draw_array(screen, arr, [left, mid, right], Screen.COLOUR_BLUE)
        if arr[mid] == target:
            screen.print_at(f"Target found at index {mid}!", 0, 5)
            screen.refresh()
            sleep(2)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    screen.print_at("Target not found in the array.", 0, 5)
    screen.refresh()
    sleep(2)
    return -1

def run_visualization(screen):
    screen.print_at("Choose an algorithm to visualize (1-Bubble Sort, 2-Binary Search): ", 0, 0)
    screen.refresh()

    while True:
        evt = screen.get_key()
        if evt in (ord('1'), ord('2')):
            if evt == ord("1"):
                arr = [64, 34, 25, 12, 22, 11, 90]
                bubble_sort_visualization(screen, arr)
            elif evt == ord("2"):
                arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                target = 40
                binary_search_visualization(screen, arr, target)
            break

# running the visualizer
Screen.wrapper(run_visualization)

import pyautogui
import tkinter as tk
## Let's build a function to move the mouse


def mouseMove(Direction):
    print("Single Click, "+Direction)
    x, y = pyautogui.position()
    print(x,y)
    if(Direction == "Left"):
        x += 200
    else:
        x -= 200
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()


if __name__ == '__main__':

    ## Make a window for GUI
    root = tk.Tk()
    root.geometry('500x200')
    root.resizable(width=0, height=0)

    button1 = tk.Button(root, text="Left", command=lambda: mouseMove("Left"))
    button1.place(x=100, y=50, height=100, width=100)

    button2 = tk.Button(root, text="Right", command=lambda: mouseMove("Right"))
    button2.place(x=300, y=50, height=100, width=100)

    root.mainloop()



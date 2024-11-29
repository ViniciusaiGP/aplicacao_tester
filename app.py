from functions.screenshot import screenshot
from functions.event_pyautogui import EventPyautogui
from pages.home_page import HomePage
import tkinter as tk


if __name__ == "__main__":
    #print("Iniciando o processo de captura de tela...")
    #ret = screenshot()
    #print(ret)

    #a = ret["center"]["x"]
    #b = ret["center"]["y"]

    #EventPyautogui.execute('moveTo', a, b)
    #print("Captura de tela concluída!")

    #print(EventPyautogui.auto_complete_event())

    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
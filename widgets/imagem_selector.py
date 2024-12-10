from tkinter import Toplevel, filedialog, messagebox
import tkinter as tk

from functions.screenshot import Lightshot
from utils.open_folder import OpenFolder

class ImageActionModal:
    def __init__(self, master, action_index, on_image_selected):
        self.master = master
        self.action_index = action_index
        self.on_image_selected = on_image_selected

        # Cria a janela modal
        self.modal = Toplevel(self.master)
        self.modal.title("Escolher Opção")
        self.modal.geometry("300x150")
        self.modal.grab_set()  # Torna a modal modal

        # Título
        tk.Label(self.modal, text="Escolha uma opção:", font=("Arial", 12, "bold")).pack(pady=10)

        # Botão para importar imagem
        import_button = tk.Button(
            self.modal,
            text="Importar Imagem",
            command=self.import_image,
            width=20
        )
        import_button.pack(pady=5)

        # Botão para capturar tela
        capture_button = tk.Button(
            self.modal,
            text="Capturar Tela",
            command=self.capture_screenshot,
            width=20
        )
        capture_button.pack(pady=5)

    def import_image(self):
        # Cria a janela principal
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal

        OpenFolder.selecionar_arquivo()
        self.modal.destroy()

    def capture_screenshot(self):
        # Lógica para capturar a tela
        self.modal.destroy()
        try:
            screenshot_path = Lightshot.screenshot()  # Ajuste conforme a lógica da sua classe Lightshot
            if screenshot_path and screenshot_path.strip():  # Verifica se o caminho da captura é válido
                print(f"Captura de tela salva em: {screenshot_path}")  # Exibe o caminho da captura
                self.on_image_selected(screenshot_path)
            else:
                messagebox.showwarning("Aviso",
                                       "Falha ao capturar a tela.")  # Alerta se o caminho da captura for inválido
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao capturar a tela: {str(e)}")  # Exibe mensagem de erro
        self.modal.destroy()
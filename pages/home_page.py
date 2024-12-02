import tkinter as tk
from tkinter import messagebox

from pages.novo_page import NewTestScreen


class TestManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Meus Testes")

        # Título e botão "Novo"
        self.title_frame = tk.Frame(master)
        self.title_frame.pack(pady=10, padx=10, fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Meus Testes", font=("Arial", 16, "bold"))
        self.title_label.pack(side=tk.LEFT)

        self.new_button = tk.Button(self.title_frame, text="Novo", command=self.create_new_test)
        self.new_button.pack(side=tk.RIGHT)

        # Frame para a lista
        self.list_frame = tk.Frame(master)
        self.list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Dados iniciais
        self.tests = [
            {"name": "Teste 1"},
            {"name": "Teste 2"},
        ]

        self.update_list()

    def create_new_test(self):
        # Abre uma nova janela para a tela de novo teste
        new_window = tk.Toplevel(self.master)
        new_window.geometry("900x400")

        # Centralizar a nova janela na tela
        self.center_window(new_window, 900, 400)

        NewTestScreen(new_window)  # Inicializa a classe NewTestScreen com a nova janela como master


    def update_list(self):
        # Remove todos os widgets existentes antes de recriar
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for idx, test in enumerate(self.tests, start=1):
            row_frame = tk.Frame(self.list_frame)
            row_frame.pack(fill=tk.X, pady=5)

            # Número
            num_label = tk.Label(row_frame, text=f"{idx}.", width=5, anchor=tk.W)
            num_label.pack(side=tk.LEFT)

            # Nome do teste
            name_label = tk.Label(row_frame, text=test["name"], anchor=tk.W)
            name_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            # Botões
            play_button = tk.Button(row_frame, text="▶", command=lambda i=idx: self.play_test(i), width=3)
            play_button.pack(side=tk.LEFT, padx=5)

            edit_button = tk.Button(row_frame, text="✏", command=lambda i=idx: self.edit_test(i), width=3)
            edit_button.pack(side=tk.LEFT, padx=5)

            delete_button = tk.Button(row_frame, text="🗑", command=lambda i=idx: self.delete_test(i), width=3)
            delete_button.pack(side=tk.LEFT, padx=5)

    def play_test(self, index):
        messagebox.showinfo("Play Teste", f"Iniciando o {self.tests[index-1]['name']}")

    def edit_test(self, index):
        messagebox.showinfo("Editar Teste", f"Editando o {self.tests[index-1]['name']}")

    def delete_test(self, index):
        confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o {self.tests[index-1]['name']}?")
        if confirm:
            del self.tests[index - 1]
            self.update_list()

    def center_window(self, window, width, height):
        # Obtém o tamanho da tela
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calcula as coordenadas x e y para centralizar a janela
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Define a posição da janela
        window.geometry(f"{width}x{height}+{x}+{y}")


# Inicializa a janela principal
def main():
    root = tk.Tk()
    app = TestManagerApp(root)

    # Tamanho da janela
    width = 900
    height = 600

    # Centraliza a janela principal
    center_window(root, width, height)

    root.mainloop()


def center_window(window, width, height):
    # Obtém o tamanho da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula as coordenadas x e y para centralizar a janela
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Define a posição e o tamanho da janela
    window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    main()

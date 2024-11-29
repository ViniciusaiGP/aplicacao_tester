import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
from functions.screenshot import Lightshot


class NewTestScreen:
    def __init__(self, master):
        self.master = master
        master.title("Ações")

        # Título
        self.title_label = tk.Label(master, text="Ações", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Campo para o nome do teste
        self.test_name_frame = tk.Frame(master)
        self.test_name_frame.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(self.test_name_frame, text="Nome do Teste:").pack(side=tk.LEFT)
        self.test_name_entry = tk.Entry(self.test_name_frame, width=30)
        self.test_name_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        # Botão para adicionar nova ação
        self.add_action_button = tk.Button(master, text="Adicionar Ação", command=self.add_action)
        self.add_action_button.pack(pady=10)

        # Frame para a lista de ações
        self.actions_frame = tk.Frame(master)
        self.actions_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Lista de ações
        self.actions = []
        self.update_actions()

    def add_action(self):
        # Adiciona uma nova ação à lista
        self.actions.append({"name": "", "type": "Tipo 1", "image": None})
        self.update_actions()

    def update_actions(self):
        # Remove todos os widgets antes de recriar
        for widget in self.actions_frame.winfo_children():
            widget.destroy()

        for idx, action in enumerate(self.actions, start=1):
            row_frame = tk.Frame(self.actions_frame)
            row_frame.pack(fill=tk.X, pady=5)

            # Número
            tk.Label(row_frame, text=f"{idx}.", width=5, anchor=tk.W).pack(side=tk.LEFT)

            # Campo de texto para o nome da ação
            name_entry = tk.Entry(row_frame, width=30)
            name_entry.insert(0, action["name"])
            name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
            name_entry.bind("<KeyRelease>", lambda e, i=idx: self.update_action_name(i, name_entry.get()))

            # Dropdown para o tipo de ação
            type_var = tk.StringVar(value=action["type"])
            type_dropdown = ttk.Combobox(row_frame, textvariable=type_var, values=["Tipo 1", "Tipo 2", "Tipo 3"], width=10)
            type_dropdown.pack(side=tk.LEFT, padx=5)
            type_dropdown.bind("<<ComboboxSelected>>", lambda e, i=idx: self.update_action_type(i, type_var.get()))

            # Botão para carregar imagem
            image_button = tk.Button(row_frame, text="🖼", command=lambda i=idx: self.load_image(i), width=3)
            image_button.pack(side=tk.LEFT, padx=5)

            # Botão de lixeira
            delete_button = tk.Button(row_frame, text="🗑", command=lambda i=idx: self.delete_action(i), width=3)
            delete_button.pack(side=tk.LEFT, padx=5)

    def update_action_name(self, index, name):
        self.actions[index - 1]["name"] = name

    def update_action_type(self, index, action_type):
        self.actions[index - 1]["type"] = action_type

    def load_image(self, index):
        ret = Lightshot.screenshot()

    def delete_action(self, index):
        confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir a ação {index}?")
        if confirm:
            del self.actions[index - 1]
            self.update_actions()


# Inicializa a janela principal
def main():
    root = tk.Tk()
    app = NewTestScreen(root)
    root.geometry("500x400")  # Tamanho da janela
    root.mainloop()


if __name__ == "__main__":
    main()

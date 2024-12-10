import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from functions.event_pyautogui import EventPyautogui
from functions.screenshot import Lightshot
from widgets.imagem_selector import ImageActionModal


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

        # Botões Salvar e Cancelar
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=10)

        self.save_button = tk.Button(self.buttons_frame, text="Salvar", command=self.save, width=12)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = tk.Button(self.buttons_frame, text="Cancelar", command=self.cancel, width=12)
        self.cancel_button.pack(side=tk.LEFT)

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
            name_entry.bind("<KeyRelease>", lambda e, i=idx-1: self.update_action_name(i, name_entry.get()))

            # Dropdown para o tipo de ação
            type_var = tk.StringVar(value=action["type"])
            list_translated = sorted(
                [method["textoTranslate"] for method in EventPyautogui.get_useful_methods()]
            )  # Ordenação alfabética
            type_dropdown = ttk.Combobox(row_frame, textvariable=type_var, values=list_translated, width=15)
            type_dropdown.pack(side=tk.LEFT, padx=5)
            type_dropdown.bind("<<ComboboxSelected>>", lambda e, i=idx-1: self.update_action_type(i, type_var.get()))

            # Botão para carregar imagem
            image_button = tk.Button(
                row_frame,
                text="Captura de tela",
                command=lambda i=idx-1: self.show_image_action_modal(i),
                width=15
            )
            image_button.pack(side=tk.LEFT, padx=5)

            # Botão de lixeira
            delete_button = tk.Button(row_frame, text="🗑", command=lambda i=idx-1: self.delete_action(i), width=3)
            delete_button.pack(side=tk.LEFT, padx=5)

    def show_image_action_modal(self, action_index):
        # Chama a modal com as opções de imagem
        modal = ImageActionModal(self.master, action_index, self.update_action_image)

    def update_action_name(self, index, name):
        self.actions[index]["name"] = name

    def update_action_type(self, index, action_type):
        self.actions[index]["type"] = action_type

    def update_action_image(self, image_path):
        # Atualiza o caminho da imagem no dicionário de ações
        self.actions[-1]["image"] = image_path
        messagebox.showinfo("Imagem Carregada", f"Imagem carregada com sucesso: {image_path}")

    def delete_action(self, index):
        confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir a ação {index + 1}?")
        if confirm:
            del self.actions[index]
            self.update_actions()

    def save(self):
        # Salva as ações (você pode implementar aqui a lógica de salvar os dados)
        test_name = self.test_name_entry.get()
        if not test_name:
            messagebox.showwarning("Aviso", "O nome do teste é obrigatório!")
            return

        # Aqui você pode adicionar a lógica para salvar os dados
        messagebox.showinfo("Sucesso", f"Test '{test_name}' salvo com sucesso!\n\nAções: {self.actions}")

    def cancel(self):
        # Cancela a ação e fecha a janela
        confirm = messagebox.askyesno("Confirmar Cancelamento", "Tem certeza que deseja cancelar?")
        if confirm:
            self.master.destroy()


# Inicializa a janela principal
def main():
    root = tk.Tk()
    app = NewTestScreen(root)
    root.geometry("900x500")  # Tamanho da janela ajustado
    root.mainloop()


if __name__ == "__main__":
    main()

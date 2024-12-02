import tkinter as tk
from tkinter import filedialog


def selecionar_arquivo():
    # Cria a janela principal
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Abre o diálogo de seleção de arquivo
    arquivo = filedialog.askopenfilename(title="Selecione um arquivo",
                                         filetypes=[("Arquivos de texto", "*.txt"),
                                                    ("Todos os arquivos", "*.*")])
    if arquivo:
        print(f"Arquivo selecionado: {arquivo}")
    else:
        print("Nenhum arquivo foi selecionado.")




# Inicializa a janela principal
def main():
    selecionar_arquivo()


if __name__ == "__main__":
    main()

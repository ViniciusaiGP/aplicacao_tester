import tkinter as tk
from tkinter import filedialog

from utils.convert_base64 import ConvertArchive


class OpenFolder:
    def selecionar_arquivo():
        # Cria a janela principal
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal

        # Abre o diálogo de seleção de arquivo
        arquivo = filedialog.askopenfilename(title="Selecione um arquivo",
                                             filetypes=[("Imagens", "*.*"),
                                                        ("Todos os arquivos", "*.*")])
        if arquivo:
            ConvertArchive.convert_file_to_base64(arquivo)
            #print(f"Arquivo selecionado: {arquivo}")
            return 'Arquivo gerado para base64'
        else:
            print("Nenhum arquivo foi selecionado.")

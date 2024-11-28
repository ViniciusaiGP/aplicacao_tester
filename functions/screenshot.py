import tkinter as tk
import os
import uuid
from PIL import ImageGrab

# Função principal que será chamada externamente
def take_screenshot_interactive(save_path=r"screenshots"):
    # Certifique-se de que o diretório de destino existe
    if save_path is None:
        # Define o caminho absoluto para a pasta screenshots
        save_path = os.path.abspath(r"screenshots")

    # Cria o diretório, se necessário
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    def take_screenshot(x1, y1, x2, y2):
        # Define as coordenadas corretamente (ordena x1, x2 e y1, y2)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        random_name = f"screenshot_{uuid.uuid4().hex}.png"

        # Captura a área selecionada
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        file_path = os.path.join(save_path, random_name)
        screenshot.save(file_path)
        print(f"Screenshot salva em: {file_path}")
        print(f"Coordenadas usadas: x1={x1}, y1={y1}, x2={x2}, y2={y2}")

    def start_selection(event):
        global start_x, start_y
        start_x, start_y = event.x, event.y
        canvas.delete("selection")  # Remove qualquer seleção anterior

    def update_selection(event):
        canvas.delete("selection")  # Redesenha a seleção
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tags="selection")

    def end_selection(event):
        global start_x, start_y
        # Calcula as coordenadas finais e tira a captura
        x1, y1, x2, y2 = start_x, start_y, event.x, event.y
        root.destroy()  # Fecha a janela
        take_screenshot(x1, y1, x2, y2)  # Captura a área selecionada

    # Configuração inicial da janela de seleção
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Tela cheia
    root.attributes("-alpha", 0.3)  # Escurece a tela
    root.configure(bg="black")  # Tela preta semi-transparente

    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Eventos do mouse
    canvas.bind("<Button-1>", start_selection)  # Início da seleção
    canvas.bind("<B1-Motion>", update_selection)  # Atualização da seleção
    canvas.bind("<ButtonRelease-1>", end_selection)  # Finaliza a seleção

    root.mainloop()

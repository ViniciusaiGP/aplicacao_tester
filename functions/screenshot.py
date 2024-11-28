import tkinter as tk
import os
import uuid
from PIL import ImageGrab

# Função principal que será chamada externamente
def screenshot(save_path=r"./screenshots"):
    var = {}

    # Verifica se o diretório de destino existe
    if save_path is None:
        save_path = os.path.abspath(r"./screenshots")

    # Cria o diretório, se necessário
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    def get_screen_size():
        # Obtém a largura e a altura da tela
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        print(f"Resolução total da tela: {screen_width}x{screen_height}")
        return {"width": screen_width, "height": screen_height}

    def take_screenshot(x1, y1, x2, y2):
        # Define as coordenadas corretamente (ordena x1, x2 e y1, y2)
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        random_name = f"screenshot_{uuid.uuid4().hex}.png"

        # Captura a área selecionada
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Garante que o caminho esteja correto
        file_path = os.path.join(save_path, random_name)
        
        # Salva a captura
        screenshot.save(file_path)
        print(f"Screenshot salva em: {file_path}")
        print(f"Coordenadas usadas: x1={x1}, y1={y1}, x2={x2}, y2={y2}")

        # Cálculo do centro
        centro_x = (x1 + x2) / 2
        centro_y = (y1 + y2) / 2

        print(f"Centro da área: ({centro_x}, {centro_y})")
        
        # Retorna os dados estruturados
        return {
            "file_path": file_path,
            "coordinates": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
            "center": {"x": centro_x, "y": centro_y},
        }

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
        # Captura a área selecionada e atualiza a variável var
        var.update(take_screenshot(x1, y1, x2, y2))

    def cancel_selection(event):
        # Fechar a janela sem fazer a captura
        print("Ação cancelada.")
        root.destroy()

    # Configuração inicial da janela de seleção
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Tela cheia
    root.attributes("-alpha", 0.3)  # Escurece a tela
    root.configure(bg="black")  # Tela preta semi-transparente

    # Obtém o tamanho total da tela
    screen_size = get_screen_size()
    var["screen_size"] = screen_size  # Adiciona as dimensões da tela ao retorno

    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Eventos do mouse
    canvas.bind("<Button-1>", start_selection)  # Início da seleção
    canvas.bind("<B1-Motion>", update_selection)  # Atualização da seleção
    canvas.bind("<ButtonRelease-1>", end_selection)  # Finaliza a seleção

    # Evento de tecla ESC para cancelar a captura
    root.bind("<Escape>", cancel_selection)

    root.mainloop()

    return var

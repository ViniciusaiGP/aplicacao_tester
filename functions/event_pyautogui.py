import pyautogui

def execute_pyautogui_event(event, *args, **kwargs):
    """
    Executa dinamicamente uma função do pyautogui com base no nome da função.

    Args:
        event (str): O nome do evento/método do pyautogui a ser executado.
        *args: Argumentos posicionais para o método.
        **kwargs: Argumentos nomeados para o método.

    Returns:
        O resultado da chamada do método, se houver retorno.
    """
    try:
        # Obtém o método do pyautogui dinamicamente
        method = getattr(pyautogui, event)
        
        # Verifica se é um método chamável
        if callable(method):
            return method(*args, **kwargs)
        else:
            raise ValueError(f"O atributo '{event}' não é um método.")
    except AttributeError:
        raise AttributeError(f"'{event}' não é um método válido do pyautogui.")
    except Exception as e:
        raise RuntimeError(f"Erro ao executar '{event}': {e}")

# Exemplo de uso:
try:
    # Move o mouse para a posição (100, 100)
    execute_pyautogui_event("moveTo", 100, 100)

    # Pressiona a tecla 'enter'
    execute_pyautogui_event("press", "enter")
    
    # Obtem a posição atual do mouse
    position = execute_pyautogui_event("position")
    print(f"Posição atual do mouse: {position}")
except Exception as e:
    print(e)

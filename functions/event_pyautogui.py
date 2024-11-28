import pyautogui

class EventPyautogui:
    def execute(event, *args, **kwargs):
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
    
    def auto_complete_event():
        """
        Retorna uma string com sugestões de métodos chamáveis no pyautogui.
        """
        return "\n".join([method for method in dir(pyautogui) if callable(getattr(pyautogui, method)) and not method.startswith('_')])

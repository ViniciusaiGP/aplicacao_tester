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

    def get_useful_methods():
        useful_keywords = ["click", "write", "drag", "move", "press", "type", "scroll"]
        exclude_methods = ["typewrite"]  # Lista de métodos que você não quer no retorno
        translations = {
            "click": "clicar",
            "doubleClick": "clique duplo",
            "drag": "arrastar",
            "dragRel": "arrastar relativo",
            "dragTo": "arrastar para",
            "hscroll": "rolagem horizontal",
            "leftClick": "clique esquerdo",
            "middleClick": "clique do meio",
            "move": "mover",
            "moveRel": "mover relativo",
            "moveTo": "mover para",
            "press": "pressionar",
            "rightClick": "clique direito",
            "scroll": "rolar",
            "tripleClick": "clique triplo",
            "vscroll": "rolagem vertical",
            "write": "escrever",
        }

        methods = [
            {
                "textoOrg": method,
                "textoTranslate": translations.get(method, "tradução não disponível"),
            }
            for method in sorted(
                [
                    method for method in dir(pyautogui)
                    if callable(getattr(pyautogui, method))
                       and not method.startswith('_')
                       and any(keyword in method.lower() for keyword in useful_keywords)
                       and method not in exclude_methods  # Exclui métodos indesejados
                ]
            )
        ]

        return methods


if __name__ == "__main__":
    EventPyautogui.get_useful_methods()
    print(EventPyautogui.get_useful_methods())

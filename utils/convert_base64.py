import base64
import json

class ConvertArchive:

    def convert_file_to_base64(file_path):
        """
        Converte um arquivo para uma string Base64.

        :param file_path: Caminho completo do arquivo.
        :return: String Base64 representando o conteúdo do arquivo.
        """
        try:
            with open(file_path, "rb") as file:
                base64_encoded = base64.b64encode(file.read()).decode("utf-8")
            return base64_encoded
        except FileNotFoundError:
            return "Erro: Arquivo não encontrado."
        except Exception as e:
            return f"Erro: {str(e)}"

    def save_base64_to_json(base64_string, json_file_path):
        """
        Salva uma string Base64 em um arquivo JSON.

        :param base64_string: String Base64.
        :param json_file_path: Caminho completo do arquivo JSON onde será salvo.
        """
        try:
            data = {"base64_content": base64_string}
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Base64 salvo em {json_file_path}")
        except Exception as e:
            print(f"Erro ao salvar o JSON: {str(e)}")

    # Caminho do arquivo e onde salvar o JSON
    file_path = "/Users/gttech-jonatas/Downloads/80dcdb6a-5ad3-4c9d-b203-e5d2d851caef.jpeg"
    json_file_path = "/Users/gttech-jonatas/Downloads/base64_output.json"

    # Convertendo para Base64
    base64_string = convert_file_to_base64(file_path)

    # Salvando em um arquivo JSON
    if "Erro" not in base64_string:
        save_base64_to_json(base64_string, json_file_path)
    else:
        print(base64_string)


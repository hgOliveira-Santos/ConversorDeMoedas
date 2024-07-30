import requests

def converter_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    requisição = requests.get(link)

    if requisição.status_code == 200:
        resposta_json = requisição.json()

        chave = f"{moeda_origem}{moeda_destino}"
        if chave in resposta_json:
            cotação = resposta_json[chave]["bid"]
            return cotação
        else:
            return "Chave não encontrada na resposta"
    else:
        return f"Erro na requisição: {requisição.status_code}"

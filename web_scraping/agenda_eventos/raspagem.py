import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"


def extrair_eventos(html: str) -> list[dict[str, object]]:
    """Extrai os dados dos eventos presentes em um HTML."""
    soup = BeautifulSoup(html, "html.parser")
    eventos = []

    for artigo in soup.select("main article"):
        titulo = artigo.select_one("h2")
        valores = {}

        for rotulo in artigo.select("dt"):
            valor = rotulo.find_next_sibling("dd")
            if valor is not None:
                valores[rotulo.get_text(" ", strip=True).lower()] = valor

        palestrante_elemento = valores.get("palestrante") or valores.get("palestrantes")
        palestrantes = []
        if palestrante_elemento is not None:
            itens = palestrante_elemento.select("li")
            if itens:
                palestrantes = [item.get_text(" ", strip=True) for item in itens]
            else:
                palestrantes = [palestrante_elemento.get_text(" ", strip=True)]

        link = artigo.select_one("a.inscricao")
        eventos.append(
            {
                "nome": titulo.get_text(" ", strip=True) if titulo else "",
                "data": valores.get("data", "").get_text(" ", strip=True)
                if valores.get("data")
                else "",
                "horario": valores.get("horário", "").get_text(" ", strip=True)
                if valores.get("horário")
                else "",
                "local": valores.get("local", "").get_text(" ", strip=True)
                if valores.get("local")
                else "",
                "palestrantes": palestrantes,
                "possui_mais_de_um_palestrante": len(palestrantes) > 1,
                "inscricao": {
                    "texto": link.get_text(" ", strip=True) if link else "",
                    "href": link.get("href", "") if link else "",
                },
            }
        )

    return eventos


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_eventos(eventos: list[dict[str, object]]) -> None:
    """Exibe os dados extraídos em formato legível."""
    print(f"Total de eventos: {len(eventos)}")

    for numero, evento in enumerate(eventos, start=1):
        palestrantes = evento["palestrantes"]
        print(f"\nEvento {numero}: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Horário: {evento['horario']}")
        print(f"Local: {evento['local']}")
        print(f"Palestrantes: {', '.join(palestrantes)}")
        print(
            "Possui mais de um palestrante: "
            f"{'Sim' if evento['possui_mais_de_um_palestrante'] else 'Não'}"
        )
        print(f"Link de inscrição: {evento['inscricao']['texto']}")
        print(f"Href: {evento['inscricao']['href']}")


if __name__ == "__main__":
    exibir_eventos(extrair_eventos(obter_html(URL)))

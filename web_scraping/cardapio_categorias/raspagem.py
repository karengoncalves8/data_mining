import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"


def texto(elemento) -> str:
    """Retorna o texto de um elemento ou string vazia se ele não existir."""
    return elemento.get_text(" ", strip=True) if elemento else ""


def extrair_cardapio(html: str) -> list[dict[str, object]]:
    """Extrai as seções do cardápio e os itens de cada uma."""
    soup = BeautifulSoup(html, "html.parser")
    categorias = []

    for secao in soup.select("main section.categoria"):
        itens = []

        for artigo in secao.select("article.item"):
            itens.append(
                {
                    "nome": texto(artigo.select_one("h3")),
                    "descricao": texto(artigo.select_one("p.descricao")),
                    "preco": texto(artigo.select_one("p.preco")),
                }
            )

        categorias.append({"categoria": texto(secao.select_one("h2")), "itens": itens})

    return categorias


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_cardapio(categorias: list[dict[str, object]]) -> None:
    """Exibe o cardápio preservando a organização por categoria."""
    for categoria in categorias:
        print("\n" + "=" * 40)
        print(f"{categoria['categoria'].upper()} ({len(categoria['itens'])} itens)")
        print("=" * 40)
        for item in categoria["itens"]:
            print(f"\n  {item['nome']} - {item['preco']}")
            print(f"  {item['descricao']}")


if __name__ == "__main__":
    exibir_cardapio(extrair_cardapio(obter_html(URL)))

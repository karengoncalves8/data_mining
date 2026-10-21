import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"


def extrair_produtos(html: str) -> list[dict[str, str]]:
    """Extrai os dados dos produtos presentes em um HTML."""
    soup = BeautifulSoup(html, "html.parser")
    produtos = []

    for artigo in soup.select("main article.produto"):
        titulo = artigo.select_one("h2")
        valores = {}

        for rotulo in artigo.select("dt"):
            valor = rotulo.find_next_sibling("dd")
            if valor is not None:
                valores[rotulo.get_text(" ", strip=True).lower()] = valor.get_text(
                    " ", strip=True
                )

        produtos.append(
            {
                "nome": titulo.get_text(" ", strip=True) if titulo else "",
                "fabricante": valores.get("fabricante", ""),
                "categoria": valores.get("categoria", ""),
                "preco": valores.get("preço", ""),
                "estoque": valores.get("estoque", ""),
            }
        )

    return produtos


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_produto(numero: int, produto: dict[str, str]) -> None:
    """Exibe os dados de um produto em formato legível."""
    print(f"\nProduto {numero}: {produto['nome']}")
    print(f"Fabricante: {produto['fabricante']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: {produto['preco']}")
    print(f"Estoque: {produto['estoque']}")


def exibir_produtos(produtos: list[dict[str, str]]) -> None:
    """Exibe todos os produtos e, depois, apenas os disponíveis."""
    print(f"Total de produtos: {len(produtos)}")
    for numero, produto in enumerate(produtos, start=1):
        exibir_produto(numero, produto)

    disponiveis = [produto for produto in produtos if produto["estoque"] == "Disponível"]
    print("\n" + "=" * 40)
    print(f"Produtos disponíveis: {len(disponiveis)}")
    print("=" * 40)
    for numero, produto in enumerate(disponiveis, start=1):
        exibir_produto(numero, produto)


if __name__ == "__main__":
    exibir_produtos(extrair_produtos(obter_html(URL)))

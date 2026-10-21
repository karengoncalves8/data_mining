import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"


def extrair_livros(html: str) -> list[dict[str, object]]:
    """Extrai os dados dos livros presentes em um HTML."""
    soup = BeautifulSoup(html, "html.parser")
    livros = []

    for artigo in soup.select("main article.livro"):
        titulo = artigo.select_one("h2")
        valores = {}

        for rotulo in artigo.select("dt"):
            valor = rotulo.find_next_sibling("dd")
            if valor is not None:
                valores[rotulo.get_text(" ", strip=True).lower()] = valor.get_text(
                    " ", strip=True
                )

        palavras_chave = [
            item.get_text(" ", strip=True) for item in artigo.select("ul.palavras-chave li")
        ]

        livros.append(
            {
                "titulo": titulo.get_text(" ", strip=True) if titulo else "",
                "autor": valores.get("autor", ""),
                "ano": valores.get("ano", ""),
                "genero": valores.get("gênero", ""),
                "situacao": valores.get("situação", ""),
                "palavras_chave": palavras_chave,
            }
        )

    return livros


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_livro(numero: int, livro: dict[str, object]) -> None:
    """Exibe os dados de um livro em formato legível."""
    print(f"\nLivro {numero}: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']}")
    print(f"Gênero: {livro['genero']}")
    print(f"Situação: {livro['situacao']}")
    print("Palavras-chave:")
    for palavra in livro["palavras_chave"]:
        print(f"  - {palavra}")


def exibir_livros(livros: list[dict[str, object]]) -> None:
    """Exibe todos os livros e, depois, apenas os disponíveis."""
    print(f"Total de livros: {len(livros)}")
    for numero, livro in enumerate(livros, start=1):
        exibir_livro(numero, livro)

    disponiveis = [livro for livro in livros if livro["situacao"] == "Disponível"]
    print("\n" + "=" * 40)
    print(f"Livros disponíveis: {len(disponiveis)}")
    print("=" * 40)
    for numero, livro in enumerate(disponiveis, start=1):
        exibir_livro(numero, livro)


if __name__ == "__main__":
    exibir_livros(extrair_livros(obter_html(URL)))

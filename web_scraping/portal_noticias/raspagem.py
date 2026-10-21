import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"
CATEGORIA_ESCOLHIDA = "Tecnologia"


def texto(elemento) -> str:
    """Retorna o texto de um elemento ou string vazia se ele não existir."""
    return elemento.get_text(" ", strip=True) if elemento else ""


def extrair_noticias(html: str) -> list[dict[str, str]]:
    """Extrai os dados das notícias presentes em um HTML."""
    soup = BeautifulSoup(html, "html.parser")
    noticias = []

    for artigo in soup.select("main article.noticia"):
        data = artigo.select_one("time")
        noticias.append(
            {
                "categoria": texto(artigo.select_one(".categoria")),
                "titulo": texto(artigo.select_one("h2")),
                "data": texto(data),
                "data_iso": data.get("datetime", "") if data else "",
                "resumo": texto(artigo.select_one("p.resumo")),
                "autor": texto(artigo.select_one("p.autor span")),
            }
        )

    return noticias


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_noticias(noticias: list[dict[str, str]], categoria: str) -> None:
    """Exibe todas as notícias e, ao final, os títulos da categoria escolhida."""
    print(f"Total de notícias: {len(noticias)}")

    for numero, noticia in enumerate(noticias, start=1):
        print("\n" + "-" * 40)
        print(f"Notícia {numero}")
        print("-" * 40)
        print(f"Categoria: {noticia['categoria']}")
        print(f"Título: {noticia['titulo']}")
        print(f"Data: {noticia['data']} ({noticia['data_iso']})")
        print(f"Resumo: {noticia['resumo']}")
        print(f"Autor: {noticia['autor']}")

    titulos = [
        noticia["titulo"]
        for noticia in noticias
        if noticia["categoria"].lower() == categoria.lower()
    ]
    print("\n" + "=" * 40)
    print(f"Títulos da categoria {categoria}: {len(titulos)}")
    print("=" * 40)
    for titulo in titulos:
        print(f"- {titulo}")


if __name__ == "__main__":
    exibir_noticias(extrair_noticias(obter_html(URL)), CATEGORIA_ESCOLHIDA)

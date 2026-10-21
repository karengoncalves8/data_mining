import requests

from bs4 import BeautifulSoup


URL = "http://127.0.0.1:8000"


def extrair_cursos(html: str) -> list[dict[str, object]]:
    """Extrai os dados dos cursos presentes em um HTML."""
    soup = BeautifulSoup(html, "html.parser")
    cursos = []

    for artigo in soup.select("main article.curso"):
        titulo = artigo.select_one("h2")
        valores = {}

        for rotulo in artigo.select("dt"):
            valor = rotulo.find_next_sibling("dd")
            if valor is not None:
                valores[rotulo.get_text(" ", strip=True).lower()] = valor

        assuntos = [item.get_text(" ", strip=True) for item in artigo.select("ul.assuntos li")]

        cursos.append(
            {
                "nome": titulo.get_text(" ", strip=True) if titulo else "",
                "area": valores["área"].get_text(" ", strip=True)
                if valores.get("área")
                else "",
                "carga_horaria": valores["carga horária"].get_text(" ", strip=True)
                if valores.get("carga horária")
                else "",
                "assuntos": assuntos,
            }
        )

    return cursos


def obter_html(url: str) -> str:
    """Obtém o HTML da página servida pelo servidor local."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    return resposta.text


def exibir_cursos(cursos: list[dict[str, object]]) -> None:
    """Exibe os dados extraídos em formato legível."""
    print(f"Total de cursos: {len(cursos)}")

    for numero, curso in enumerate(cursos, start=1):
        print(f"\nCurso {numero}: {curso['nome']}")
        print(f"Área: {curso['area']}")
        print(f"Carga horária: {curso['carga_horaria']}")
        print("Assuntos estudados:")
        for posicao, assunto in enumerate(curso["assuntos"], start=1):
            print(f"  {posicao}. {assunto}")


if __name__ == "__main__":
    exibir_cursos(extrair_cursos(obter_html(URL)))

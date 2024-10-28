from openai import OpenAI
import PyPDF2
from dotenv import load_dotenv

load_dotenv()
API_ENV = os.getenv('API_KEY')

# Configure sua chave de API do OpenAI
client = OpenAI(
    api_key = API_ENV
)
def ler_pdf(caminho):
    """Lê o conteúdo de um PDF e retorna como texto."""
    texto = ""
    with open(caminho, "rb") as arquivo_pdf:
        leitor = PyPDF2.PdfReader(arquivo_pdf)
        for pagina in leitor.pages:
            texto += pagina.extract_text() + "\n"
    return texto

def perguntar(texto_pdf, pergunta):
    """Faz uma pergunta sobre o texto do PDF usando a API do OpenAI."""
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ou outro modelo desejado
        messages=[
            {"role": "user", "content": f"Texto do PDF:\n{texto_pdf}\n\n. Pergunta: {pergunta}"}
        ]
    )
    resposta = resposta.choices[0].message.content
    return resposta
       
def main():
    caminho_pdf = 'WEG-w22-three-phase-electric-motor-50029265-brochure-english-web-6-2.pdf'  # Altere para o caminho do seu PDF
    texto_pdf = ler_pdf(caminho_pdf)

    while True:
        pergunta = input("Faça sua pergunta sobre o PDF (ou digite 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            break
        resposta = perguntar(texto_pdf, pergunta)
        print("Resposta:", resposta)

if __name__ == "__main__":
    main()
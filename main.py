# 1 - Importar bibliotecas
import pyttsx3
import PyPDF2

# 2 -  Abrir o arquivo PDF
pdf_file = open('meu_arquivo.pdf', 'rb')

# 3 - Criar um objeto de leitura do PDF
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# 4 -Obter o número total de páginas do PDF
num_pages = pdf_reader.numPages

# 5 - Criar um objeto de sintetização de voz
engine = pyttsx3.init()

# 6 - Percorrer cada página do PDF
for page in range(num_pages):
    # 7 - Extrair o texto da página atual
    page_text = pdf_reader.getPage(page).extractText()

    # 8 - Configurar a velocidade da voz
    engine.setProperty('rate', 150)

    # 9 - Sintetizar a voz para o texto da página
    engine.say(page_text)

    # 10 -Reproduzir o áudio
    engine.runAndWait()

# 11 - Fechar o arquivo PDF
pdf_file.close()
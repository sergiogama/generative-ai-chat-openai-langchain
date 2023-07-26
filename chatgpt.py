# Autor: Sergio Gama
import os
import pdfplumber
from langchain.document_loaders import TextLoader

pdf = 0
if pdf == 1:
    pdf_file = 'Reforma-Tributaria-2023.pdf'
    with pdfplumber.open(pdf_file) as pdf:
        # Remove a local file if it exists
        if os.path.exists('data_from_pdf.txt'):
            os.remove('data_from_pdf.txt')
            
        # ler todas as páginas do pdf e salve em um arquivo local
        for i in range(0, len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()

            with open('data_from_pdf.txt', 'a') as f:
                f.write(text)
                f.write('\n')
                f.close()
    loader = TextLoader('data_from_pdf.txt')
else:
    loader = TextLoader('data.txt', autodetect_encoding=True)

from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

# prompt para o usuário digitar a pergunta, em loop
while True:
    query = input("Digite a pergunta: ")
    print(index.query(query))

#query = "O que seria o IVA?" # Pergunta para os dados da reforma tributária
#print(index.query(query))

#query = "Quais produtos tem, e qual é o mais barato?" # Pergunta parta os dados de produtos contidos em data.txt
#print(index.query_with_sources(query))

#query = "Quanta custa o sapato, e quantos tem em estoque?" # Pergunta parta os dados de produtos contidos em data.txt
#print(index.query_with_sources(query))


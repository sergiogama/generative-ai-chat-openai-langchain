# Autor: Sergio Gama
import os
import pdfplumber

roda = 0
if roda == 1:
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

from langchain.document_loaders import TextLoader
if roda == 1:
    loader = TextLoader('data_from_pdf.txt')
else:
    loader = TextLoader('data.txt', autodetect_encoding=True)

from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

# prompt para o su;ario digitar a pergunta, em loop
while True:
    query = input("Digite a pergunta: ")
    print(index.query(query))









#query = "Qual o preço do sapato?"
#query = "Quantos dias tenho para devolver um produto? em português"
#query = "Sergio Gama já trabalhou fora do Brasil? em português"
#print(index.query(query))

#query = "Tem sapato no estoque?"
#query = "E quanto ao manual do produto, é obrigado ser fornecido?"
#query = "Qual a formação do Sergio Gama? em português"
#print(index.query(query))

#query = "Qual o produto mais barato que você tem?"
#query = "Quantos anos Sergio Gama trabalhou na IBM? em português"
#query = "Por liste os principais direitos do consumidor"
#print(index.query(query))

#query = "As áreas de serviços serão afetadas, se sim, como?"
#query = "Quantos anos Sergio Gama trabalhou na IBM? em português"
#query = "Por liste os principais direitos do consumidor"
#print(index.query(query))

#query = "Quem é Sergio?"
#print(index.query_with_sources(query))

#query = "Qual o telefone do Sergio Gama. Em português"
#print(index.query_with_sources(query))


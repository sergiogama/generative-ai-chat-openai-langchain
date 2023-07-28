# Generative AI Chat - OpenAI Langchain (Chat Gerativo de IA - OpenAI Langchain)

Este repositório contém um script Python que possibilita a extração de dados de um arquivo PDF (se necessário) e permite a realização de consultas interativas aos dados utilizando a biblioteca `langchain` juntamente com o modelo GPT-3.5 da OpenAI.

## Pré-requisitos

Antes de executar o script, certifique-se de que possui os seguintes pacotes instalados em seu sistema:

- langchain
- openai
- chromadb
- tiktoken
- pdfplumber

Você pode instalar os pacotes necessários usando `pip` com o seguinte comando:

```bash
pip install langchain openai chromadb tiktoken pdfplumber
```

Além disso, será necessário criar uma chave de API para a plataforma da OpenAI. Siga os passos abaixo para obter e configurar sua chave de API:

1. Crie uma conta na OpenAI em https://platform.openapi.com/account/api-keys, caso ainda não tenha uma.

2. Gere uma nova chave de API e certifique-se de mantê-la em segurança.

3. Exporte a chave de API como uma variável de ambiente em seu sistema. Substitua `<API_KEY>` pela sua chave de API real.

   ```bash
   export OPENAI_API_KEY="<API_KEY>"
   ```
## Diagrama da solução

![Captura de Tela 2023-07-28 às 17 37 59](https://github.com/sergiogama/generative-ai-chat-openai-langchain/assets/7747903/f0bb5864-a205-4c49-a956-4273c8580b61)

Obs.: Gerado por Generative AI, à partir do código

## Uso

1. Clone este repositório para sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/sergiogama/generative-ai-chat-openai-langchain.git
```

2. Navegue para o diretório do repositório:

```bash
cd generative-ai-chat-openai-langchain
```

3. Abra o script Python `script_name.py` em um editor de texto ou um Ambiente de Desenvolvimento Integrado (IDE).

4. Dependendo de suas necessidades, ajuste o valor da variável `pdf`:

   - Se `pdf` estiver definido como 1:
     - O script extrairá dados do arquivo PDF especificado por `pdf_file` e os salvará em um arquivo de texto local chamado `data_from_pdf.txt`.
     - Certifique-se de que a variável `pdf_file` esteja configurada com o caminho correto do arquivo PDF que você deseja extrair dados.

   - Se `pdf` estiver definido como 0:
     - O script carregará dados de um arquivo de texto existente chamado `data.txt`.
     - Certifique-se de que o arquivo `data.txt` contenha os dados que você deseja consultar.

5. Execute o script usando o seguinte comando:

```bash
python script_name.py
```

6. Você será solicitado a inserir uma pergunta. Digite sua pergunta e pressione `Enter` para obter as respostas relevantes com base nos dados extraídos.

7. Para sair do loop e interromper o script, pressione `Ctrl + C`.

## Código Fonte

O código-fonte deste projeto está disponível no GitHub. Você pode clonar o repositório usando o seguinte link:

[Generative AI Chat - OpenAI Langchain](https://github.com/sergiogama/generative-ai-chat-openai-langchain.git)

Sinta-se à vontade para explorar o código-fonte, contribuir para o projeto ou usá-lo como referência para suas próprias tarefas de extração e consulta de dados.

## Notas Adicionais

- O script utiliza a biblioteca `pdfplumber` para extrair texto de um arquivo PDF. Se você encontrar algum problema com a extração de PDFs, verifique se possui a versão mais recente do `pdfplumber` instalada.

- A biblioteca `langchain` é usada para criar um índice e realizar consultas nos dados. Certifique-se de ter instalado as bibliotecas necessárias usando `pip`.

- Antes de executar o script, verifique se você configurou sua chave de API da OpenAI como uma variável de ambiente.

- Sinta-se à vontade para modificar o código conforme necessário ou integrá-lo em seus projetos para a extração e consulta de dados.

## Exemplos de Consultas

O script permite que você faça perguntas interativas com base nos dados e obtenha respostas. Aqui estão alguns exemplos de consultas que você pode experimentar:

1. "O que seria o IVA?" (Pergunta relacionada aos dados da reforma tributária)
2. "Quais produtos tem, e qual é o mais barato?" (Pergunta relacionada aos dados de produtos armazenados em `data.txt`)
3. "Quanto custa o sapato, e quantos tem em estoque?" (Pergunta relacionada aos dados de produtos armazenados em `data.txt`)

Sinta-se à vontade para experimentar diferentes consultas e explorar as capacidades do script.

É isso! Agora você tem um poderoso script Python para extrair dados de PDFs, usar o modelo GPT-3.5 da OpenAI para conversações gerativas e realizar consultas interativas. Feliz codificação!

Obs: Criado pelo ChatGPT baseado no código

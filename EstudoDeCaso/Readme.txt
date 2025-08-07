#Estudo de caso - Deploy de app com docker e agente de ia para provisionamento de infraestrutura IaC

#Estrtutura de arquivos do estudo de caso:
# .
# ├── app
# │   ├── app.py
# │   └── requirements.txt
# ├── .env
# ├── docker-compose.yml
# └── Dockerfile

#Passo 1: Arquivos e Diretórios
- Crie estrutura de diretórios e os arquivos exatamente como mostrado acima.

#Passo 2: Configure sua chave api da OpenAI
- Crie um arquivo chamado .env na raiz do seu projeto (no mesmo nível que o docker-compose.yml).
- Abra o arquivo .env e adicione sua chave de API da OpenAI: OPENAI_API_KEY=sk-xxxxx
- Importante: Substitua sk-xxxxx pela sua chave real da OpenAI.

# Passo 3: Construa e Execute o Contêiner Docker

- Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
- Abra um terminal na raiz do seu projeto.
- Execute o seguinte comando:

docker-compose -p dsaestudodecaso up --build

- Este comando irá:

- Construir a imagem Docker com base no seu Dockerfile, instalando todas as dependências.
- Iniciar um contêiner a partir dessa imagem.
- Mapear a porta 8501 do contêiner para a porta 8000 da sua máquina local.

# Passo 4: Interaja com o Agente

- Após a conclusão do comando, abra seu navegador e acesse:

http://localhost:8501

- Teste a app, por exemplo, com esse texto: Crie o código IaC com Terraform para criar um bucket S3 na AWS com o nome 'dsa-bucket-super-seguro-12345', com versionamento e criptografia SSE-S3 habilitados.





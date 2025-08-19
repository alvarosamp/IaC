## Estudo de caso - Deploy de app com docker e agente de ia para provisionamento de infraestrutura IaC

# Estrutura de arquivos do estudo de caso:

 ├── app
 │   ├── app.py
 │   └── requirements.txt
 ├── .env
 ├── docker-compose.yml
 └── Dockerfile

# Passo 1 : Arquivos e Diretorios 
- Crie a estrutura de diretórios como mostrado acima

# Passo 2: Configure sua chave api da OpenAi
- Crie um arquivo chamado .env na raiz do seu projeto (no mesmo nível que o docker-compose.yaml)
- ABra o arquivo .env sua chave api da open ai
- Importante : Substitua sk-xxxx pela suachave real da open ai

# Passo 3 : Construa e execute o container docker
- Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina
- Abra um terminal na raiz do projeto 
- Execute o seguinte comando :

'docker-compose -p dsaestudocaso up --build'

# Este comando irá :
- Construir a imagem docker com base no seu dockerfile, instlaando todas as dependencias
- Iniciar um container a partir dessa imagem
- Mapear a porta 8501 do container para a porta 8000  da maquina local

# Passo 4 : Interaja com o agente
- Apos a conclusao do comando, abra seu navegador e acesse
'http://localhost:8501'

- Teste a app, por exemplo, com esse texto : Crie o codigo IaC com terraform para criar um bucket B3 na AWS com nome 'dsa-bucket-super-seguro-12345', com versionamento e criptografia SSE-S3 habilitados;  
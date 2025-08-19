# Instruções do lab1

# Abra o terminal ou prompt de comando e navegue até a pasta onde voce esta trabalhando

# Execute o comando abaixo para criar a imagem Docker
docker build -t dsa-terraform-image:lab1 .

# Execute o comando abaixo para criar o container Docker
docker run -dit --name dsa-lab1 dsa-terraform-image:lab1 /bin/bash

# Verifique as versões do terraform e do AWS CLI com os comandos abaixo

terraform version
aws --version

# Para rodar o codigo, primeiro precisamos iniciar o terraform dentro do terminal do container
terraform init

# Para checar se os arquivoos foram criados (dentro do terminal do container)
ls -la

# Para rodar o projeto da automação rodamos
terraform apply
colocar um yes 

# Para apagar a aplicação
terraform detroy (se deixar ligado consome horas aws)
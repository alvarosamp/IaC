# Dockerfile para a aplicação Python
# Este arquivo define a imagem Docker para executar um script Python simples.

#Falando para executar o Python 3.12 em uma imagem leve 
FROM python:3.12-slim  

# Copia o arquivo Python para dentro do container
# Isso permite que o script seja executado quando o container for iniciado.
COPY testedsa.py /testedsa.py

# Define o comando a ser executado quando o container iniciar
CMD ["python", "/testedsa.py"]
#Imagem base:
FROM python:3.12-slim

#Define o diretorio de trabalho dentro do container
WORKDIR /app
#Copia o arquivo de requisitos para o container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copia o restante dos arquivos para o container
COPY . .

#Expoe a porta do stramlit
EXPOSE 8501

#Comando para rodar o streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address= 0.0.0.0"]
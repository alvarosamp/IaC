#Imagem base
FROM python:3.12.3-slim

#Define o diretorio de trabalho dentro do container
WORKDIR /app

#Copia e instala as dependencias python
COPY C:\Users\vish8\OneDrive\Desktop\DSA\IaC\Iac\FundamentosDocker\EC1\app\requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

#Copia o restante dos arquivos da aplicação
COPY ./app .

#Expoe a porta do Streamlit
EXPOSE 8501

#Cmando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
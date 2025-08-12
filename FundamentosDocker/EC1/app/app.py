#Deploy de app com docker e agente de IA para provisionamento de Infraestrutura Iac
#Script para aplicação para criar a interface de usuário e gerenciar a interação com o agente de IA

import os
import streamlit as st
import crewai import Agent, Task, Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#Carregnado todas as variaveis de ambiente. Essencial para o docker
load_dotenv()

#Configuração de pagina do streamlit
st.set_page_config(
    page_title = 'Deploy de app com docker e agente de IA',
    page_icon = ':100',
    layout = 'wide',
)

st.title('Gerador de scripts terraform com agente de IA')
st.markdown('' \
'Esta ferramenta utiliza um agente de IA especializado para converter suas descrições de infraestrutura em código terraform' \
'(HCL)  pronto para uso')

#Configuração de agente crewaAI
# 0 try-except garante que nosso app mostre um erro amigavel se a chave da api nao for encontrada
try: 
    openai_llm = ChatOpenAI(
        model = 'gpt-4',
        api_key = os.getenv('OPENAI_API_KEY')
    )
except Exception
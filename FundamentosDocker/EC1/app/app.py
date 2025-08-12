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
except Exception as e:
    st.error(f'Erro ao inicializar o modelo de linguagem : {e}')
    openai_llm = None
#Define o agente de ia
terraform_expert = Agent(
  role='Especialista Sênior em Infraestrutura como Código',
  goal='Criar scripts Terraform precisos, eficientes e seguros com base nos requisitos do usuário.',
  backstory=(
    "Você é um Engenheiro de DataOps altamente experiente com uma década de experiência na automação "
    "de provisionamento de infraestrutura na nuvem usando Terraform. Você tem um profundo conhecimento "
    "dos provedores de nuvem como AWS, Azure e GCP, e é mestre em escrever código HCL (HashiCorp "
    "Configuration Language) limpo, modular e reutilizável. Sua missão é traduzir "
    "descrições de alto nível da infraestrutura desejada em código Terraform pronto para produção."
  ),
  verbose=True,
  allow_delegation=False,
  llm=openai_llm
)
# Interface do usurio 
prompt = st.text_area(
    "Forneça um prompt claro e detalhado. Quanto mais específico você for, melhor será o resultado.",
    height=150,
    placeholder="Exemplo: Crie o código IaC com Terraform para criar um bucket S3 na AWS com o nome 'dsa-bucket-super-seguro-12345', com versionamento e criptografia SSE-S3 habilitados."
)
if st.button('Gerar script terraform', type = 'primary', disabled= (not openai_llm)):
    if prompt:
        with st.spinner('Gerando script Terraform...'):
            try:
                #Define a tarefa para o agente com base no prompt do usuario
                terraform_task = Task(
                    description = (
                        f'Com base na seguinte solicitação do usaurio, gere um script em terraform completo e funcional.',
                        f'A saída deve ser APENAS o bloco de código HCL, sem nenhuma explicação ou texto adicional.',
                        f'O código deve ser bem formatado e pronto para ser salvo em um arquivo .tf \n\n'
                    ),
                    expected_output = 'Um bloco de código contendo o script terraform(HCL). O código deve ser completo e não deve conter placeholders como "sua configuração".',
                    agent = terraform_expert
                )
                #Cria e executa a equipe (CREW)
                terraform_crew = Crew(
                    agents = [terraform_expert],
                    tasks = [terraform_task],
                    process = Process.sequential,
                    verbose = True
                )

                #Inicia o processo e obtém o resultado
                result = terraform_crew.kickoff()
                
                #Exibe o resultado
                st.header('Resultado Gerado')
                st.code(result, language = 'terraform'),
                st.sucess('Script gerado com sucesso! Obrigado DSA')
            except Exception as e:
                st.error(f'Erro ao gerar o script durante a exução {e}')
    else:
        st.warning('Por favor, forneça um prompt antes de gerar o script.')
st.markdown('---')
st.markdown('Contruido com streamlit e crew ai)

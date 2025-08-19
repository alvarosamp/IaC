#Deploy de app com docker e agente de IA para provisionamento de Infraestrutura Iac
#Script para aplicação para criar a interface de usuário e gerenciar a interação com o agente de IA

import os
import time
import streamlit as st
import crewai
from crewai import Agent, Task, Crew
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
    openai_model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    openai_llm = ChatOpenAI(
        model = openai_model,
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
                    description=(
                        "Com base na seguinte solicitação do usuário, gere um script em Terraform completo e funcional. "
                        "A saída deve ser APENAS o bloco de código HCL, sem nenhuma explicação ou texto adicional. "
                        "O código deve ser bem formatado e pronto para ser salvo em um arquivo .tf.\n\n"
                        f"Solicitação do usuário: {prompt}"
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

                # Inicia o processo com tentativas e backoff para lidar com RateLimit/quota
                max_attempts = 3
                delay = 2  # segundos
                last_err = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        result = terraform_crew.kickoff()
                        break
                    except Exception as e:
                        msg = str(e)
                        last_err = e
                        if any(x in msg for x in [
                            'RateLimitError',
                            'rate limit',
                            'quota',
                            '429'
                        ]):
                            if attempt < max_attempts:
                                st.info(f"Limite de taxa/quota atingido. Nova tentativa em {delay}s (tentativa {attempt}/{max_attempts})…")
                                time.sleep(delay)
                                delay *= 2
                                continue
                        # Outro erro ou esgotou tentativas
                        raise
                
                #Exibe o resultado
                st.header('Resultado Gerado')
                st.code(result, language='terraform')
                st.success('Script gerado com sucesso! Obrigado DSA')
            except Exception as e:
                st.error(f'Erro ao gerar o script durante a execução: {e}')
                if any(x in str(e) for x in ['quota', 'RateLimit', '429']):
                    st.warning('Parece um erro de cota/limite de taxa. Verifique seu plano e créditos na OpenAI ou tente novamente mais tarde.')
    else:
        st.warning('Por favor, forneça um prompt antes de gerar o script.')
st.markdown('---')
st.markdown('Construído com streamlit e crew ai')

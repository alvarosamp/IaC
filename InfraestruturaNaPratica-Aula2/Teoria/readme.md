# Resumo teoria - Infraestrutura de codigo com IaC com Terraform, AWS, Azure e Datrabricks

## 1 -> Conceitos fundamentais 

**DevOps e IaC :** 
- DevOps é uma abordagem colaborativa que intergra desenvolvimento e operações, buscando maior agilidade, qualidade e frequencia nas entregas, com menos falhas.
- Envolve integração contínua(CI), entrega contínua (CD), automação e colaboração.
- IaC(Infraestructure as Code) é um pilar de DevOps, pois permite gerenciar infraestrutura de forma automatizada, versionada e declarativa.

-> Beneficios:
- Padronização das configurações
- Reprodutibilidade dos ambientes
- Redução de eros humanos
- Facilidade de auditoria e rollback

## 2-> Componentes de infraestrutura
- Servidores físicos ou virtuais
- Armazenamento(discos, cloud storage, banco de dados)
- Rede (roteadores, switches, firewall)
- Ferramentas de monitoramento e gestao (desempenho, incidente, qualidade)
- Plataformas de nuvem(AWS, Azure, GCP)
- Ferramentas de automação e provisionamento

## 3-> O que não é IaC :
- Gerenciamento manual da infraestrutura (sem scripts/ configuração automatizada)
- Scripts isolados que não integram toda a infraestrutura
- Ferramentas de configuração de servidores que não abrangem redes, nuvens e serviçoes.
- Código sem controle de versão -- IaC exige rastreabilidade e versionamento.
- Abordagem não declarativa - IaC foca no estado final desejado, não em instruções passo a passo.

## 4-> Quando e pq usar IaC :
- Para automatizar o provisionamento e configuração de recursos (VMs, containers, redes, storage)
- Em escalabilidade horizontal e vertical
- Na implantação ágil de aplicações 
- Em ambientes de nuvem, onde recursos podem ser criados e destruidos rapidamente
- Juntos o DevOps e metodologias ageis para acelerar o ciclo de desenvolvimento

## 5-> Como representar infraestrutura como codigo
 1 -> Escolher a ferramenta:
    - Terraform(HCL, multi-cloud, open source)
    - Ansible (YAML, automação agentless)
    - Chef (Ruby DSL, 'recipes')
    - Pupppet (Ruby DSL, gerenciamento declarativo)
    - AWS CloudFormation(JSON/YAML)
    - Azure ARM Templates (JSON)

 2 -> Aprender a linguagem de configuração da ferramenta

 3-> Definir o estado desejado da infraestrutura em arquivos de configuração

 4-> Versionar com o git
    

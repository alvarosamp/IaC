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

## 6 -> Testes unitários e integrados
**Testes unitários :**
São testes que garantem a qualidade, confiabilidade e desempenho adequado ao software. O teste unitário é realizado para verificar a funcionalidade de uma unidade de código isolada, como uma função ou método. O objetivo é testar cada parte do código de forma isolada para gartir se ela se comporta conforme o esperado, dado uma entrada específica.
Teste unitários tem as seguintes características :
 - Focam em unica unidade de código (função, método ou classe)
 - São rápidos e leves, o que permite a execução frequente durante o desenvolvimento
 - Utilizam técnicas de teste para simular o comportamento de componentes externos ou dependencias
 - Ajudam a identificar e corrigir problemas em estágios iniciais do desenvolvimento reduzindo o custo e o esforço da correção

**Testes intregrados :**
veriicam a iteração entre varias unidades de codigo, componente ou sistemas, garantindo que eles trabalhem juntos corretamente. São usados para identificar problemas de comunicação e incompatibilidade entre componentes que podem nao ser detectados pelos teste unitários isoladamente. Os testes integrados tem as seguintes características :
 - Focam nas iterações entre as unidades do código, componente ou sistemas
 - Podem ser mais lentos e mais complexos do uqe os testes unitários devido a necessidade de configurar e gerenciar varias dependecias
 - Ajudam a garantir que as interfaces e a comunicação entre componentes funcionem conforme o esperado, identificando o problemas de integração e incompatibilidade

Ambos dois tipos de teste servem para garantir a confiabilidade do software. Tendo o teste unitário para partes menores e os testes integrados para todo o sitema

## 7-> Integração contínua (CI/CD)

**CI**
A integração continua contem praticas que visam melhorar a aqualidade  e a velocidade das entregas de software. Juntas formam uma pipeline que automatiza o processo das entregas de software, permitindo uma entrega mais rapida e confiável.
Além disso, é um processo que garente que as mudanças no codigo fonte sejam integradas regularmente e testadas automaticamente, geralmente varias vezes ao dia. Reduzindo o tempo de lançamento de novos recursos e melhorias. O processo de CI geralmente incluem
 - Uso de um sistema como git para controle de versao
 - Automatizçaão do codigo e de testes unitários sempre que uma mudança é enviada ao repositorio do codigo.
 - Fornecimento de feedback rapido aos devs de sucesso ou falha da compilação e dos testes
 - Manutenção de um ambiente de integração onde as mudanças são testadas e validades antes de serem mescladas(merge) na branch principal

**CD**
A entrega contínua é uma extensão da CI que visa automatizar o processo de implantação do software em ambiente de produção ou pré-produção. Garantindo que o software esteja sempre pronto para ser lançado, permitindo lançamentos rápidos e confiáveis.
 - Automação da implementação de um software em ambiente real ou de teste
 - Execução de testes automatizados, como testes de integração, de desempenho, garantindo a qualidade do software.
 - Implementação automática do software em produção, ou implantação manual com aprovação.
 - Monitoramento e registro do desempenho e da ssaude do softweare em produção para facilitar e identificar os problemas;

Ao adotar uma pipeline CI/CD, as equipes podem entregar o codigo com uma qualidade maior e com maior rapidez, reduzindo o tempo de lançamento no mercado e melhorando a satisfação do usuário. Além disso, a automação ajuda a diminuir o risco de erros humanos e a garantir com praticas e politacas de desenoviment estabelecidas.

## 8-> Como entregar as mudanças em produção :
Para entregar algumas mudanças em produção temos alguns passos :

**Desenvolvimento e revisão do codigo :** Desenvolver o codigo para implementar novos recursos, correções e bugs. Fazer as reunioes com membros da equipe visando obter o melhor do codigo;

**Controle de versão :** Um sistema que controla as versões do código, como o git. Permitindo rastrear as mudanças, colaborar com outros desenvolvedores e manter um histórico de versoes.

**Testes automatizados :** Execute testes automatizados, incluindo testes unitários e de integração, garantindo que o software funcione conforme esperado e não introduza novos modelos.

**Integração contínua (CI) :** Usar um processo de CI para compilar, testar e validar o código regularmente , gartindo que as mudanças sejam integradas de maneira eficiente e que os problemas sejam identificados cedo.

**Entrega contínua (CD) :** Um processo de CD para implantar de forma automática o software em ambientes de teste ou pré-produção. Isso permite validr as mudanças em um ambiente proximo ao de produção antes do lançamento.

**Testes adicionais :** Realizar testes adicionais, como testes de carga, desempenho, segurança e aceitação do usuário, garantindo ao software diversos cenários e condições.

**Implementação em produção :** Quando o software passa por todos os testes e validações, implementar as mudanças em produção. Pode ser automática ou manual, dependendo da politica da equipe.

**Monitoramento e registro :** Monitorar o desempenho, disponibilidade e os eventos de segunraça do software em produção. Ajudando a identificar os problemas rapidamente e garante confirmidade com politas e requisitos de auditoria

**Feedback e ajustes :** Coletar feedback dos usuaurios e analise os dados de monitoramento e registro para identificar ares de melhoria e ajustar o software conforme necessário.

## 9-> Versionamento GitOps
Metodolia de gerenciamento e entrega da infraestrutura e aplicações que utiliza o sistema de controel de versão Git como fonte unica da verdade para a configuração e o estado desejado dos sistemas.
O versionamento com git nos permite algumas coisas:
 - Armazenamento de configuração em um repo GIT : Todas as configurações de infraestrutura e aplicação são armazenadas em um repo git. 
 - Declaração do estado desejado : A configuração no repo do git define o estado desejado dos sistemas. os devs alteram nessa parte para modificar a infraestrutura e as aplicações.
 - Automação e convergencia : As ferramentas de automação monitoram o repo do git em busca de mudanças de configuração e convergem o estado atual dos sistemas para o estado desejado declarado no git. Podendo incluir criação ou atualização de recursos de infraestrutura, a implementação de aplicações e de políticas de segurança.
 - Operações baseadas em pull request : Mudanças são feitas por meio de pull-request. isso permite que as equipes aceitem as mudanças antes do request.
 - Feedback e monitoramento : O estado atual dos sistemas é monitorado e registrado continuamente. As ferramentas podem gerar alertas ou eventos com bse em desvios do estasdo desejado.

O GitOps oferece várias vantagens em comparação às abordagens tradicionais de gerenciamento e entrega de infraestrutura e aplicações: 
 
 - Melhora a rastreabilidade e a auditoria, pois todas as mudanças na configuração são 
armazenadas no Git e associadas a um autor e a um histórico de commit. 
 - Facilita  a  colaboração  entre  desenvolvedores  e  operadores,  permitindo  que  ambos 
trabalhem com a mesma configuração e processo de controle de versão. 
 - Reduz o risco de erros humanos e inconsistências, pois as mudanças na configuração 
são revisadas, aprovadas e aplicadas automaticamente. 
 - Acelera o tempo de lançamento no mercado, pois as equipes podem fazer alterações 
na infraestrutura e nas aplicações com mais rapidez e confiança. 

## 10 -> Segurança e compliance
conformidade ao trabalhar com Infraestrutura como Código (IaC):

Aplique o princípio do menor privilégio, concedendo apenas os acessos necessários.
Gerencie chaves e senhas de forma segura e centralizada, usando ferramentas apropriadas.
Mantenha rastreabilidade e auditoria das mudanças na infraestrutura.
Utilize ferramentas de análise estática e verificação de conformidade, como Checkov e Terrascan.
Integre testes automatizados de segurança no pipeline CI/CD.
Implemente segurança em camadas (firewalls, redes isoladas, criptografia, MFA).
Realize monitoramento e alertas contínuos para detectar desvios e atividades suspeitas.
Mantenha a infraestrutura atualizada com patches e correções.
Promova capacitação e conscientização sobre segurança entre os envolvidos.
Essas práticas ajudam a garantir uma infraestrutura segura, conforme as políticas e regulamentações aplicáveis.
FROM ubuntu:latest

LABEL maintainer="DSA"

# Dependências + APT da HashiCorp + Terraform + Python + AWS CLI deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      gnupg \
      software-properties-common \
      curl \
      unzip \
      python3 \
      python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Adiciona repositório oficial da HashiCorp e instala Terraform
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | \
      gpg --dearmor -o /etc/apt/keyrings/hashicorp-archive-keyring.gpg && \
    chmod a+r /etc/apt/keyrings/hashicorp-archive-keyring.gpg && \
    . /etc/os-release && \
    echo "deb [signed-by=/etc/apt/keyrings/hashicorp-archive-keyring.gpg] \
      https://apt.releases.hashicorp.com ${VERSION_CODENAME} main" | \
      tee /etc/apt/sources.list.d/hashicorp.list > /dev/null && \
    apt-get update && \
    apt-get install -y terraform && \
    rm -rf /var/lib/apt/lists/*

# Diretório de trabalho e arquivo
RUN mkdir -p /lab1-exercicio
WORKDIR /lab1-exercicio
COPY main.tf /lab1-exercicio/

# Instala AWS CLI v2
RUN mkdir -p /tmp/Downloads && \
    cd /tmp/Downloads && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf /tmp/Downloads

CMD ["/bin/bash"]

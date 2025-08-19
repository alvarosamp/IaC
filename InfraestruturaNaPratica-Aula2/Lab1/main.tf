provider "aws" {
  region  = "sa-east-1" #Regiao no qual estou usando na aws (Sao paulo)
}

resource "aws_instance" "tarefa1" { # Criando uma instância EC2
  ami           = "ami-0a0d9cf81c479446a"  # AMI na AWS (numero da imagem da instância dentro d aws)
  instance_type = "t2.micro" #Tipo de instancia(encontramos dentro da aws tambem), temos varias intancias disponiveis. A t2micro é a unica camada gratuita

  tags = {
    Name = "lab1-terraform"
  }
}

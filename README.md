# fastapi-desafio-bemol

## Desenvolvendo e testando a API com FastAPI e Pytest

# Configuração do Projeto

Este documento descreve os passos necessários para configurar e executar o projeto fastapi-desafio-bemol.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha instalado os seguintes pré-requisitos em seu ambiente de desenvolvimento:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://github.com/wswilliams/fastapi-desafio-bemol) (para clonar o repositório)


## Configuração do Ambiente

Siga estas etapas para configurar o ambiente de desenvolvimento:

1. Clone o repositório do projeto (se você ainda não o fez):

2. Navegue até o diretório do projeto:


## Configuração do Docker

Siga estas etapas para configurar e executar os contêineres Docker:

1. Certifique-se de que o Docker e o Docker Compose estejam instalados e em execução.

2. Crie e inicie os contêineres usando o Docker Compose:

```sh
$ docker-compose up -d --build
```

3. Aguarde até que os contêineres estejam em execução. Você pode verificar o status dos contêineres com o seguinte comando:

```sh
$ docker ps
```

## Executando o Projeto

Agora que o ambiente está configurado e os contêineres estão em execução, você pode iniciar o projeto:

1. Inicie o aplicativo Interface Swagger UI:

2. O aplicativo estará acessível em nterface Swagger UI [http://localhost:8003/docs](http://localhost:8003/docs).

## Encerrando o Projeto

Para encerrar a execução do projeto e desligar os contêineres Docker, execute o seguinte comando:
```sh
$ docker stop CONTAINER_ID
```

## Conclusão

O projeto fastapi-desafio-bemol está configurado e pronto para ser executado em seu ambiente de desenvolvimento. Certifique-se de seguir as etapas de configuração e execução conforme descrito acima.



## Notação C4 Model: Vsão arquitetural da infraestrutura

<img src="notacao C4 Model_arquitetura.png">

## Diagrama de Design da Solução, Utilizando a notação C4 Model

<img src="diagrama de Design da Solucao.png">
# Suite CE Monitor Process

> Voltado para servidores do estado do Ceará, este projeto realiza o monitoramento ativo dos processos administrativos internos no Sistema Único Integrado de Tramitação Eletrônica ([SUITE](https://suite.ce.gov.br/consultar-processo/)), notificando os usuários por e-mail sobre novas atualizações em suas tramitações. O projeto otimiza o acompanhamento de processos, garantindo que os servidores estejam sempre informados sobre o andamento de suas solicitações.

## Motivação

> A informação em tempo real é crucial para a eficiência e a transparência dos processos administrativos. No entanto, muitos servidores do estado do Ceará enfrentam a árdua tarefa de acompanhar manualmente as atualizações no SUITE, devido à ausência de um sistema de notificação adequado. Este projeto surge como uma resposta a essa necessidade, buscando fornecer aos servidores informações precisas e oportunas sobre o andamento de seus processos. Ao automatizar o monitoramento e entregar notificações em tempo real, almejamos empoderar os servidores com o conhecimento necessário para tomar decisões informadas e otimizar seu trabalho.

## Instalação

Este projeto é executado dentro de um container Docker. Para iniciar o monitoramento, certifique-se que o docker esteja instalado corretamente e siga as instruções abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/ElizeuS/SuiteCE-Process-Monitor.git](https://github.com/ElizeuS/SuiteCE-Process-Monitor.git)
    cd SuiteCE-Process-Monitor/
    ```

2.  **Crie o arquivo de configuração na raiz do projeto:**

    Crie um arquivo chamado `usuarios.json` no diretório raiz do projeto. Este arquivo mapeará para o sistema as informações principais dos processos e dos interessados pelo monitoramento.

    ```json
    [
        {
            "nome": "Nome Sobrenome",
            "email": "interessado@email.com",
            "processo": "12345678910"
        }
    ]
    ```

    * **Formato JSON**: O arquivo usa o formato JSON.
    * **Estrutura do Array**: O arquivo contém um array (`[]`), o que significa que você pode definir vários usuários e processos para monitoramento.
    * **Objetos de Usuário**: Cada objeto dentro do array representa um usuário e suas configurações de monitoramento.
        * **`nome`**: O nome completo ou parcial do interessado no monitoramento.
        * **`email`**: O endereço de e-mail para onde as notificações serão enviadas.
        * **`processo`**: O número do processo a ser monitorado no SUITE CE.

    **Exemplo Detalhado:**

    ```json
    [
        {
            "nome": "João Evangelista",
            "email": "joao@email.com",
            "processo": "12345678910"
        },
        {
            "nome": "Maria Madalena",
            "email": "maria@email.com",
            "processo": "98765432101"
        }
    ]
    ```

    Neste exemplo:

    * João Evangelista será notificado por e-mail sobre atualizações no processo 12345678910.
    * Maria Madalena será notificada por e-mail sobre atualizações no processo 98765432101.

3.  **Construa e execute os containers usando Docker Compose:**

    ```bash
    docker-compose up -d --build
    ```

    Este comando irá construir a imagem Docker definida no `Dockerfile` e iniciar os containers definidos no `docker-compose.yml` em modo detached (-d).

## Uso

Após a instalação e execução dos containers, o monitoramento será iniciado automaticamente.

* Para verificar os logs do sistema, utilize o comando:

    ```bash
    docker-compose logs
    ```

* Para parar o monitoramento, utilize o comando:

    ```bash
    docker-compose down
    ```

* As notificações de atualização serão enviadas para os endereços de e-mail definidos no arquivo `usuarios.json`.

## Observações

* Certifique-se de que o arquivo `usuarios.json` esteja formatado corretamente. Erros de formatação podem impedir o funcionamento do sistema.
* Para modificar variaveis de ambiente, edite o arquivo docker-compose.yml
* Caso precise persistir dados, certifique-se que os volumes do docker-compose.yml estejam configurados corretamente.

## Pré-requisitos

* Docker e Docker Compose devem estar instalados em seu sistema. Você pode encontrar instruções de instalação nos links abaixo:
    * [Docker Installation](https://docs.docker.com/engine/install/)
    * [Docker Compose Installation](https://docs.docker.com/compose/install/)
# Pipeline de Dados Anac: Processamento de Dados do setor Aéreo ✈️ 🎲


## 🚀 Descrição  do projeto

O objetivo do projeto  foi criar uma Pipeline ETL com dados  brutos extraidos do site no [Portal de Dados Abertos](https://dados.gov.br/home) pela **ANAC (Agência Nacional de Aviação Civil)** no intuito de contabilizar o número de peças de avião em um setor aéreo, para realizar o tratamento foi utilizado o Jupyter Python   e a disponibilidade com o banco de dados PostgreSql, assim como a criação de dashboard com Power Bi para visualização de dados na tomada de decisões na   análise estratégica de voos e aeronaves.

## 🛠️ Ferramentas Utilizadas 

* Linguagem: Python 
* Ambiente de trabalho: Vscode
* Biblioteca: Pandas,SQLAlchemy, Psycopg2
* Banco de Dados: PostgreSQL
* Ferramentas de SQL: DBeaver /pgAdmin
* Ferramentas de Bi : Power Bi

## 📋 Pré-requisitos, Instalação  e Configuração 

### 1. Pré-Requisito:
* Python 3.x
* PostgreSQL
* Visual Studio Code
* Power BI Desktop (para visualizar o arquivo .pbix)

### 2. Instalação:


### 2.1 Instalação do ambiente Virtual:

``` 
01.Criando o Ambiente Virtual:

py -m venv venv

02.Ativando o Ambiente Virtual:

mome_do_ambiente \Scripts\activate
Ex: venv\Scripts\activate

03.Configuração do Ambiente Virtual:

pip install virtualenv  ou pip3 install virtualenv

04.Caso de erro na restrição na ativação do ambiente Virtual abra o powershell e  o execute  como adm:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy 
RemoteSigned

```
### 2.2 Instalação das demais bibliotecas(Pandas/SqlAlchemy/Pyscopg2/Openpyxl/Dotenv)
```
pip install -r requirements.txt
```
### 3. Configuração no banco de dados:

1. Abra o seu PostgreSQL e crie um banco de dados (ex: db_anac).

2. Dentro do projeto na pasta **transact-SQL** copie  os dois arquivos e os leve para o PostgreSQL para  criar as tabelas do proejto.

3. Após isso, no   projeto crie um arquivo chamado **.env** dentro dele você ira preencher todos os seus dados sensíveis no banco de dados para serem protegidos. 

### 3.1 Configuração do banco de dados(PostgresSql) no Visual Studio Code: 

```
01.pyscopg:

DB_NAME=seu_banco
DB_USER=seu_usuario 
DB_PASSWORD=sua_senha 
DB_HOST=localhost
DB_PORT=5432

02.SQLAlchemy:

DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
 ```


## 🏗️ Arquitetura do Projeto
1.  **Extração:** Leitura de arquivos JSON da ANAC.
2.  **Transformação (ETL):** Limpeza, tipagem e manipulação de dados utilizando a biblioteca **Pandas**.
3.  **Carga:** Ingestão automatizada no banco de dados **PostgreSQL** através do **SQLAlchemy**.
4.  **Análise:** Criação de dashboard interativo no **Power BI** conectado diretamente ao banco de dados.

```
Anac-/
├──Arquivo-Json/PecasAprovadas.json
├──Arquivo-Dataframes
├──Scripts/
|Dataframes+ReadingFiles.ipynb
|ETL.py
|Models.py
├──Transact-SQL/
|Enviando dados para o Postgres.sql
|Mapeamento de dados  na tabela.sql
├──venv
├── env  

```



 ##  📊 Visualização do Dashboard

Vislumbre do arquivo feito no power bi para a visualização dos dados da  tabela ANAC

<img width="1910" height="981" alt="Dashbhoard Anac-py" src="https://github.com/user-attachments/assets/31b5b74d-d017-43ca-9ea7-004eee8ec92c" />




## 📜 Referências da Web 

[PostgreSQL datatype](https://www.postgresql.org/docs/current/datatype.html)

[ manual postgreSQL](https://www.postgresql.org/docs/current/dml-insert.html)

[TABLE](https://www.postgresql.org/docs/current/sql-droptable.html)



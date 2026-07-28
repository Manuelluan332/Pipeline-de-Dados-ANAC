
# Pipeline de Dados Anac: Processamento de Dados do setor Aéreo ✈️ 🎲


## 🚀 Descrição  do projeto
Este projeto consiste na construção de uma Pipeline ETL para processamento de dados públicos disponibilizados pela ANAC (Agência Nacional de Aviação Civil). Os dados são extraídos do Portal Brasileiro de Dados Abertos, transformados utilizando Python e Pandas, armazenados em PostgreSQL e posteriormente utilizados na criação de um  dashboard interativo  no Power BI para apoio à análise de informações do setor aeronáutico.


## 🛠️ Ferramentas Utilizadas 

* Linguagem: Python 
* Ambiente de trabalho: Vscode
* Bibliotecas:  Pandas,SQLAlchemy,Psycopg2,Path,loggin
* Banco de Dados: PostgreSQL
* Ferramentas de SQL: PgAdmin/Dbeaver
* Ferramentas de Bi : Power Bi

## 📋 Pré-requisitos, Instalação  e Configuração 

### 1. Pré-Requisito:
* Python 3.4
* PostgreSQL ou DBeaver
* Visual Studio Code
* Power BI Desktop (para visualizar o arquivo .pbix)

### 2. Instalação:

### 2.1 Instalação do ambiente Virtual:

##### Windows:

```
1.Criando o Ambiente Virtual:

py -m venv venv

2.Ativando o Ambiente Virtual:

mome_do_ambiente \Scripts\activate
Ex: venv\Scripts\activate

3.Configuração do Ambiente Virtual:

pip install virtualenv  ou pip3 install virtualenv

4.Caso de erro na restrição na ativação do ambiente Virtual abra o powershell e  o execute  como adm:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy 
RemoteSigned
```
##### Linux:
```
1.Criando o Ambiente Virtual: 
python3 -m venv .venv

2.Ativando o Ambiente Virutal:
source .venv/bin/activate
```
### 2.2 Instalação das demais bibliotecas para o projeto:
```
pip install -r requirements.txt
```


### 3.1 Configuração do banco de dados no Visual Studio Code para inserir seus dados : 

```
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
 ```


## 🏗️ Arquitetura do Projeto
1.  **Extração:** Leitura de arquivos JSON da ANAC.
2.  **Transformação (ETL):** Limpeza, tipagem e manipulação de dados utilizando a biblioteca **Pandas**.
3.  **Carga:** Ingestão automatizada no banco de dados **PostgreSQL** através do **SQLAlchemy**.
4.  **Análise:** Criação de dashboard interativo no **Power BI** conectado diretamente ao banco de dados.

<img width="1491" height="507" alt="Captura de tela de 2026-07-25 14-17-10" src="https://github.com/user-attachments/assets/1ac29482-0647-4a49-96d6-6b126ee3a30d" />


## 📂 Estrutura das Pastas
```
Anac/
│
├── Arquivo-Json/
│   └── PecasAprovadas.json
│
├── Dataframes/
│   ├──Anac.CSV
|   ├──Anac.json
|   └──Anac.parquet
|
├── Scripts/
│   ├── ETL.py
│   └── Data.ipynb
│
├── Transact-SQL/
│   └── Mapeamento_Dados_Tabela_Postgres.sql
│
|
├── requirements.txt
├── README.md
└── .env
  

```



 ##  📊 Visualização do Dashboard

Vislumbre do arquivo feito no power bi para a visualização dos dados da  tabela ANAC

<img width="1910" height="981" alt="Dashbhoard Anac-py" src="https://github.com/user-attachments/assets/31b5b74d-d017-43ca-9ea7-004eee8ec92c" />




## 📜 Referências da Web 

[PostgreSQL datatype](https://www.postgresql.org/docs/current/datatype.html)

[ manual postgreSQL](https://www.postgresql.org/docs/current/dml-insert.html)

[TABLE](https://www.postgresql.org/docs/current/sql-droptable.html)



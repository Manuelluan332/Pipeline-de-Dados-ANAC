<<<<<<< Updated upstream
# Pipeline de Dados Anac: Processamento de Dados do setor Aéreo ✈️ 🎲


## 🚀 Descrição  do projeto
Este projeto consiste na construção de uma Pipeline ETL para processamento de dados públicos disponibilizados pela ANAC (Agência Nacional de Aviação Civil). Os dados são extraídos do Portal Brasileiro de Dados Abertos, transformados utilizando Python e Pandas, armazenados em PostgreSQL e posteriormente utilizados na criação de dashboards interativos no Power BI para apoio à análise de informações do setor aeronáutico.


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
##### Linux
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


=======
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

### 2.1 Instale as dependências  iniciais

``` 
#01.Criando o Ambiente Virtual:

py -m venv sgbds

#02.Ativando o Ambiente Virtual:

mome_do_ambiente \Scripts\activate
Ex: Sgbds\Scripts\activate

#03.Configuração do Ambiente Virtual:

pip install virtualenv  ou pip3 install virtualenv

#04.Caso de erro na restrição na ativação do ambiente Virtual abra o power shell e execute  como adm:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy 
RemoteSigned

```
### 2.2 Instalação das demais bibliotecas(Pandas/SqlAlchemy/Pyscopg2)
```
#01.Biblioteca Pandas:
    pip install pandas

#02.Biblioteca SqlAlchemy:
    pip install SQLAlchemy

#03.Biblioteca Pyscopg2:
   pip install pyscopg2

```
### 3. Configuração:

1. Abra o seu PostgreSQL e crie um banco de dados (ex: db_anac).

2. No ficheiro anac.py, preencha  as credenciais de conexão:
### 3.1 Configuração do banco de dados(PostgresSql) no Visual Studio Code 

```
dbname = 'seu_banco'   
user = 'seu_usuario'        
password = 'sua_senha'       
host = 'localhost'
port = '5432'
 ```


## 🏗️ Arquitetura do Projeto
1.  **Extração:** Leitura de arquivos JSON da ANAC.
2.  **Transformação (ETL):** Limpeza, tipagem e manipulação de dados utilizando a biblioteca **Pandas**.
3.  **Carga:** Ingestão automatizada no banco de dados **PostgreSQL** através do **SQLAlchemy**.
4.  **Análise:** Criação de dashboard interativo no **Power BI** conectado diretamente ao banco de dados.



 ##  📊 Visualização do Dashboard

Vislumbre do arquivo feito no power bi para a visualização dos dados da  tabela ANAC

<img width="1910" height="981" alt="Dashbhoard Anac-py" src="https://github.com/user-attachments/assets/31b5b74d-d017-43ca-9ea7-004eee8ec92c" />

## 📜 Referências da Web 

[PostgreSQL datatype](https://www.postgresql.org/docs/current/datatype.html)

[ manual postgreSQL](https://www.postgresql.org/docs/current/dml-insert.html)

[TABLE](https://www.postgresql.org/docs/current/sql-droptable.html)


>>>>>>> Stashed changes

# Pipeline de Dados Anac: Processamento de Dados do setor Aéreo ✈️ 🎲


## 🚀 Descrição  do projeto

O objetivo do projeto  foi criar uma Pipeline ETL com dados  brutos extraidos do site do Gov pela ANAC (Agência Nacional de Aviação Civil) no intuito de realizar o tratamento via Jupyter Python  e a disponibilidade com o banco de dados PostgreSql, assim como a criação de dashboard com power bi para visualização de dados na tomada de deciões na   análise estratégica de voos e areonaves.

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

  <img width="1913" height="992" alt="ANAC-POWERBI" src="https://github.com/user-attachments/assets/ead273be-39c8-4b15-b65f-9247b917a472" />


## Referências da Web 

[PostgreSQL datatype](https://www.postgresql.org/docs/current/datatype.html)

[ manual postgreSQL](https://www.postgresql.org/docs/current/dml-insert.html)

[TABLE](https://www.postgresql.org/docs/current/sql-droptable.html)



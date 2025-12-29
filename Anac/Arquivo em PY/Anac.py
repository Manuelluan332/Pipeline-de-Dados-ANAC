#
import pandas as pd 
import   psycopg2



#Tratamento de dados:          
caminho_do_arquivo = r"C:\Users\manue\OneDrive\Desktop\Projeto_Anac-SGBDS\Anac\Arquivo Json\PecasAprovadas.json" #Arquivo json  na sua pasta
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')


#Colunas selecionadas:
colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS']
df = df[colunas]      

#Parametro de conexão:
dbname = 'seu_banco'   
user = 'seu_usuario'        
password = 'sua_senha'       
host = 'localhost'
port = '5432'

#Cria uma conexão:
conexao= psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

#Cria uma cursor  para manipular os dados:
cursor = conexao.cursor()
#Delete base antes da Carga:
#cursor.execute("  delete from anac  ")

#Carga dos Dados:
for indice,coluna_df in df.iterrows():
      cursor.execute( """  insert into  ANAC  (
				ORG_NOME,
				PAPP_COD,
				PAPP_NOME,
				PAPP_PN,
			    APAA_CODI,
				APAA_DATA,
				APAA_STATUS
		) VALUES (%s,%s,%s,%s,%s,%s,%s) 

		""", (
				coluna_df["ORG_NOME"],
				coluna_df["PAPP_COD"],
				coluna_df["PAPP_NOME"],
				coluna_df["PAPP_PN"],
				coluna_df["APAA_CODI"],
		    	coluna_df["APAA_DATA"],
				coluna_df["APAA_STATUS"]
		)
		 )
conexao.commit()
cursor.close()
conexao.close()



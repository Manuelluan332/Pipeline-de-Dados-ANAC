CREATE TABLE IF NOT EXISTS Anac_Mapeamento(
	Name_Organizacao varchar(50),
	Cod_Pad int,
	Parametro_name varchar(85),
	PAPP_PN VARCHAR(85),
	APAA_CODI varchar(85), 
	Data_Arpp TIMESTAMP,
	APAA_STATUS VARCHAR(2)
);

select * from Anac_Mapeamento
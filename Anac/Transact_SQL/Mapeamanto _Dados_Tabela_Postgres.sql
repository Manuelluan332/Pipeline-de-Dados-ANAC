CREATE TABLE IF NOT EXISTS anac(
		Organization_Name: VARCHAR(85),
        Product_Code: INTEGER,
        Name_Product: VARCHAR(85),
        Part_Number: VARCHAR(85),
        Approval_Code:VARCHAR(85),
        Approval_Date:DATE,
        Organization_Manufactures_Product: VARCHAR(85)   
	
);


--Teste ao inserir dados no  banco
INSERT INTO anac (

)VALUES('AGS AEROHOSES INDÚSTRIA AERONÁUTICA COMÉRCIO E REPRESENTAÇÕES LTDA',642,'Mangueira - TSO C75',	'-'	,'2006P02-19',	2006-02-06,	'AGS'
	);

SELECT * FROM anac;
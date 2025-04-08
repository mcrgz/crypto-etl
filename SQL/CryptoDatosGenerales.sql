CREATE TABLE Crypto (
IDCrypto int identity(1,1),
Crypto varchar(30),
Symbol varchar(10),
Name varchar(100),
Image varchar(150)
)

ALTER TABLE Crypto
ADD CONSTRAINT PK_Crypto_IDCrypto PRIMARY KEY CLUSTERED (IDCrypto);

ALTER TABLE Crypto
ADD CONSTRAINT UQ_Crypto_Crypto UNIQUE (Crypto);

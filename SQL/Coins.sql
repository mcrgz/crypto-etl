CREATE TABLE Coins (
IDCoin int identity(1,1),
Coin varchar(100),
Symbol varchar(50),
Name varchar(150),

)

ALTER TABLE Coins
ADD CONSTRAINT PK_Coins_IDCoin PRIMARY KEY CLUSTERED (IDCoin);

ALTER TABLE Coins
ADD CONSTRAINT UQ_Coins_Coins UNIQUE (Coin);

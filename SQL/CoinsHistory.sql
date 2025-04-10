CREATE TABLE CoinsHistory
(
IDCoin int,
fecha datetime,
value float,
type varchar(25)
)

ALTER TABLE CoinsHistory WITH CHECK
ADD CONSTRAINT FK_CoinsHistory_IDCoin
FOREIGN KEY(IDCoin)
REFERENCES Coins (IDCoin)

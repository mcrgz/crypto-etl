CREATE TABLE CoinsTrendings
(IDCoin int,
market_cap_rank int,
thumb varchar(95),
price_btc float,
price float,
market_cap float,
market_cap_btc float,
total_volume float,
total_volume_btc float
)

ALTER TABLE CoinsTrendings WITH CHECK
ADD CONSTRAINT FK_CoinsTrendings_IDCoin
FOREIGN KEY(IDCoin)
REFERENCES Coins (IDCoin)

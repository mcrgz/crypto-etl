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

--#################################################################
Create Table CoinsMarkets(
    IDCoin int,
    image varchar(100),
    current_price float,
    market_cap bigint,
    market_cap_rank bigint,
    fully_diluted_valuation bigint,
    total_volume bigint,
    high_24h float,
    low_24h float,
    price_change_24h float,
    price_change_percentage_24h float,
    market_cap_change_24h float,
    market_cap_change_percentage_24h float,
    circulating_supply float,
    total_supply float,
    max_supply float,
    ath float,
    ath_change_percentage float,
    ath_date datetime,
    atl float,
    atl_change_percentage float,
    atl_date datetime,
    last_updated datetime,
    roi_times float,
    roi_currency varchar(3),
    roi_percentage float
)

ALTER TABLE CoinsMarkets WITH CHECK
ADD CONSTRAINT FK_CoinsMarkets_IDCoin
FOREIGN KEY(IDCoin)
REFERENCES Coins (IDCoin)

--#################################################################
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
--#################################################################

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

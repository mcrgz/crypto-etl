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

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
cg.get_price(ids='bitcoin', vs_currencies='usd')
d = {}
def functopn(n):
    a = cg.get_coins_markets('usd')
    for i in range(n):
        b = a[i]['id']
        c = cg.get_price(b, 'usd', include_market_cap=True)
        for k, v in c.items():
            for value in v.items():
                d[k] = value[1]
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k, v in d1:
        print(k, v)
n = int(input())
functopn(n)
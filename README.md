CoinGecko API wrapper
PyPi Version GitHub

Python3 wrapper around the CoinGecko API (V3)

Installation
PyPI

pip install pycoingecko
or from source

git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
Usage
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.
Any optional parameters can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

For any parameter:

Lists are supported as input for multiple-valued comma-separated parameters
(e.g. see /simple/price usage examples).
Booleans are supported as input for boolean type parameters; they can be str ('true', 'false'') or bool (True, False)
(e.g. see /simple/price usage examples).
Usage examples:

# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

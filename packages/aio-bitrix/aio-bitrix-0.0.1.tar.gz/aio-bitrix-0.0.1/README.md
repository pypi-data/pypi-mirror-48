# Simple Django-Mongo-models

# Requirements

* Python (3.6, 3.7)
* aiohttp==3.4.4

# Installation

Install using `pip`...

    pip install aio-bitrix




# Usage

```python
from aio_bitrix import Bitrix
bitrix = Bitrix(access_token='access_token', refresh_token='refresh_token', client_id='', client_secret='')
deals = bitrix.bitrix_call('crm.deal.list') # return paginated deal result

```
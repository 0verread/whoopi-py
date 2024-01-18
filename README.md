# whoopi-py
whoopi's python sdk

## Usage

### Installation
```sh
pip3 install whoopi
```

### Import Lib
```python
from whoopi import Whoopi
```

### Initialize Client
```python

whoopi = Whoopi(ptoken='<whoopi-app-token>')

```

### Start tracking API Events

```python
whoopi.logit(ukey="<unique-value>", method="<API HTTP VERB>", endpoint="<API ENDPOINT>", status="<RESPONSE CODE>")
```

### Explantion

#### ukey

This is unique key value to track API call usage. It could be userId, event name or anything that trigger that API call.


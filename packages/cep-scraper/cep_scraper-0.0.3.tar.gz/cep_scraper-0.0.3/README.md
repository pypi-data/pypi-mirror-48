[![Coverage Status](https://coveralls.io/repos/github/cuenca-mx/cep-scraper/badge.svg?t=6NYZDQ)](https://coveralls.io/github/cuenca-mx/cep-scraper?branch=master)

# cep-scraper

CEP scraper library for consulting transactions in CEP ([COMPROBANTE ELECTRÓNICO DE PAGO](http://www.banxico.org.mx/cep/))

## Requirements
Python 3.7+

## Installation
```bash
pip install cep_scraper
```

## Tests
```bash
make test
```

## Basic usage
Consult a transaction
```python
from cep_scraper import get_tx_info

transaction = dict(
        fecha_proceso='31-03-2019',
        clave_rastreo='CUENCA1554068382',
        institucion_ordenante='90646',
        institucion_beneficiaria='40012',
        cuenta_beneficiario='4152313324202675',
    )
get_tx_info(transaction)
```

## Release to PyPi

```bash
pip install -U setuptools wheel twine
make release
# PyPi will prompt you to log in
```
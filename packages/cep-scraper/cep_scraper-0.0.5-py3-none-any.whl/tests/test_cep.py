import pytest

from cep_scraper import get_transaction


@pytest.mark.vcr
def test_get_transaction_success():
    transaction = dict(
        fecha_proceso='31-03-2019',
        clave_rastreo='CUENCA1554068382',
        institucion_ordenante='90646',
        institucion_beneficiaria='40012',
        cuenta_beneficiario='4152313324202675',
    )
    response = get_transaction(transaction)
    assert response['estado'] == 'Liquidado'


@pytest.mark.vcr
def test_get_transaction_no_exists():
    transaction = dict(
        fecha_proceso='31-03-2019',
        clave_rastreo='TEST',
        institucion_ordenante='90646',
        institucion_beneficiaria='40012',
        cuenta_beneficiario='3746283646344384',
    )
    response = get_transaction(transaction)
    assert response == {}

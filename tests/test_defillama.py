from unittest import TestCase

import pytest


@pytest.mark.usefixtures('llama')
class TestDefiLlama:
    """
    Test class for DefiLlama
    """

    @pytest.mark.skip(reason='TBD')
    def test__send_message(self):
        assert False

    @pytest.mark.skip(reason='TBD')
    def test__get(self):
        assert False

    def test_get_all_protocols(self, llama):
        response = llama.get_all_protocols()
        assert type(response) is list

    # @pytest.mark.skip(reason='TBD')
    def test_get_protocol(self, llama, protocol_json):
        response = llama.get_protocol(name='aave')
        assert type(response) is dict
        for k in protocol_json.keys():
            assert k in response

    # @pytest.mark.skip(reason='TBD')
    def test_get_historical_tvl(self, llama):
        response = llama.get_historical_tvl()
        assert type(response) is list
        for data in response:
            assert 'date' in data
            assert 'tvl' in data
            break

    def test_get_historical_tvl_chain(self, llama):
        response = llama.get_historical_tvl_chain('Ethereum')
        assert type(response) is list
        for data in response:
            assert 'date' in data
            assert 'tvl' in data
            break

    def test_get_protocol_current_tvl(self, llama):
        response = llama.get_protocol_current_tvl('uniswap')
        assert type(response) is float

    def test_get_chains_current_tvl(self, llama):
        response = llama.get_chains_current_tvl()
        assert type(response) is list
        for data in response:
            assert 'gecko_id' in data
            assert 'tvl' in data
            assert 'tokenSymbol' in data
            assert 'cmcId' in data
            assert 'name' in data
            assert 'chainId' in data
            break

    def test_get_pools(self, llama):
        response = llama.get_pools()
        assert type(response) is dict
        assert 'status' in response
        assert 'data' in response

    def test_get_pool(self, llama):
        response = llama.get_pool('747c1d2a-c668-4682-b9f9-296708a3dd90')
        assert type(response) is dict
        assert 'status' in response
        assert 'data' in response

    def test_get_dexs(self, llama):
        response = llama.get_dexs()
        assert type(response) is dict
        assert 'totalDataChart' in response
        assert 'totalDataChartBreakdown' in response
        assert 'protocols' in response

    def test_get_chain_dexs(self, llama):
        response = llama.get_dexs('ethereum')
        assert type(response) is dict
        assert 'totalDataChart' in response
        assert 'totalDataChartBreakdown' in response
        assert 'protocols' in response

    def test_get_dex_summary(self, llama):
        response = llama.get_dex_summary('uniswap')
        assert type(response) is dict
        assert 'id' in response
        assert 'name' in response
        assert 'url' in response
        assert 'totalDataChart' in response

    def test_get_options_dexs(self, llama):
        response = llama.get_options_dexs()
        assert type(response) is dict
        assert 'totalDataChart' in response
        assert 'totalDataChartBreakdown' in response
        assert 'protocols' in response

    def test_get_chain_options_dexs(self, llama):
        response = llama.get_chain_options_dexs('ethereum')
        assert type(response) is dict
        assert 'totalDataChart' in response
        assert 'totalDataChartBreakdown' in response
        assert 'protocols' in response

    def test_get_options_dex_summary(self, llama):
        response = llama.get_options_dex_summary('lyra')
        assert type(response) is dict
        assert 'id' in response
        assert 'name' in response
        assert 'url' in response
        assert 'totalDataChart' in response

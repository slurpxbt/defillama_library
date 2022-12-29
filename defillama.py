import requests


#########################
# TVL
#########################


def get_protocols():
    """
    Function returns list of all defillama protocols and their tvl
    :return :: list[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/protocols"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_protocol_hist_tvl(protocol_slug:str):
    """
    Function returns historical TVL and breakdown by by token and chain

    protocol_slug :: string(protocol slug from defilama)
    :return :: list[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/protocol/{protocol_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_charts():
    """
    Function returns historical TVL of Defi on all chains

    :return :: list[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/charts"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_charts_by_chain(chain:str):
    """
    Function returns historical TVL of Defi on all chains

    chain :: string (chain name from defilama)
    :return :: list[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/charts/{chain}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_protocol_tvl(protocol:str):
    """
    Function returns current protocol tvl

    chain :: string (chain name from defilama)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/tvl/{protocol}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_chains_tvl():
    """
    Function returns current tvl of every chain

    chain :: string (chain name from defilama)
    :return :: list[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/chains"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


#########################
# COINS
#########################

def get_current_price_of_tokens_by_contract(coins:str):
    """
    Function returns price of token from contract address

    coins :: strin (set of comma-separated tokens defined as {chain}:{address})
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/prices/current/{coins}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_historical_token_price_by_contract(coins:str, timestamp:int):
    """
    Function returns price of token from contract address at specific timestamp

    coins :: strin (set of comma-separated tokens defined as {chain}:{address})
    timestamp :: int (unix timestamp of the time you want price)
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/prices/historical/{timestamp}/{coins}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_coin_chart(coins:str):
    """
    Function returns token price at regular intervals

    coins :: strin (set of comma-separated tokens defined as {chain}:{address})
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/chart/{coins}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_pct_change(coins:str):
    """
    Function returns percentage change in price over time

    coins :: strin (set of comma-separated tokens defined as {chain}:{address})
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/percentage/{coins}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_first_recorded_price(coins:str):
    """
    Function returns earliest price record

    coins :: strin (set of comma-separated tokens defined as {chain}:{address})
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/prices/first/{coins}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_block(chain:str, timestamp:int):
    """
    Function returns earliest block to the timestamp

    chain :: string (chain name from defilama)
    timestamp :: int (unix timestamp of the time you want price)
    :return :: dict[success]/string[fail]
    """
    url = "https://coins.llama.fi"
    endpoint = f"{url}/block/{chain}/{timestamp}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg

# EXAMPLES

# block = get_block("ethereum", 1603964988)
# first_price = get_first_recorded_price("ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1")
# pct_change = get_pct_change("ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1")
# coin_chart = get_coin_chart("ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1")
# historical_token_price = get_historical_token_price_by_contract("ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1", 1648680149)
# current_token_price = get_current_price_of_tokens_by_contract("ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1")

# tvl = get_charts()
# print(tvl)

# data = get_protocols()
# print(data)

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

    :protocol :: string (protocol slug)
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

    coins :: string (set of comma-separated tokens defined as {chain}:{address})
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

#########################
# STABLECOINS
#########################


def get_stables_circulating_amounts():
    """
    Function returns list of all stablecoins and their circulating amounts
    :return :: dict[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoins"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_stablecoin_chart():
    """
    Function returns historical mcap of all stablecoins
    :return :: list[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoincharts/all"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_chain_stablecoin_chart(chain:str):
    """
    Function returns historical mcap of all stablecoins on specific chain
    :chain :: int(chain slug)
    :return :: list[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoincharts/{chain}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_stablecoin_hist(stablecoin_id:int):
    """
    Function returns historical mcap and historical chain distribution of a stablecoin
    :stablecoin_id :: int(you can get those from get_stables_circulating_amounts())
    :return :: dict[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoin/{stablecoin_id}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_stablecoinchains():
    """
    Function returns mcap of all stables on each chains
    :return :: list[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoinchains"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_stablecoinprices():
    """
    Function returns historical prices of all stablecoins
    :return :: list[success]/string[fail]
    """
    url = "https://stablecoins.llama.fi"
    endpoint = f"{url}/stablecoinprices"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


#########################
# YIELDS
#########################

def get_pools():
    """
    Function returns latest data for all pools and all enriched information
    :return :: dict[success]/string[fail]
    """
    url = "https://yields.llama.fi"
    endpoint = f"{url}/pools"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_pool_historical_apy(pool_id:str):
    """
    Function returns latest data for all pools and all enriched information
    :pool_id :: string (pool id can be retrieved from get_pools() pool field in returned dict)
    :return :: dict[success]/string[fail]
    """
    url = "https://yields.llama.fi"
    endpoint = f"{url}/chart/{pool_id}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


#########################
# BRIDGES
#########################


def get_bridges():
    """
    Function returns all bridges and their latest volume data
    :return :: dict[success]/string[fail]
    """
    url = "https://bridges.llama.fi"
    endpoint = f"{url}/bridges"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_bridge_summary(bridge_id:int):
    """
    Function returns all bridges and their latest volume data
    :bridge_id :: int (you can get bridge ids from get_bridges())
    :return :: dict[success]/string[fail]
    """
    url = "https://bridges.llama.fi"
    endpoint = f"{url}/bridge/{bridge_id}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_bridge_volume_on_chain(chain_slug:str, bridge_id:int):
    """
    Function returns historical volumes for a bridge, chain, or bridge on a particular chain
    :chain :: int(chain slug)
    :bridge_id :: int (you can get bridge ids from get_bridges())
    :return :: dict[success]/string[fail]
    """
    url = "https://bridges.llama.fi"
    endpoint = f"{url}/bridgevolume/{chain_slug}?id={bridge_id}"
    resp = requests.get(endpoint,)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_bridgedaystats(timestamp:int, chaind_slug:str,bridge_id:int):
    """
    Function returns 24h token and volume breakdown for a bridge
    :chaind_slug :: int (unix timestamp)
    :timestamp ::
    :return :: dict[success]/string[fail]
    """
    url = "https://bridges.llama.fi"
    endpoint = f"{url}/bridgedaystats/{timestamp}/{chaind_slug}?id={bridge_id}"
    resp = requests.get(endpoint, )

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


#########################
# VOLUMES
#########################


def get_dexs_volume_overview():
    """
    Function returns list of all dexes and their volumes
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/dexs"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_dexs_volume_overview_on_chain(chain_slug:str):
    """
    Function returns list of all dexes and their volumes on a chain
    :chaind_slug :: int (unix timestamp)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/dexs/{chain_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_dex_volume(protocol_slug:str):
    """
    Function returns summary of dex historical volumes
    :protocol :: string (protocol slug)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/summary/dexs/{protocol_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def options_dexes_overview(chain_slug:str):
    """
    Function returns list of options dexes and overview of their volumes
    :chaind_slug :: int (unix timestamp)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/options/{chain_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_options_dex_volume(protocol_slug:str):
    """
    Function returns summary of dex historical volumes
    :protocol :: string (protocol slug)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/summary/options/{protocol_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


#########################
# FEES AND REVENUE
#########################

def get_fee_overview():
    """
    Function returns list of all protocols with summary of their fees and revenue
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/fees"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_fee_overview_by_chain(chain_slug:str):
    """
    Function returns list of all protocols with summary of their fees and revenue by chain
    :chaind_slug :: int (unix timestamp)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/fees/{chain_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg


def get_fee_overview_by_protocol(protocol_slug:str):
    """
    Function returns list of all protocols with summary of their fees and revenue by chain
    :protocol_slug :: string (protocol slug)
    :return :: dict[success]/string[fail]
    """
    url = "https://api.llama.fi"
    endpoint = f"{url}/overview/fees/{protocol_slug}"
    resp = requests.get(endpoint)

    if resp.status_code == 200:
        return resp.json()
    else:
        msg = f"failed api call on endpoint: {endpoint}"
        return msg



# EXAMPLES
# pools = get_pools()
# print(pools)
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

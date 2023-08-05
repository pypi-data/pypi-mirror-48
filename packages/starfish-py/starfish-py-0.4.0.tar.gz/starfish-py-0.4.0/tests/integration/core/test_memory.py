"""
    Test ocean class

"""

import pathlib
import json
import logging
import time
import secrets
from web3 import Web3

from starfish import Ocean
from starfish.agent import MemoryAgent
from starfish.asset import MemoryAsset



def _register_asset_for_sale(agent, metadata, account):

    asset = MemoryAsset(metadata=metadata, data=secrets.token_hex(256))
    listing = agent.register_asset(asset, account=account)
    assert listing
    assert listing.asset.did
    return listing

def test_asset(ocean, metadata, config):

    # create an ocean object

    agent = MemoryAgent(ocean, metadata)
    assert agent


    # test node has the account #0 unlocked
    publisher_account = ocean.get_account(config.publisher_account)

    listing = _register_asset_for_sale(agent, metadata, publisher_account)
    assert listing
    assert publisher_account

    listing_id = listing.listing_id
    # start to test getting the asset from storage
    listing = agent.get_listing(listing_id)
    assert listing
    assert listing.listing_id == listing_id


    purchase_account = ocean.get_account(config.purchaser_account)

    # test purchase an asset
    purchase_asset = listing.purchase(purchase_account)
    assert purchase_asset


    assert purchase_asset.is_purchased
    assert(purchase_asset.wait_for_completion(purchase_account))
    assert(purchase_asset.is_completed(purchase_account))
    assert purchase_asset.is_purchase_valid(purchase_account)

    purchase_asset.consume(purchase_account, '')



def test_search_listing(ocean, metadata, config):

    agent = MemoryAgent(ocean)

    # test node has the account #0 unlocked
    publisher_account = ocean.get_account(config.publisher_account)

    agent = MemoryAgent(ocean)

    listing = _register_asset_for_sale(agent, metadata, publisher_account)
    assert listing
    assert publisher_account

    # choose a word from the description field
    text = metadata['base']['description']
    words = text.split(' ')
    word = words[0]

    # should return at least 1 or more assets
    logging.info(f'search word is {word}')
    searchResult = agent.search_listings(word)
    assert searchResult

    assert(len(searchResult) > 0)

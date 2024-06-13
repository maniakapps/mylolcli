"""
Module for interacting with the Riot API to retrieve summoner information.

This module provides functions to retrieve summoner information by various identifiers,
such as summoner name, account ID, PUUID, and summoner ID. The functions use the Riot API
to make HTTP requests and handle any errors that may occur during the requests.

Functions:
- get_summoner_by_name(summoner_name): Retrieves summoner information by summoner name.
- get_summoner_by_account_id(account_id): Retrieves summoner information by account ID.
- get_summoner_by_puuid(puuid): Retrieves summoner information by PUUID.
- get_summoner_by_summoner_id(summoner_id): Retrieves summoner information by summoner ID.

Each function returns a dictionary containing the summoner's information.
"""
import requests
from requests.exceptions import HTTPError
from api_wrapper.config import RIOT_API_KEY

headers = {"X-Riot-Token": RIOT_API_KEY}


def get_summoner_by_name(summoner_name: str) -> dict:
    """
    Retrieves summoner information by summoner name using the Riot API.

    Parameters:
    summoner_name (str): The name of the summoner.

    Returns:
    dict: A dictionary containing the summoner's information.

    Raises:
    HTTPError: If the request to the Riot API fails.

    Example:
    >>> get_summoner_by_name('SummonerName')
    {
        "id": "91KHQCxVeVKhElhpkp_S4cNBb3CF2Dg6UVbv5UtyEKgTuw",
        "accountId": "b7gImwtBlJuU0zuSNvZ6Ia2hOJ1MmnI0iLq_eMY9mcZlhaE",
        "puuid": "hi7994wx5vIA-qdfTz6J_KVxQoZ1lcc9wS4aBuqETIkut5NtcNVlYu9zJf4lqZjaikZCxMulFqgyTw",
        "profileIconId": 5896,
        "revisionDate": 1717831613370,
        "summonerLevel": 673
    }
    """
    url = f"{BASE_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise


def get_summoner_by_account_id(account_id: str) -> dict:
    """
    Retrieves summoner information by account ID using the Riot API.

    Parameters:
    account_id (str): The account ID of the summoner.

    Returns:
    dict: A dictionary containing the summoner's information.

    Raises:
    HTTPError: If the request to the Riot API fails.

    Example:
    >>> get_summoner_by_account_id('b7gImwtBlJuU0zuSNvZ6Ia2hOJ1MmnI0iLq_eMY9mcZlhaE')
    {
        "id": "91KHQCxVeVKhElhpkp_S4cNBb3CF2Dg6UVbv5UtyEKgTuw",
        "accountId": "b7gImwtBlJuU0zuSNvZ6Ia2hOJ1MmnI0iLq_eMY9mcZlhaE",
        "puuid": "hi7994wx5vIA-qdfTz6J_KVxQoZ1lcc9wS4aBuqETIkut5NtcNVlYu9zJf4lqZjaikZCxMulFqgyTw",
        "profileIconId": 5896,
        "revisionDate": 1717831613370,
        "summonerLevel": 673
    }
    """
    url = f"{BASE_URL}/lol/summoner/v4/summoners/by-account/{account_id}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise


def get_summoner_by_puuid(puuid: str) -> dict:
    """
    Retrieves summoner information by PUUID (Player Universe Unique Identifier) using the Riot API.

    Parameters:
    puuid (str): The PUUID of the summoner.

    Returns:
    dict: A dictionary containing the summoner's information.

    Raises:
    HTTPError: If the request to the Riot API fails.

    Example:
    >>> get_summoner_by_puuid('hi7994wx5vIA-qdfTz6J_KVxQoZ1lcc9wS4aBuqETIkut5NtcNVlYu9zJf4lqZjaikZCxMulFqgyTw')
    {
        "id": "91KHQCxVeVKhElhpkp_S4cNBb3CF2Dg6UVbv5UtyEKgTuw",
        "accountId": "b7gImwtBlJuU0zuSNvZ6Ia2hOJ1MmnI0iLq_eMY9mcZlhaE",
        "puuid": "hi7994wx5vIA-qdfTz6J_KVxQoZ1lcc9wS4aBuqETIkut5NtcNVlYu9zJf4lqZjaikZCxMulFqgyTw",
        "profileIconId": 5896,
        "revisionDate": 1717831613370,
        "summonerLevel": 673
    }
    """
    url = f"{BASE_URL}/lol/summoner/v4/summoners/by-puuid/{puuid}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise


def get_summoner_by_summoner_id(summoner_id: str) -> dict:
    """
    Retrieves summoner information by summoner ID using the Riot API.

    Parameters:
    summoner_id (str): The summoner ID of the summoner.

    Returns:
    dict: A dictionary containing the summoner's information.

    Raises:
    HTTPError: If the request to the Riot API fails.

    Example:
    >>> get_summoner_by_summoner_id('91KHQCxVeVKhElhpkp_S4cNBb3CF2Dg6UVbv5UtyEKgTuw')
    {
        "id": "91KHQCxVeVKhElhpkp_S4cNBb3CF2Dg6UVbv5UtyEKgTuw",
        "accountId": "b7gImwtBlJuU0zuSNvZ6Ia2hOJ1MmnI0iLq_eMY9mcZlhaE",
        "puuid": "hi7994wx5vIA-qdfTz6J_KVxQoZ1lcc9wS4aBuqETIkut5NtcNVlYu9zJf4lqZjaikZCxMulFqgyTw",
        "profileIconId": 5896,
        "revisionDate": 1717831613370,
        "summonerLevel": 673
    }
    """
    url = f"{BASE_URL}/lol/summoner/v4/summoners/{summoner_id}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise

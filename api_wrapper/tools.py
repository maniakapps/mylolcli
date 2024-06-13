import click
import requests
from cli import headers


def get_puuid_by_summoner_name_and_tagline(summoner_name: str, tag_line: str) -> str:
    """
    This function retrieves the Player Unified Unique Identifier (PUUID) of a League of Legends summoner
    using their summoner name and tagline.

    Parameters:
    summoner_name (str): The name of the League of Legends summoner.
    tag_line (str): The tagline of the League of Legends summoner.

    Returns:
    str: The PUUID of the League of Legends summoner.

    Raises:
    requests.exceptions.HTTPError: If the request to the Riot Games API fails.

    Note:
    This function assumes that the 'equests' and 'headers' modules are already imported.
    The 'headers' module should contain the necessary headers for making requests to the Riot Games API.
    """

    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    summoner_info = response.json()
    puuid = summoner_info["puuid"]
    return puuid


def info(summoner_info: dict) -> None:
    click.echo(f"Summoner's name: {summoner_info['name']}")
    click.echo(f"Summoner's level: {summoner_info['summonerLevel']}")
    click.echo(f"Summoner's ID: {summoner_info['id']}")


if __name__ == "__main__":
    summoner_name_ = input("Enter summoner name: ")
    tag_line_ = input("ENTER TAG LINE: ")
    puuid_ = get_puuid_by_summoner_name_and_tagline(summoner_name_, tag_line_)
    print(f"The puuid of {summoner_name_} is: {puuid_}")

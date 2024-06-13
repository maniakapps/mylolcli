import click
import requests
from api_wrapper.cli import (
    get_summoner_by_name,
    get_summoner_by_account_id,
    get_summoner_by_puuid,
    get_summoner_by_summoner_id,
)
from api_wrapper.tools import info


@click.group()
def cli():
    """CLI to obtain summoner's information using the Riot API."""
    pass


@cli.command()
@click.argument("summoner_name")
def summoner_name(summoner_name):
    """
    This function retrieves summoner information by their name.

    Parameters:
    summoner_name (str): The name of the summoner to search for.

    Returns:
    None. Prints the summoner's name, level, and ID to the console.

    Raises:
    requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
    Exception: If any other error occurs during the API request.
    """
    try:
        summoner_info = get_summoner_by_name(summoner_name)
        info(summoner_info)
    except requests.exceptions.HTTPError as e:
        click.echo(f"HTTP error: {e}")
    except Exception as e:
        click.echo(f"An error has occurred: {e}")


@cli.command()
@click.argument("account_id")
def account_id(account_id):
    """
    Retrieves summoner information by their account ID.

    Parameters:
    account_id (str): The account ID of the summoner to search for.

    Returns:
    None. Prints the summoner's name, level, and ID to the console.

    Raises:
    requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
    Exception: If any other error occurs during the API request.
    """
    try:
        summoner_info = get_summoner_by_account_id(account_id)
        info(summoner_info)
    except requests.exceptions.HTTPError as e:
        click.echo(f"HTTP error: {e}")
    except Exception as e:
        click.echo(f"An error has occurred: {e}")


@cli.command()
@click.argument("puuid")
def puuid(puuid):
    """
    Retrieves summoner information by their PUUID (Player Universe Unique Identifier).

    Parameters:
    puuid (str): The PUUID of the summoner to search for.

    Returns:
    None. Prints the summoner's name, level, and ID to the console.

    Raises:
    requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
    Exception: If any other error occurs during the API request.
    """
    try:
        summoner_info = get_summoner_by_puuid(puuid)
        info(summoner_info)
    except requests.exceptions.HTTPError as e:
        click.echo(f"HTTP error: {e}")
    except Exception as e:
        click.echo(f"An error has occurred: {e}")


@cli.command()
@click.argument("summoner_id")
def summoner_id(summoner_id):
    """
    Retrieves summoner information by their summoner ID.

    Parameters:
    summoner_id (str): The summoner ID of the summoner to search for.

    Returns:
    None. Prints the summoner's name, level, and ID to the console.

    Raises:
    requests.exceptions.HTTPError: If an HTTP error occurs during the API request.
    Exception: If any other error occurs during the API request.
    """
    try:
        summoner_info = get_summoner_by_summoner_id(summoner_id)
        info(summoner_info)
    except requests.exceptions.HTTPError as e:
        click.echo(f"HTTP error: {e}")
    except Exception as e:
        click.echo(f"An error has occurred: {e}")


if __name__ == "__main__":
    cli()

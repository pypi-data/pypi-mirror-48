#!/usr/bin/env python3

import os
import sys
import click

from pathlib import Path
from envault.utils import config, yaml
from envault import vault, shell, aws, __version__


def get_vault_secrets(server, secret, token, profile=None):
    """ Renew token and fetch secrets from Vault Server """
    profile_configs = {
        "vault_token": None,
        "vault_server": None,
        "vault_secret_path": None,
    }
    if profile:
        profile_configs = config.get_profile_configs(profile)

    token = token or profile_configs.get("vault_token") or os.environ.get("VAULT_TOKEN")
    server = (
        server or profile_configs.get("vault_server") or os.environ.get("VAULT_SERVER")
    )
    secret = (
        secret
        or profile_configs.get("vault_secret_path")
        or os.environ.get("VAULT_SECRETS_PATH")
    )

    if not server:
        raise SystemExit(
            "Error: Vault Server URI is not present. Add '-server' flag or VAULT_SERVER variable in your environment"
        )

    if not token:
        raise SystemExit(
            "Error: Vault Token is not present. Add '-token' flag or VAULT_TOKEN variable in your environment"
        )

    vault.renew_token(server, token)

    return vault.get_secrets(server, secret, token)


def get_aws_secrets(secret, region, accessid, secretkey):
    """ Get AWS secrets using environment variables """
    secret_name = secret or os.environ.get("SECRET_NAME")
    region_name = region or os.environ.get("REGION_NAME")
    aws_access_key_id = accessid or os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = secretkey or os.environ.get("AWS_SECRET_ACCESS_KEY")

    if not secret_name:
        raise SystemExit("Error: Secret Name is not present")

    if not region_name:
        raise SystemExit("Error: Region Name is not present")

    if not aws_access_key_id:
        raise SystemExit("Error: AWS Access Key ID is not present")

    if not aws_secret_access_key:
        raise SystemExit("Error: AWS Secret Access Key is not present")

    return aws.get_secrets(
        aws_access_key_id, aws_secret_access_key, secret_name, region_name
    )


@click.group()
@click.version_option(message=__version__)
def cli():
    pass


@cli.command("init")
def init():
    """ Initialize envault config for vault secret manager"""
    click.echo("Enter the profile name, server, token and path to vault secrets")
    profile_name = click.prompt("Profile Name", type=str)
    vault_server = click.prompt("Vault Server", type=str)
    vault_token = click.prompt("Vault Token", type=str)
    vault_secret_path = click.prompt("Path to vault secret", type=str)

    config_file = config.create_config_file(
        vault_server, vault_token, vault_secret_path, profile_name
    )

    yaml.dump_data_to_yml(config_file)

    click.echo(
        """
        Following information is saved.
        name: {name}
        vault_server: {server}
        vault_token: {token}
        vault_secret_path: {secret_path}
        """.format(
            name=profile_name,
            server=vault_server,
            token=vault_token,
            secret_path=vault_secret_path,
        )
    )


@cli.command("list")
@click.option("-server", help="Server URI")
@click.option("-secret", help="Path to the secrets")
@click.option("-token", help="Vault token")
@click.option("-profile", help="Profile name stored in yml file")
@click.option("-region", help="AWS Secret manager region name")
@click.option("-accessid", help="AWS Access Key ID")
@click.option("-secretkey", help="AWS Secret Access Key")
@click.option("-engine", help="Secret Manager", default="asm")
def list(server, secret, token, profile, region, accessid, secretkey, engine):
    """ List secrets from a given path """
    secrets = {}
    engine = engine or os.environ.get("ENGINE")
    
    if engine == "asm":
        secrets = get_aws_secrets(secret, region, accessid, secretkey)
    if engine == "vault":
        secrets = get_vault_secrets(server, secret, token,profile)

    for key, value in secrets.items():
        click.echo("{}={}".format(key, value))


@cli.command("run")
@click.option("-server", help="Server URI")
@click.option("-secret", help="Path to the Vault secrets or AWS Secret Manager secret name")
@click.option("-token", help="Vault token")
@click.option("-region", help="AWS Secret manager region name")
@click.option("-accessid", help="AWS Access Key ID")
@click.option("-secretkey", help="AWS Secret Access Key")
@click.option("-engine", help="Secret Manager", default="asm")
@click.argument("command")
def run(server, secret, token, region, accessid, secretkey, engine, command):
    """ Run a command with the injected env variables """
    if engine == "asm":
        secrets = get_aws_secrets(secret, region, accessid, secretkey)
    if engine == "vault":
        secrets = get_vault_secrets(server, secret, token)

    sys.exit(shell.run_with_env(command, secrets))


if __name__ == "__main__":
    cli()
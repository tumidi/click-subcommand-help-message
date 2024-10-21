#!/usr/bin/env python3
import click


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    pass


@click.command()
@click.argument("required_arg")
@click.option("--host", "-h", "host", default="localhost")
def foo(required_arg, host):
    click.echo(f"Foo command required_arg={required_arg} host={host}")


cli.add_command(foo)

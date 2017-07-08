import click

import repl as aquarepl

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
	"""
	`aquactl` is a tool to connect to a running aqua instance and manually run modules or manage jobs.

	It is additionally used to configure and administrate running instances.
	"""

@cli.command()
def repl():
	"""Starts a REPL which can be used to interact with a running aqua instance."""

	aquarepl.run()

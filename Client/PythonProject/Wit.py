import os
import click
from Repository import Repository
from Modul import create_a_new_folder

repository = Repository()


@click.group()
def cli():
    pass


@click.command()
def init():
    if not os.path.exists(os.path.join(os.getcwd(), '.wit')):
        create_a_new_folder(os.getcwd(), '.wit')
        print(".wit folder initialized.")
    else:
        print(".wit folder already exists.")


@click.command()
@click.argument('path')
def add(path):
    repository.add(path)


@click.command()
@click.argument('message')
def commit(message):
    repository.commit(message)


@click.command()
def log():
    repository.log()


@click.command()
def status():
    repository.status()


@click.command()
@click.argument('commit_id')
def checkout(commit_id):
    repository.checkout(commit_id)


@click.command()
def push():
    repository.push()


cli.add_command(init)
cli.add_command(add)
cli.add_command(commit)
cli.add_command(log)
cli.add_command(status)
cli.add_command(checkout)
cli.add_command(push)

if __name__ == '__main__':
    cli()

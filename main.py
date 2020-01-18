import click
from converter.converter import NoSqlConverter


@click.group(chain=True)
def cli():
    pass


@click.command('convert_data', help='Convert data from SQL to No-SQL.')
def task_convert_data():
    NoSqlConverter().start()


if __name__ == '__main__':
    cli.add_command(task_convert_data)
    cli()

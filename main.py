import time

import click
import schedule

from converter.converter import NoSqlConverter
from util.util import Util


@click.group(chain=True)
def cli():
    pass


@click.command('convert_data', help='Convert data from SQL to No-SQL.')
@click.option('--period', '-p',
              type=int,
              default=24,
              show_default=True,
              help='Analysis period in hour')
def task_convert_data(period):
    click.echo('do nosql converter')
    Util().load_environment_variable()
    schedule.every(period).hours.do(NoSqlConverter().start)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    cli.add_command(task_convert_data)
    cli()

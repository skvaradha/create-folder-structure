from datetime import datetime
import site
import os

import click

from common.utils import get_project_root
from tasks.create_directories_task import CreateDirectory


@click.command()
@click.option('--start_date', required=True, default=None)
@click.option('--end_date', required=True, default=None)
@click.option('--root_path', required=True, default=get_project_root())
@click.option('--keep_file', required=False, default=False)
def create_directories(start_date, end_date, root_path, keep_file):
    """
    enable cli to create directories based on date range
    start_date: start date in text format
    end_date: end date in text format
    root_path: root directory path in text to create the new directories structure
    keep_file: boolean to specify to create keep_file or not
    """
    start_date_format = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_format = datetime.strptime(end_date, '%Y-%m-%d')

    create_directory = CreateDirectory(start_date=start_date_format, end_date=end_date_format, root_path=root_path,
                                       keep_file=keep_file)
    create_directory.execute()


if __name__ == '__main__':
    create_directories()

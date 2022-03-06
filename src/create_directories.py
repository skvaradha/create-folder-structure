from datetime import datetime
from common.utils import raise_error_message

import click

from common.utils import get_project_root
from tasks.create_directories_task import CreateDirectory


@click.command()
@click.option('--start_date', required=True, default=None, help="date format yyyy-mm-dd")
@click.option('--end_date', required=True, default=None, help="date format yyyy-mm-dd")
@click.option('--root_path', required=False, default=get_project_root(), help="If not path specified root of this "
                                                                              "project will be used")
@click.option('--keep_file', required=False, default=False, help="True or False")
@click.option('--clear_old_content', required=False, default=False, help="True or False")
def create_directories(start_date, end_date, root_path, keep_file, clear_old_content):
    """
    Enable cli to create directories based on date range
    start_date: date - YYYY-mm-dd
            start date in text format
    end_date: date - YYYY-mm-dd
            end date in text format - YYYY-mm-dd
    root_path: string
            root directory path in text to create the new directories structure,
            if no path is specified default would be the parent location where this project runs
    keep_file: boolean
            to specify to create keep_file or not
    clear_old_content: boolean
            to specify whether to clear date folders which are not in the mentioned date range
    """
    try:
        start_date_format = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_format = datetime.strptime(end_date, '%Y-%m-%d')
    except (ValueError, TypeError):
        raise_error_message("Check start/end date format, it should be yyyy-mm-dd and valid date")

    if start_date_format > end_date_format:
        raise_error_message("End date should be greater than start date")

    create_directory = CreateDirectory(start_date=start_date_format, end_date=end_date_format, root_path=root_path,
                                       keep_file=keep_file, clear_old_content=clear_old_content)
    create_directory.execute()


if __name__ == '__main__':
    create_directories()

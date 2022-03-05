from pathlib import Path
from datetime import timedelta
import os
import shutil


def get_project_root() -> Path:
    """ get the root of the current executing project
    """
    return Path(__file__).parent.parent.parent.parent


def next_date(date, period):
    """Increase the date by timedelta
        date: datetime object
        period: timedelta to increase our date by
    """
    new_date = date + timedelta(days=period)
    return '/'.join(('year=' + str(new_date.year), 'month=' + str(new_date.month), 'day=' + str(new_date.day)))


def delete_contents(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
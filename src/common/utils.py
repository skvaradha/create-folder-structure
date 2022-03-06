from pathlib import Path
from datetime import timedelta
import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
MAKE_FILE = '.make'


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
    return os.path.join('year=' + str(new_date.year), 'month=' + str(new_date.month), 'day=' + str(new_date.day))


def delete_contents(folder):
    """ cleanup specified folder
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def log_info_message(directory_path, directory_created=False, directory_already_exists=False, make_file_created=False,
                     make_file_already_exists=False):
    """ Log info messages as per input parameters
        directory_path:  required, string
        directory_created: boolean default False
        directory_already_exists: boolean default False
        make_file_created: boolean default False
        make_file_already_exists: boolean default False
    """

    if not directory_path:
        raise Exception("Please provide valid directory_path --> {}".format(directory_path))

    if directory_created:
        logging.info('Directory --> {} created'.format(directory_path))

    if directory_already_exists:
        logging.info('Directory --> {} already exists'.format(directory_path))

    if make_file_created:
        logging.info('.make file --> {} file created'.format(os.path.join(directory_path, MAKE_FILE)))

    if make_file_already_exists:
        logging.info('.make file --> {} already exists'.format(os.path.join(directory_path, MAKE_FILE)))


def raise_error_message(error, error_type=None, custom_message=None):
    """ Log error messages as per input parameters
            error:  Exception type, required -> error passed from calling code
            error_type: string -> type of error
            custom_message: string
        """
    if error_type:
        logging.info("Error Type: {}".format(error_type))

    if custom_message:
        logging.info(custom_message)

    logging.error(error)
    raise Exception(error)


def clear_old_contents(root_path, all_paths):
    """ clear old contents
        root_path: string, required
        all_paths: list, required
    """
    for root, dirs, files in os.walk(root_path, topdown=False):
        path = os.path.normpath(root)
        split_path = path.split(os.sep)
        # if .make is the only file in the day=xx folder then delete the folder
        if len(split_path) >= 3:
            if split_path[-1].startswith("day=") and split_path[-2].startswith("month=") and \
                    split_path[-3].startswith("year="):
                if os.path.join(split_path[-3], split_path[-2], split_path[-1]) not in all_paths:
                    if (len(files) == 1 and files[0] == '.make') or len(files) == 0:
                        shutil.rmtree(root)

        # after deleting the day=xx folder and month=xx exists without a day then delete it
        if len(split_path) >= 2:
            if split_path[-1].startswith("month=") and split_path[-2].startswith("year="):
                if len(os.listdir(root)) == 0:
                    shutil.rmtree(root)

        # after deleting the month=xx folder and year=xxx exists without a month then delete it
        if len(split_path) >= 1:
            if split_path[-1].startswith("year="):
                if len(os.listdir(root)) == 0:
                    shutil.rmtree(root)


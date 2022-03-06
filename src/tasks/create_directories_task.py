import shutil
from datetime import datetime
from common.utils import next_date, log_info_message, raise_error_message, clear_old_contents
import os
import logging

MAKE_FILE = '.make'
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


class CreateDirectory:
    """create directory for the specified date range
        start_date: start datetime object
        end_date: end datetime object
        root_path: string path where the directories to be created
        keep_file: boolean to specify to create keep_file or not
    """
    def __init__(self, start_date: datetime, end_date: datetime, root_path: str, keep_file: bool = False,
                 clear_old_content=False):
        self.start_date = start_date
        self.end_date = end_date
        self.root_path = root_path
        self.keep_file = keep_file
        self.clear_old_content = clear_old_content

    def execute(self):
        try:
            delta = self.end_date - self.start_date
            all_paths = []

            for day_increment in range(delta.days + 1):
                date_structure = next_date(self.start_date, day_increment)

                dir_path = os.path.join(self.root_path, date_structure)
                all_paths.append(date_structure)

                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                    log_info_message(dir_path, directory_created=True)

                    if self.keep_file:
                        with open(os.path.join(dir_path, MAKE_FILE), 'w') as fp:
                            pass
                        log_info_message(dir_path, make_file_created=True)
                elif os.path.exists(dir_path) and self.keep_file and not os.path.exists(os.path.join(dir_path, MAKE_FILE)):
                    with open(os.path.join(dir_path, MAKE_FILE), 'w') as fp:
                        pass
                    log_info_message(dir_path, directory_already_exists=True, make_file_created=True)
                elif os.path.exists(dir_path) and self.keep_file and os.path.exists(os.path.join(dir_path, MAKE_FILE)):
                    log_info_message(dir_path, directory_already_exists=True, make_file_already_exists=True)
                else:
                    log_info_message(dir_path, directory_already_exists=True)

            if self.clear_old_content:
                clear_old_contents(self.root_path, all_paths)

        except IOError as error:
            raise_error_message(error, custom_message="There was an error creating/deleting File or Folder")
        except Exception as error:
            raise_error_message(error)






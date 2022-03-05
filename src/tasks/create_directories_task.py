from datetime import datetime
from common.utils import next_date
import os

MAKE_FILE = '.make'


class CreateDirectory:
    """create directory for the specified date range
        start_date: start datetime object
        end_date: end datetime object
        root_path: string path where the directories to be created
        keep_file: boolean to specify to create keep_file or not
    """
    def __init__(self, start_date: datetime, end_date: datetime, root_path: str, keep_file: bool = False):
        self.start_date = start_date
        self.end_date = end_date
        self.root_path = root_path
        self.keep_file = keep_file

    def execute(self):
        delta = self.end_date - self.start_date

        for day_increment in range(delta.days + 1):
            date_structure = next_date(self.start_date, day_increment)

            dir_path = os.path.join(self.root_path, date_structure)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print('Directory {} created'.format(dir_path))

                if self.keep_file:
                    with open(os.path.join(dir_path, MAKE_FILE), 'w') as fp:
                        pass
                    print('.make {} file created'.format(dir_path + MAKE_FILE))
            elif os.path.exists(dir_path) and self.keep_file and not os.path.exists(os.path.join(dir_path, MAKE_FILE)):
                with open(os.path.join(dir_path, MAKE_FILE), 'w') as fp:
                    pass
                print('Directory {} already exists'.format(dir_path))
                print('.make {} file created'.format(dir_path + '/' + MAKE_FILE))
            elif os.path.exists(dir_path) and self.keep_file and os.path.exists(os.path.join(dir_path, MAKE_FILE)):
                print('Directory {} already exists'.format(dir_path))
                print('.make {} already exists'.format(dir_path + '/' + MAKE_FILE))
            else:
                print('Directory {} already exists'.format(dir_path))


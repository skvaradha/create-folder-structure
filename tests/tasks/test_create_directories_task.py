import unittest
import datetime
import os

from src.common.utils import get_project_root, delete_contents
from src.tasks.create_directories_task import CreateDirectory


class CreateDirectoryTests(unittest.TestCase):
    def test_create_directory_without_keep_file(self):
        delete_contents(str(get_project_root()) + '/test')
        create_directory = CreateDirectory(start_date=datetime.datetime(2021, 12, 31),
                                           end_date=datetime.datetime(2022, 1, 2),
                                           root_path=str(get_project_root()) + '/test',
                                           keep_file=False)
        create_directory.execute()

        total_dirs = 0
        for base, dirs, files in os.walk(str(get_project_root()) + '/test'):
            for dir in dirs:
                total_dirs += 1

        self.assertEqual(7, total_dirs)

    def test_create_directory_with_keep_file(self):
        delete_contents(str(get_project_root()) + '/test')
        create_directory = CreateDirectory(start_date=datetime.datetime(2021, 12, 31),
                                           end_date=datetime.datetime(2022, 1, 2),
                                           root_path=str(get_project_root()) + '/test',
                                           keep_file=True)
        create_directory.execute()

        total_files = 0
        for base, dirs, files in os.walk(str(get_project_root()) + '/test'):
            for Files in files:
                if Files == '.make':
                    total_files += 1

        self.assertEqual(3, total_files)



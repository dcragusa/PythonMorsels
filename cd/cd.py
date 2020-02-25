import os
from pathlib import Path
from collections import namedtuple
from contextlib import contextmanager
from tempfile import TemporaryDirectory

# @contextmanager
# def cd(sub_dir):
#     current_dir = Path.cwd()
#     new_dir = current_dir.joinpath(sub_dir)
#     try:
#         os.chdir(new_dir)
#         yield
#     finally:
#         os.chdir(current_dir)

# @contextmanager
# def cd(sub_dir=None):
#     current_dir = Path.cwd()
#     temp_dir = tempfile.TemporaryDirectory() if sub_dir is None else None
#     new_dir = temp_dir.name if sub_dir is None else current_dir.joinpath(sub_dir)
#     try:
#         os.chdir(new_dir)
#         yield
#     finally:
#         os.chdir(current_dir)
#         if temp_dir is not None:
#             temp_dir.cleanup()

#
# @contextmanager
# def cd(sub_dir=None):
#     current_dir = Path.cwd()
#     temp_dir = TemporaryDirectory() if sub_dir is None else None
#     new_dir = temp_dir.name if sub_dir is None else current_dir.joinpath(sub_dir)
#     try:
#         os.chdir(new_dir)
#         yield cd_attributes(current_dir, new_dir)
#     finally:
#         os.chdir(current_dir)
#         if temp_dir is not None:
#             temp_dir.cleanup()


cd_attributes = namedtuple('cd_attributes', ['previous', 'current'])


class CD:
    def __init__(self, sub_dir=None):
        self.sub_dir = sub_dir

    def __enter__(self):
        self.current_dir = Path.cwd()
        self.temp_dir = TemporaryDirectory() if self.sub_dir is None else None
        self.new_dir = self.temp_dir.name if self.sub_dir is None else self.current_dir.joinpath(self.sub_dir)
        os.chdir(self.new_dir)
        return cd_attributes(self.current_dir, self.new_dir)

    def enter(self):
        self.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_dir)
        if self.temp_dir is not None:
            self.temp_dir.cleanup()

    def exit(self):
        # if exiting manually, no exception
        self.__exit__(None, None, None)


cd = CD

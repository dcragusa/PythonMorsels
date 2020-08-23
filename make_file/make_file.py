import os
from contextlib import ContextDecorator
from tempfile import NamedTemporaryFile


class MakeFile(ContextDecorator):

    def __init__(self, contents='', directory=None, mode='w', **kwargs):
        self.contents, self.directory, self.mode, self.kwargs = contents, directory, mode, kwargs

    def __enter__(self):
        self.file = NamedTemporaryFile(delete=False, mode=self.mode, dir=self.directory, **self.kwargs)
        with self.file as f:
            f.write(self.contents)
        return self.file.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.file.name)


make_file = MakeFile

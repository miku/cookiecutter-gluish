# coding: utf-8

import logging
import os

from gluish.task import BaseTask

class Task(BaseTask):
    """
    Base directory.
    """
    BASE = os.path.join(os.path.dirname(__file__), '..', 'derived')

    def data(self, path):
        """
        Return the absolute path to the asset. `path` is the relative path
        below the data dir.
        """
        return os.path.join(os.path.dirname(__file__), 'data', path)

    def assets(self, path):
        """
        Return the absolute path to the asset. `path` is the relative path
        below the assets root dir.
        """
        return os.path.join(os.path.dirname(__file__), 'assets', path)

    @property
    def logger(self):
        """
        Return the logger. Module logging uses singleton internally, so no worries.
        """
        return logging.getLogger('{{ cookiecutter.name }}')

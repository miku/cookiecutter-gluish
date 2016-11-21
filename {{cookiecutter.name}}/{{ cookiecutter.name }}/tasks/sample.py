# coding: utf-8

from {{ cookiecutter.name}}.task import Task

class Hello(Task):
    """
    A sample task.
    """
    def run(self):
        print("Hello Pipes!")

    def complete(self):
        return False

# coding: utf-8

from {{ cookiecutter.name}}.task import Task
import luigi

class Hello(Task):
    """
    A sample task.
    """
    def run(self):
        with self.output().open('w') as output:
            output.write("Hello Pipes!\n")
            output.write("Second line!\n")

    def output(self):
        return luigi.LocalTarget(path=self.path())

class Analysis(Task):
    """
    Sample task.
    """
    def requires(self):
        return Hello()

    def run(self):
        with self.input().open() as handle:
            for line in handle:
                print('%s: %s' % (line, len(line)))

    def complete(self):
        return False

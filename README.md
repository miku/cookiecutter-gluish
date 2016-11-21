README
======

Quickstart data pipeline project, with [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html).

```
$ cookiecutter gh:miku/cookiecutter-gluish
name [xpipe]: mel16
repository [https://github.com/miku/mel16]:
author [Martin Czygan]:
author_email [martin.czygan@gmail.com]:

$ cd mel16
$ mkvirtualenv mel16
(mel16) $ python setup.py develop
```

There is some strange error with `python-daemon`, maybe install it separately.

```
(mel16) $ pip install python-daemon
(mel16) $ python setup.py develop
(mel16) $ mel16-build Hello --local-scheduler
...
```

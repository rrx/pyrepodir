from setuptools import setup
# you may need setuptools instead of distutils

setup(
    name='repodir',
    version='0.0.1',
    description='Manage Multiple Git Repositories in a Directory',
    author='Ryan Sadler',
    author_email='rrsadler@gmail.com',
    url='https://bitbucket.org/aix/pyrepodir',
    packages=['repodir'],

    scripts=[
        'bin/repodir'
    ]
)
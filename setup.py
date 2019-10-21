from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pycgilib',
    packages=['pycgilib'],
    version='0.0.1',
    description='Simple CGI helper library',
    install_requires=required
)

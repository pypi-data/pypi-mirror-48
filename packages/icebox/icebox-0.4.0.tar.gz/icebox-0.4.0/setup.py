from os import path
from setuptools import setup, find_packages

from app import NAME, VERSION


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,

    python_requires='>=3.6',
    install_requires=[
        'boto3>=1.9',
        'click>=7.0',
        'python-gnupg>=0.4',
        'pyyaml>=5.1',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'tmp']),
    entry_points={'console_scripts': ['icebox=app.cli:icebox']},

    author='Alexander Dietrich',
    author_email='alexander@dietrich.cx',
    description='Encrypting cold storage archiver for Amazon S3 and Glacier.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/7adietri/icebox',
    license='GPLv3+',
)

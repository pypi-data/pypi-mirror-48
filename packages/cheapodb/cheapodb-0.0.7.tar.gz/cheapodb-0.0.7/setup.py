import os
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = '0.0.7'


class VerifyVersionCommand(install):
    description = 'verify that git tag matches VERSION prior to publishing to pypi'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = 'Git tag: {0} does not match the version of this app: {1}'.format(
                tag, VERSION
            )
            sys.exit(info)


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


install_requires = [
    'boto3==1.9.180',
    'dask[dataframe]==2.0.0',
    'fastparquet==0.3.1',
    'joblib==0.13.2',
    'pandas==0.24.2',
    'PyAthena==1.6.1',
    's3fs==0.2.1'
]

setup(
    name='cheapodb',
    version=VERSION,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    extras_require={
        'pandas': ['pandas>=0.24.0']
    },
    url='https://github.com/mineralzen/cheapodb',
    keywords=['data', 'aws'],
    packages=find_packages(exclude=('test*',)),
    package_dir={'directaccess': 'directaccess'},
    license='MIT',
    author='Cole Howard',
    author_email='cole@mineralzen.com',
    description='Opinionated implementation of AWS Glue',
    cmdclass={
        'verify': VerifyVersionCommand,
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)

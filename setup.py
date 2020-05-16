# encoding: utf-8
import io
import setuptools


__author__ = 'David Schenk'
__version__ = '0.0.1'

try:
    with io.open('README.md', 'r') as file:
        LONG_DESCRIPTION = file.read()
except Exception:
    LONG_DESCRIPTION = None


setuptools.setup(
    name='webapi',
    version=__version__,
    author=__author__,
    maintainer=__author__,
    description='Base class for the development of a Python web API. ',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests==2.23.0'
    ],
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    python_requires='>=3.7.5',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries'
    ])

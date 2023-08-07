"""Setup for nft"""

import pickle
from os.path import isfile, join
import yaml
import io
import ast
import glob
from setuptools import setup, find_packages


INSTALL_REQUIRES = (
    ['plumbum>=1.6.7', 'setuptools>=40.7.3', 'PyYAML>=5.1.1']
)

templates_list = glob.glob("templates/*")
print(templates_list)

def version():
    """Return version string."""
    with io.open('nft.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with io.open('README.rst') as readme:
    setup(
        name='nft',
        version=version(),
        description='A tool for quickly creating a New File form a Template',
        long_description=readme.read(),
        license='Expat License',
        author='Daniel Richards',
        author_email='ddrichar@ucsc.edu',
        data_files   = [ ("nft/templates",  templates_list)],
       # data_files=[('', ['templates/Python.py', 'templates/README' ])],
        include_package_data=True,
        url='https://github.com/dan-rds/NFT',
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Quality Assurance',
        ],
        keywords='automation, template',
        install_requires=INSTALL_REQUIRES,
        py_modules=['nft'],
        zip_safe=False,
       # scripts=['bin/nft'],
        entry_points={'console_scripts': ['nft = nft:nft']},
    )
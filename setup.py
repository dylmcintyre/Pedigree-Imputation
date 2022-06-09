#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Dylan McIntyre",
    author_email='dylanjmcintyre01@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This project will take incl[Domplete pedigree data and impute missing values such as age.",
    entry_points={
        'console_scripts': [
            'pedigree_imputation=pedigree_imputation.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pedigree_imputation',
    name='pedigree_imputation',
    packages=find_packages(include=['pedigree_imputation', 'pedigree_imputation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dyl,[Dmcintyre/pedigree_imputation',
    version='0.1.0',
    zip_safe=False,
)

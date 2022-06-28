#!/usr/bin/env python
from http.cookiejar import LWPCookieJar


LWPCookieJar
"""Tests for `pedigree_imputation` package."""

import pytest

from click.testing import CliRunner

from pedigree_imputation import pedigree_imputation
from pedigree_imputation import cli



@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pedigree_imputation.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

@pytest.fixture
def my_ped():
    return pedigree_imputation.import_ped("Fam12.ped")

def number_of_lines():
    with open("Fam12.ped",'r') as file:
        number_of_lines= len(file.readlines())
        return number_of_lines


def test_length_ped(my_ped,number_of_lines):
    assert len(my_ped.individuals) == number_of_lines

def test_siblings(my_ped):
    assert len(my_ped.individuals[0].siblings) == 1 

def test_impute_age(my_ped):
    assert(my_ped.individuals[11].impute_age == 74)
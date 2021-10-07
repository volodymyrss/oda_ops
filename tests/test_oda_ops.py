#!/usr/bin/env python

"""Tests for `oda_ops` package."""


import unittest
from click.testing import CliRunner

from oda_ops import oda_ops
from oda_ops import cli


class TestOda_ops(unittest.TestCase):
    """Tests for `oda_ops` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'oda_ops.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

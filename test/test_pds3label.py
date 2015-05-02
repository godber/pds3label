"""
Tests for `pds3label` module.
"""
import pytest
from pds3label import Pds3Label


class TestPds3label(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_file(self):
        l = Pds3Label('test/data/tiny2.lbl')
        assert l.infile == 'test/data/tiny2.lbl'

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

    def test_based_integer(self):
        f = 'test/data/based_integer1.lbl'
        label = Pds3Label(f)
        assert label.infile == f
        assert label['BASED_INT1'].int_value == 4095
        assert str(label['BASED_INT1']) == '2#0000111111111111#'
        assert label['BASED_INT2'].int_value == 75
        assert label['BASED_INT3'].int_value == 75
        assert label['BASED_INT4'].int_value == 75
        assert label['BASED_INT5'].int_value == 75
        assert label['BASED_INT6'].int_value == -75

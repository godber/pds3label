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

    def test_tiny2(self):
        label = Pds3Label('test/data/tiny2.lbl')
        assert label.infile == 'test/data/tiny2.lbl'
        assert label.label_dict['PDS_VERSION_ID'] == 'PDS3'
        assert label.label_dict['RECORD_TYPE'] == 'STREAM'
        assert label.label_dict['RECORD_BYTES'] == 89
        assert label.label_dict['FILE_RECORDS'] == 20

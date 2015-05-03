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

    def test_string2(self):
        label = Pds3Label('test/data/string2.lbl')
        assert label.infile == 'test/data/string2.lbl'
        assert label.label_dict['INTEGER1'] == 1
        assert label.label_dict['FLOAT'] == 2.3
        assert label.label_dict['COMMENT1'] == "THING TEST"
        assert label.label_dict['COMMENT2'] == "Alive."
        assert label.label_dict['COMMENT_1'] == "THING TEST"
        assert label.label_dict['COMMENT_2'] == "Alive."
        assert label.label_dict['COMMENT_2_A'] == "Alive Again."
        assert label.label_dict['SYMBOL_STR'] == "JBD-123"

    def test_string3(self):
        label = Pds3Label('test/data/string3.lbl')
        assert label.infile == 'test/data/string3.lbl'
        assert label.label_dict['MULTILINE'] == 'This is a test of the emergency broadcasting system.'
        assert label.label_dict['HYPHENATED'] == 'The planet Jupiter is very big'
        assert label.label_dict['EMPTY_STRING'] == ''

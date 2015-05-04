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
        assert label['PDS_VERSION_ID'] == 'PDS3'
        assert label['RECORD_TYPE'] == 'STREAM'
        assert label['RECORD_BYTES'] == 89
        assert label['FILE_RECORDS'] == 20

    def test_string2(self):
        label = Pds3Label('test/data/string2.lbl')
        assert label.infile == 'test/data/string2.lbl'
        assert label['INTEGER1'] == 1
        assert label['FLOAT'] == 2.3
        assert label['COMMENT1'] == "THING TEST"
        assert label['COMMENT2'] == "Alive."
        assert label['COMMENT_1'] == "THING TEST"
        assert label['COMMENT_2'] == "Alive."
        assert label['COMMENT_2_A'] == "Alive Again."
        assert label['SYMBOL_STR'] == "JBD-123"

    def test_string3(self):
        label = Pds3Label('test/data/string3.lbl')
        assert label.infile == 'test/data/string3.lbl'
        assert label['MULTILINE'] == 'This is a test of the emergency broadcasting system.'
        assert label['HYPHENATED'] == 'The planet Jupiter is very big'
        assert label['EMPTY_STRING'] == ''

    @pytest.mark.parametrize("infile,expected", [
        ('test/data/group1.lbl', 'test/data/group1.lbl'),
        ('test/data/group2.lbl', 'test/data/group2.lbl'),
        ('test/data/group3.lbl', 'test/data/group3.lbl'),
    ])
    def test_group1(self, infile, expected):
        label = Pds3Label(infile)
        assert label.infile == expected
        assert label['IMAGE']['_type'] == 'OBJECT'
        assert label['IMAGE']['MAXIMUM'] == 255
        assert label['IMAGE']['STANDARD_DEVIATION'] == 16.97019
        assert label['IMAGE']['CHECKSUM'] == 25549531
        assert label['SHUTTER_TIMES']['_type'] == 'GROUP'
        assert label['SHUTTER_TIMES']['START'] == 1234567
        assert label['SHUTTER_TIMES']['STOP'] == 2123232

    def test_group4_non_group_elements(self):
        label = Pds3Label('test/data/group4.lbl')
        assert label.infile == 'test/data/group4.lbl'
        assert label['IMAGE']['_type'] == 'OBJECT'
        assert label['IMAGE']['MAXIMUM'] == 255
        assert label['IMAGE']['STANDARD_DEVIATION'] == 16.97019
        assert label['IMAGE']['CHECKSUM'] == 25549531
        assert label['SHUTTER_TIMES']['_type'] == 'GROUP'
        assert label['SHUTTER_TIMES']['START'] == 1234567
        assert label['SHUTTER_TIMES']['STOP'] == 2123232
        assert label['FILENAME'] == 'ImageFile-00112.IMG'
        assert label['WINDOW'] == 12.455

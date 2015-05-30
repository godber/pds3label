"""
Tests for `pds3label` module.
"""
import pytest
from pds3label import Pds3Label

def test_based_integer():
    f = 'test/data/simple_image_1.lbl'
    label = Pds3Label(f)
    assert label.infile == f
    assert label['RECORD_TYPE'] == 'FIXED_LENGTH'
    assert label['RECORD_BYTES'] == 824
    assert label['LABEL_RECORDS'] == 1
    assert label['FILE_RECORDS'] == 601
    assert label['IMAGE']['LINES'] == 600
    assert label['IMAGE']['LINE_SAMPLES'] == 824
    image_group = label['IMAGE']
    assert image_group['SAMPLE_TYPE'] == 'MSB_INTEGER'
    assert image_group['SAMPLE_BITS'] == 8
    assert abs(image_group['MEAN'] - 51.6778539644) <= 0.00001
    assert image_group['MEDIAN'] == 50.0
    assert image_group['MINIMUM'] == 0
    assert image_group['MAXIMUM'] == 255
    assert image_group['STANDARD_DEVIATION'] == 16.97019
    assert image_group['CHECKSUM'] == 25549531

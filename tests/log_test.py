#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Logging 
"""

import cycles.cyclometer.log as log
import pytest
from freezegun import freeze_time


@freeze_time("Jan 1st, 2016")
def test_beat_log(capsys):
    log.beat()
    expected = '2016-01-01T00:00:00.000+00:00 [INFO] [BEAT] .\n'
    with open('cycles.log', "r") as file_handle:
        file = file_handle.readlines()
    assert file[-1] == expected


@freeze_time("Jan 1st, 2016")
def test_error_log(capsys):
    log.error('bad!')
    expected = '2016-01-01T00:00:00.000+00:00 [ERROR] bad!\n'
    with open('cycles.log', "r") as file_handle:
        file = file_handle.readlines()
    assert file[-1] == expected


@freeze_time("Jan 1st, 2016")
def test_info_log(capsys):
    log.info('FYI')
    expected = '2016-01-01T00:00:00.000+00:00 [INFO] FYI\n'
    with open('cycles.log', "r") as file_handle:
        file = file_handle.readlines()
    assert file[-1] == expected

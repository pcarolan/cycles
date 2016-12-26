#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from cycles import Hub

hub = Hub()

def test_my_stuff(benchmark):

    result = benchmark(hub.wheel.spin)

    assert result
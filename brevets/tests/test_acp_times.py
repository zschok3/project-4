"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import arrow
import logging
import acp_times as acp
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_example_one():
    time = arrow.get('2021-01-21T00:00')
    assert acp.open_time(890, 1000, time) - time == arrow.get_timedelta('29:09:22.184874')
    assert acp.close_time(890,1000,time) - time == arrow.get_timedelta('63:22:34.567728') 
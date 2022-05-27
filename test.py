from unittest import TestCase

from exceptions import (
    UnacceptableHourError, UnacceptableIntervalError, UnacceptableMinuteError,
)
from managers import WorkIntervalManager, WorkTimeManager


class WorkTimeManagerTestCase(TestCase):

    def test_not_valid_hour(self):
        time1 = '25:15'
        time2 = '-1:10'
        self.assertRaises(UnacceptableHourError,
                          lambda: WorkTimeManager.create(time1))
        self.assertRaises(UnacceptableHourError,
                          lambda: WorkTimeManager.create(time2))

    def test_not_valid_minute(self):
        time1 = '10:-8'
        time2 = '15:60'
        self.assertRaises(UnacceptableMinuteError,
                          lambda: WorkTimeManager.create(time1))
        self.assertRaises(UnacceptableMinuteError,
                          lambda: WorkTimeManager.create(time2))


class WorkIntervalManagerTestCase(TestCase):

    def test_not_valid_interval(self):
        interval1 = '10:30-9:15'
        self.assertRaises(UnacceptableIntervalError,
                          lambda: WorkIntervalManager.create(interval1))

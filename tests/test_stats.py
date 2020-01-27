from unittest import TestCase
from unittest.mock import ANY

import kb_python.stats as stats
from tests.mixins import TestMixin


class TestStats(TestMixin, TestCase):

    def test_start(self):
        s = stats.Stats()
        s.start()

        self.assertIsNotNone(s.start_time)
        self.assertIsNotNone(s.call)
        self.assertEqual([], s.commands)

    def test_command(self):
        s = stats.Stats()
        s.command(['test', 'command'])

        self.assertEqual(['test command'], s.commands)

    def test_end(self):
        s = stats.Stats()
        s.start()
        s.end()

        self.assertIsNotNone(s.end_time)
        self.assertTrue(s.elapsed > 0)

    def test_to_dict(self):
        s = stats.Stats()
        s.start()
        s.command(['test'])
        s.end()

        self.assertEqual({
            'start_time': ANY,
            'end_time': ANY,
            'elapsed': ANY,
            'call': ANY,
            'commands': ['test'],
        }, s.to_dict())
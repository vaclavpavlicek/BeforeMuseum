import unittest
import main


class TestBeforeMuseum(unittest.TestCase):
    def test_index_of_pupil(self):
        self.assertEquals(0, main.index_of_pupil('A', 'ABA'))

    def test_index_of_pupils_in_group(self):
        self.assertEquals([0, 1], main.index_of_pupils_in_group(['A', 'B'], 'ABA'))

    def test_read_group_from_input_file(self):
        self.assertEquals('JAJ', main.test_read_group_from_input_file('input.txt'))

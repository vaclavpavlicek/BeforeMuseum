import unittest
import main


class TestBeforeMuseum(unittest.TestCase):

    def test_index_of_pupils_in_group(self):
        self.assertEquals([1, 2], main.index_of_pupils_in_group(['A', 'B'], 'ABA'))

    def test_read_group_from_input_file(self):
        self.assertEquals('JAJ', main.read_group_from_input_file('input.txt'))

    def test_read_all_pupils_from_input_file(self):
        self.assertEquals('AJJBAJAJ', main.read_all_pupils_from_input_file('input.txt'))

    def test_find_group_of_pupils(self):
        self.assertEquals([2, 5, 6], main.find_group_of_pupils('input.txt'))

    def test_generate_output_file(self):
        self.assertEquals('2 5 6', main.generate_output_file(main.find_group_of_pupils('input.txt')))

import unittest
import controller

class PathProjectTestCase(unittest.TestCase):
    def test_get_file(self):
        control = controller.Controller('../data/paths.pkl.xz')
        file = control.get_file()

    def test_drow(self):
        control = controller.Controller('../data/paths.pkl.xz')
        control.drow()

    def test_drow_by_filter(self):
        pass

    def test_hours_filter(self):
        pass

    def test_date_and_hours_filter(self):
        pass

    def test_area_filter(self):
        pass

    def test_specific_area_filter(self):
        pass
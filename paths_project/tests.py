import unittest
import controller

class PathProjectTestCase(unittest.TestCase):
    def test_get_file(self):
        control = controller.Controller('../data/paths.pkl.xz')


    def test_drow(self):
        control = controller.Controller('../data/paths.pkl.xz','../data/paths0.png')
        control.draw_lines([([30,100,150,200,250],[30,40,60,90,150]),([350,300],[30,50]),([400,300],[30,100]),([250,150],[30,50]),([100,250],[30,50])],False)

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
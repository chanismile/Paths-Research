import unittest
import controller
import datetime

class PathProjectTestCase(unittest.TestCase):
    def test_get_file(self):
        control = controller.Controller('../data/paths.pkl.xz')


    def test_drow(self):
        control = controller.Controller('../data/sample.csv','../data/paths0.png')
        control.draw_lines([([30,100,150,200,250],[30,40,60,90,150]),([350,300],[30,50]),([400,300],[30,100]),([250,150],[30,50]),([100,250],[30,50])],False)

    def test_drow_by_filter(self):
        pass

    def test_hours_filter(self):
        control = controller.Controller('../data/sample.csv','../data/paths0.png')
        self.assertEquals(control.hours_filter(datetime.time(int(1), int(27), int(9)), datetime.time(int(1), int(28), int(19))).shape[0],16)

    def test_date_and_hours_filter(self):
        control = controller.Controller('../data/sample.csv', '../data/paths0.png')
        self.assertEquals(
            control.hours_and_date_filter(datetime.time(int(1), int(27), int(9)), datetime.time(int(1), int(28), int(19)),datetime.date(int(2017), int(8), int(17))).shape[
                0], 16)

    def test_area_filter(self):
        control = controller.Controller('../data/sample.csv', '../data/paths0.png')
        self.assertEquals(
            control.area_filter((5,76), (149,112)).shape[
                0], 12)

    def test_specific_area_filter(self):
        control = controller.Controller('../data/sample.csv', '../data/paths0.png')
        self.assertEquals(
            control.specific_area_filter(((0,8),)).shape[
                0], 1)
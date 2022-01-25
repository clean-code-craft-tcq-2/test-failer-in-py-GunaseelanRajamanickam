import unittest
import mock
from tshirts import *
from misaligned import *
import alerter

class TestTshirts(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(38), 'S')
        self.assertEqual(size(42), 'M')
        self.assertEqual(size(0), 'Not a valid tshirt size')
        self.assertEqual(size(-20), 'Not a valid tshirt size')

    def test_input_value(self):
        self.assertRaises(TypeError, size, True)

class testMisaligned(unittest.TestCase):
    printed_list = []
    def formatted_string_stub(self):
        major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                element = f"{i * 5 + j} | {major} | {minor}"
                testMisaligned.printed_list.append(element)
        return testMisaligned.printed_list
        
    def test_print_color_map(self):
        testMisaligned.formatted_string_stub(self)
        test_string_first = testMisaligned.printed_list[0]
        test_string_last = testMisaligned.printed_list[-1]

        self.assertEqual(test_string_first.find('|'), test_string_last.find('|'))
        self.assertEqual(len(test_string_first.split(' | ')[0]), len(test_string_last.split(' | ')[0]))

class TestAlerter(unittest.TestCase):
    def mock_network_alert_stub(self):
        return 500
    
    @mock.patch('alerter.network_alert_stub', return_value = mock_network_alert_stub)
    def test_alert_in_celcius(self, return_value):
        alerter.alert_in_celcius(400.5)
        print(f'{alerter.alert_failure_count} alerts failed.')
        self.assertEqual(alerter.alert_failure_count, 1)

if __name__ == '__main__':
    unittest.main()
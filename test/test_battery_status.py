import unittest
from unittest.mock import MagicMock, patch

from battery_status import get_battery_status

class TestGetBatteryStatus(unittest.TestCase):
    def test_get_battery_status_full(self):
        result = get_battery_status()
        self.assertEqual(result, 100)

    def test_positive(self):
        result = get_battery_status()
        self.assertGreater(result,0)

    def test_bounds(self):
        result = get_battery_status()
        self.assertTrue(0 < result <= 100)

    @patch('psutil.sensors_battery')
    def test_battery_status_zero(self, mock_sensors_battery):
        mock_battery = MagicMock()
        mock_battery.percent = 0
        mock_sensors_battery.return_value = mock_battery

        result = get_battery_status()
        self.assertEqual(result, 0)

    @patch('psutil.sensors_battery')
    def test_battery_status_full(self, mock_sensors_battery):
        mock_battery = MagicMock()
        mock_battery.percent = 100
        mock_sensors_battery.return_value = mock_battery

        result = get_battery_status()
        self.assertEqual(result, 100)
    @patch('psutil.sensors_battery')
    def test_battery_status_rounding_edge_case(self, mock_sensors_battery):
        mock_battery = MagicMock()
        mock_battery.percent = 99.9  # Should round down to 99
        mock_sensors_battery.return_value = mock_battery

        result = get_battery_status()
        self.assertEqual(result, 99)

print("-------------------------")
print("Testing battery_status.py")
print("-------------------------")

if __name__ == '__main__':
    unittest.main()


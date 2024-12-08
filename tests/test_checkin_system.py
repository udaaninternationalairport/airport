import unittest
from src.passenger_management.checkin_system import check_in_passenger

class TestCheckInSystem(unittest.TestCase):
    def test_check_in_passenger(self):
        result = check_in_passenger("P12345", "AI2024")
        self.assertEqual(result["status"], "success")
        self.assertIn("boarding_pass", result)

if __name__ == "__main__":
    unittest.main()
import unittest
from unittest.mock import patch, Mock
from main import(
    greet_human, 
    is_it_cold_f,
    Temp_Threshold_F
)

class TestMainApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['alice'])
    @patch('builtins.print')
    def test_greethuman_alice(self, mock_print: Mock, _: Mock) -> None:
        """Test inputting alice to greet_human"""
        greet_human()
        expected_calls = [
            unittest.mock.call("Hello alice, nice to meet you!")
        ]
        mock_print.assert_has_calls(expected_calls)
    def test_isitcoldf_freezing(self) -> None:
        """Tests is_it_cold_f for freezing"""
        self.assertTrue(is_it_cold_f(32))
    def test_isitcoldf_boiling(self) -> None:
        """Tests is_it_cold_f for boiling"""
        self.assertFalse(is_it_cold_f(212))
    def test_isitcoldf_negative(self) -> None:
        """Tests is_it_cold_f for negative"""
        self.assertTrue(is_it_cold_f(-40))
    def test_isitcoldf_thresh(self) -> None:
        """Tests is_it_cold_f for threshold"""
        self.assertTrue(is_it_cold_f(Temp_Threshold_F))
    def test_isitcoldf_abovethresh(self) -> None:
        """Tests is_it_cold_f for above the threshold"""
        self.assertFalse(is_it_cold_f(Temp_Threshold_F+1))
    def test_isitcoldf_belowthresh(self) -> None:
        """Tests is_it_cold_f for below the threshold"""
        self.assertTrue(is_it_cold_f(Temp_Threshold_F-1))

if __name__ == "__main__":
    unittest.main()
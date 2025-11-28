import pytest
from calculate_speed import get_speed_info

def test_get_speed_info():
    expected_output = (
        "Distance: 100 km\n"
        "Time: 2 hr\n"
        "Speed: 50.00 km/hr"
    )

    result = get_speed_info(100, 2)
    assert result == expected_output

import pytest
from unittest.mock import patch
import logging
from task import main


@patch('builtins.input', side_effect=[str(3), str(4), str(5)])
def test_triangle_exists(mock_input):
    with patch.object(logging.Logger, 'info') as mock_info:
        main()
    mock_info.assert_any_call("Треугольник существует")


@patch('builtins.input', side_effect=[str(3), str(3), str(33)])
def test_no_triangle(mock_input):
    with patch.object(logging.Logger, 'error') as mock_error:
        main()
    mock_error.assert_any_call("Треугольник не существует")


@patch('builtins.input', side_effect=[str(1), str(1), str(1)])
def test_equilateral_triangle(mock_input):
    with patch.object(logging.Logger, 'info') as mock_info:
        main()
    mock_info.assert_any_call("Треугольник равносторонний")

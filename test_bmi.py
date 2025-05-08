import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'Lab2'))

import calculate_bmi as bmi

import pytest

from calculate_bmi import calculate_bmi

def test_bmi_normal_weight():
    height = 1.75  # meters
    weight = 70    # kg
    bmi, classification = calculate_bmi(height, weight)

    
    assert bmi == 22.86

    
    assert classification == "0"  

def test_bmi_over_weight():
    height = 1.75  # meters
    weight = 85    # kg
    bmi, classification = calculate_bmi(height, weight)

    
    assert bmi == 27.76

    
    assert classification == "1"  

def test_bmi_under_weight():
    height = 1.75  # meters
    weight = 50    # kg
    bmi, classification = calculate_bmi(height, weight)

    
    assert bmi == 16.33

    
    assert classification == "-1" 
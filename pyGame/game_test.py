import pytest
import pygame



#First arg will be the input to the test functions, and the second will be the
# outputs. 
@pytest.mark.parametrize("password,passes_check", [
    ("123456", False),

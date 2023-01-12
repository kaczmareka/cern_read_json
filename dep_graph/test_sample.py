import pytest
from function_new import *

def test_function():
    variable=function_new('tmp\\deps2.json')
    assert type(variable)==str

def test_function_working():
    variable=function_new('tmp\\deps.json')
    splited_variable=variable.split("\n")
    assert splited_variable==['-pkg1', '  -pkg2', '    -pkg3', '  -pkg3', '-pkg2', '  -pkg3', '-pkg3']
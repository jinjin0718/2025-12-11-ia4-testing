import sys
import os

# python might not be able to find the folder because you might not be in the correct directory, 
# we can use this line of code to get full path of this '__file__', and add it to the system path
# so python can correctly cd to the correct location
# kinda like double ensuring that the next line import won't have problem
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from scripts.wordcount import load_text

def test_load_text(): 
    text = load_text("test/example.txt")
    print(text)
    assert text == ['hello class', 'line 2']
    assert text != ["aslgaiodjfosadjf"]

def test_example(): 
    assert 3 + 3 == 6

def test_fail(): 
    assert False

def hello(): 
    assert True




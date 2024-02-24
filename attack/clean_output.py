import json
import re
from collections import defaultdict

def is_string_an_int(s):
    try:
        int(s)  # Try to convert the string to an integer
        return True  # Conversion successful means the string is an integer
    except ValueError:
        return False  # Conversion failed means the string is not an integer


def convert_string_to_float(s):
    if s is None:
        return None

    if is_string_an_int(s):
        return round(float(s), 2)

    if '/' in s:
        numerator, denominator = s.split('/')
        return float(numerator) / float(denominator)
    else:
        # Remove any non-numeric characters except for '.'
        clean_string = re.sub(r'[^\d.]', '', s)
        # if there is a period mark at the end of the string, remove it
        if clean_string[-1] == '.': 
            clean_string = clean_string[:-1]
        return round(float(clean_string), 2)


def extractAnswer(answer):
    numbers = re.findall(r"\d+\.?\,?\d*", answer)
    if len(numbers)==0:
        return -9999
    else:
        solution = re.sub(r"[^0-9.]", "", numbers[-1])
        return solution
    

def extract_numerical_value(s):
    return extractAnswer(s)

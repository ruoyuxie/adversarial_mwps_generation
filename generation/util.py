import itertools
import locale
import math
import random
import re
from typing import Union

from numpy.random import poisson
from primefac import primefac

factor_dict = {}


def get_factor_count(num):
    if num in factor_dict:
        return factor_dict[num]
    factor_dict[num] = len(list(primefac(num)))
    return factor_dict[num]


def get_random_num_with_same_digits(num):
    ten_mult = 0
    if not is_int(num):
        num, ten_mult = get_scientific_notation(num)
    base = math.floor(math.log10(num))
    base = base if base > 0 else 0

    upper = math.log10(num)
    upper = upper + 1 if is_int(upper) else upper
    upper = math.ceil(upper)
    upper = upper if upper > 2 else 2

    res = generate_random_int(10 ** base, 10 ** upper - 1)

    return res * 10 ** ten_mult


def get_scientific_notation(val):
    ten_multiplier = 0
    if is_int(val):
        val = int(val)
        while val % 10 == 0 and val >= 100:
            val //= 10
            ten_multiplier += 1
    else:
        val = round(val, 6)
        while not is_int(val):
            val *= 10
            ten_multiplier -= 1
    val = int(val)
    return val, ten_multiplier


# some primes
primes = [2, 3, 5, 7, 11, 13]


def generate_random_factors_ev(orig_val):
    # This method returns a bunch of factors that, when multiplied together,
    # has the same expected value as the original value
    n = len(primes)
    res = []
    for prime in primes:
        lam = math.log(orig_val, prime) / n
        res += [prime] * poisson(lam)

    return res


def generate_random_factor_num_ev(orig_val):
    _factors = generate_random_factors_ev(orig_val)
    _base = 1.0
    for factor in _factors:
        _base *= factor
    return int(_base)


def generate_random_num_poisson(orig_val):
    return int(poisson(orig_val))


def generate_random_int(start=1, finish=100, ten_mult=None):
    if ten_mult:
        return random.randint(start, finish) * 10 ** ten_mult
    return random.randint(start, finish)


def generate_random_num(orig_val):
    if 0 <= orig_val <= 8:
        return generate_random_int(1, 8)
    return generate_random_num_poisson(orig_val)


def into_two_nums(num):
    # This function will output (num1, num2), such that num1 + num2 = num
    num1 = random.randint(0, num)
    return num1, num - num1


def generate_placeholder():
    i = 0
    while True:
        yield f"{{{i}}}"
        i += 1


def get_all_num_from_string(string):
    pattern = re.compile(r"[-+]?\d+(?:,\d\d\d)*[.]?\d*(?:[eE][-+]?\d+)?")
    locale.setlocale(locale.LC_ALL, '')
    res = []
    res_str = ""
    i = 0
    placeholder = generate_placeholder()

    for s in re.finditer(pattern, string):
        s_str = s.group(0)
        res.append(to_num(s_str))
        res_str += string[i:s.start()] + next(placeholder)
        if s_str[-1] == ".":
            # The last char is period, meaning it is the end of a sentence
            res_str += "."
        i = s.end()
    res_str += string[i:]
    return res, res_str


def to_num(string):
    if isinstance(string, int) or isinstance(string, float):
        return string
    return to_int_if_int(locale.atof(string.replace(',', '')))


def is_same_num(a: Union[int, float], b: Union[int, float]):
    return abs(a - b) <= 1e-6


def is_in_list(num, _list):
    for n in _list:
        if is_same_num(n, num):
            return True
    return False


def get_index_in_list(num, _list):
    for i in range(len(_list)):
        if is_same_num(num, _list[i]):
            return i
    return -1


def get_indices_in_list(num, _list):
    res = []
    for i in range(len(_list)):
        if is_same_num(num, _list[i]):
            res.append(i)
    return res


def generate_temp_name(string):
    i = 0
    while True:
        yield f"{string}_{i}"
        i += 1


def to_int_if_int(num):
    if is_int(num):
        return int(num)
    return num


def is_int(num):
    return isinstance(num, int) or float.is_integer(num) or abs(num - round(num)) < 1e-6


def decompose_var_name(var_name: str):
    """
    example var_name: thisIsA_long_AndWeird_varName
    return: this_is_a_long_and_weird_var_name
    """
    # First split by '_'
    res = var_name.split('_')
    # Then split by capital letters
    res = [re.sub(r"([A-Z])", r" \1", s).split() for s in res]
    # Flatten the 2D array into 1D
    res = list(itertools.chain.from_iterable(res))
    # Lower case the words and join by '_'
    return "_".join([s.lower() for s in res])

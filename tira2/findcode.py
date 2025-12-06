from itertools import permutations
from random import choice
import re

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code        

def find_code(oracle):
    guesses = []
    
    in_place, in_code = oracle.check_code("1234")

    guess = {"code": "1234",
             "in_place": in_place,
             "in_code": in_code}
    guesses.append(guess)

    in_place, in_code = oracle.check_code("5678")

    guess = {"code": "5678",
             "in_place": in_place,
             "in_code": in_code}
    guesses.append(guess)
    
    possible_codes = list(permutations(range(1, 10), 4))
    possible_codes = list(map(lambda c: "".join(map(str, c)), possible_codes))

    possible_codes = filter_possible_codes(possible_codes, guesses)
    while len(possible_codes) > 1:
        code = choice(possible_codes)
        in_place, in_code = oracle.check_code(code)
        guess = {"code": code,
                 "in_place": in_place,
                 "in_code": in_code}
        guesses.append(guess)

        possible_codes = filter_possible_codes(possible_codes, guesses)
    return possible_codes.pop()

def filter_possible_codes(codes, guesses):
    possible = []
    for code in codes:
        in_place = in_code = 0
        for guess in guesses:
            for pos in range(4):
                if code[pos] in guess["code"]:
                    if code[pos] == guess["code"][pos]:
                        in_place += 1
                    else:
                        in_code += 1
            if in_place == guess["in_place"] and in_code == guess["in_code"]:
                possible.append(code)
            
    print(len(possible))
    return possible
            
                

if __name__ == "__main__":
    # esimerkki oraakkelin toiminnasta
    # oracle = Oracle("4217")
    # print(oracle.check_code("1234")) # (1, 2)
    # print(oracle.check_code("3965")) # (0, 0)
    # print(oracle.check_code("4271")) # (2, 2)
    # print(oracle.check_code("4217")) # (4, 0)

    # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217

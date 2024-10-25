#!/usr/bin/env python3

import sys
import random

def play_game(user_number):
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)    
  
    user_number = int(sys.argv[1])
    rand_number = random.randint(1, 10)
    
    if user_number == rand_number:
        print("Congratulations! You won!")
        return True
    else:
        print("Oops! Try again!")
        return False


if __name__ == "__main__":
    play_game(sys.argv)
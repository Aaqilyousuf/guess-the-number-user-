import random

def user_guess(x):
    low = 1
    high = x
    feed_back = ''

    while feed_back != "correct":
        if low!=high:
            guess = random.randint(1,x)
        else:
            guess = low

        feed_back = input(f"is {guess} is too high , too low or correct : ").lower()
        if feed_back == 'high':
            guess -= high
        elif feed_back == 'low':
            guess += low

    print(f"YAY Computer guessed correctly {guess}")

user_guess(20)


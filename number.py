import random


class Number:
    digit_list = []

    def __init__(self):
        self.num = random.randint(1,1_000_000)

    def __int__(self):
        return self.num
    
    def __str__(self):
        return f"Psst! The answer is {self.num}"

    def get_digit(self, num):
        """Extracts each digit and put digit_list"""
        if num < 10:
            Number.digit_list.append(num)
        else:
            self.get_digit(num // 10)
            Number.digit_list.append(num % 10)

    def num_of_digits(self):
        return len(str(int(self.num)))

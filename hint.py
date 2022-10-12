from number import Number


class Hint(Number):
    def __init__(self):
        super().__init__()
        pass

    def hint1(self):
        self.hint1 = input("Do you need a hint? Y/N: ").lower()
        if self.hint1 == "y":
                print(f"There are {Number.num_of_digits(self)} digits\n")

    def hint2(self):
        self.hint2 = input("Do you need another hint? Y/N: ").lower()
        if self.hint2 == "y":
            print(f"The last digit is {Number.digit_list[-1]}\n")

    def hint3(self):
        self.hint3 = input("It seems like you need one more hint. Y/N: ")
        if self.hint3 == "y":
            print(f"The second last digit is {Number.digit_list[-2]}\n")

    def hint4(self):
        self.hint4 = input("This is the last hint. Y/N: ")
        if self.hint4 == "y":
            print(f"The third last digit is {Number.digit_list[-3]}\n")   
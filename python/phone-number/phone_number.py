PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '


class PhoneNumber:
    def __init__(self, number: str):
        self.number = number

        for punc in PUNCTUATION:
            self.number = self.number.replace(punc, "")

        if len(self.number) > 11:
            raise ValueError("Number of digits is incorrect (>11)")

        elif len(self.number) == 11:
            if self.number.startswith('1'):
                self.number = self.number[1:]
            else:
                raise ValueError("Phone number should start with '1'")

        self.area_code = self.number[:3]
        if self.area_code.startswith(("0", "1")):
            raise ValueError(f"Area code is incorrect (should not start with {self.area_code[0]}) ")

        exchange_code = self.number[3:6]
        if exchange_code.startswith(("0", "1")):
            raise ValueError(f"Exchange code is incorrect (should not start with {exchange_code[0]})")

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
        # or :
        # return "(" + self.number[:3] + ")-" + self.number[3:6] + "-" + self.number[6:]

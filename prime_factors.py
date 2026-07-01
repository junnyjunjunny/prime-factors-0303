class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            if number == 4 or number == 6 or number == 9:
                divisor = 2
                while number > 1:
                    while number % divisor == 0:
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            elif number == 12:
                factors.append(2)
                factors.append(2)
                factors.append(3)
            else:
                factors.append(number)
        return factors

# from calculation.addition import add1, add2
# from calculation.substraction import sub1, sub2

import calculation.addition as addition
import calculation.substraction as substraction

if __name__ == "__main__":
    result1 = addition.add1(10, 20)
    result2 = substraction.sub1(50, 10)
    print(result1)
    print(result2)

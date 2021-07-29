# Program to measuring the time that elapases between start and end clicks
import logging
from random import *


log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="coupon_numbers.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New coupon number generator request came !")


class Coupon:
    @staticmethod
    def coupon_generator():
        try:
            coupon_lenth = int(input
                               ("Please enter lenth of coupon you need !"))
        # handling the Exception if user enter invalid number
        except Exception as massage:
            print("invaild input please enter number only ..!")
            logging.exception(massage)
        # if there is no exception than only else block will execute !
        else:
            coupon = ""
            # generating random number accordingly user input
            for element in range(coupon_lenth):
                number = randrange(0, 10)
                coupon += str(number)
            logging.info(coupon)
            logging.info(
                "New Coupon number request processing completed.....!")
            print("Distinct Coupon number is : ", coupon)


# creating object to the class and assign to variable
reference = Coupon()
# using object reference we are calling static method !
reference.coupon_generator()


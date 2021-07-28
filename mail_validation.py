# Program to check whether given mail id is valid or not
import logging
import re


log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="mail_validation.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")


# this function for to validate user enter mail
def mail_valid(mail_id):
    result_mail = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", mail_id)
    if result_mail != None:
        logging.info(result_mail)
        logging.info("mail id validation request processing completed.....!")
        return "email id is valid.....!"
    else:
        logging.error("mail id not match with required format...!")
        return "email id is invalid.....!"


logging.info("New mail id validation request came !")
# to store user input we defind one variable name as mail_id
mail_id = input("Enter mail id to valid: ")
# Here we calling the function
print(mail_valid(mail_id))


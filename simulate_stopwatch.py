# Program to measuring the time that elapases between start and end clicks
import logging
from datetime import datetime


log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="stopwatch.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")

logging.info("New stopwatch request came !")


# this function for to measuring the time that elapases between start and end clicks
def stop_watch():
    # to start time count we take user action
    input("press enter to start : ")
    start_time = datetime.now()
    # to stop time count we take user action
    input("press enter to stop : ")
    time_elapsed = datetime.now() - start_time
    logging.info(time_elapsed)
    logging.info("stopwatch request processing completed.....!")
    return "Time elapsed (HH:MM:SS) {}" .format(time_elapsed)


# Here we calling the function
print(stop_watch())


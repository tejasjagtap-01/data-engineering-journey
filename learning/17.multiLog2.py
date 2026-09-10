import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(message)s')

file_handler = logging.FileHandler('samples.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    return x / y

num1 = 250 
num2 = 100

add_result = add(num1,num2)
logger.debug('Add: {} + {} = {}'.format(num1,num2,add_result))

subtract_result = subtract(num1,num2)
logger.debug('Subtract: {} - {} = {}'.format(num1,num2,subtract_result))

multiply_result = multiply(num1,num2)
logger.debug('Multiply: {} * {} = {}'.format(num1,num2,multiply_result))

division_result = division(num1,num2)
logger.debug('Division: {} / {} = {}'.format(num1,num2,division_result))
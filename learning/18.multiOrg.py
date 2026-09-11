import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(message)s')

file_handler = logging.FileHandler('sampless.log')
file_handler.setLevel(logging.ERROR )
file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler() used to print log msg on console
# stream_handler.setFormatter(formatter) just for formattingg 

logger.addHandler(file_handler)
# logger.addHandler(stream_handler) used to add handler 


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    try:
        result = x /y
    except ZeroDivisionError:
        logger.error('Tried to divide by zero')
    else:
        return result

num1 = 250 
num2 = 0

add_result = add(num1,num2)
logger.debug('Add: {} + {} = {}'.format(num1,num2,add_result))

subtract_result = subtract(num1,num2)
logger.debug('Subtract: {} - {} = {}'.format(num1,num2,subtract_result))

multiply_result = multiply(num1,num2)
logger.debug('Multiply: {} * {} = {}'.format(num1,num2,multiply_result))

division_result = division(num1,num2)
logger.debug('Division: {} / {} = {}'.format(num1,num2,division_result))
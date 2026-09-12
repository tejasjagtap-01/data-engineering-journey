# 1
# import logging
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

# 2
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

# # 3
# import logging
# # assuming loglevel is bound to the string value obtained from the
# # command line argument. Convert to upper case to allow the user to
# # specify --log=DEBUG or --log=debug
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


# 4
# import logging
# logging.warning('%s before you %s', 'Look', 'leap!')


# 5
# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')


# 6
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.')


# import logging
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')
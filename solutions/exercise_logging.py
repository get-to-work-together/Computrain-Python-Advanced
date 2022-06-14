import logging

logging.basicConfig(
    filename = None, # or to a file 'example.log',
    level = logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format = '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('Watch out!')
logging.critical('ERROR!!!!!')

for i in range(10):
    logging.debug(i)

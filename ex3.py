import logging

logging.basicConfig(filename="new12.log", level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("New file is created")
def fact(n):
    logging.debug(n)
    total = 1
    for i in range(n+1):
        logging.debug(i)
        total*=i
        logging.debug(total)
        return total
print(fact(5))
import logging

logging.basicConfig(filename="new13.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG)

a = int(input("Enter the A : "))
b = int(input("Enter the B : "))

try:
    c= a/b
    print(c)
except Exception as d:
    logging.error("Exception error")    
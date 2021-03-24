import logging

logging.basicConfig(filename="new11.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("New file is created")

a = int(input("Enter A : "))
b = int(input("Enter B : "))
if a>10 or b>10:
    logging.debug("A or B values are greaterthan the limit provide by the user")
    
elif a<b:
    c = a + b
    logging.info("Add operation is performing")
    print(c)

else:
    c = a-b
    logging.info("Subtraction operation is performing")
    print(c)
    

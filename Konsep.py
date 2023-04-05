import threading
import logging
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
# ------------------- Membuat THREADING -------------------#
logging.info("Main    : before creating thread")
my_thread = threading.Thread(target=thread_function,args=(1,))
logging.info("Main    : before running thread")
my_thread.start()


#------------------- STOP THREADING -------------------#
if my_thread.is_alive():
    my_thread.join()
    
    
#------------------- PRORITAS THREADING -------------------#

my_thread1 = threading.Thread(target=thread_function,args=(1,))
my_thread2 = threading.Thread(target=thread_function,args=(2,))
my_thread3 = threading.Thread(target=thread_function,args=(3,))

# Set prioritas thread
my_thread1.priority = 1
my_thread2.priority = 2
my_thread3.priority = 3

my_thread1.start()
my_thread2.start()
my_thread3.start()

my_thread1.join()
my_thread2.join()
my_thread3.join()

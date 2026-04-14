import time

def stopwatch():
    input("Press Enter to START stopwatch...")
    
    start_time = time.time()   # current time store

    input("Press Enter to STOP stopwatch...")
    
    end_time = time.time()     # current time store

    elapsed_time = end_time - start_time

    print("Elapsed Time:", elapsed_time, "seconds")


# run function
stopwatch()
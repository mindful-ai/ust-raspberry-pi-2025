import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(0.5)   # simulate a delay

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter : {letter}")
        time.sleep(0.5)


if __name__ == "__main__":

    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    # Wait for both threads to finish the job
    t1.join()
    #t2.join()

    print("This is the next block of the code")


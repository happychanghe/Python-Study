import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)

def print_letters():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(0.5)

# Create thread objects
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("Done")

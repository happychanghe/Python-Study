import threading
import time
from queue import Queue

def producer(queue):
    for i in range(5):
        item = f'Item {i}'
        queue.put(item)
        print(f'Produced: {item}')
        time.sleep(2)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consumed: {item}')
        time.sleep(1)

# Create a shared queue
queue = Queue()

# Create thread objects
producer_thread = threading.Thread(target=producer, args=(queue,))
consumer_thread = threading.Thread(target=consumer, args=(queue,))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish
producer_thread.join()

# Add a None item to signal the consumer to exit
queue.put(None)

# Wait for the consumer to finish
consumer_thread.join()

print("Done")

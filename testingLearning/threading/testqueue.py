import threading
import time
from queue import Queue

def producer(queue):
    for i in range(1, 6):
        item = f'Item {i}'
        queue.put(item)
        print(f'Produced: {item}')
        time.sleep(0.5)

def processor(queue_in, queue_out):
    while True:
        item = queue_in.get()
        if item is None:
            break
        processed_item = f'Processed {item}'
        queue_out.put(processed_item)
        print(f'Processed: {processed_item}')
        time.sleep(0.5)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consumed: {item}')
        time.sleep(1)

# Create shared queues
queue1 = Queue()
queue2 = Queue()

# Create thread objects
producer_thread = threading.Thread(target=producer, args=(queue1,))
processor_thread = threading.Thread(target=processor, args=(queue1, queue2,))
consumer_thread = threading.Thread(target=consumer, args=(queue2,))

# Start the threads
producer_thread.start()
processor_thread.start()
consumer_thread.start()

# Wait for the producer to finish
producer_thread.join()

# Add None items to signal the processor and consumer to exit
queue1.put(None)
queue2.put(None)

# Wait for the processor and consumer to finish
processor_thread.join()
consumer_thread.join()

print("Done")
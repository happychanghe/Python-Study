import turtle
import threading

# Function to get user input
def get_input():
    radius = float(input("Enter the radius of the circle: "))
    color = input("Enter the color of the circle: ")
    return radius, color

# Function to draw the circle
def draw_circle(radius, color):
    # Create turtle object
    turtle_object = turtle.Turtle()
    turtle_object.color(color)
    turtle_object.shape("turtle")
    turtle_object.circle(radius)

# Create a threading.Event object
input_event = threading.Event()

# Function to wait for input
def wait_for_input():
    # Wait for the event to be set
    input_event.wait()
    # Get user input
    radius, color = get_input()
    # Draw the circle
    draw_circle(radius, color)

# Create the thread for waiting input
input_thread = threading.Thread(target=wait_for_input)

# Start the input thread
input_thread.start()

# Set the event to signal the input thread to proceed
input_event.set()

# Keep the turtle window open until it is closed by the user
turtle.done()

# Self demo

class food:
    def __init__(produce, fruit, color):
        produce.fruit =  fruit
        produce.color = color

    # Define show()
    def show(produce):
        print('fruit is', produce.fruit)
        print('color is', produce.color)

# Create two objects
apple = food('apple', 'red')
grape = food('grapes', 'green')

# Display each object's fields, namely fruit and color
apple.show()
grape.show()



import turtle

def draw_square(turtle_obj, size):
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)

def draw_concentric_squares(turtle_obj, initial_size, num_squares, spacing):
    for _ in range(num_squares):
        draw_square(turtle_obj, initial_size)
        turtle_obj.penup()
        turtle_obj.goto(-initial_size / 2, initial_size / 2)  # Move to starting position for the next square
        turtle_obj.pendown()
        initial_size -= spacing

def main():

    drawer = turtle.Turtle()
    drawer.speed(0)  
    drawer.penup()
    drawer.goto(-100, 100)  # Start position; adjust as needed

    initial_size = 200
    num_squares = 20
    spacing = initial_size / num_squares

    draw_concentric_squares(drawer, initial_size, num_squares, spacing)

    turtle.done()

if __name__ == "__main__":
    main()

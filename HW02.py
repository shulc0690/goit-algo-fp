import turtle

TTL = turtle.Turtle()
screen = turtle.Screen()  # Create the screen.


def draw_tree(branch_length, angle, level):
    if level == 0:
        return
    TTL.forward(branch_length)
    TTL.left(angle)
    draw_tree(branch_length * 0.7, angle, level - 1)
    TTL.right(2 * angle)
    draw_tree(branch_length * 0.7, angle, level - 1)
    TTL.left(angle)
    TTL.backward(branch_length)


def main():
    window = turtle.Screen()
    window.bgcolor("white")

    TTL.speed(0)
    TTL.left(90)
    TTL.up()
    TTL.backward(200)
    TTL.down()

    level = int(input("Введіть рівень рекурсії: "))
    draw_tree(100, 30, level)
    screen.exitonclick()  # Exit screen


if __name__ == "__main__":
    main()

import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length = length / 3

        koch_curve(t, length, level - 1)
        t.left(60)

        koch_curve(t, length, level - 1)
        t.right(120)

        koch_curve(t, length, level - 1)
        t.left(60)

        koch_curve(t, length, level - 1)


def main():
    level = int(input("Введіть рівень рекурсії (0-5): "))

    if level < 0 or level > 5:
        print("Введіть число від 0 до 5.")
        return

    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400

    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

    screen.mainloop()


if __name__ == "__main__":
    main()

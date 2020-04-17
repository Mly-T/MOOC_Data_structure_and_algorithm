import turtle

t = turtle.Turtle()

def tree(branch_len):
    t.pendown()
    t.forward(branch_len)
    t.penup()
    if branch_len > 5:
        t.left(20)
        tree(branch_len - 5)
        t.right(40)
        tree(branch_len - 5)
        t.left(20)
    t.backward(branch_len)

tree(25)

turtle.done()
import shapes

def tall_arrow():
    shapes.triangle()
    shapes.rectangle()
    shapes.rectangle()

def short_arrow():
    shapes.triangle()
    shapes.rectangle()

def tree():
    shapes.triangle()
    shapes.triangle()
    shapes.rectangle()

print('This is a design for a tall arrow')
shapes.line(33)
tall_arrow()
print()
print()
print('This is a design for a short arrow')
shapes.line(34)
short_arrow()



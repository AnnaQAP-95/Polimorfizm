from Rectangl_1 import Rectangle,Square,Circle
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
print(rect_1.get_are(),rect_2.get_are())

sq_1 = Square(5)
sq_2 = Square(10)
print(sq_1.get_area_square(),sq_2.get_area_square())

cl_1 = Circle(2)
cl_2 = Circle(5)
print(cl_1.get_area_circle(),cl_2.get_area_circle())

figures = [rect_1,rect_2,sq_1,sq_2,cl_1,cl_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_are())
























from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle("blue", 12, 12)
    c = Circle("green",12)
    s = Square("red", 12)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
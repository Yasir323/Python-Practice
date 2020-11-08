import math


def AC(radius):
    # Area of a circle
    area = math.pi * radius ** 2
    return area


def AR(length, width):
    # Area of a rectangle or square
    return length * width


def VC(radius, height):
    # Volume of a cylinder
    return math.pi * (radius ** 2) * height


def VR(length, width, height):
    # Volume of a rectangular prism
    return length * width * height


def VS(radius):
    # Volume of a sphere
    return (4 / 3) * math.pi * (radius ** 3)


def SAC(length):
    # Surface area of a cube
    return 6 * (length ** 2)


def SAS(radius):
    # Surface area of a sphere
    return 4 * math.pi * (radius ** 2)


def main():
    infile = open("lab9_input.py", "r")

    # get first calculation type, but wait on dimension(s) because
    # number of dimensions is dependent on the type of shape
    type = (infile.readline()).strip()

    while(type != "###"):
        if (type == "AC"):
            # read only one dimension for a circle
            radius = float(infile.readline())
            circleArea = AC(radius)
            print(format("Area of a Circle", "30s"), format(circleArea, "15.2f"))

        if (type == "AR"):
            # read two dimension for a rectangle
            length = float(infile.readline())
            width = float(infile.readline())
            rectArea = AR(length, width)
            print(format("Area of a Rectangle/Square", "30s"), format(rectArea, "15.2f"))

        if (type == "VC"):
            # read two dimensions for a cylinder
            radius = float(infile.readline())
            height = float(infile.readline())
            cylinderVol = VC(radius, height)
            print(format("Volume of a Cylinder", "30s"), format(cylinderVol, "15.2f"))

        if (type == "VR"):
            # read 3 dimensions for a rectangular prism
            length = float(infile.readline())
            width = float(infile.readline())
            height = float(infile.readline())
            cuboidVol = VR(length, width, height)
            print(format("Volume of a Rectangular Prism", "30s"), format(cuboidVol, "15.2f"))

        if (type == "VS"):
            # read only one dimension for a sphere
            radius = float(infile.readline())
            sphereVol = VS(radius)
            print(format("Volume of a Sphere", "30s"), format(sphereVol, "15.2f"))

        if (type == "SAC"):
            # read only one dimension for a cube
            length = float(infile.readline())
            cubeSA = SAC(length)
            print(format("Surface Area of a Cube", "30s"), format(cubeSA, "15.2f"))

        if (type == "SAS"):
            # read only one dimension for a sphere
            radius = float(infile.readline())
            sphereSA = SAS(radius)
            print(format("Surface Area of a Sphere", "30s"), format(sphereSA, "15.2f"))

        # get next calculation type, but wait on dimension(s)
        type = (infile.readline()).strip()

    # close the file when you exit the while loop
    infile.close()
main()

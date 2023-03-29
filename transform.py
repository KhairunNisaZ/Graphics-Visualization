import turtle
import numpy as np

t = turtle.Turtle()
t.speed(0)

def draw_polygon(polygon, color):
    t.penup()
    t.goto(polygon[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for point in polygon[1:]:
        t.goto(point)
    t.goto(polygon[0])
    t.end_fill()

def scale(polygon, x_scaling_factor, y_scaling_factor):
    scaled_polygon = np.array(polygon)
    scaled_polygon[:, 0] *= x_scaling_factor  
    scaled_polygon[:, 1] *= y_scaling_factor  
    return scaled_polygon

def translate(polygon, translation_vector):
    return np.array(polygon) + translation_vector

def rotate(polygon, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return np.dot(rotation_matrix, np.array(polygon).T).T

def shear_x(polygon, shear_factor):
    shear_matrix = np.array([[1, shear_factor], [0, 1]])
    return np.dot(shear_matrix, np.array(polygon).T).T

def shear_y(polygon, shear_factor):
    shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    return np.dot(shear_matrix, np.array(polygon).T).T

def get_polygon_coords(num_sides):
    coords = []
    for i in range(num_sides):
        input_str = input(f"Input koordinat x dan y sisi ke-{i+1} dari {num_sides} (x y): ")
        split_result = input_str.split()
        if len(split_result) == 2:
            x, y = split_result
            coords.append([float(x), float(y)])
        else:
            print("Error: expected 2 values, got", len(split_result))
            # Handle the error condition
    return coords

print ("-----------------------Implementasi Transformasi 2D---------------------------")
num_sides = int(input("Input jumlah sisi yang anda inginkan: "))
polygon_coords_original = get_polygon_coords(num_sides)

draw_polygon(polygon_coords_original, "gray")

while True:
    print ("---------------------------------------------Pilih Transformasi-------------------------------------------------")
    transform = input("Pilih transformasi yang anda inginkan (scale, translate, rotate, shear_x, shear_y) atau 'done' untuk exit: ").lower()
    if transform == "done":
        break
    elif transform == "scale":
        x_scaling_factor = float(input("Input scaling factor untuk X: "))
        y_scaling_factor = float(input("Input scaling factor untuk Y: "))
        polygon_coords = scale(polygon_coords_original, x_scaling_factor, y_scaling_factor)
        draw_polygon(polygon_coords, "light green")
        draw_polygon(polygon_coords_original, "gray")
    elif transform == "translate":
        x, y = input("Input vektor translasi (x y): ").split()
        translation_vector = np.array([float(x), float(y)])
        polygon_coords = translate(polygon_coords_original, translation_vector)
        draw_polygon(polygon_coords, "light blue")
        draw_polygon(polygon_coords_original, "gray")
    elif transform == "rotate":
        angle = np.radians(float(input("Input sudut untuk rotasi (dalam derajat): ")))
        polygon_coords = rotate(polygon_coords_original, angle)
        draw_polygon(polygon_coords, "light yellow")
        draw_polygon(polygon_coords_original, "gray")
    elif transform == "shear_x":
        shear_factor = float(input("Input shear factor: "))
        polygon_coords = shear_x(polygon_coords_original, shear_factor)
        draw_polygon(polygon_coords, "lavender")
        draw_polygon(polygon_coords_original, "gray")
    elif transform == "shear_y":
        shear_factor = float(input("Input shear factor: "))
        polygon_coords = shear_y(polygon_coords_original, shear_factor)
        draw_polygon(polygon_coords, "khaki")
        draw_polygon(polygon_coords_original, "gray")

turtle.done()
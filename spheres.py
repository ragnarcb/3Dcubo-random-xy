from vpython import *

# Velocidade inicial de rotação
rotation_speed_x = 0.5
rotation_speed_y = 1
scene = canvas(width=1920, height=1080)
cor = color.red
def cubo():
    # Cria o cubo
    cubo = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=cor)

    while True:
        # Atualiza a rotação do cubo
        cubo.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        cubo.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))


        rate(100) # pode mudar o valor para controlar a velocidade do loop

def piramide():
    # Cria a pirâmide
    piramide = pyramid(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=cor)

    while True:
        # Atualiza a rotação da pirâmide
        piramide.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        piramide.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))

        # Espera um pequeno intervalo de tempo
        rate(100)

def ring():
    ring_object = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.1, color=cor)


    while True:
        ring_object.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        ring_object.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))
        rate(100)

def sphere_():

    esfera = sphere(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.1, color=cor)

    while True:
        esfera.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        esfera.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))
        rate(100)

def cone_():
    Cone = cone(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.1, color=cor)

    while True:
        Cone.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        Cone.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))
        rate(100)

def cylinderCylinder_():
    Cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.1, color=cor)

    while True:
        Cylinder.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        Cylinder.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))
        rate(100)

def arrow_():
    Arrow = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.1, color=cor)

    while True:
        Arrow.rotate(angle=radians(rotation_speed_x), axis=vector(1, 0, 0))
        Arrow.rotate(angle=radians(rotation_speed_y), axis=vector(0, 1, 0))
        rate(100)

print("1-cubo:\n2-piramide:\n3: ring:\n4-sphere:\n5-cone:")

while True:
    valor = input("digite o valor correspondente a forma desejada:")
    if valor == "1":
        cubo()
    elif valor == "2":
        piramide()
    elif valor == "3":
        ring()
    elif valor == "4":
        sphere_()
    elif valor == "5":
        cone_()
    elif valor == "6":
        cylinderCylinder_()
    elif valor == "7":
        arrow_()
    else:
        print("valor incorreto")


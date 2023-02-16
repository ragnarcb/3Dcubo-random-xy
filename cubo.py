from vpython import *

# Cria o cubo
scene = canvas(width=1920, height=1080)
cubo = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.red)

# Velocidade inicial de rotação
velocidade_x = 0.5
velocidade_y = 1

while True:
    # Atualiza a rotação do cubo
    cubo.rotate(angle=radians(velocidade_x), axis=vector(1, 0, 0))
    cubo.rotate(angle=radians(velocidade_y), axis=vector(0, 1, 0))

    # Espera um pequeno intervalo de tempo
    rate(100) # pode mudar o valor para controlar a velocidade do loop

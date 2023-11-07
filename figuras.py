import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Crear una figura tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordenadas de los vértices del cuadrado en 3D
vertices = np.array([
    [1, 1, 1],
    [1, 2, 1],
    [2, 2, 1],
    [2, 1, 1],
    [1, 1, 2],
    [1, 2, 2],
    [2, 2, 2],
    [2, 1, 2]
])

# Definir las caras del cuadrado
caras = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[0], vertices[3], vertices[7], vertices[4]],
    [vertices[1], vertices[2], vertices[6], vertices[5]]
]

# Crear una colección de caras
cuadrado3d = Poly3DCollection(caras, edgecolor='b', linewidths=1, alpha=0.5)

# Agregar la colección al gráfico
ax.add_collection3d(cuadrado3d)


# Coordenadas de la esfera con radio 0.5 y ubicación en (1, 1, 1)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
radius = 0.5
x = 1 + radius * np.outer(np.cos(u), np.sin(v))
y = 1 + radius * np.outer(np.sin(u), np.sin(v))
z = 1 + radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Trazar la superficie de la esfera
ax.plot_surface(x, y, z, color='b')


# Coordenadas de los vértices del prisma triangular en 3D (nueva posición)
vertices = np.array([
    [1, 1, 2],
    [2, 1, 2],
    [1.5, 1 + np.sqrt(3)/2, 2],
    [1.5, 1 + np.sqrt(3)/6, 2 + np.sqrt(2/3)],
])

# Definir caras del prisma triangular
caras = [[vertices[0], vertices[1], vertices[2]],
         [vertices[0], vertices[1], vertices[3]],
         [vertices[1], vertices[2], vertices[3]],
         [vertices[2], vertices[0], vertices[3]]]

# Graficar las caras del prisma triangular
for cara in caras:
    x, y, z = zip(*cara)
    ax.plot(x + (x[0],), y + (y[0],), z + (z[0],), color='b')


# Coordenadas de los vértices del rectángulo en 3D
vertices = np.array([
    [0, 0, 0],
    [2, 0, 0],
    [2, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [2, 0, 1],
    [2, 1, 1],
    [0, 1, 1]
])

# Definir caras del rectángulo
caras = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[3], vertices[0], vertices[4], vertices[7]],
    [vertices[4], vertices[5], vertices[6], vertices[7]]
]

# Crear una colección de caras
rectangulo3d = Poly3DCollection(caras, edgecolor='b', linewidths=1, alpha=0.5)

# Agregar la colección al gráfico
ax.add_collection3d(rectangulo3d)

# Coordenadas de la dona (toro) más pequeña y en diferentes coordenadas
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
R = 0.5  # Reduz el radio mayor de la dona
r = 0.1  # Reduz el radio menor de la dona
x = 2  # Cambia la coordenada x
y = 2  # Cambia la coordenada y
z = 1  # Cambia la coordenada z
u, v = np.meshgrid(u, v)
x = x + (R + r * np.cos(v)) * np.cos(u)
y = y + (R + r * np.cos(v)) * np.sin(u)
z = z + r * np.sin(v)

# Trazar la superficie de la dona
ax.plot_surface(x, y, z, color='r')


# Coordenadas del cono pequeño
radius = 0.3  # Radio del cono
height = 0.5  # Altura del cono
n_points = 50  # Número de puntos en la base del cono

# Generar las coordenadas del cono
theta = np.linspace(0, 2 * np.pi, n_points)
z = np.linspace(0, height, n_points)
Z, Theta = np.meshgrid(z, theta)
R = radius * (1 - Z / height)  # Radio variable a lo largo de la altura

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Trama la superficie del cono
ax.plot_surface(X, Y, Z, color='g')


# Etiquetas de ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Definir límites de ejes
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_zlim(0, 3)

# Mostrar el gráfico
plt.show()

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


# Coordenadas de la esfera con radio 0.5
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
radius = 0.5
x = radius * np.outer(np.cos(u), np.sin(v))
y = radius * np.outer(np.sin(u), np.sin(v))
z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Trazar la superficie de la esfera
ax.plot_surface(x, y, z, color='r')

# Coordenadas de los vértices del triángulo en 3D
x = [0, 1, 0]
y = [0, 0, 1]
z = [0, 0, 0]

# Conectar los vértices para formar el triángulo
ax.plot(x + [x[0]], y + [y[0]], z + [z[0]], color='g')


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

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

# межі інтегрування
a = 0 # нижня межа
b = 2 # верхня межа
N = 100000  # кількість випадкових точок

# Метод Монте-Карло
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand <= f(x_rand)
monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / N

# Аналітичний розрахунок
analytical_result, error = spi.quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.scatter(x_rand[under_curve], y_rand[under_curve], color='green', s=0.5, alpha=0.5)
ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='red', s=0.5, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Вивід результатів
print(f"Інтеграл (Монте-Карло): {monte_carlo_integral}")
print(f"Інтеграл (quad): {analytical_result} ± {error}")

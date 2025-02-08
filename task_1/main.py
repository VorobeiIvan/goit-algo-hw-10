import pulp

# Завдання 1: Оптимізація виробництва

# Створення змінних для кількості продуктів
lemonade = pulp.LpVariable("lemonade", lowBound=0, cat="Continuous")
juice = pulp.LpVariable("juice", lowBound=0, cat="Continuous")

# Створення проблеми лінійного програмування
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Мета: максимізувати загальну кількість продуктів
prob += lemonade + juice, "Total_Production"

# Обмеження:
prob += 2*lemonade + 1*juice <= 100, "Water_Constraint"
prob += 1*lemonade <= 50, "Sugar_Constraint"
prob += 1*lemonade <= 30, "Lemon_Constraint"
prob += 2*juice <= 40, "Fruit_Puree_Constraint"

# Розв'язок задачі
prob.solve()

# Виведення результатів
print(f"Максимальна кількість Лимонаду: {lemonade.varValue} одиниць")
print(f"Максимальна кількість Фруктового соку: {juice.varValue} одиниць")

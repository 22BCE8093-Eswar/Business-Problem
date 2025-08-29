# Import PuLP library
from pulp import LpMaximize, LpProblem, LpVariable, value

# Create the Linear Programming problem
prob = LpProblem("Product_Mix_Optimization", LpMaximize)

# Decision variables: number of units to produce for each product
xA = LpVariable('Product_A', lowBound=0, cat='Continuous')
xB = LpVariable('Product_B', lowBound=0, cat='Continuous')

# Objective function: Maximize profit
prob += 40*xA + 30*xB, "Total_Profit"

# Constraints
prob += 2*xA + 1*xB <= 100, "Labor_Constraint"
prob += 3*xA + 2*xB <= 120, "Material_Constraint"

# Solve the problem
prob.solve()

# Print the results
print("Status:", prob.status)
print(f"Optimal Production of Product A: {xA.value():.2f} units")
print(f"Optimal Production of Product B: {xB.value():.2f} units")
print(f"Maximum Profit: ${value(prob.objective):.2f}")

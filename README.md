###Business Problem Using Linear Programming (LP)

***Project Overview***

This project demonstrates how to solve a business problem using Linear Programming (LP) in Python with the PuLP library.
The example problem is a Product Mix Optimization, where a factory wants to maximize profit by deciding the optimal number of units to produce for each product while respecting labor and material constraints.

***Problem Description***

A factory produces two products: Product A and Product B.
Each product requires labor hours and raw material:

Product	  Profit per unit ($)	  Labor (hours/unit)	  Material (kg/unit)
A	         40	                   2	                    3
B	         30	                   1	                    2

Available resources:

Labor: 100 hours

Material: 120 kg

Goal: Determine how many units of each product to produce to maximize total profit.

Solution Approach

Define decision variables: Number of units to produce for Product A and Product B.

Define the objective function: Maximize total profit.

Define constraints: Labor and material usage should not exceed available resources.

Solve the LP problem using PuLP.

Interpret the results and gain business insights.

Insights

The factory should produce 30 units of Product A and 40 units of Product B.

Material is fully utilized, but 10 hours of labor remain unused.

Linear Programming provides a structured method to maximize profit while satisfying constraints.

Requirements

Python 3.x

PuLP library

Install PuLP using:

pip install pulp

How to Run

Clone or download the repository.

Open terminal in project directory.

Run the script:

python main.py


View optimal production and maximum profit in the console.

***Author***

Eswar Reddy Boyi
eswarboyi7@gmail.com | https://github.com/22BCE8093-Eswar/Business-Problem
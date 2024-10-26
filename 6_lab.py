import numpy as np

P = np.array([1/2, 1/3, 1/6])

F1 = np.array([
    [2.5, 3.5, 4.0],  
    [4.5, 2.5, 3.0],  
    [3.0, 5.0, 2.0],  
    [5.5, 1.0, 4.0]   
])

F2 = np.array([
    [20, 35, 50],     
    [25, 30, 40],     
    [30, 20, 25],     
    [15, 40, 30]      
])

expected_losses = np.dot(F1, P)
expected_production = np.dot(F2, P)

V1 = 3  
V2 = 1  

combined_scores = V1 * expected_losses - V2 * expected_production

best_solution_index = np.argmin(combined_scores)

print("Очікувані збитки для кожного варіанту рішення:", expected_losses)
print("Очікуваний обсяг виробництва для кожного варіанту рішення:", expected_production)
print("Комбіновані оцінки для кожного варіанту рішення:", combined_scores)
print("Найкраще рішення (варіант):", best_solution_index + 1)

print("\nОбґрунтування вибору:")
print(f"Найкраще рішення - варіант {best_solution_index + 1} з комбінованою оцінкою {combined_scores[best_solution_index]:.2f}.")
print("Це рішення вибране з урахуванням компромісу між мінімальними сподіваними збитками та мінімальним ризиком невикористаних можливостей.")

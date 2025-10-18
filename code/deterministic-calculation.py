import numpy as np
import math
import scipy


n = 100  # total number of people
initial_cases = 3
infection_prob = 0.23 # this is p/100
healing_prob = 0.10 # this is q/100
days = 10

# infection_chance[i] = the chance for a healthy person to get sick if there are i infected people
infection_chance = np.zeros((n + 1), dtype=float)
infection_chance[0] = 0
for i in range(1, n + 1):
    infection_chance[i] = 1 - (1 - infection_prob) ** i

# inf[i][j] = probability of going from i infected to j infected after the morning phase
inf = np.zeros((n + 1, n + 1), dtype=float)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < i:
            inf[i, j] = 0
        else:
            inf[i, j] = scipy.special.comb(n - i, j - i) * (infection_chance[i] ** (j - i)) * ((1 - infection_chance[i]) ** (n - j))

# heal[i][j] = probability of going from i infected to j infected after the evening phase
heal = np.zeros((n + 1, n + 1), dtype=float)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j:
            heal[i, j] = 0
        else:
            heal[i, j] = scipy.special.comb(i, i - j) * (healing_prob ** (i - j)) * ((1 - healing_prob) ** j)

# dp[i][j] = probability of going from i infected to j infected after one full day
dp = np.matmul(inf, heal)

# final[i][j] will be the probability of going from i infected to j infected after 'days' days
final = np.identity(n + 1, dtype=float)
for i in range(1, days + 1):
    final = np.matmul(final, dp)

ans = 0.0
for i in range(0, n + 1):
    ans += i * final[initial_cases][i]
print("Expected value:", ans)  # returns the expected value

# --- Calculation for the required number of simulations ---

expected_value = ans
expected_value_of_square = 0.0

for i in range(0, n + 1):
    expected_value_of_square += i * i * final[initial_cases][i]

variation = expected_value_of_square - (expected_value * expected_value)

accuracy_percentage = 95
epsilon = 0.25

sim_number = ((variation / (epsilon * epsilon)) / (1 - accuracy_percentage / 100)) + 1
sim_number = int(sim_number)

print("Required number of simulations:", sim_number)
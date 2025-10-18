import numpy as np

def simulate_infections(n, initial_cases, infection_prob, healing_prob, days):
    # 1 means sick, 0 means healthy
    status = np.zeros(n, dtype=int)
    # Set the initial infected individuals
    for i in range(initial_cases):
        status[i] = 1
    
    # This implementation has a subtle detail: a person who gets infected on a given day
    # can immediately start infecting others on the same day.
    # We create a temporary array for the next day's status to model interactions happening simultaneously.
    
    for day in range(days):
        # Morning phase: infections
        next_day_status = np.copy(status)
        for i in range(n):
            for j in range(n):
                # An infected person meets a healthy person
                if status[i] == 1 and status[j] == 0:
                   infection_roll = np.random.random() # A random float between 0.0 and 1.0
                   if infection_roll < infection_prob:
                       next_day_status[j] = 1 # The healthy person gets infected
        
        status = next_day_status
        
        # Evening phase: healing
        for i in range(n):
            if status[i] == 1: # Check only sick people
                healing_roll = np.random.random()
                if healing_roll < healing_prob:
                   status[i] = 0 # The person recovers
                   
    # Count the final number of infected people
    final_cases = np.sum(status)
    return final_cases

# The number of simulations can be determined by Chebyshev's inequality to guarantee a certain accuracy.
# Here, it is set to a fixed number for a practical demonstration.
num_simulations = 5000 
total_infected_sum = 0

# The parameters for the simulation runs
n_people = 100
initial_infected = 3
p_infection = 0.23 / (n_people -1) # The probability p in the problem is per encounter. 
                                   # We must divide by (n-1) to get the per-person probability used here.
q_healing = 0.10
z_days = 10

for i in range(num_simulations):
    total_infected_sum += simulate_infections(n_people, initial_infected, p_infection, q_healing, z_days)

# Calculate and print the average number of infected people over all simulations
average_infected = total_infected_sum / num_simulations
print("Monte Carlo Simulation Average:", average_infected)
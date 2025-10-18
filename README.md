# Pandemic Simulator

![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![Libraries](https://img.shields.io/badge/Libraries-NumPy%20%7C%20SciPy%20%7C%20Matplotlib-orange.svg)

A comprehensive simulation and analysis of infectious disease dynamics within a small population. This project implements two distinct approaches: a deterministic theoretical model using matrix algebra to calculate the exact expected value of infected individuals, and a stochastic Monte Carlo simulation to validate the theoretical results empirically.

## Key Features

-   **Theoretical Modeling:** Calculates the precise expected number of infected individuals after a set number of days using probability theory and matrix exponentiation.
-   **Monte Carlo Simulation:** Simulates the day-by-day interactions of individuals based on probabilistic rules for infection and recovery.
-   **Statistical Validation:** Uses Chebyshev's inequality to determine the sufficient number of simulations required to achieve a desired statistical accuracy.
-   **Data Visualization:** Provides a clear visual comparison of the theoretical prediction versus the simulated results, demonstrating the Law of Large Numbers.

## How It Works

The simulation models a town of **N** inhabitants, with **K** initially infected people, over **Z** days. The core parameters are:
-   `p%`: The probability of a healthy person getting infected upon meeting an infected person.
-   `q%`: The probability of an infected person recovering at the end of a day.

### 1. The Theoretical Model (Deterministic)

This model calculates the exact expected value without running any simulations.

1.  **Infection & Healing Matrices:** Two transition matrices are constructed:
    -   An **Infection Matrix (`inf`)**: `inf[i][j]` stores the probability of going from `i` infected people in the morning to `j` by noon.
    -   A **Healing Matrix (`heal`)**: `heal[i][j]` stores the probability of going from `i` infected people at noon to `j` by evening.
2.  **Daily Transition Matrix:** These matrices are multiplied (`dp = inf * heal`) to create a single-day transition matrix. `dp[i][j]` represents the probability of starting a day with `i` infected and ending with `j`.
3.  **Multi-Day Projection:** This daily matrix is raised to the power of **Z** days (`final = dp**Z`). The resulting matrix `final[i][j]` gives the probability of having `j` infected people after `Z` days, given an initial count of `i`.
4.  **Expected Value:** The final expected value is calculated by summing `j * final[K][j]` for all possible `j`.

### 2. The Monte Carlo Simulation (Stochastic)

This model simulates the pandemic directly to approximate the expected value.

1.  **Required Runs (`R`):** The theoretical model is first used to calculate the variance of the outcome. This variance, along with a desired error margin (`epsilon`) and confidence level, is plugged into a formula derived from **Chebyshev's inequality** to determine the necessary number of simulations (`R`) for a statistically significant result.
2.  **Simulation Loop:** For each of the `R` simulations:
    - A population vector is initialized.
    - For each of the `Z` days:
        - Every pair of individuals meets, and infections are simulated based on probability `p`.
        - At the end of the day, recoveries are simulated for each sick person based on probability `q`.
3.  **Final Result:** The average number of infected people across all `R` simulations is calculated. This average converges to the theoretical expected value.

## Results and Validation

The model's robustness is confirmed by comparing the output of the Monte Carlo simulation with the value predicted by the theoretical model. As the number of simulations increases, the running average of the simulation results converges precisely to the deterministic expected value.

![Simulation Convergence and Distribution](path/to/your/simulation_results.png)
*Left: The running average of infected cases converges to the theoretical expected value. Right: A histogram showing the frequency distribution of outcomes across all simulations.*

## Technology Stack

-   **Language:** Python
-   **Numerical Computation:** NumPy, SciPy (specifically for binomial coefficients)
-   **Data Visualization:** Matplotlib

## Setup and Usage

**1. Prerequisites:**
-   Python 3.x
-   Pip

**2. Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**3. Install dependencies:**
*(Note: Please create a `requirements.txt` file for a professional project. You can generate one with `pip freeze > requirements.txt`)*
```bash
pip install numpy scipy matplotlib
```

**4. Run the simulation:**
*(You can create a `main.py` script that takes command-line arguments for the parameters)*
```bash
python main.py --population 100 --infected 10 --days 30 --infection-prob 5 --recovery-prob 10
```

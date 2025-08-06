
# Genetic Algorithm for Solving the Travelling Salesman Problem (TSP)

## A Python-based heuristic optimization tool for finding efficient solutions to the classic NP-hard TSP

---

### Introduction

This project implements a **Genetic Algorithm (GA)** to solve the **Travelling Salesman Problem (TSP)** — a well-known NP-hard problem in combinatorial optimization. Given a set of cities and their coordinates, the goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

The genetic algorithm uses a population-based approach with crossover, mutation, selection, and elitism to evolve high-quality solutions over multiple generations. It is written in Python and designed to be both **educational** and **extensible**, making it useful for both students and researchers.

---

### Features

* Flexible parameter tuning via configuration file
* Two crossover methods: PMX (Partially Mapped) and OX1 (Order Crossover)
* Tournament and roulette wheel selection strategies
* Displacement mutation
* Elitism and stagnation handling through population reset
* Modular code structure with reusable components

---

## Installation and Usage (For End Users)

### 1. Requirements

* Python 3.7+

### 2. Prepare Input

Create a `.txt` file containing the city coordinates in the following format:

```
CityID x  y
0      22 45
1      41 65
...
```

### 3. Run the Algorithm

Edit `params.py` to customize parameters like population size, mutation rate, and number of generations.

Then run:

```
python3 main.py
```

Results will be printed to the console.

---

## 🛠️ Development & Contribution Guide (For Contributors)

If you’re interested in improving or extending the project, follow these steps:

### 1. Clone the Repository

```
git clone https://github.com/aleksa2105/traveling-salesman-problem
cd traveling-salesman-problem
```

### 2. Project Structure

```
.
├── main.py                 # Entry point
├── params.py               # Algorithm parameters
├── chromosome.py           # Chromosome representation
├── population.py           # Population and evolution logic
├── selection.py            # Selection strategies
├── crossover.py            # PMX and OX1 crossover operators
├── genome.py               # Genome functions
├── utils.py                # Utility functions
└── README.md               # Project documentation
```

### 3. Run in Dev Mode

Use `main.py` for quick testing, or write new scripts/tests under a `benchmark/` folder. Pull requests are welcome!

---

## 📝 Example Parameters (`params.py`)

```python
FILE_NAME = "data/data_tsp.txt"
NUM_GENERATIONS = 2000
POPULATION_SIZE = 520
TOURNAMENT_SELECTION_SIZE = 5
MUTATION_CHANCE = 0.3
ELITISM_RATE = 0.02
RESET_RATE = 0.1
CHROMOSOME_MAX_AGE = 30
```

---

## ✅ Results

In multiple test scenarios, the algorithm consistently converges to high-quality solutions. The population reset mechanism and chromosome aging help prevent premature convergence, while the ability to switch between crossover and selection strategies supports experimentation and optimization.

---

## 📚 References

* Ü. Çölük – *TSP: New Genetic Representations and Operators*, Middle East Technical University
  [PDF](https://user.ceng.metu.edu.tr/~ucoluk/research/publications/tspnew.pdf)

* P. Larrañaga, J.A. Lozano – *Genetic Algorithms for the Travelling Salesman Problem: A Review of Representations and Operators*, 2002
  [ResearchGate](https://www.researchgate.net/publication/226665831)

---

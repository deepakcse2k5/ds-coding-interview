import random

def six_sided_die():
    """Simulates rolling a fair six-sided die."""
    return random.randint(1, 6)

def seven_sided_die():
    """Simulates rolling a fair seven-sided die using two six-sided dice."""
    results = {
        (1, 1): 1,
        (1, 2): 2,
        (1, 3): 3,
        (1, 4): 4,
        (1, 5): 5,
        (1, 6): 6,
        (2, 1): 7
    }
    while True:
        o1 = six_sided_die()
        o2 = six_sided_die()
        if (o1, o2) in results:
            return results[(o1, o2)]
        # else: keep looping until a valid pair occurs

def run_simulation(trials, seed=123):
    """Runs the simulation for the specified number of trials."""
    random.seed(seed)
    counts = [0] * 7
    for _ in range(trials):
        outcome = seven_sided_die()
        counts[outcome - 1] += 1
    return counts

def print_proportions(counts, trials):
    """Prints the proportion of each outcome rounded to 3 decimal places."""
    proportions = [round(c / trials, 3) for c in counts]
    print(proportions)

def main():
    trials = 10000
    counts = run_simulation(trials)
    print_proportions(counts, trials)

if __name__ == "__main__":
    main()

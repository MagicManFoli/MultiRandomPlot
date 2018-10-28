import random
import time
import matplotlib.pyplot as plt


def plot(results):
    plt.plot(results)
    plt.ylabel("Value")
    plt.xlabel("Try")
    plt.show()


def get_random():
    max_deviation = 0.05

    random_number = random.uniform(1 - max_deviation, 1 + max_deviation)
    return random_number


def main():
    n_tries = 1000
    n_iterations = 100

    print("Starting up")
    t_start = time.perf_counter()

    results = []

    for i_try in range(n_tries):
        curr_value = 1
        for i_iteration in range(n_iterations):
            curr_value *= get_random()
        results.append(curr_value)

    print(f"Took {time.perf_counter() - t_start:2.5} seconds")
    print("Showing results")
    # print(results)
    print(f"Min: {min(results)}, Avg: {sum(results) / len(results)}, Max: {max(results)}")
    plot(results)

    print("Done")


if __name__ == '__main__':
    main()

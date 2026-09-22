import random
 
 
def binary_search_count(numbers, x):
    low = 0
    high = len(numbers) - 1
    iterations = 0
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if numbers[mid] == x:
            return iterations
        elif numbers[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return iterations
 
def main():
    size = 1000
    numbers = sorted(random.sample(range(1, 1000000), size))
 
    trials = 1000
    results = []
 
    for i in range(trials):
        target = random.choice(numbers)
        count = binary_search_count(numbers, target)
        results.append(count)
 
    best_case = min(results)
    worst_case = max(results)
    average_case = sum(results) / len(results)
 
    print(f"List size: {size}")
    print(f"Number of trials: {trials}")
    print(f"Best case (fewest iterations): {best_case}")
    print(f"Worst case (most iterations): {worst_case}")
    print(f"Average number of iterations: {average_case:.2f}")
 
 
if __name__ == "__main__":
    main()
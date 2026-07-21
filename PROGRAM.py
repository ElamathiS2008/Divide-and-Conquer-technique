# PROGRAM.py

comparison_count = 0


# Divide and Conquer Method
def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: Single element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    # Find min and max in left half
    lmin, lmax = min_max_dc(arr, low, mid)

    # Find min and max in right half
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Compare minimum values
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    # Compare maximum values
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


# Naive Method
def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]

    comparisons = 0

    for x in arr[1:]:

        # Compare with minimum
        comparisons += 1

        if x < mn:
            mn = x

        # Compare with maximum
        comparisons += 1

        if x > mx:
            mx = x

    return mn, mx, comparisons


# Run Divide and Conquer
def run_divide_conquer(arr):
    global comparison_count

    comparison_count = 0

    minimum, maximum = min_max_dc(
        arr,
        0,
        len(arr) - 1
    )

    return minimum, maximum, comparison_count


# Run Naive Method
def run_naive(arr):
    minimum, maximum, comparisons = min_max_naive(arr)

    return minimum, maximum, comparisons


# Optimal Comparison Formula
def optimal_formula(n):

    if n % 2 == 0:
        # For even n
        return (3 * n // 2) - 2

    else:
        # For odd n
        return (3 * (n - 1) // 2) + 1

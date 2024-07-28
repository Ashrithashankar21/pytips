def evaluate_conditions(a: bool, b: bool, c: bool) -> bool:
    # Count the number of True values
    true_count = sum([a, b, c])

    # Return True if at least two are True
    return true_count >= 2


if __name__ == "__main__":
    result = evaluate_conditions(True, False, True)
    print(result)

    result = evaluate_conditions(True, False, False)
    print(result)

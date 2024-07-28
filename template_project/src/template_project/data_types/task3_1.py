def classify_number(number: int) -> str:
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    classification = classify_number(number)
    print(f"The number is {classification}")

def expression_evaluator(expression: str) -> float:
    try:
        result = eval(expression)
        # Step 4: Return the calculated result of the expression
        return result
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        # Handle potential parsing errors for invalid inputs
        return f"Error: {str(e)}"
    except Exception as e:
        # Handle any other unexpected exceptions
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print(expression_evaluator("3 + 5 * 2 - 8 / 4"))
    print(expression_evaluator("(3 + 5) * (2 - 8) / 4"))
    print(expression_evaluator("2 / 0"))

def safe_division(a, b):
    try:
        result = a / b
        assert result >= 0, "Result is negative"
        return result
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    finally:
        print("Division operation completed")

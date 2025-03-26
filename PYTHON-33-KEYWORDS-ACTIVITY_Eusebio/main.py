from calculator_class import Calculator
from loop_controls import demonstrate_loops
from exception_handling import safe_division
from scope_variables import outer_function
from logical_operations import logical_operations
from advanced_features import generate_timestamps, square

def main():
 
    calc = Calculator(5)
    print(f"Calculator add: {calc.add(3)}")
    print(f"Is positive: {calc.is_positive()}")


    print("\nTesting loops:")
    demonstrate_loops()

  
    print("\nTesting division:")
    safe_division(10, 2)


    print("\nLogical operations:")
    print(logical_operations(True, False))

    print("\nSquare of 5:", square(5))
    

    print("\nGenerating timestamps:")
    gen = generate_timestamps()
    for _ in range(3):  
        print(next(gen))

if __name__ == "__main__":
    main()
def check_number():
    try:
        num = float(input("Enter a number: "))
        if num > 7:
            print("Hello")
    except ValueError:
        print("Invalid number entered.")

def check_name():
    name = input("Enter a name: ")
    if name.strip().lower() == "john":
        print("Hello, John")
    else:
        print("There is no such name")

def check_multiples_of_three():
    raw_input = input("Enter numbers separated by spaces (e.g., 1 3 6 7 9): ")
    try:
        numbers = [float(x) for x in raw_input.strip().split()]
        multiples = [str(x) for x in numbers if x % 3 == 0]
        
        if multiples:
            print("Elements that are multiples of 3:", ", ".join(multiples))
        else:
            print("No multiples of 3 found.")
    except ValueError:
        print("Please enter valid numbers only.")

def main():
    print("=== Task 1: Number Check ===")
    check_number()
    
    print("\n=== Task 2: Name Check ===")
    check_name()
    
    print("\n=== Task 3: Multiples of 3 ===")
    check_multiples_of_three()

if __name__ == "__main__":
    main()

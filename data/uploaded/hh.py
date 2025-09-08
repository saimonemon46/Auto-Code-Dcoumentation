import math

class BigCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return "Error: Division by zero" if b == 0 else a / b
    def modulus(self, a, b): return a % b

    # Advanced
    def power(self, a, b): return math.pow(a, b)
    def sqrt(self, a): return math.sqrt(a)
    def log(self, a, base=10): return math.log(a, base)
    def ln(self, a): return math.log(a)
    def exp(self, a): return math.exp(a)

    # Trigonometry
    def sin(self, angle): return math.sin(math.radians(angle))
    def cos(self, angle): return math.cos(math.radians(angle))
    def tan(self, angle): return math.tan(math.radians(angle))

    # Memory
    def memory_store(self, value): self.memory = value
    def memory_recall(self): return self.memory
    def memory_clear(self): self.memory = 0


def main():
    calc = BigCalculator()

    menu = """
    ==== BIG CALCULATOR ====
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Power (x^y)
    7. Square Root
    8. Logarithm (base 10)
    9. Natural Log (ln)
    10. Exponential (e^x)
    11. Sine (degrees)
    12. Cosine (degrees)
    13. Tangent (degrees)
    14. Memory Store
    15. Memory Recall
    16. Memory Clear
    0. Exit
    ========================
    """

    while True:
        print(menu)
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Enter a number from 0-16.")
            continue

        if choice == 0:
            print("Exiting... Goodbye!")
            break

        elif choice in [1, 2, 3, 4, 5, 6]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == 1: print("Result:", calc.add(a, b))
            elif choice == 2: print("Result:", calc.subtract(a, b))
            elif choice == 3: print("Result:", calc.multiply(a, b))
            elif choice == 4: print("Result:", calc.divide(a, b))
            elif choice == 5: print("Result:", calc.modulus(a, b))
            elif choice == 6: print("Result:", calc.power(a, b))

        elif choice == 7:
            a = float(input("Enter number: "))
            print("Result:", calc.sqrt(a))

        elif choice == 8:
            a = float(input("Enter number: "))
            print("Result:", calc.log(a))

        elif choice == 9:
            a = float(input("Enter number: "))
            print("Result:", calc.ln(a))

        elif choice == 10:
            a = float(input("Enter number: "))
            print("Result:", calc.exp(a))

        elif choice in [11, 12, 13]:
            angle = float(input("Enter angle (degrees): "))
            if choice == 11: print("Result:", calc.sin(angle))
            elif choice == 12: print("Result:", calc.cos(angle))
            elif choice == 13: print("Result:", calc.tan(angle))

        elif choice == 14:
            val = float(input("Enter value to store in memory: "))
            calc.memory_store(val)
            print("Stored in memory.")

        elif choice == 15:
            print("Memory Recall:", calc.memory_recall())

        elif choice == 16:
            calc.memory_clear()
            print("Memory Cleared.")

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

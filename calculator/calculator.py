class Calculator:
    """
    Basic calculator app that can add, subtract, multiply,
    divide, take (n) root from a number.

    Methods:
        value: returns current value in memory
        reset_value: resets current value in memory to 0
        add: adds a given number to the current value in memory
        subtract: subtracts given number from the current value in memory
        multiply: multiplies the current value in memory by the given number
        divide: divides the current value in memory by the given number
        n_root: takes nth root from the current value in memory
    """

    def __init__(self, value: float = 0) -> None:
        """
        Initialization function that sets an initial memory value to be 0

        :param value: float Sets memory value, default: 0
        :raise ValueError: if value is not float or int:
        """
        if not isinstance(value, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value = value

    @property
    def value(self) -> float:
        """
        Returns the current memory value
        :return: Current memory value float
        """
        return self.__value

    @value.setter
    def value(self, new_value: float) -> None:
        """
        Memory value getter method
        :param new_value: A new number for the memory value float
        :raise: ValueError if new_value not int or float
        """
        if not isinstance(new_value, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value = new_value

    def reset_value(self) -> None:
        """
        Resets the memory value to the initial equal to 0
        """
        self.__value = 0

    def add(self, a: float) -> float:
        """
        Method adds number to the current memory value and returns the result
        :param a: number to be added int or float
        :raise: ValueError if param a not int or float
        :return: Sum of memory value and param a float
        """
        if not isinstance(a, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value += a
        return self.__value

    def subtract(self, a: float) -> float:
        """
        Method subtracts number from the current memory value and returns the result
        :param a: number to be subtracted int or float
        :raise: ValueError if param a not int or float
        :return: Subtraction of memory value and param a float
        """
        if not isinstance(a, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value -= a
        return self.__value

    def multiply(self, a: float) -> float:
        """
        Method multiplies current memory value by param a and returns the result
        :param a: multiplier int or float
        :raise: ValueError if param a not int or float
        :return: Multiplication result of memory value and param a float
        """
        if not isinstance(a, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value *= a
        return self.__value

    def divide(self, a: float) -> float:
        """
        Method divides current memory value by param a and returns the result
        :param a: divisor int or float
        :raise: ValueError if param a not int or float
        :return: Division result of memory value and param a float
        """
        if not isinstance(a, (int, float)):
            raise ValueError('An int or float must be entered!')
        if a == 0:
            raise ZeroDivisionError('You cannot divide by zero!')
        self.__value /= a
        return self.__value

    def n_root(self, n: float) -> float:
        """
        Method takes param n root of the current memory value returns the result
        :param n: root number int or float
        :raise: ValueError if param n not int or float
        :return: n root of current memory value float
        """
        if not isinstance(n, (int, float)):
            raise ValueError('An int or float must be entered!')
        self.__value = self.__value ** (1/n)
        return self.__value


if __name__ == "__main__":
    print("Calculator is starting...")
    calculator = Calculator()
    print("Calculator has started. Initial value:", calculator.value)

    while True:
        try:
            # Prompt for command
            print("Enter command (add, subtract, multiply, divide, root, reset, exit): ", end='', flush=True)
            command = input().strip().lower()

            if command == "exit":
                break
            elif command in ("add", "subtract", "multiply", "divide", "root"):
                print("Enter number: ", end='', flush=True)
                num = float(input().strip())

                if command == "add":
                    result = calculator.add(num)
                elif command == "subtract":
                    result = calculator.subtract(num)
                elif command == "multiply":
                    result = calculator.multiply(num)
                elif command == "divide":
                    result = calculator.divide(num)
                elif command == "root":
                    result = calculator.n_root(num)
                print(f"Result: {result}")
            elif command == "reset":
                calculator.reset_value()
                print("Value reset to 0")
            else:
                print("Unknown command")
        except EOFError:
            print("EOF Error: Exiting")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

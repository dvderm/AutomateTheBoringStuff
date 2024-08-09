# Wordt gebruikt in AutomateBoring.ipynb
def some_function():
    return "Hello from the function!"

print(f"The value of __name__ is: {__name__}")

if __name__ == '__main__':
    print("This script is being run directly")
    print(some_function())
else:
    print("This script is being imported as a module")
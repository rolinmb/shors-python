from shors import *

if __name__ == "__main__":
    print("Factoring 15...")
    for _ in range(10):
        result = shor(15)
        if result:
            print("Found factor:", result)
            break
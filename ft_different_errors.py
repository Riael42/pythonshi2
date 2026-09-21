def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        with open("/non/existent/file", "r") as f:
            f.read()
    elif operation_number == 3:
        "hello" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

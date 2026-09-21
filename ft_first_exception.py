def ft_first_exception(temp_str: str) -> int:
    try:
        val = int(temp_str)
        return (val)
    except ValueError:
        raise ValueError("Invalid int base 10: " + temp_str)


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        result = ft_first_exception("25")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"Error: {err_msg}")
    print("Input data is 'abc'")
    try:
        ft_first_exception("abc")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"Error: {err_msg}")


if __name__ == "__main__":
    test_temperature()

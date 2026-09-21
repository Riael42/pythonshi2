def ft_first_exception(temp_str: str) -> int:
    try:
        val = int(temp_str)
    except ValueError:
        raise ValueError("Invalid int base 10: " + temp_str)
    if val < 0:   # this is so damn ugly thank you python
        raise ValueError(
            f"{val} degrees C is too cold for plants! (min 0 degrees C)")
    if val > 40:
        raise ValueError(
            f"{val} degrees C is too hot for plants! (max 40 degrees C)")
    return val


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        result = ft_first_exception("25")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"input_temperature Error: {err_msg}")
    print("Input data is 'abc'")
    try:
        ft_first_exception("abc")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"input_temperature Error: {err_msg}")
    print("Input data is '100'")
    try:
        result = ft_first_exception("100")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"input_temperature Error: {err_msg}")
    print("Input data is '-100'")
    try:
        result = ft_first_exception("-100")
        print(f"Temp is now: {result}")
    except ValueError as err_msg:
        print(f"input_temperature Error: {err_msg}")


if __name__ == "__main__":
    test_temperature()

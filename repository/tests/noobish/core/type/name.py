from noobish.core import type_name


def test_type_name():
    # Standard Assertion Test
    assert type_name("") == "str"
    assert type_name(5) == "int"
    assert type_name(5.5) == "float"
    assert type_name(lambda: 0) == "function"
    assert type_name(True) == "bool"
    assert type_name(False) == "bool"
    assert type_name({}) == "dict"
    assert type_name({"fruit": "apple"}) == "dict"

    # Normal function is considered as function
    def example():
        return None

    assert type_name(example) == "function"

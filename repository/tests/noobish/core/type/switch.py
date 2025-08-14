from noobish.core import type_switch

def test_what():
    print(type("test"))

def test_type_switch():
    # Building Type Switch
    result = type_switch("string",{
        "str": lambda: "string",
        "int": lambda: "integer",
    })

    # Testing if result is equal to string
    assert result == "string"
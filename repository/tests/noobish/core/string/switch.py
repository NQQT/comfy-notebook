from noobish.core import string_switch


def test_default_string():
    def default_callback():
        return "works"

    # Initialisation
    value = string_switch("404", {
        "default": default_callback
    })

    # Checking if the same
    assert value == "works"

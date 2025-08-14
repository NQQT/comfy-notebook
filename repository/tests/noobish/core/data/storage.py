from noobish.core import data_storage


def test_default_storage():
    # Initialisation
    variables = data_storage()

    # Checking if the same
    assert variables() == {}


def test_initialised_storage():
    # Initialisation
    variables = data_storage({
        "fruit": "banana"
    })

    # Checking if the same
    assert variables() == {
        "fruit": "banana"
    }


def test_accessing_storage():
    # Initialisation
    variables = data_storage({
        "fruit": "banana",
        "animal": "cat",
        "person": "james",
        "family": {
            "father": "john",
            "mother": "jane"
        }
    })

    # For Accessing Fruits
    assert variables("fruit") == "banana"
    # Accessing invalid field returns a new dictionary
    assert variables("colour") == {}

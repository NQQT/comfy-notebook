# For testing dictionary merging function
from noobish.core import dict_merge


def test_dict_merge():
    example1 = {"fruit": "apple"}
    example2 = {"colour": "blue"}
    example3 = {"family": {
        "father": "john",
        "mother": "jane",
        "children": {
            "son": "jack",
            "daughter": "jill"
        }
    }}
    example4 = {"family": {
        "father": "john",
        "mother": "jane",
        "pet": "dog"
    }}

    # The resulting merge should be correct
    assert dict_merge(example1, example2) == {
        "fruit": "apple",
        "colour": "blue",
    }

    # Nest merges
    assert dict_merge(example2, example3) == {
        "colour": "blue",
        "family": {
            "father": "john",
            "mother": "jane",
            "children": {
                "son": "jack",
                "daughter": "jill"
            }
        }
    }

    # Recursive nest merging
    assert dict_merge(example3, example4) == {
        "family": {
            "father": "john",
            "mother": "jane",
            "children": {
                "son": "jack",
                "daughter": "jill"
            },
            "pet": "dog"
        }
    }

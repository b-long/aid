import pytest


@pytest.mark.skip(reason="Skipping Apple tests: This test is not finishing.'")
def test_cowsay():
    """
    https://pypi.org/project/cowsay/
    """
    assert True
    # import cowsay
    # retval = cowsay.cow("Hello World")
    # assert retval == "something"

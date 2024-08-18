# Test layouts: https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout
from my_project.main import my_function


def test_my_function():
    assert my_function(10, 2) == 12

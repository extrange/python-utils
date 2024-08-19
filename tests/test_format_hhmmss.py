# Test layouts: https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout
from python_utils.format_hhmmss import format_hhmmss


def test_format():
    assert format_hhmmss(100) == "0:01:40"

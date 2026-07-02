import pytest
import sys

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="not supported on Windows"
)
def test_linux_only():
    assert True
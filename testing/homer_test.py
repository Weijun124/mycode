#!/usr/bin/python3
"""Alta3 Research | Building functions to test"""

def homer(name="abc"):
    return f"You don't {name}"
def test_homer():
    assert homer("cba")=="You don't cba"

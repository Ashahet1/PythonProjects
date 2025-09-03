import pytest
def test_fail_case_pdb():
    x=5
    y=10
    import pdb; pdb.set_trace() # debugging starts here if test fails
    assert x+y == 20 # This will fail (expected is 15 and not 20)
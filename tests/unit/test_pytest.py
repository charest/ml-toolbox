# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x


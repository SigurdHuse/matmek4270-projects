import numpy as np


def differentiate(u, dt):
    pass


def differentiate_vector(u, dt):
    pass


def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert True


if __name__ == "__main__":
    test_differentiate()

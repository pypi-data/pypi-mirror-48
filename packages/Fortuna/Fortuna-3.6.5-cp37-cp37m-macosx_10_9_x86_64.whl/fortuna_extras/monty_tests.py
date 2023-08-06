from Fortuna import *


def monty_tests():
    print("\nQuantum Monty Methods:\n")
    monty = QuantumMonty(range(10))

    distribution_timer(monty.flat_uniform)
    distribution_timer(monty.front_linear)
    distribution_timer(monty.middle_linear)
    distribution_timer(monty.back_linear)
    distribution_timer(monty.quantum_linear)
    distribution_timer(monty.front_gauss)
    distribution_timer(monty.middle_gauss)
    distribution_timer(monty.back_gauss)
    distribution_timer(monty.quantum_gauss)
    distribution_timer(monty.front_poisson)
    distribution_timer(monty.middle_poisson)
    distribution_timer(monty.back_poisson)
    distribution_timer(monty.quantum_poisson)
    distribution_timer(monty.quantum_monty)


if __name__ == "__main__":
    monty_tests()

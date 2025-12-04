from alle_effect import AlleeEffect as AE
model = AE(0.03, 9000, 1000)
model.plot_evolutions(list(range(0, 10000, 100)), 100, 0.1)
from predator_prey import PredatorPrey as PP

model = PP(0.16, 2400, 5, 1000, 0.01, 2)
model.plot_evolution(120, 40, 1000)
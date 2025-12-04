import matplotlib.pyplot as plt


class PredatorPrey:
    def __init__(self, r, K, a, D, s, m):
        self.r = r
        self.K = K
        self.a = a
        self.D = D
        self.s = s
        self.m = m
        
    def __str__(self):
        return f'r = {self.r}, K = {self.K}, a = {self.a}, D = {self.D}, s = {self.s} and m = {self.m}'
    
    def update(self, N, P):
        self.N = N
        self.P = P

        delta_N = self.r * self.N * (1 - (self.N / self.K)) - self.a * self.P * (self.N / (self.N + self.D))

        delta_P = self.s * self.P * (1 - (self.m * self.P) / self.N)

        return (self.N + delta_N), (self.P + delta_P)
    

    def plot_evolution(self, N, P, ita):
        plot_values_N = []
        plot_values_P = []

        for  i in range(ita):
            N, P = model.update(N, P)

            plot_values_N.append(N)
            plot_values_P.append(P) 

        #     plt.plot(i, N, 'r.')
        #     plt.plot(i, P, 'b.')
        # plt.show()
        
        plt.plot(plot_values_N, plot_values_P)
        plt.show()

          
model = PredatorPrey(0.16, 2400, 5, 1000, 0.01, 2)

model.plot_evolution(120, 40, 1000)




import matplotlib.pyplot as plt

class AlleeEffect:

    def __init__(self, r, K, A):
        self.r = r
        self.K = K
        self.A = A
    
    def __str__(self):
        return f'r = {self.r}, K = {self.K} and A = {self.A}'
    
    def update(self, N, t):
        self.N = N
        self.t = t

        delta_N = self.r * self.N * (1 - (self.N / self.K)) * ((self.N / self.A) - 1)

        return (self.N + (self.t * delta_N))
    
    def evolve(self, N, L, dt):
    
        time_list = [0]
        population_list = [N]

        while time_list[-1] < L:    # Mens det sidst index i tiden ikke har nået længden endnu
            current_time = time_list[-1] + dt
            time_list.append(current_time)
            current_population = self.update(population_list[-1], dt)
            population_list.append(current_population)
    
        return time_list, population_list
    
    def plot_evolutions(self, init_populations, L, dt):
        #plt.figure(figsize=(10, 8))
        
        for N in init_populations:

            time_list, population_list = self.evolve(N, L, dt)
            plt.plot(time_list, population_list)
        
        # plt.xlabel('Time')
        # plt.ylabel('Population Size')
        # plt.title(f'Allee Effect Dynamics\n{self.__str__()}, dt={dt}')
        # plt.ylim(0, self.K)  # Begræns y-aksen til bærekapaciteten
        # plt.grid(alpha=0.3)  # Tilføj et let grid for bedre læsbarhed
        plt.show()


           
model = AlleeEffect(0.03, 9000, 1000)

model.plot_evolutions(list(range(0, 10000, 100)), 100, 0.1)       

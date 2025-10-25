import matplotlib.pyplot as plt
import numpy as np

from tsp import (
    create_population,
    calculate_distance,
    generate_children
)


class EvolutionaryAlgorithm:
    def __init__(self, cities, μ=50, λ=100, mutation_rate=0.05, generations=1000):
        """
        Initialisiert den evolutionären Algorithmus.
        
        Args:
            cities: Liste von Städten als (x,y)-Tupel
            μ: Anzahl der Eltern
            λ: Anzahl der Kinder
            mutation_rate: Mutationswahrscheinlichkeit
            generations: Anzahl der Generationen
        """
        self.cities = cities
        self.μ = μ
        self.λ = λ
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population_size = μ + λ
        self.best_distances = []
        self.avg_distances = []
        self.best_solution = None
        self.best_distance = float('inf')
    
    def run(self):
        """
        Führt den evolutionären Algorithmus aus.
        """
        # Erstelle initiale Population
        print(f"Starte EA mit μ={self.μ}, λ={self.λ}, Mutationsrate={self.mutation_rate}")
        population = create_population(self.population_size, len(self.cities))
        
        # Berechne initiale Fitness
        distances = [calculate_distance(self.cities, tour) for tour in population]
        
        # Hauptschleife des EA
        for generation in range(self.generations):
            # Generiere Kinder
            children = generate_children(population, self.cities, self.μ, self.λ, self.mutation_rate)
            
            # Vereinige Eltern und Kinder
            combined = population + children
            
            # Bewerte alle Individuen
            distances = [calculate_distance(self.cities, tour) for tour in combined]
            
            # (μ + λ) Selektion: Behalte die besten μ + λ Individuen
            indices = np.argsort(distances)[:self.population_size]
            population = [combined[i] for i in indices]
            distances = [distances[i] for i in indices]
            
            # Statistiken aktualisieren
            current_best = min(distances)
            avg_distance = sum(distances) / len(distances)
            self.best_distances.append(current_best)
            self.avg_distances.append(avg_distance)
            
            # Beste Lösung aktualisieren
            if current_best < self.best_distance:
                best_idx = distances.index(current_best)
                self.best_solution = population[best_idx]
                self.best_distance = current_best
            
            # Fortschritt alle 50 Generationen ausgeben
            if generation % 50 == 0 or generation == self.generations - 1:
                print(f"Generation {generation}: Beste Distanz = {current_best:.2f}, Durchschnittliche Distanz = {avg_distance:.2f}")
        
        return self.best_solution, self.best_distance
    
    def plot_progress(self):
        """
        Zeigt den Fortschritt des Algorithmus grafisch an.
        """
        plt.figure(figsize=(12, 8))
        
        # Konvergenzplot
        plt.subplot(2, 1, 1)
        plt.plot(self.best_distances, 'r-', label='Beste Distanz')
        plt.plot(self.avg_distances, 'b-', label='Durchschnittliche Distanz')
        plt.xlabel('Generation')
        plt.ylabel('Distanz')
        plt.title('Konvergenz des Evolutionären Algorithmus')
        plt.legend()
        plt.grid(True)
        
        # Beste Tour visualisieren
        if self.best_solution:
            plt.subplot(2, 1, 2)
            x = [self.cities[city][0] for city in self.best_solution]
            y = [self.cities[city][1] for city in self.best_solution]
            
            # Füge den Start/Zielpunkt am Ende hinzu, um den Kreis zu schließen
            x.append(x[0])
            y.append(y[0])
            
            plt.plot(x, y, 'b-', linewidth=0.8)
            plt.plot(x, y, 'ro', markersize=4)
            plt.xlabel('X-Koordinate')
            plt.ylabel('Y-Koordinate')
            plt.title(f'Beste Tour (Distanz: {self.best_distance:.2f})')
            plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def run_and_plot(self):
        """
        Führt den Algorithmus aus und zeigt die Ergebnisse an.
        """
        self.run()
        self.plot_progress()
        return self.best_solution, self.best_distance





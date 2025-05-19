from filesanddata import filesandata
from evolutionary_algorithm_visualization import EvolutionaryAlgorithm
import time

def main():
    # Lade die TSP-Instanzen
    kroA100 = "kroA100.tsp"
    kroB100 = "kroB100.tsp"
    
    print("Lade Testinstanzen...")
    city_a = filesandata(kroA100)
    city_b = filesandata(kroB100)
    
    print(f"kroA100: {len(city_a.citys)} Städte")
    print(f"kroB100: {len(city_b.citys)} Städte")
    
    # Teste verschiedene Parameter
    parameter_sets = [
        # μ, λ, Mutationsrate, Generationen
        (50, 100, 0.05, 500),   # Standard
        (20, 40, 0.1, 500),     # Höhere Mutationsrate
        (100, 200, 0.01, 500),  # Größere Population, niedrigere Mutationsrate
    ]
    
    # Teste verschiedene Parameter für kroA100
    print("\n--- Tests für kroA100 ---")
    for i, params in enumerate(parameter_sets):
        μ, λ, mutation_rate, generations = params
        print(f"\nTest {i+1}: μ={μ}, λ={λ}, Mutationsrate={mutation_rate}")
        
        start_time = time.time()
        ea = EvolutionaryAlgorithm(city_a.citys, μ, λ, mutation_rate, generations)
        best_tour, best_distance = ea.run()
        end_time = time.time()
        
        print(f"Beste Distanz: {best_distance:.2f}")
        print(f"Rechenzeit: {end_time - start_time:.2f} Sekunden")
        
        # Zeichne Konvergenzplot
        ea.plot_progress()
    
    # Test für kroB100 mit den besten Parametern
    print("\n--- Test für kroB100 mit den besten Parametern ---")
    best_params = parameter_sets[0]  # Wir nehmen vorerst die ersten Parameter an
    μ, λ, mutation_rate, generations = best_params
    
    ea = EvolutionaryAlgorithm(city_b.citys, μ, λ, mutation_rate, generations)
    best_tour, best_distance = ea.run_and_plot()
    
    print(f"Beste Distanz für kroB100: {best_distance:.2f}")

if __name__ == "__main__":
    main()
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# 1. Creamos un circuito con 1 qubit y 1 bit clásico
qc = QuantumCircuit(1, 1)

# 2. Aplicamos la compuerta Hadamard (H) para entrar en SUPERPOSICIÓN
# El qubit ahora es 0 y 1 al mismo tiempo.
qc.h(0)

# 3. Medimos el qubit y guardamos el resultado en el bit clásico
qc.measure(0, 0)

# 4. Mostramos cómo quedó el dibujo del circuito en la terminal
print("--- Estructura del Circuito ---")
print(qc.draw(output='text'))

# 5. Ejecutamos la simulación 1000 veces
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()

# 6. Obtenemos los conteos (debería ser cercano a 50/50)
counts = result.get_counts()
print(f"\nResultados de las mediciones: {counts}")

# 7. Graficamos el resultado
from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()
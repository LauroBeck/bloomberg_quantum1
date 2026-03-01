# run_quantum.py
import qsharp
from BeckQuantumProject import MyQuantumOps

qsharp.reload()  # Load Q# operations

result = MyQuantumOps.HelloQ.simulate()
print(f"Quantum operation result: {result}")

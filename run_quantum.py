import qsharp
from qsharp import TargetProfile

# Initialize runtime
qsharp.init(target_profile=TargetProfile.Base)

# Evaluate a Q# expression directly
result = qsharp.eval("""
{
    Message("Hello from Q#!");
    Zero
}
""")

print("Quantum result:", result)

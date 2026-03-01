namespace BeckQuantumProject {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation HelloQ() : Result {
        Message("Hello from Q#!");
        return Zero;
    }
}

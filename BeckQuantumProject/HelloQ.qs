namespace BeckQuantumProject {
    open Microsoft.Quantum.Intrinsic;

    @EntryPoint()
    operation HelloQ() : Result {
        Message("Hello from Q#!");
        return Zero;
    }
}

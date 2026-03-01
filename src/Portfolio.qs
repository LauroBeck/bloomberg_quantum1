namespace BloombergQuantum {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement; // 👈 This is required for MeasureEachZ
    open Microsoft.Quantum.Canon;

    operation EncodePortfolio(volatilities : Double[]) : Result[] {
        let n = Length(volatilities);
        use qubits = Qubit[n];
        
        for i in 0 .. n - 1 {
            Ry(2.0 * volatilities[i], qubits[i]);
        }

        // Apply some basic entanglement (optional)
        if (n > 1) {
            CNOT(qubits[0], qubits[1]);
        }

        // Measure each qubit and return as an array of Results
        return MeasureEachZ(qubits); 
    }
}

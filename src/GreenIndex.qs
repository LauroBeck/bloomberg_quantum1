namespace BloombergQuantum {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation GreenIndexSample() : (Result, Result) {
        use (q1, q2) = (Qubit(), Qubit());

        H(q1);
        CNOT(q1, q2);

        let r1 = MResetZ(q1);
        let r2 = MResetZ(q2);

        return (r1, r2);
    }
}

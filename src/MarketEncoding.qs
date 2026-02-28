namespace BloombergQuantum {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Canon;

    operation EncodeMarketState(
        spVol : Double,
        ndxVol : Double,
        ftseVol : Double,
        rateVol : Double
    ) : (Result, Result, Result, Result) {

        use (sp, ndx, ftse, rate) = (Qubit(), Qubit(), Qubit(), Qubit());

        // 🔹 Encode volatility as amplitude rotations
        Ry(2.0 * spVol, sp);
        Ry(2.0 * ndxVol, ndx);
        Ry(2.0 * ftseVol, ftse);
        Ry(2.0 * rateVol, rate);

        // 🔹 Entanglement structure (macro correlations)

        // SP500 ↔ Nasdaq (strong positive correlation)
        CNOT(sp, ndx);

        // Nasdaq ↔ Rates (tech sensitive to rates)
        CNOT(rate, ndx);

        // SP500 ↔ FTSE (global spillover)
        CNOT(sp, ftse);

        // 🔹 Measure
        let r1 = M(sp);
        let r2 = M(ndx);
        let r3 = M(ftse);
        let r4 = M(rate);

        ResetAll([sp, ndx, ftse, rate]);

        return (r1, r2, r3, r4);
    }
}

namespace BloombergQuantum {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Arrays;

    // 1. LEGACY WRAPPER (Fixes main1.py)
    operation EncodeMarketState(
        spVol : Double, 
        ndxVol : Double, 
        ftseVol : Double, 
        rateVol : Double
    ) : (Result, Result, Result, Result) {
        
        let vols = [spVol, ndxVol, ftseVol, rateVol, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        
        // We pass 0.0 as the crisisLevel so legacy calls don't trigger a crash
        let res = EncodeGlobalMarket(vols, 0.0);
        
        return (res[0], res[1], res[2], res[3]);
    }

    // 2. GLOBAL ENGINE (Supports main5.py and main6.py)
    operation EncodeGlobalMarket(vols : Double[], crisisLevel : Double) : Result[] {
        use qubits = Qubit[10];
        
        // Initialize Volatility
        for i in 0 .. 9 {
            Ry(2.0 * vols[i], qubits[i]);
        }

        // --- SECTION A: Normal Correlations ---
        CNOT(qubits[0], qubits[1]); // SP -> NASDAQ
        CNOT(qubits[0], qubits[2]); // SP -> FTSE
        CNOT(qubits[6], qubits[0]); // WORLD -> SP
        CNOT(qubits[3], qubits[7]); // RATES -> MAG7
        CNOT(qubits[1], qubits[7]); // NASDAQ -> MAG7
        CNOT(qubits[5], qubits[4]); // BBDXY -> BCOM
        CNOT(qubits[5], qubits[2]); // BBDXY -> FTSE
        CNOT(qubits[0], qubits[8]); // SP -> AGG (Flight to quality)

       // --- SECTION B: THE VIX SHOCK & GOLD HEDGE ---
if (crisisLevel > 0.5) {
    H(qubits[9]); // VIX enters uncertainty
    for i in 0 .. 8 {
        if (i == 4) { 
            // GOLD HEDGE: Flip Gold OPPOSITE to the market crash
            CNOT(qubits[9], qubits[i]);
            X(qubits[i]); // The "Safe Haven" inverter
        } else {
            CNOT(qubits[9], qubits[i]); // Everything else crashes together
        }
    }
}

        let results = MeasureEachZ(qubits);
        ResetAll(qubits);
        return results;
    }
}

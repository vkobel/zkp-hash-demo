# ZoKrates Hash Demo

Say we want to prove we know the secret value `68656c6c6f20776f726c64`:


```bash
$ python3 padhash.py 68656c6c6f20776f726c64
secretValue: 0 0 0 0 0 6841708 1819222135 1869769828
publicHash: 1379473483 405191205 2428772561 3398226132 3043549376 3391682572 1446190607 1803527562

$ mkdir zok-working-dir && cd zok-working-dir

$ zokrates compile -i ../prove_sha256.zok
Compiling ../prove_sha256.zok

Compiled code written to 'out'
Number of constraints: 26832

$ zokrates compute-witness -a 0 0 0 0 0 6841708 1819222135 1869769828 1379473483 405191205 2428772561 3398226132 3043549376 3391682572 1446190607 1803527562
Computing witness...
Witness file written to 'witness'

$ zokrates setup
Performing setup...
Verification key written to 'verification.key'
Proving key written to 'proving.key'
Setup completed

$ zokrates generate-proof
Generating proof...
Proof written to 'proof.json'

$ zokrates verify
Performing verification...
PASSED

$ zokrates export-verifier
Exporting verifier...
Verifier exported to 'verifier.sol'
```

## Verification contract (Sepolia)
A verification contract has been deployed: https://sepolia.etherscan.io/address/0x686f9d460637d2ddcdc9407a2adcf240733b9dd8

This is just for illustration purposes only, this won't work because the prover key being created here don't match the verifier key embedded in the contract above.



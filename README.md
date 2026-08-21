# Pulse Commons

## Field notebook 08.21 — allocating a scarce commons from observable demand

### Hypothesis

If demand is published under a frozen metric policy, a shared resource can be allocated without trusting applicants to report their own need and without allowing submission order to influence the result.

### Apparatus

- one resource epoch;
- a hard capacity ceiling;
- a public metric-policy URL;
- participant labels;
- one public pulse URL for every participant;
- GenLayer validators able to retrieve and interpret those records.

### Method

The epoch is opened before demand is known. On closure, validators fetch the metric policy and participant pulses, extract only eligible demand, and agree on the values that matter. The contract sorts participant labels and performs proportional allocation deterministically.

The caller submits locations of evidence—not requested amounts.

### Invariants under observation

```text
Σ allocation ≤ epoch capacity
allocation[p] ≤ authenticated demand[p]
permuting participants does not alter the result
unreadable policy or demand cannot receive allocation
```

### Recorded outcomes

| State | Interpretation |
|---|---|
| `SETTLED` | Verified demand consumed the available capacity. |
| `OPEN_CAPACITY` | All verified demand was served and capacity remains. |
| `FROZEN` | Evidence quality was insufficient to allocate safely. |

### Observation record

`get_epoch` returns more than a colored status. It preserves policy and demand snapshots, verified demand per participant, the allocation vector, unused capacity, missing evidence, rationale, and confidence. That record is what the frontend visualizes.

### Reproduce the experiment

1. Inspect the policy and allocation logic in `contracts/contract.py`.
2. Run the cases in `tests/`, including permutation and capacity properties.
3. Validate the contract with GenVM lint.
4. Build the experimental console in `frontend/`.
5. Deploy with the utilities under `scripts/` and provide the address as `NEXT_PUBLIC_CONTRACT_ADDRESS`.

### Chain environment

The experiment targets GenLayer Bradbury, where independent validators can retrieve the public measurements that ordinary deterministic contracts cannot interpret.

Observed contract: `0xA89C222954db3f65745d15da9b1137b27dD0ef80`

### Result

Pulse Commons turns “I need the most” into a claim that must survive observation.

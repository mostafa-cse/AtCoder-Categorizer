# [Technique] XOR Basis ft Reduced Row Echelon Form

**Taxonomy Path**: `Math` > `Linear Algebra` > `[Technique] XOR Basis ft Reduced Row Echelon Form`

## Description
This topic focuses on [technique] xor basis ft reduced row echelon form techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Once the basis B_0 < B_1 < ... < B_{d-1} is in canonical RREF (each basis vector has a unique pivot bit that is 0 in all other basis vectors), lexicographical order of subset XORs matches the standard integer binary order. Thus, the k-th smallest subset XOR is obtained directly by taking linear combinations matching the binary representation of k - 1.
- Common Reductions: Find the k-th smallest subset XOR value for each k in [L, R]. Construct a linear basis of the given integers over F_2 and diagonalize it into Reduced Row Echelon Form (RREF). The sorted distinct subset XOR values correspond 1-to-1 with the binary representations of integers 0 <= idx < 2^d expanded over the basis.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc283_g`](../../analysis/AtCoder-abc283_g.md) | G. Partial Xor Enumeration | 2173 | Find the k-th smallest subset XOR value for each k in [L, R]. Construct a linear basis of the given integers over F_2 an... |

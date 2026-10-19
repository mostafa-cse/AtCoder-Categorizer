# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since all t >= max L_j >= L_i for all i, no variable ever enters the linear state from 0; variables are initially in state (t - L_i) if R_i > max L_j (or constant if R_i <= max L_j), and at t = R_i they exit to constant (R_i - L_i). Thus, the polynomial P(t) only undergoes divisions by (t - L_i), each taking O(N) via Horner's synthetic division.
- Common Reductions: For N independent uniform continuous variables x_i ~ U[L_i, R_i], E[max x_i] = T_max - int_{max L_i}^{T_max} F(t) dt where F(t) = prod g_i(t) / prod(R_i - L_i). On [max L_i, T_max], each factor g_i(t) transitions from linear (t - L_i) to constant (R_i - L_i) exactly at t = R_i. By sweeping t across sorted distinct R_i >= max L_i, we maintain the polynomial prod (t - L_i) using synthetic polynomial division in O(N^2) total time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-hhkb2020_f`](../../analysis/AtCoder-hhkb2020_f.md) | Random Max | 2691 | For N independent uniform continuous variables x_i ~ U[L_i, R_i], E[max x_i] = T_max - int_{max L_i}^{T_max} F(t) dt whe... |

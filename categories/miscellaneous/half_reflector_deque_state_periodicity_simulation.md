# Invariants and Monovariants

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Invariants and Monovariants`

## Description
This topic focuses on invariants and monovariants techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: An entering ball travels through the device. If the first reflector is 'A', it flips to 'B' and reflects the ball out to the left in 1 step. If the first reflector is 'B', it flips to 'A', lets the ball pass, and by induction, passing through a sequence of reflectors inverts every encountered reflector and shifts the pattern left by 1 position, appending an 'A' at the right end! Thus the string evolution is a deque pop-front, invert, push-back. After at most 2N steps, the string enters a periodic cycle of length 1 or 2.
- Common Reductions: A sequence of N half-reflectors 'A' and 'B'. A ball enters from the left K times (K <= 10^9). Determine the final configuration of reflectors.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc011_d`](../../analysis/AtCoder-agc011_d.md) | D. Half Reflector | 2931 | A sequence of N half-reflectors 'A' and 'B'. A ball enters from the left K times (K <= 10^9). Determine the final config... |

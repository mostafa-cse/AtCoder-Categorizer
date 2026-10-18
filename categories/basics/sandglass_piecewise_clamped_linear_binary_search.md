# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Both draining and filling operations compose with clamping to preserve the functional invariant f(a) = clamp(a + D, A, B). Because the function is monotonic, the state at any time t can be evaluated in O(1) from the latest preceding flip event.
- Common Reductions: Maintain the sandglass state transformation as a piecewise-linear clamped function f(a) = min(B, max(A, a + D)) across flip events, and answer queries in O(log K) via binary search on flip times.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc082_d`](../../analysis/AtCoder-arc082_d.md) | Sandglass | 2429 | Maintain the sandglass state transformation as a piecewise-linear clamped function f(a) = min(B, max(A, a + D)) across f... |

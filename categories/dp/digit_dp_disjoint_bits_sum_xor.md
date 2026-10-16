# Digit DP on Bitwise Condition a + b = a ^ b (Disjoint Bits)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP on Bitwise Condition a + b = a ^ b (Disjoint Bits)**.

---

## Curated Problems

### `[problem:AtCoder-abc129_e]` — Sum Equals Xor
- **Rating / Difficulty**: 1547
- **Contest**: `abc129`
- **Analysis**: [`analysis/AtCoder-abc129_e.md`](../../analysis/AtCoder-abc129_e.md)
- **Key Idea**: a + b = a ^ b holds iff a AND b = 0 (no carry in binary addition). At each bit position, the pair of bits (a_bit, b_bit) can be (0, 0) [1 choice, sum bit 0], or (1, 0) / (0, 1) [2 choices, sum bit 1].
- **Time Complexity**: `O(|L|)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string L;
    if (!(cin >> L)) return 0;

    long long dp_eq = 1, dp_less = 0;

    for (char c : L) {
        long long next_eq = 0, next_less = 0;
        if (c == '1') {
            // Choice 1: sum bit = 1 (2 choices: (1,0) or (0,1)), stays equal
            next_eq = (dp_eq * 2) % MOD;
            // Choice 2: sum bit = 0 (1 choice: (0,0)), transitions from equal to less
            // Plus all 3 choices for existing less
            next_less = (dp_eq + dp_less * 3) % MOD;
        } else {
            // Choice 1: sum bit = 0 (1 choice: (0,0)), stays equal
            next_eq = dp_eq;
            // Choice 2: all 3 choices for existing less
            next_less = (dp_less * 3) % MOD;
        }
        dp_eq = next_eq;
        dp_less = next_less;
    }

    cout << (dp_eq + dp_less) % MOD << "\n";
    return 0;
}
```

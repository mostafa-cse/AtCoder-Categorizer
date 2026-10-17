# Subsequence Pattern Matching Expectation / DP on Automaton with Wildcards

**Domain**: `Dynamic Programming`  
**Subtopic**: `Automaton DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Subsequence Pattern Matching Expectation / DP on Automaton with Wildcards**.

---

## Curated Problems

### `[problem:AtCoder-abc104_d]` — We Love ABC
- **Rating / Difficulty**: 1739
- **Contest**: `abc104`
- **Analysis**: [`analysis/AtCoder-abc104_d.md`](../../analysis/AtCoder-abc104_d.md)
- **Key Idea**: Maintain a 4-state vector [cnt, a, ab, abc] representing the total ways to form prefixes of 'ABC'. Each character updates the state vector linearly.
- **Time Complexity**: `O(N)`
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

    string s;
    if (!(cin >> s)) return 0;

    long long cnt = 1; // 3^(number of '?')
    long long a = 0;   // ways to form "A"
    long long ab = 0;  // ways to form "AB"
    long long abc = 0; // ways to form "ABC"

    for (char c : s) {
        if (c == 'A') {
            a = (a + cnt) % MOD;
        } else if (c == 'B') {
            ab = (ab + a) % MOD;
        } else if (c == 'C') {
            abc = (abc + ab) % MOD;
        } else if (c == '?') {
            long long next_abc = (3 * abc + ab) % MOD;
            long long next_ab = (3 * ab + a) % MOD;
            long long next_a = (3 * a + cnt) % MOD;
            long long next_cnt = (3 * cnt) % MOD;

            abc = next_abc;
            ab = next_ab;
            a = next_a;
            cnt = next_cnt;
        }
    }

    cout << abc << "\n";
    return 0;
}
```

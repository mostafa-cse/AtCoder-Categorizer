# Modulo-5 Arithmetic Residue Selection for Prime Subsets

**Domain**: `Number Theory`  
**Subtopic**: `Modular Arithmetic`  

This workbook contains curated, high-quality competitive programming problems teaching **Modulo-5 Arithmetic Residue Selection for Prime Subsets**.

---

## Curated Problems

### [problem:AtCoder-abc096_d] — Five, Five Everywhere
- **Contest**: `abc096`
- **Rating / Difficulty**: 1226
- **Specific Skill**: Modulo-5 Arithmetic Residue Selection for Prime Subsets
- **Individual Analysis**: [`../../analysis/AtCoder-abc096_d.md`](../../analysis/AtCoder-abc096_d.md)
- **Problem Statement Summary**: Find N distinct prime numbers <= 55,555 (N <= 55) such that any 5 chosen primes have a composite sum.
- **Core Insight**: If all chosen primes p satisfy p = 1 (mod 5), then the sum of any 5 chosen primes is: sum_{i=1}^5 p_i = 1 + 1 + 1 + 1 + 1 = 5 = 0 (mod 5). Since each prime >= 11, the sum of 5 primes is at least 55 > 5, guaranteeing that the sum is strictly composite!
- **Complexity**: Time: `O(MAX log log MAX)` | Space: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 55555;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<bool> is_prime(MAX + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX; i += p) {
                is_prime[i] = false;
            }
        }
    }

    vector<int> selected;
    for (int p = 2; p <= MAX; ++p) {
        if (is_prime[p] && p % 5 == 1) {
            selected.push_back(p);
            if ((int)selected.size() == n) break;
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << selected[i] << (i + 1 == n ? '\n' : ' ');
    }

    return 0;
}
```

# Sieve Divisor Elimination / Multiples Marking

**Domain**: `Number Theory`  
**Subtopic**: `Sieve & Multiples`  

This workbook contains curated, high-quality competitive programming problems teaching **Sieve Divisor Elimination / Multiples Marking**.

---

## Curated Problems

### [problem:AtCoder-abc170_d] — Not Divisible
- **Contest**: `abc170`
- **Rating / Difficulty**: 1033
- **Specific Skill**: Sieve Divisor Elimination / Multiples Marking
- **Individual Analysis**: [`../../analysis/AtCoder-abc170_d.md`](../../analysis/AtCoder-abc170_d.md)
- **Problem Statement Summary**: Given an array A of N positive integers. Count the number of elements A_i such that A_i is not divisible by any other element A_j (j != i) in the array.
- **Core Insight**: Let MAX = 10^6. An element x can be selected if and only if: (1) x appears exactly once in A; (2) no smaller element in A divides x. Marking multiples takes sum MAX/x = O(MAX log MAX).
- **Complexity**: Time: `O(MAX log MAX + N)` | Space: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> freq(MAX + 1, 0);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        freq[a[i]]++;
    }

    vector<bool> bad(MAX + 1, false);

    for (int x = 1; x <= MAX; ++x) {
        if (freq[x] > 0) {
            for (int mult = 2 * x; mult <= MAX; mult += x) {
                bad[mult] = true;
            }
            if (freq[x] > 1) {
                bad[x] = true;
            }
        }
    }

    int ans = 0;
    for (int x : a) {
        if (!bad[x]) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

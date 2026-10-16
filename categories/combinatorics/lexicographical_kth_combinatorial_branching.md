# Lexicographical K-th Permutation via Combinatorial Branching

**Domain**: `Combinatorics`  
**Subtopic**: `Lexicographical Ranking`  

This workbook contains curated, high-quality competitive programming problems teaching **Lexicographical K-th Permutation via Combinatorial Branching**.

---

## Curated Problems

### [problem:AtCoder-abc202_d] — aab aba baa
- **Contest**: `abc202`
- **Rating / Difficulty**: 966
- **Specific Skill**: Lexicographical K-th Permutation via Combinatorial Branching
- **Individual Analysis**: [`../../analysis/AtCoder-abc202_d.md`](../../analysis/AtCoder-abc202_d.md)
- **Problem Statement Summary**: Find the K-th lexicographically smallest string among all strings consisting of A 'a's and B 'b's (A, B <= 30, K <= C(A+B, A) <= 10^18).
- **Core Insight**: If we place 'a' at the current position, the remaining A - 1 'a's and B 'b's can form C(A - 1 + B, A - 1) distinct strings. If K <= C(A - 1 + B, A - 1), the K-th string must start with 'a' (decrement A). Otherwise, it must start with 'b' (decrement B and subtract C(A - 1 + B, A - 1) from K).
- **Complexity**: Time: `O((A + B)^2)` | Space: `O((A + B)^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    long long k;
    if (!(cin >> a >> b >> k)) return 0;

    int total_len = a + b;
    vector<vector<long long>> c(total_len + 1, vector<long long>(total_len + 1, 0));

    for (int i = 0; i <= total_len; ++i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
        }
    }

    string res = "";
    while (a > 0 || b > 0) {
        if (a > 0) {
            long long count_a = c[a - 1 + b][a - 1];
            if (k <= count_a) {
                res += 'a';
                a--;
            } else {
                res += 'b';
                b--;
                k -= count_a;
            }
        } else {
            res += 'b';
            b--;
        }
    }

    cout << res << "\n";
    return 0;
}
```

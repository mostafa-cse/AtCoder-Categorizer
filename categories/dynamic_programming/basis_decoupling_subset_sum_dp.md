# Basis Decoupling Sign DP and Subset Sum Reduction

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Basis Decoupling Sign DP and Subset Sum Reduction**.

---

## Curated Problems

### `[problem:AtCoder-arc214_c]` — Divide into 4 Teams
- **Rating / Difficulty**: 2070
- **Contest**: `arc214`
- **Analysis**: [`analysis/AtCoder-arc214_c.md`](../../analysis/AtCoder-arc214_c.md)
- **Key Idea**: Represent team assignment as independent sign pairs (u_i, v_i) in {+1, -1}^2: A = (+1, +1), B = (-1, -1), C = (+1, -1), D = (-1, +1). The conditions sum(P_A) = sum(P_B) and sum(P_C) = sum(P_D) decouple into two independent equations: sum u_i P_i = 0 and sum v_i P_i = 0. Each choice of signs summing to 0 is equivalent to choosing a subset summing to Total/2. If C is the number of such subsets, there are C^2 total sign assignments. A team can be empty iff an entire pair {A, B} or {C, D} is empty (since P_i >= 1 and sum(A) = sum(B)), which contributes 2C invalid assignments. Thus the answer is exactly C(C - 2) modulo 998244353.
- **Time Complexity**: `O(N * sum(P))`
- **Space Complexity**: `O(sum(P))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        total += p[i];
    }

    if (total % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int target = total / 2;
    vector<long long> dp(target + 1, 0);
    dp[0] = 1;

    for (int x : p) {
        for (int w = target; w >= x; --w) {
            dp[w] = (dp[w] + dp[w - x]) % MOD;
        }
    }

    long long C = dp[target];
    long long ans = (C * (C - 2 + MOD)) % MOD;
    cout << ans << "\n";
    return 0;
}
```

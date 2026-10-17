# Map-Accelerated Digit DP on Sparse Product States

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Map-Accelerated Digit DP on Sparse Product States**.

---

## Curated Problems

### `[problem:AtCoder-abc208_e]` — Digit Products
- **Rating / Difficulty**: 2024
- **Contest**: `abc208`
- **Analysis**: [`analysis/AtCoder-abc208_e.md`](../../analysis/AtCoder-abc208_e.md)
- **Key Idea**: The product of digits in base 10 has prime factors only in {2, 3, 5, 7}: 2^a * 3^b * 5^c * 7^d. The number of reachable distinct products is remarkably sparse (at most ~50,000 values <= 10^9). We use standard Digit DP tracking (pos, is_less, is_started) and represent the current product dynamically using an std::map or unordered_map. Capping values at K + 1 collapses all products > K into a single absorbing failure state.
- **Time Complexity**: `O(len(N) * sparse_products * 10)`
- **Space Complexity**: `O(len(N) * sparse_products)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string S;
long long K;
map<long long, long long> memo[20][2][2];

long long dfs(int pos, long long cur_prod, bool is_less, bool is_started) {
    if (pos == (int)S.size()) {
        return (is_started && cur_prod <= K) ? 1 : 0;
    }

    if (memo[pos][is_less][is_started].count(cur_prod)) {
        return memo[pos][is_less][is_started][cur_prod];
    }

    int limit = (is_less ? 9 : S[pos] - '0');
    long long res = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_less = is_less || (d < limit);
        bool next_started = is_started || (d > 0);
        long long next_prod;
        if (!next_started) {
            next_prod = 1;
        } else if (!is_started) {
            next_prod = d;
        } else {
            next_prod = min(K + 1, cur_prod * d);
        }
        res += dfs(pos + 1, next_prod, next_less, next_started);
    }

    return memo[pos][is_less][is_started][cur_prod] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n >> K)) return 0;

    S = to_string(n);
    cout << dfs(0, 1, false, false) << "\n";

    return 0;
}
```

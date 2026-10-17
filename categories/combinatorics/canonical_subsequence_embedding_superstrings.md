# Canonical Greedy Subsequence Embedding / Distinct Superstring Counting

**Domain**: `Combinatorics`  
**Subtopic**: `Subsequence Counting`  

This workbook contains curated, high-quality competitive programming problems teaching **Canonical Greedy Subsequence Embedding / Distinct Superstring Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc171_f]` — Strivore
- **Rating / Difficulty**: 1795
- **Contest**: `abc171`
- **Analysis**: [`analysis/AtCoder-abc171_f.md`](../../analysis/AtCoder-abc171_f.md)
- **Key Idea**: A superstring T contains S iff the greedy leftmost match of S in T succeeds. Let the greedy match of S complete at index i in [N, N + K]. Then each non-matched character before index i has 25 choices (cannot match current character), the N matched characters are fixed, and characters after index i have 26 choices.
- **Time Complexity**: `O(N + K)`
- **Space Complexity**: `O(N + K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    string s;
    cin >> s;
    int n = s.size();

    int max_len = n + k;
    vector<long long> fact(max_len + 1), inv(max_len + 1);
    vector<long long> pow25(max_len + 1), pow26(max_len + 1);

    fact[0] = inv[0] = 1;
    pow25[0] = pow26[0] = 1;

    for (int i = 1; i <= max_len; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        pow25[i] = (pow25[i - 1] * 25) % MOD;
        pow26[i] = (pow26[i - 1] * 26) % MOD;
    }
    inv[max_len] = power(fact[max_len], MOD - 2);
    for (int i = max_len - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int total, int choose) -> long long {
        if (choose < 0 || choose > total) return 0;
        return fact[total] * inv[choose] % MOD * inv[total - choose] % MOD;
    };

    long long ans = 0;
    for (int i = n; i <= max_len; ++i) {
        long long ways = nCr(i - 1, n - 1) * pow25[i - n] % MOD * pow26[max_len - i] % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

# Greedy Maximum Product of K Integers with Signed Extremum

**Domain**: `Basics`  
**Subtopic**: `Greedy Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Maximum Product of K Integers with Signed Extremum**.

---

## Curated Problems

### `[problem:AtCoder-abc173_e]` — Multiplication 4
- **Rating / Difficulty**: 1607
- **Contest**: `abc173`
- **Analysis**: [`analysis/AtCoder-abc173_e.md`](../../analysis/AtCoder-abc173_e.md)
- **Key Idea**: Handle sign casework carefully: if all elements must yield a negative product (e.g. all numbers negative and K is odd), pick the K numbers with the SMALLEST absolute values. Otherwise, greedily pair up two positives vs two negatives by larger product.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    vector<long long> pos, neg;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] >= 0) pos.push_back(a[i]);
        else neg.push_back(a[i]);
    }

    sort(pos.rbegin(), pos.rend());
    sort(neg.begin(), neg.end()); // Most negative first

    bool must_be_negative = false;
    if (pos.empty() && k % 2 == 1) must_be_negative = true;
    if (n == k && neg.size() % 2 == 1) must_be_negative = true;

    if (must_be_negative) {
        // Pick k elements with smallest absolute values
        sort(a.begin(), a.end(), [](long long x, long long y) {
            return abs(x) < abs(y);
        });
        long long prod = 1;
        for (int i = 0; i < k; ++i) {
            prod = (prod * ((a[i] % MOD + MOD) % MOD)) % MOD;
        }
        cout << prod << "\n";
        return 0;
    }

    long long prod = 1;
    size_t pi = 0, ni = 0;

    if (k % 2 == 1) {
        prod = (prod * pos[pi++]) % MOD;
        k--;
    }

    while (k > 0) {
        long long p_pair = (pi + 1 < pos.size() ? pos[pi] * pos[pi + 1] : -1);
        long long n_pair = (ni + 1 < neg.size() ? neg[ni] * neg[ni + 1] : -1);

        if (p_pair >= n_pair) {
            prod = (prod * (pos[pi] % MOD)) % MOD;
            prod = (prod * (pos[pi + 1] % MOD)) % MOD;
            pi += 2;
        } else {
            prod = (prod * ((neg[ni] % MOD + MOD) % MOD)) % MOD;
            prod = (prod * ((neg[ni + 1] % MOD + MOD) % MOD)) % MOD;
            ni += 2;
        }
        k -= 2;
    }

    cout << prod << "\n";
    return 0;
}
```

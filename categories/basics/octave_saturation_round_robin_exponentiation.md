# Octave Saturation / Min-Heap Transition to Modular Round-Robin Exponentiation

**Domain**: `Basics`  
**Subtopic**: `Priority Queue / Math`  

This workbook contains curated, high-quality competitive programming problems teaching **Octave Saturation / Min-Heap Transition to Modular Round-Robin Exponentiation**.

---

## Curated Problems

### `[problem:AtCoder-arc051_c]` — 掛け算
- **Rating / Difficulty**: 1898
- **Contest**: `arc051`
- **Analysis**: [`analysis/AtCoder-arc051_c.md`](../../analysis/AtCoder-arc051_c.md)
- **Key Idea**: If multiplier A == 1, array never changes. If A > 1: using a min-heap, repeatedly multiply the minimum element by A until all elements are within the same 'octave' [max, max * A) or operations run out. Once saturated, operations cycle round-robin across all N elements.
- **Time Complexity**: `O(N log(max_val) + N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

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

    int n;
    long long A, B;
    if (!(cin >> n >> A >> B)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    if (A == 1) {
        sort(a.begin(), a.end());
        for (int i = 0; i < n; ++i) {
            cout << a[i] % MOD << "\n";
        }
        return 0;
    }

    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        pq.push(a[i]);
        max_val = max(max_val, a[i]);
    }

    while (B > 0 && pq.top() * A <= max_val) {
        long long mn = pq.top();
        pq.pop();
        pq.push(mn * A);
        max_val = max(max_val, mn * A);
        B--;
    }

    vector<long long> elems;
    while (!pq.empty()) {
        elems.push_back(pq.top());
        pq.pop();
    }

    long long q = B / n;
    long long r = B % n;

    vector<long long> ans(n);
    for (int i = 0; i < n; ++i) {
        long long exp = q + (i < r ? 1 : 0);
        ans[i] = (elems[i] % MOD) * power(A, exp) % MOD;
    }

    // Output starting from index r to maintain sorted order
    for (int i = 0; i < n; ++i) {
        int idx = (r + i) % n;
        cout << ans[idx] << "\n";
    }

    return 0;
}
```

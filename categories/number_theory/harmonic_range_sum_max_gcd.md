# Harmonic Range Sum with Prefix Aggregates for Maximum GCD

**Domain**: `Number Theory`  
**Subtopic**: `Harmonic Range Sum`  

This workbook contains curated, high-quality competitive programming problems teaching **Harmonic Range Sum with Prefix Aggregates for Maximum GCD**.

---

## Curated Problems

### `[problem:AtCoder-arc126_c]` — Maximize GCD
- **Rating / Difficulty**: 1824
- **Contest**: `arc126`
- **Analysis**: [`analysis/AtCoder-arc126_c.md`](../../analysis/AtCoder-arc126_c.md)
- **Key Idea**: If K is sufficient to make all A_i equal to max(A), then remaining operations can be split equally to make GCD = max(A) + floor((K - rem) / N). Otherwise, GCD g <= max(A). For each candidate g in [2, max(A)], evaluate the cost to round every A_i up to the next multiple of g using prefix sums in O(max(A) / g) harmonic sum time.
- **Time Complexity**: `O(N + M log M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    long long sum_a = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        sum_a += a[i];
    }

    long long cost_to_max = max_val * n - sum_a;
    if (k >= cost_to_max) {
        long long extra = (k - cost_to_max) / n;
        cout << max_val + extra << "\n";
        return 0;
    }

    int limit = 2 * max_val;
    vector<long long> cnt(limit + 1, 0), pref_sum(limit + 1, 0);

    for (int i = 0; i < n; ++i) {
        cnt[a[i]]++;
        pref_sum[a[i]] += a[i];
    }

    for (int i = 1; i <= limit; ++i) {
        cnt[i] += cnt[i - 1];
        pref_sum[i] += pref_sum[i - 1];
    }

    for (long long g = max_val; g >= 1; --g) {
        long long cur_cost = 0;
        for (long long mult = g; mult - g < max_val; mult += g) {
            long long l = mult - g + 1;
            long long r = mult;
            long long c = cnt[r] - cnt[l - 1];
            long long s = pref_sum[r] - pref_sum[l - 1];
            cur_cost += c * mult - s;
        }

        if (cur_cost <= k) {
            cout << g << "\n";
            return 0;
        }
    }

    return 0;
}
```

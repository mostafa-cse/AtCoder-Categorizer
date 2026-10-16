# Prefix and Suffix GCD Arrays (Exclusion Technique)

**Domain**: `Data Structures`  
**Subtopic**: `Prefix & Suffix Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix and Suffix GCD Arrays (Exclusion Technique)**.

---

## Curated Problems

### [problem:AtCoder-abc125_c] — GCD on Blackboard
- **Contest**: `abc125`
- **Rating / Difficulty**: 1197
- **Specific Skill**: Prefix and Suffix GCD Arrays (Exclusion Technique)
- **Individual Analysis**: [`../../analysis/AtCoder-abc125_c.md`](../../analysis/AtCoder-abc125_c.md)
- **Problem Statement Summary**: Given N integers A_1..A_N. Replace at most one integer with any integer you choose. Maximize the greatest common divisor of all elements in the array.
- **Core Insight**: Precompute prefix GCD array pref[i] = gcd(pref[i-1], A[i]) and suffix GCD array suff[i] = gcd(suff[i+1], A[i]). Then the GCD of all elements except A_i is gcd(pref[i-1], suff[i+1]) in O(log(MAX)). Maximize over all 1 <= i <= N.
- **Complexity**: Time: `O(N log(MAX))` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 2, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<long long> pref(n + 2, 0);
    vector<long long> suff(n + 2, 0);

    for (int i = 1; i <= n; ++i) {
        pref[i] = gcd_ll(pref[i - 1], a[i]);
    }
    for (int i = n; i >= 1; --i) {
        suff[i] = gcd_ll(suff[i + 1], a[i]);
    }

    long long max_gcd = 0;
    for (int i = 1; i <= n; ++i) {
        long long g = gcd_ll(pref[i - 1], suff[i + 1]);
        max_gcd = max(max_gcd, g);
    }

    cout << max_gcd << "\n";
    return 0;
}
```

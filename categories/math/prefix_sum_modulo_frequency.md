# Prefix Sum Modulo Frequency Matching

**Domain**: `Math`  
**Subtopic**: `Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix Sum Modulo Frequency Matching**.

---

## Curated Problems

### `[problem:AtCoder-abc105_d]` — Candy Distribution
- **Rating / Difficulty**: 1458
- **Contest**: `abc105`
- **Analysis**: [`analysis/AtCoder-abc105_d.md`](../../analysis/AtCoder-abc105_d.md)
- **Key Idea**: The subarray sum is pref[r] - pref[l-1]. It is divisible by M if and only if pref[r] = pref[l-1] (mod M). Count the frequency of each remainder.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    map<long long, long long> cnt;
    cnt[0] = 1;

    long long pref = 0;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        pref = (pref + a) % m;
        ans += cnt[pref];
        cnt[pref]++;
    }

    cout << ans << "\n";
    return 0;
}
```

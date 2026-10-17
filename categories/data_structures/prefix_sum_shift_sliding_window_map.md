# Prefix Sum Shift Transformation (S_i - i) mod K with Sliding Window Map

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Sliding Window Hash`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix Sum Shift Transformation (S_i - i) mod K with Sliding Window Map**.

---

## Curated Problems

### `[problem:AtCoder-abc146_e]` — Rem of Sum is Num
- **Rating / Difficulty**: 1762
- **Contest**: `abc146`
- **Analysis**: [`analysis/AtCoder-abc146_e.md`](../../analysis/AtCoder-abc146_e.md)
- **Key Idea**: The condition (S_r - S_{l-1}) = r - (l - 1) (mod K) rearranges to (S_r - r) = (S_{l-1} - (l - 1)) (mod K). Defining B_i = (S_i - i) mod K, we require B_r == B_{l-1} within a sliding window of length at most K - 1.
- **Time Complexity**: `O(N log K)`
- **Space Complexity**: `O(K)`
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n + 1);
    vector<long long> b(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    long long pref = 0;
    for (int i = 1; i <= n; ++i) {
        pref += a[i];
        b[i] = ((pref - i) % k + k) % k;
    }

    map<long long, int> freq;
    long long ans = 0;

    freq[0] = 1;

    for (int r = 1; r <= n; ++r) {
        if (r >= k) {
            freq[b[r - k]]--;
        }
        ans += freq[b[r]];
        freq[b[r]]++;
    }

    cout << ans << "\n";
    return 0;
}
```

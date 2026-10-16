# Two Pointers Contribution to Sum for Non-Matching Pairs

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Two Pointers Contribution to Sum for Non-Matching Pairs**.

---

## Curated Problems

### `[problem:AtCoder-abc290_e]` — Make it Palindrome
- **Rating / Difficulty**: 1485
- **Contest**: `abc290`
- **Analysis**: [`analysis/AtCoder-abc290_e.md`](../../analysis/AtCoder-abc290_e.md)
- **Key Idea**: Instead of checking each subarray, count the total pairs (i, j) that are symmetric counterparts in some subarray, and subtract those where A[i] == A[j].
- **Time Complexity**: `O(N log N) or O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<vector<int>> pos(n + 1);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pos[a[i]].push_back(i);
    }

    // Total symmetric pairs over all subarrays
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += 1LL * min(i + 1, n - i) * (n - 1 - i);
    }
    // Alternatively: sum over all i < j min(i + 1, n - j)
    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        total_pairs += 1LL * (i + 1) * (n - 1 - 2 * i > 0 ? n - 1 - 2 * i : 0);
    }

    // Precise total sum of min(i + 1, n - j)
    long long all_pairs = 0;
    for (int i = 0; i < n; ++i) {
        long long c = min(i + 1, n - i);
        all_pairs += c * (n - i - 1);
    }

    // Subtract matching pairs
    long long matches = 0;
    for (int v = 1; v <= n; ++v) {
        const auto& p = pos[v];
        int l = 0, r = (int)p.size() - 1;
        while (l < r) {
            if (p[l] + 1 <= n - p[r]) {
                matches += 1LL * (p[l] + 1) * (r - l);
                l++;
            } else {
                matches += 1LL * (n - p[r]) * (r - l);
                r--;
            }
        }
    }

    cout << all_pairs - matches << "\n";
    return 0;
}
```

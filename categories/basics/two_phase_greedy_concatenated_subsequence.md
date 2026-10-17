# Lexicographical Minimal Concatenated Subsequence via Two-Phase Greedy Selection

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Lexicographical Minimal Concatenated Subsequence via Two-Phase Greedy Selection**.

---

## Curated Problems

### `[problem:AtCoder-arc134_d]` — Concatenate Subsequences
- **Rating / Difficulty**: 1998
- **Contest**: `arc134`
- **Analysis**: [`analysis/AtCoder-arc134_d.md`](../../analysis/AtCoder-arc134_d.md)
- **Key Idea**: The first element of x must be the global minimum of a: m = min(a). If there exists any index i with a_i = m such that b_i <= m, then selecting ONLY this single index i yields (m, b_i) with b_i <= m, which is strictly smaller than any sequence starting with (m, >m). If no such index exists, we must select ALL occurrences of m. Let the minimum b among all chosen indices be min_b. We can then greedily append subsequent elements j with a_j < min_b, or if a_j == min_b, only if the resulting b_j maintains lexicographical superiority.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
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
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    int min_a = *min_element(a.begin(), a.end());

    int best_single_b = 2e9;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a && b[i] <= min_a) {
            best_single_b = min(best_single_b, b[i]);
        }
    }

    if (best_single_b <= min_a) {
        cout << min_a << " " << best_single_b << "\n";
        return 0;
    }

    vector<int> idx;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a) {
            idx.push_back(i);
        }
    }

    int min_b = 2e9;
    for (int i : idx) {
        min_b = min(min_b, b[i]);
    }

    // Determine whether to accept a[j] == min_b
    bool take_equal = false;
    for (int i : idx) {
        if (b[i] != min_b) {
            take_equal = (b[i] < min_b);
            break;
        }
    }

    int cur_idx = idx.back();
    for (int i = cur_idx + 1; i < n; ++i) {
        if (a[i] < min_b || (a[i] == min_b && take_equal)) {
            if (idx.empty() || a[i] >= a[idx.back()]) {
                idx.push_back(i);
            }
        }
    }

    vector<int> ans;
    for (int i : idx) ans.push_back(a[i]);
    for (int i : idx) ans.push_back(b[i]);

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

# Constructive XOR Palindromic Sandwich Sequence

**Domain**: `Basics`  
**Subtopic**: `Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Constructive XOR Palindromic Sandwich Sequence**.

---

## Curated Problems

### `[problem:AtCoder-abc126_f]` — XOR Matching
- **Rating / Difficulty**: 1770
- **Contest**: `abc126`
- **Analysis**: [`analysis/AtCoder-abc126_f.md`](../../analysis/AtCoder-abc126_f.md)
- **Key Idea**: For M >= 2, the XOR sum of all integers in [0, 2^M - 1] is 0. If K >= 2^M, impossible. For M = 1: K = 0 gives 0 0 1 1, K = 1 is impossible. For M >= 2, construct: [all elements except K in ascending order] + [K] + [all elements except K in descending order] + [K].
- **Time Complexity**: `O(2^M)`
- **Space Complexity**: `O(2^M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long k;
    if (!(cin >> m >> k)) return 0;

    int total_vals = 1 << m;

    if (k >= total_vals) {
        cout << -1 << "\n";
        return 0;
    }

    if (m == 0) {
        if (k == 0) cout << "0 0\n";
        else cout << -1 << "\n";
        return 0;
    }

    if (m == 1) {
        if (k == 0) cout << "0 0 1 1\n";
        else cout << -1 << "\n";
        return 0;
    }

    vector<int> ans;
    for (int i = 0; i < total_vals; ++i) {
        if (i != k) ans.push_back(i);
    }
    ans.push_back(k);
    for (int i = total_vals - 1; i >= 0; --i) {
        if (i != k) ans.push_back(i);
    }
    ans.push_back(k);

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

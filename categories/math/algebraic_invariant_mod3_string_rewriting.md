# Algebraic Invariant / Value Mapping Modulo 3 on String Rewriting

**Domain**: `Math`  
**Subtopic**: `Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Algebraic Invariant / Value Mapping Modulo 3 on String Rewriting**.

---

## Curated Problems

### `[problem:AtCoder-arc071_c]` — TrBBnsformBBtion
- **Rating / Difficulty**: 1739
- **Contest**: `arc071`
- **Analysis**: [`analysis/AtCoder-arc071_c.md`](../../analysis/AtCoder-arc071_c.md)
- **Key Idea**: Map 'A' to 1 and 'B' to 2. Notice that 'A' <-> 'BB' means 1 <-> 2 + 2 = 4 = 1 (mod 3), and 'B' <-> 'AA' means 2 <-> 1 + 1 = 2 (mod 3). Thus, the sum of values modulo 3 is strictly invariant under all operations.
- **Time Complexity**: `O(|S| + |T| + Q)`
- **Space Complexity**: `O(|S| + |T|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> pref_s(n + 1, 0), pref_t(m + 1, 0);

    for (int i = 0; i < n; ++i) {
        pref_s[i + 1] = pref_s[i] + (s[i] == 'A' ? 1 : 2);
    }
    for (int i = 0; i < m; ++i) {
        pref_t[i + 1] = pref_t[i] + (t[i] == 'A' ? 1 : 2);
    }

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int sum_s = (pref_s[b] - pref_s[a - 1]) % 3;
        int sum_t = (pref_t[d] - pref_t[c - 1]) % 3;
        if (sum_s == sum_t) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
```

# Alphabet Bijection / Isomorphism Verification

**Domain**: `Strings`  
**Subtopic**: `Character Bijections`  

This workbook contains curated, high-quality competitive programming problems teaching **Alphabet Bijection / Isomorphism Verification**.

---

## Curated Problems

### [problem:AtCoder-abc110_c] — String Transformation
- **Contest**: `abc110`
- **Rating / Difficulty**: 949
- **Specific Skill**: Alphabet Bijection / Isomorphism Verification
- **Individual Analysis**: [`../../analysis/AtCoder-abc110_c.md`](../../analysis/AtCoder-abc110_c.md)
- **Problem Statement Summary**: Given two strings S and T of the same length. You can choose two distinct characters c_1 and c_2 and swap all occurrences of c_1 and c_2 in S. Can S be transformed into T?
- **Core Insight**: Verify two conditions: (1) each character in S maps to at most one character in T; (2) each character in T is mapped from at most one character in S.
- **Complexity**: Time: `O(|S| + |Sigma|)` | Space: `O(|Sigma|)`
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

    vector<int> s_to_t(26, -1);
    vector<int> t_to_s(26, -1);

    for (size_t i = 0; i < s.size(); ++i) {
        int u = s[i] - 'a';
        int v = t[i] - 'a';

        if (s_to_t[u] != -1 && s_to_t[u] != v) {
            cout << "No\n";
            return 0;
        }
        if (t_to_s[v] != -1 && t_to_s[v] != u) {
            cout << "No\n";
            return 0;
        }

        s_to_t[u] = v;
        t_to_s[v] = u;
    }

    cout << "Yes\n";
    return 0;
}
```

# Rightmost Match Lexicographical Minimization

**Domain**: `Strings`  
**Subtopic**: `String Matching & Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Rightmost Match Lexicographical Minimization**.

---

## Curated Problems

### [problem:AtCoder-abc076_c] — Dubious Document 2
- **Contest**: `abc076`
- **Rating / Difficulty**: 846
- **Specific Skill**: Rightmost Match Lexicographical Minimization
- **Individual Analysis**: [`../../analysis/AtCoder-abc076_c.md`](../../analysis/AtCoder-abc076_c.md)
- **Problem Statement Summary**: Given string S containing lowercase letters and '?', and string T. Replace all '?' such that T appears as a contiguous substring of S and the resulting string is lexicographically smallest. If impossible, output UNRESTORABLE.
- **Core Insight**: Iterate backwards over all possible start positions i for T in S. The first (rightmost) index i where T matches S[i .. i + |T| - 1] (allowing '?' to match any char) gives the optimal placement. All remaining '?' in S become 'a'.
- **Complexity**: Time: `O(|S| * |T|)` | Space: `O(|S|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size();
    int m = t.size();

    int best_pos = -1;
    for (int i = n - m; i >= 0; --i) {
        bool match = true;
        for (int j = 0; j < m; ++j) {
            if (s[i + j] != '?' && s[i + j] != t[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            best_pos = i;
            break;
        }
    }

    if (best_pos == -1) {
        cout << "UNRESTORABLE\n";
    } else {
        string res = s;
        for (int j = 0; j < m; ++j) {
            res[best_pos + j] = t[j];
        }
        for (int i = 0; i < n; ++i) {
            if (res[i] == '?') res[i] = 'a';
        }
        cout << res << "\n";
    }

    return 0;
}
```

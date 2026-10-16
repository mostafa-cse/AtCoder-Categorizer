# Periodic String Subsequence Matching via Position Binary Search

**Domain**: `Strings`  
**Subtopic**: `Subsequences`  

This workbook contains curated, high-quality competitive programming problems teaching **Periodic String Subsequence Matching via Position Binary Search**.

---

## Curated Problems

### [problem:AtCoder-abc138_e] — Strings of Impurity
- **Contest**: `abc138`
- **Rating / Difficulty**: 1257
- **Specific Skill**: Periodic String Subsequence Matching via Position Binary Search
- **Individual Analysis**: [`../../analysis/AtCoder-abc138_e.md`](../../analysis/AtCoder-abc138_e.md)
- **Problem Statement Summary**: Given string s and string t. Let s' be an infinite concatenation of s. Find the shortest prefix length of s' that contains t as a subsequence (or -1 if impossible).
- **Core Insight**: Store 0-indexed positions of each character in s: pos[c]. Maintain current index in s: cur_pos. For character t[i]: binary search with std::upper_bound in pos[t[i]] for the first position > cur_pos. If found, advance cur_pos to that position. If not found, wrap around to the next copy of s (advance copy count) and set cur_pos to pos[t[i]][0].
- **Complexity**: Time: `O(|s| + |t| log |s|)` | Space: `O(|s|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    vector<vector<int>> pos(26);
    for (int i = 0; i < (int)s.size(); ++i) {
        pos[s[i] - 'a'].push_back(i);
    }

    long long copies = 0;
    int cur_idx = -1;

    for (char c : t) {
        int char_code = c - 'a';
        if (pos[char_code].empty()) {
            cout << -1 << "\n";
            return 0;
        }

        auto it = upper_bound(pos[char_code].begin(), pos[char_code].end(), cur_idx);
        if (it != pos[char_code].end()) {
            cur_idx = *it;
        } else {
            copies++;
            cur_idx = pos[char_code][0];
        }
    }

    long long total_len = copies * (long long)s.size() + cur_idx + 1;
    cout << total_len << "\n";
    return 0;
}
```

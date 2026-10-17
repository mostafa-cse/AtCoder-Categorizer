# Greedy Lexicographical String Construction with Feasibility Verification under Edit Budget

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Lexicographical String Construction with Feasibility Verification under Edit Budget**.

---

## Curated Problems

### `[problem:AtCoder-abc009_3]` — 辞書式順序ふたたび
- **Rating / Difficulty**: 1915
- **Contest**: `abc009`
- **Analysis**: [`analysis/AtCoder-abc009_3.md`](../../analysis/AtCoder-abc009_3.md)
- **Key Idea**: Construct T character by character from position 0 to N - 1. At index i, try characters c in ['a'..'z'] in alphabetical order. If character c is placed at position i, verify whether the remaining characters can be assigned to satisfy the edit budget K. The minimum extra mismatches for suffix i + 1..N - 1 is (length - sum_{ch} min(count_T(ch), count_S(ch))). If (current_diff + extra_diff <= K), greedily commit to c.
- **Time Complexity**: `O(N^2 * 26)`
- **Space Complexity**: `O(N)`
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

    int n, k;
    if (!(cin >> n >> k)) return 0;
    string s;
    cin >> s;

    vector<int> count(26, 0);
    for (char c : s) count[c - 'a']++;

    string t = "";
    int diff_so_far = 0;

    for (int i = 0; i < n; ++i) {
        for (int c = 0; c < 26; ++c) {
            if (count[c] == 0) continue;

            count[c]--;
            int cur_diff = diff_so_far + (c != (s[i] - 'a'));

            vector<int> s_rem(26, 0);
            for (int j = i + 1; j < n; ++j) {
                s_rem[s[j] - 'a']++;
            }

            int matches = 0;
            for (int ch = 0; ch < 26; ++ch) {
                matches += min(count[ch], s_rem[ch]);
            }
            int extra_diff = (n - 1 - i) - matches;

            if (cur_diff + extra_diff <= k) {
                t += (char)('a' + c);
                diff_so_far = cur_diff;
                break;
            }

            count[c]++;
        }
    }

    cout << t << "\n";
    return 0;
}
```

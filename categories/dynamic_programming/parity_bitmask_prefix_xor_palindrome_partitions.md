# Bitmask DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask DP**.

---

## Curated Problems

### `[problem:AtCoder-code_festival_2017_qualc_d]` — Yet Another Palindrome Partitioning
- **Rating / Difficulty**: 2132
- **Contest**: `code_festival_2017_qualc`
- **Analysis**: [`analysis/AtCoder-code_festival_2017_qualc_d.md`](../../analysis/AtCoder-code_festival_2017_qualc_d.md)
- **Key Idea**: A substring can be rearranged into a palindrome iff at most one character appears an odd number of times. Let pref[i] be the 26-bit bitmask where the c-th bit is the parity of character c in prefix S[1..i]. A substring S[j..i] can form a palindrome iff popcount(pref[i] ^ pref[j-1]) <= 1. Maintaining min_dp[mask] as the minimum partitions for any prefix with parity mask, each step checks mask itself and the 26 masks differing by 1 bit in O(26) time.
- **Time Complexity**: `O(26 * |S|)`
- **Space Complexity**: `O(2^{26})`
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

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    int full = 1 << 26;
    vector<int> min_dp(full, 1e9);
    min_dp[0] = 0;

    int cur_mask = 0;
    int cur_ans = 0;

    for (char c : s) {
        cur_mask ^= (1 << (c - 'a'));
        int best = min_dp[cur_mask] + 1;
        for (int i = 0; i < 26; ++i) {
            best = min(best, min_dp[cur_mask ^ (1 << i)] + 1);
        }
        cur_ans = best;
        min_dp[cur_mask] = min(min_dp[cur_mask], cur_ans);
    }

    cout << cur_ans << "\n";
    return 0;
}
```

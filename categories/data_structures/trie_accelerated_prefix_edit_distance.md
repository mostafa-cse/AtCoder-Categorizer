# Trie-Accelerated Prefix Edit Distance / LCS Minimization

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Trie`  

This workbook contains curated, high-quality competitive programming problems teaching **Trie-Accelerated Prefix Edit Distance / LCS Minimization**.

---

## Curated Problems

### `[problem:AtCoder-abc377_g]` — Edit to Match
- **Rating / Difficulty**: 1782
- **Contest**: `abc377`
- **Analysis**: [`analysis/AtCoder-abc377_g.md`](../../analysis/AtCoder-abc377_g.md)
- **Key Idea**: If S_i shares a common prefix of length d with S_j, transforming S_i into S_j's prefix costs |S_i| - d + (|S_j| - d) = |S_i| + (|S_j| - 2d). In a Trie, each node at depth d maintains min(|S_j| - 2d) over all strings passing through it.
- **Time Complexity**: `O(sum |S_i|)`
- **Space Complexity**: `O(sum |S_i| * 26)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct TrieNode {
    int next[26];
    int min_val;
    TrieNode() : min_val(INF) {
        fill(next, next + 26, -1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<TrieNode> trie;
    trie.emplace_back(); // Root at index 0

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        int len = s.size();

        int ans = len; // Delete all characters to become empty string
        int u = 0;

        // Query step
        ans = min(ans, len + trie[u].min_val);
        for (int d = 1; d <= len; ++d) {
            int c = s[d - 1] - 'a';
            if (trie[u].next[c] == -1) break;
            u = trie[u].next[c];
            ans = min(ans, len + trie[u].min_val);
        }

        cout << ans << "\n";

        // Insert step
        u = 0;
        trie[u].min_val = min(trie[u].min_val, len);
        for (int d = 1; d <= len; ++d) {
            int c = s[d - 1] - 'a';
            if (trie[u].next[c] == -1) {
                trie[u].next[c] = trie.size();
                trie.emplace_back();
            }
            u = trie[u].next[c];
            trie[u].min_val = min(trie[u].min_val, len - 2 * d);
        }
    }

    return 0;
}
```

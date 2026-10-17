# Problem Analysis: AtCoder-abc377_g — Edit to Match

**Problem ID**: `AtCoder-abc377_g`  
**Contest**: `abc377`  
**Rating / Difficulty**: 1782  
**URL**: https://atcoder.jp/contests/abc377/tasks/abc377_g  
**VJudge Tag**: `[problem:AtCoder-abc377_g]`  
**Category File**: [`../categories/data_structures/trie_accelerated_prefix_edit_distance.md`](../categories/data_structures/trie_accelerated_prefix_edit_distance.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie-Accelerated Prefix Edit Distance / LCS Minimization`  

---

## 1. Problem Statement & Key Idea
Given N strings S_1, ..., S_N. For each S_i, find the minimum cost to transform S_i into a prefix of some previously processed string S_j (j < i) or an empty string, where operations are: delete the last character (cost 1) or append any character (cost 1).

**Key Insight**: If S_i shares a common prefix of length d with S_j, transforming S_i into S_j's prefix costs |S_i| - d + (|S_j| - d) = |S_i| + (|S_j| - 2d). In a Trie, each node at depth d maintains min(|S_j| - 2d) over all strings passing through it.

## 2. Core Observation & Invariant
For query S_i, walk down the Trie. At each matched prefix node at depth d, best cost is |S_i| + min_val[node]. Then insert S_i into the Trie updating min_val.

## 3. Step-by-Step Algorithm
1. Initialize Trie where each node stores min_val initialized to INF.
2. For each string S_i:
3.   ans = |S_i| (reducing to empty string).
4.   Walk S_i down the Trie:
5.     at node u with depth d: ans = min(ans, |S_i| + node.min_val).
6.   Print ans.
7.   Insert S_i into Trie: at each node u with depth d, node.min_val = min(node.min_val, |S_i| - 2 * d).

## 4. Complexity Analysis
- **Time Complexity**: `O(sum |S_i|)`
- **Space Complexity**: `O(sum |S_i| * 26)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Trie node caching of prefix match metric min(|S_j| - 2d) for linear edit distance.
- **Reusable Pattern**: `Trie Prefix Edit Distance: Cache min(|S_j| - 2*depth) at each node to query in O(|S|).`

# Problem Analysis: AtCoder-codefestival_2016_qualB_e — E. Lexicographical disorder

**Problem ID**: `AtCoder-codefestival_2016_qualB_e`  
**Contest**: `codefestival_2016_qualB`  
**Rating / Difficulty**: 2576  
**URL**: https://atcoder.jp/contests/codefestival_2016_qualB/tasks/codefestival_2016_qualB_e  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_qualB_e]`  
**Category File**: [`../categories/data_structures/lexicographical_disorder_trie_query_matrix.md`](../categories/data_structures/lexicographical_disorder_trie_query_matrix.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
Answer $Q$ queries finding the 1-based lexicographical rank of string $S_k$ under custom alphabet permutations $p$.

## 2. Core Observation & Invariant
In the Trie of all strings, any string $S_j$ smaller than $S_k$ either ends at an ancestor of $S_k$ (constant prefix contribution), or branches off at a node $u$ with character $c'$ where $S_k$ has $c$ and $\text{rank}(c') < \text{rank}(c)$. Summing sibling branch sizes across $S_k$'s path produces a $26 \times 26$ divergence matrix $W_k$.

## 3. Step-by-Step Algorithm
1. 1. Insert all $N$ strings into a Trie, tracking subtree string counts and end markers.
2. 2. Group queries offline by string index $k$.
3. 3. For each queried $k$, traverse $S_k$ in the Trie to compute constant ancestor count and matrix $W[c][c']$.
4. 4. For each query on $k$, evaluate $\sum_{c, c': \text{rank}(c') < \text{rank}(c)} W[c][c'] + const + 1$ in $26 \times 26$ operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(\sum |S_i| \cdot 26 + Q \cdot 26^2)`
- **Space Complexity**: `O(\sum |S_i| \cdot 26)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct TrieNode {
    int next[26];
    int sub_cnt;
    int is_end;
    TrieNode() {
        fill(next, next + 26, -1);
        sub_cnt = 0;
        is_end = 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<string> S(N);
    for (int i = 0; i < N; ++i) cin >> S[i];

    int Q;
    if (!(cin >> Q)) return 0;
    struct Query {
        int k;
        string p;
        int q_idx;
    };
    vector<vector<pair<string, int>>> queries_by_k(N);
    for (int q = 0; q < Q; ++q) {
        int k;
        string p;
        cin >> k >> p;
        queries_by_k[k - 1].push_back({p, q});
    }

    vector<TrieNode> trie;
    trie.emplace_back();

    for (int i = 0; i < N; ++i) {
        int cur = 0;
        trie[cur].sub_cnt++;
        for (char c : S[i]) {
            int idx = c - 'a';
            if (trie[cur].next[idx] == -1) {
                trie[cur].next[idx] = trie.size();
                trie.emplace_back();
            }
            cur = trie[cur].next[idx];
            trie[cur].sub_cnt++;
        }
        trie[cur].is_end++;
    }

    vector<int> ans(Q);

    for (int k = 0; k < N; ++k) {
        if (queries_by_k[k].empty()) continue;
        const string& s = S[k];

        int const_smaller = 0;
        int W[26][26] = {};

        int cur = 0;
        for (char c : s) {
            int c_idx = c - 'a';
            if (cur != 0) {
                const_smaller += trie[cur].is_end;
            }
            for (int other_c = 0; other_c < 26; ++other_c) {
                if (other_c != c_idx) {
                    int nxt = trie[cur].next[other_c];
                    if (nxt != -1) {
                        W[c_idx][other_c] += trie[nxt].sub_cnt;
                    }
                }
            }
            cur = trie[cur].next[c_idx];
        }

        for (auto& q : queries_by_k[k]) {
            const string& p = q.first;
            int q_idx = q.second;
            int rank[26];
            for (int r = 0; r < 26; ++r) {
                rank[p[r] - 'a'] = r;
            }

            int smaller = const_smaller;
            for (int c = 0; c < 26; ++c) {
                for (int other_c = 0; other_c < 26; ++other_c) {
                    if (W[c][other_c] > 0 && rank[other_c] < rank[c]) {
                        smaller += W[c][other_c];
                    }
                }
            }
            ans[q_idx] = smaller + 1;
        }
    }

    for (int q = 0; q < Q; ++q) {
        cout << ans[q] << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

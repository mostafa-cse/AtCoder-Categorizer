# Problem Analysis: AtCoder-arc087_c — Prefix-free Game

**Problem ID**: `AtCoder-arc087_c`  
**Contest**: `arc087`  
**Rating / Difficulty**: 2431  
**URL**: https://atcoder.jp/contests/arc087/tasks/arc087_c  
**VJudge Tag**: `[problem:AtCoder-arc087_c]`  
**Category File**: [`../categories/game_theory/prefix_free_trie_full_binary_tree_grundy_nim.md`](../categories/game_theory/prefix_free_trie_full_binary_tree_grundy_nim.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Model the prefix-free string game on a complete binary tree of depth L as an independent sum of games on missing subtrees in the trie, where each full binary subtree of depth d has Grundy value lowbit(L - d).

## 2. Core Observation & Invariant
Any available subtree in the trie is completely disjoint from all other available subtrees, making the game an impartial sum of independent games. A full binary tree with distance h to leaves has Grundy value equal to lowbit(h + 1) = lowbit(L - d).

## 3. Step-by-Step Algorithm
1. 1. Insert all N strings into a binary Trie of maximum depth L.
2. 2. For each node in the Trie at depth d, if a child branch is missing, calculate its Grundy contribution as lowbit(L - d) = (L - d) & (-(L - d)).
3. 3. XOR all Grundy values together.
4. 4. If the total XOR sum is non-zero, Alice wins; otherwise, Bob wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(sum |S_i|)`
- **Space Complexity**: `O(sum |S_i|)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Node {
    int left = -1;
    int right = -1;
    ll depth = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll L;
    if (!(cin >> n >> L)) return 0;

    vector<Node> trie;
    trie.push_back({-1, -1, 0});

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        int cur = 0;
        for (char ch : s) {
            if (ch == '0') {
                if (trie[cur].left == -1) {
                    trie[cur].left = (int)trie.size();
                    trie.push_back({-1, -1, trie[cur].depth + 1});
                }
                cur = trie[cur].left;
            } else {
                if (trie[cur].right == -1) {
                    trie[cur].right = (int)trie.size();
                    trie.push_back({-1, -1, trie[cur].depth + 1});
                }
                cur = trie[cur].right;
            }
        }
    }

    ll xor_sum = 0;
    for (size_t i = 0; i < trie.size(); i++) {
        ll d = trie[i].depth;
        if (trie[i].left == -1) {
            ll h_plus_1 = L - d;
            xor_sum ^= (h_plus_1 & (-h_plus_1));
        }
        if (trie[i].right == -1) {
            ll h_plus_1 = L - d;
            xor_sum ^= (h_plus_1 & (-h_plus_1));
        }
    }

    if (xor_sum != 0) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

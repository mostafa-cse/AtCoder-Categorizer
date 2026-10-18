# Problem Analysis: AtCoder-abc268_h — Ex. Taboo

**Problem ID**: `AtCoder-abc268_h`  
**Contest**: `abc268`  
**Rating / Difficulty**: 2560  
**URL**: https://atcoder.jp/contests/abc268/tasks/abc268_h  
**VJudge Tag**: `[problem:AtCoder-abc268_h]`  
**Category File**: [`../categories/strings/taboo_aho_corasick_greedy_censoring.md`](../categories/strings/taboo_aho_corasick_greedy_censoring.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Aho Corasick`  
- **Topic (Skill)**: `Aho Corasick`  

---

## 1. Problem Statement & Key Idea
Given string $S$ and $N$ forbidden substrings $T_1 \dots T_N$, find the minimum character modifications to make $S$ contain no $T_i$ as a substring. Build the Aho-Corasick automaton on $T_1 \dots T_N$. Mark any node as forbidden if it matches a $T_i$ or its suffix link points to a forbidden node. Walk through $S$ character by character: the moment we enter a forbidden node, we greedily modify the current character to a wildcard, resetting the automaton state to root.

## 2. Core Observation & Invariant
Greedy choice property: modifying the rightmost character of the detected forbidden substring maximizes disruption to any future overlapping forbidden substrings. When the current character is modified, the automaton resets to the root in $O(1)$ time, guaranteeing minimum total modifications.

## 3. Step-by-Step Algorithm
1. 1. Insert all strings $T_1 \dots T_N$ into a trie.
2. 2. Compute failure links via BFS to build the Aho-Corasick automaton.
3. 3. Propagate `is_bad` flags along suffix links.
4. 4. Walk through string $S$ starting at root node 0.
5. 5. If the next state is marked `is_bad`, increment modification count and reset state to root 0.
6. 6. Output total modifications.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + \sum |T_i| \cdot \Sigma)`
- **Space Complexity**: `O(\sum |T_i| \cdot \Sigma)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int next_node[26];
    int link;
    bool is_bad;
    Node() {
        for (int i = 0; i < 26; ++i) next_node[i] = 0;
        link = 0;
        is_bad = false;
    }
};

vector<Node> trie;

void insert(const string& s) {
    int u = 0;
    for (char c : s) {
        int ch = c - 'a';
        if (trie[u].next_node[ch] == 0) {
            trie[u].next_node[ch] = trie.size();
            trie.emplace_back();
        }
        u = trie[u].next_node[ch];
    }
    trie[u].is_bad = true;
}

void build_ac() {
    queue<int> q;
    for (int c = 0; c < 26; ++c) {
        int v = trie[0].next_node[c];
        if (v != 0) {
            trie[v].link = 0;
            q.push(v);
        }
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (trie[trie[u].link].is_bad) {
            trie[u].is_bad = true;
        }

        for (int c = 0; c < 26; ++c) {
            int v = trie[u].next_node[c];
            if (v != 0) {
                trie[v].link = trie[trie[u].link].next_node[c];
                q.push(v);
            } else {
                trie[u].next_node[c] = trie[trie[u].link].next_node[c];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int n;
    cin >> n;

    trie.emplace_back(); // root = 0

    for (int i = 0; i < n; ++i) {
        string t;
        cin >> t;
        insert(t);
    }

    build_ac();

    int u = 0;
    int ops = 0;
    for (char c : s) {
        int ch = c - 'a';
        u = trie[u].next_node[ch];
        if (trie[u].is_bad) {
            ops++;
            u = 0; // greedy reset
        }
    }

    cout << ops << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

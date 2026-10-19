# Problem Analysis: AtCoder-agc044_c — C. Strange Dance

**Problem ID**: `AtCoder-agc044_c`  
**Contest**: `agc044`  
**Rating / Difficulty**: 2889  
**URL**: https://atcoder.jp/contests/agc044/tasks/agc044_c  
**VJudge Tag**: `[problem:AtCoder-agc044_c]`  
**Category File**: [`../categories/data_structures/ternary_trie_lazy_carry.md`](../categories/data_structures/ternary_trie_lazy_carry.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
3^N people arranged in a circle labeled 0 to 3^N - 1 in base 3 dance according to operations 'S' (shift x -> x + 1 mod 3^N) and 'R' (reverse positions). Find final positions of all people.

## 2. Core Observation & Invariant
Represent the 3^N positions in a ternary trie of depth N. Operation 'R' swaps children 1 and 2 at every trie node, maintained by a lazy flip tag in O(1). Operation 'S' adds 1 in ternary: child 0 becomes 1, child 1 becomes 2, child 2 becomes 0 with carry propagating down child 2 in amortized O(N) time. After processing all operations, push down tags via DFS to recover each person's final position.

## 3. Step-by-Step Algorithm
1. 1. Build ternary trie of depth N with 3^N leaves.
2. 2. Maintain lazy swap tags and child pointers at each node.
3. 3. For 'R': toggle lazy flip tag at root.
4. 4. For 'S': cyclically shift children (0->1, 1->2, 2->0) and push carry into child 2.
5. 5. Traverse trie to output final coordinates for all 3^N people.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 3^N + |T| * N)`
- **Space Complexity**: `O(3^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Node {
    int child[3];
    int val;
    bool lazy;
};

const int MAX_NODES = 800000;
Node tree_nodes[MAX_NODES];
int node_cnt = 0;

int new_node(int val = -1) {
    int id = ++node_cnt;
    tree_nodes[id].child[0] = tree_nodes[id].child[1] = tree_nodes[id].child[2] = 0;
    tree_nodes[id].val = val;
    tree_nodes[id].lazy = false;
    return id;
}

int build_trie(int depth, int max_depth, int path_val, int base) {
    int u = new_node();
    if (depth == max_depth) {
        tree_nodes[u].val = path_val;
        return u;
    }
    for (int t = 0; t < 3; ++t) {
        tree_nodes[u].child[t] = build_trie(depth + 1, max_depth, path_val + t * base, base * 3);
    }
    return u;
}

inline void push(int u) {
    if (tree_nodes[u].lazy) {
        if (tree_nodes[u].child[0]) {
            swap(tree_nodes[u].child[1], tree_nodes[u].child[2]);
            for (int t = 0; t < 3; ++t) {
                int c = tree_nodes[u].child[t];
                tree_nodes[c].lazy = !tree_nodes[c].lazy;
            }
        }
        tree_nodes[u].lazy = false;
    }
}

void apply_R(int u) {
    if (!tree_nodes[u].child[0]) return;
    push(u);
    int c0 = tree_nodes[u].child[0];
    int c1 = tree_nodes[u].child[1];
    int c2 = tree_nodes[u].child[2];
    apply_R(c2);
    tree_nodes[u].child[0] = c2;
    tree_nodes[u].child[1] = c0;
    tree_nodes[u].child[2] = c1;
}

void collect_ans(int u, int depth, int max_depth, int cur_pos, int base, vector<int>& ans) {
    push(u);
    if (depth == max_depth) {
        ans[tree_nodes[u].val] = cur_pos;
        return;
    }
    for (int t = 0; t < 3; ++t) {
        collect_ans(tree_nodes[u].child[t], depth + 1, max_depth, cur_pos + t * base, base * 3, ans);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string t;
    if (!(cin >> n >> t)) return 0;

    node_cnt = 0;
    int root = build_trie(0, n, 0, 1);

    for (char ch : t) {
        if (ch == 'S') {
            tree_nodes[root].lazy = !tree_nodes[root].lazy;
        } else if (ch == 'R') {
            apply_R(root);
        }
    }

    int total_people = 1;
    for (int i = 0; i < n; ++i) total_people *= 3;
    vector<int> ans(total_people);

    collect_ans(root, 0, n, 0, 1, ans);

    for (int i = 0; i < total_people; ++i) {
        cout << ans[i] << (i + 1 == total_people ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

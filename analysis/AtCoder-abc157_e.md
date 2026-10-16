# Problem Analysis: AtCoder-abc157_e — Simple String Queries

**Problem ID**: `AtCoder-abc157_e`  
**Contest**: `abc157`  
**Rating / Difficulty**: 1443  
**URL**: https://atcoder.jp/contests/abc157/tasks/abc157_e  
**VJudge Tag**: `[problem:AtCoder-abc157_e]`  
**Category File**: [`../categories/data_structures/alphabet_frequency_fenwick_trees.md`](../categories/data_structures/alphabet_frequency_fenwick_trees.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Fenwick Tree`  
- **Topic (Skill)**: `Alphabet Frequency Fenwick Trees / Ordered Sets`  

---

## 1. Problem Statement & Key Idea
Given a string S of length N. Process Q queries of two types: 1) update character at index i to c; 2) count the number of distinct characters in substring S[l..r].

**Key Insight**: Maintain 26 separate Fenwick trees (one per character 'a'..'z'). Update in O(log N) and query distinct count by summing over all 26 characters if their range count > 0 in O(26 log N).

## 2. Core Observation & Invariant
Because the alphabet size sigma = 26 is tiny, answering range distinct queries decomposes into 26 independent range sum queries checking if count > 0.

## 3. Step-by-Step Algorithm
1. Initialize 26 Fenwick trees of size N.
2. For each character S[i], add +1 at position i in tree S[i] - 'a'.
3. For query type 1 (update i to c):
4.   Let old_c = S[i]. If old_c == c, continue.
5.   Subtract 1 at i in old_c tree, add 1 at i in c tree, update S[i] = c.
6. For query type 2 (range [l, r]):
7.   Count characters c where query(r) - query(l - 1) > 0.
8.   Print count.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) * 26 * log N)`
- **Space Complexity**: `O(26 * N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) const {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    int range_query(int l, int r) const {
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    vector<Fenwick> bits(26, Fenwick(n));
    for (int i = 0; i < n; ++i) {
        bits[s[i] - 'a'].add(i + 1, 1);
    }

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int idx;
            char c;
            cin >> idx >> c;
            if (s[idx - 1] != c) {
                bits[s[idx - 1] - 'a'].add(idx, -1);
                bits[c - 'a'].add(idx, 1);
                s[idx - 1] = c;
            }
        } else {
            int l, r;
            cin >> l >> r;
            int distinct = 0;
            for (int c = 0; c < 26; ++c) {
                if (bits[c].range_query(l, r) > 0) {
                    distinct++;
                }
            }
            cout << distinct << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Alphabet-decomposed Binary Indexed Trees for distinct character range frequency queries.
- **Reusable Pattern**: `Small Alphabet Range Queries: 26 Fenwick trees with range sum > 0 check.`

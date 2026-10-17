# Problem Analysis: AtCoder-abc308_g — Minimum Xor Pair Query

**Problem ID**: `AtCoder-abc308_g`  
**Contest**: `abc308`  
**Rating / Difficulty**: 2008  
**URL**: https://atcoder.jp/contests/abc308/tasks/abc308_g  
**VJudge Tag**: `[problem:AtCoder-abc308_g]`  
**Category File**: [`../categories/data_structures/dynamic_min_xor_adjacent_multiset.md`](../categories/data_structures/dynamic_min_xor_adjacent_multiset.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Queue & Priority Queue`  
- **Topic (Skill)**: `Dynamic Minimum XOR Pair Maintenance via Adjacent Elements in Sorted Multiset`  

---

## 1. Problem Statement & Key Idea
Maintain a multiset S under queries: 1 x (add x), 2 x (remove x), 3 (find min_{u != v} u XOR v).

**Key Idea**: In any sorted array a_1 <= a_2 <= ... <= a_k, the minimum XOR pair is always formed by two adjacent elements: min_{i < j} (a_i XOR a_j) = min_{1 <= i < k} (a_i XOR a_{i+1}). This follows from Trie properties, as adjacent elements share the longest common binary prefix. We maintain elements in a sorted std::multiset<int> S, and adjacent differences in another std::multiset<int> diffs. Insertions and deletions update only adjacent pairs in O(log |S|).

## 2. Core Observation & Invariant
In-order traversal order of a Binary Trie matches standard integer sorting, ensuring that minimal XOR pairs are always adjacent.

## 3. Step-by-Step Algorithm
1. Maintain multiset S of elements and multiset diffs of adjacent XOR values.
2. On insert(x):
3.   Find successor it = S.lower_bound(x).
4.   If it != S.end() and it != S.begin(): remove (*prev(it) ^ *it) from diffs.
5.   If it != S.end(): add (x ^ *it) to diffs.
6.   If it != S.begin(): add (*prev(it) ^ x) to diffs.
7.   Insert x into S.
8. On remove(x):
9.   Find iterator it = S.find(x).
10.   If it != S.begin(): remove (*prev(it) ^ x) from diffs.
11.   If next(it) != S.end(): remove (x ^ *next(it)) from diffs.
12.   If it != S.begin() and next(it) != S.end(): add (*prev(it) ^ *next(it)) to diffs.
13.   Erase it from S.
14. On query: print *diffs.begin().

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log Q)`
- **Space Complexity**: `O(Q)`

## 5. Core Algorithmic Skill & Learning Takeaway
Adjacent XOR pair property in sorted collections and dynamic multiset updates.

**Reusable Pattern**: Sorted Adjacent XOR Property: min_{u != v} (u ^ v) = min_{adjacent} (a_i ^ a_{i+1}) maintained via dual multisets.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<int> s;
    multiset<int> diffs;

    auto add_diff = [&](int val) {
        diffs.insert(val);
    };

    auto remove_diff = [&](int val) {
        auto it = diffs.find(val);
        if (it != diffs.end()) {
            diffs.erase(it);
        }
    };

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            auto it = s.lower_bound(x);
            if (it != s.end() && it != s.begin()) {
                remove_diff(*prev(it) ^ *it);
            }
            if (it != s.end()) {
                add_diff(x ^ *it);
            }
            if (it != s.begin()) {
                add_diff(*prev(it) ^ x);
            }
            s.insert(x);
        } else if (type == 2) {
            int x;
            cin >> x;
            auto it = s.find(x);
            auto prv = (it != s.begin() ? prev(it) : s.end());
            auto nxt = next(it);

            if (prv != s.end()) {
                remove_diff(*prv ^ x);
            }
            if (nxt != s.end()) {
                remove_diff(x ^ *nxt);
            }
            if (prv != s.end() && nxt != s.end()) {
                add_diff(*prv ^ *nxt);
            }
            s.erase(it);
        } else {
            cout << *diffs.begin() << "\n";
        }
    }

    return 0;
}
```

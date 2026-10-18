# Problem Analysis: AtCoder-abc324_g — G. Generate Arrays

**Problem ID**: `AtCoder-abc324_g`  
**Contest**: `abc324`  
**Rating / Difficulty**: 2501  
**URL**: https://atcoder.jp/contests/abc324/tasks/abc324_g  
**VJudge Tag**: `[problem:AtCoder-abc324_g]`  
**Category File**: [`../categories/data_structures_ds/generate_arrays_small_to_large_split_treap.md`](../categories/data_structures_ds/generate_arrays_small_to_large_split_treap.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Balanced Binary Search Tree (BBST)`  
- **Topic (Skill)**: `Persistent Treap`  

---

## 1. Problem Statement & Key Idea
Maintain arrays under operations: split by prefix length (type 1) and split by value threshold (type 2). Output the size of each newly generated array.

## 2. Core Observation & Invariant
Elements in every array preserve their original index $pos$. Represent each array as dual balanced sets sorted by $pos$ and by $val$. For both split-by-index and split-by-value, identify the smaller side using bidirectional finger search. Extract the smaller side and insert into the target array, swapping pointers if the left side was smaller. By small-to-large splitting, each element moves at most $O(\log N)$ times.

## 3. Step-by-Step Algorithm
1. 1. Maintain for each array $s$ two `std::set`: `by_pos` and `by_val`.
2. 2. For type 1 (split by index $x$): compare $x$ with $|A_s| / 2$. Extract the smaller partition, swap containers if necessary, and reinsert.
3. 3. For type 2 (split by value $x$): advance iterators simultaneously from $val_{min}$ and $val_{max}$ to identify the smaller partition. Extract the smaller partition, swap containers if necessary, and reinsert.
4. 4. Output the size of the newly generated array $i$.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q + N \log^2 N)`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct ArrayData {
    set<pair<int, int>> by_pos;
    set<pair<int, int>> by_val;

    int size() const {
        return by_pos.size();
    }

    void insert(int pos, int val) {
        by_pos.insert({pos, val});
        by_val.insert({val, pos});
    }

    void erase(int pos, int val) {
        by_pos.erase({pos, val});
        by_val.erase({val, pos});
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    int q;
    if (!(cin >> q)) return 0;

    vector<ArrayData> seqs(q + 1);
    for (int i = 0; i < n; ++i) {
        seqs[0].insert(i + 1, a[i]);
    }

    for (int i = 1; i <= q; ++i) {
        int t, s, x;
        cin >> t >> s >> x;
        auto &cur = seqs[s];
        auto &nxt = seqs[i];

        if (t == 1) {
            int sz = cur.size();
            if (x >= sz) {
                // nxt is empty
            } else if (x == 0) {
                swap(cur, nxt);
            } else if (x <= sz / 2) {
                // left side is smaller
                vector<pair<int, int>> extracted;
                auto it = cur.by_pos.begin();
                for (int c = 0; c < x; ++c) {
                    extracted.push_back(*it);
                    it++;
                }
                for (auto &p : extracted) {
                    cur.erase(p.first, p.second);
                }
                swap(cur, nxt);
                for (auto &p : extracted) {
                    cur.insert(p.first, p.second);
                }
            } else {
                // right side is smaller
                int cnt = sz - x;
                vector<pair<int, int>> extracted;
                auto it = cur.by_pos.rbegin();
                for (int c = 0; c < cnt; ++c) {
                    extracted.push_back(*it);
                    it++;
                }
                for (auto &p : extracted) {
                    cur.erase(p.first, p.second);
                }
                for (auto &p : extracted) {
                    nxt.insert(p.first, p.second);
                }
            }
        } else {
            // t == 2: val <= x stay in s, val > x move to i
            if (cur.size() == 0 || cur.by_val.rbegin()->first <= x) {
                // all <= x, nxt is empty
            } else if (cur.by_val.begin()->first > x) {
                // all > x, nxt gets everything
                swap(cur, nxt);
            } else {
                // determine which side is smaller
                auto it_l = cur.by_val.begin();
                auto it_r = cur.by_val.rbegin();
                bool left_smaller = false;
                while (true) {
                    if (it_l->first > x) {
                        left_smaller = true;
                        break;
                    }
                    if (it_r->first <= x) {
                        left_smaller = false;
                        break;
                    }
                    it_l++;
                    it_r++;
                }

                if (left_smaller) {
                    vector<pair<int, int>> extracted;
                    for (auto it = cur.by_val.begin(); it != cur.by_val.end() && it->first <= x; ++it) {
                        extracted.push_back({it->second, it->first});
                    }
                    for (auto &p : extracted) {
                        cur.erase(p.first, p.second);
                    }
                    swap(cur, nxt);
                    for (auto &p : extracted) {
                        cur.insert(p.first, p.second);
                    }
                } else {
                    vector<pair<int, int>> extracted;
                    for (auto it = cur.by_val.rbegin(); it != cur.by_val.rend() && it->first > x; ++it) {
                        extracted.push_back({it->second, it->first});
                    }
                    for (auto &p : extracted) {
                        cur.erase(p.first, p.second);
                    }
                    for (auto &p : extracted) {
                        nxt.insert(p.first, p.second);
                    }
                }
            }
        }
        cout << nxt.size() << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

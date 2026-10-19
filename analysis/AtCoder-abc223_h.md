# Problem Analysis: AtCoder-abc223_h — H - Xor Query

**Problem ID**: `AtCoder-abc223_h`  
**Contest**: `abc223`  
**Rating / Difficulty**: 2771  
**URL**: https://atcoder.jp/contests/abc223/tasks/abc223_h  
**VJudge Tag**: `[problem:AtCoder-abc223_h]`  
**Category File**: [`../categories/math/range_xor_basis_prefix_greedy.md`](../categories/math/range_xor_basis_prefix_greedy.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers and Q queries (L, R, X), determine whether X can be formed as the XOR sum of some subsequence of A[L..R].

## 2. Core Observation & Invariant
A linear basis over GF(2) with greedy index tracking can answer range subset XOR queries without segment trees. In the prefix XOR basis for prefix R, each basis vector basis[b] retains the latest position pos[b] among the elements that contributed to that basis vector. When inserting (A[i], i), if bit b is set and basis[b] already exists, we greedily keep the element with the larger index as basis[b] and continue inserting the swapped out element. To query (L, R, X), we only reduce X with basis vectors in prefix R whose pos[b] >= L. If X reduces to 0, it lies in the span of A[L..R].

## 3. Step-by-Step Algorithm
1. 1. Build prefix bases for i = 1 to N. Each state holds basis[60] and pos[60].
2. 2. When transitioning from i - 1 to i, copy basis and pos. Let cur_val = A[i], cur_pos = i.
3. 3. Iterate bit b from 59 down to 0: if bit b of cur_val is 1:
4.    a. If basis[b] is empty, set basis[b] = cur_val, pos[b] = cur_pos, and terminate.
5.    b. If cur_pos > pos[b], swap (cur_val, cur_pos) with (basis[b], pos[b]).
6.    c. Set cur_val ^= basis[b].
7. 4. For each query (L, R, X), take the basis at prefix R. Iterate bit b from 59 down to 0:
8.    If bit b of X is 1 and pos[R][b] >= L, set X ^= basis[R][b].
9. 5. If X == 0, output 'Yes'; else output 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) * B) where B = 60`
- **Space Complexity**: `O(N * B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Query {
    int id;
    int l;
    long long x;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    vector<vector<Query>> queries_at(N + 1);
    for (int i = 0; i < Q; ++i) {
        int l, r;
        long long x;
        cin >> l >> r >> x;
        queries_at[r].push_back({i, l, x});
    }

    vector<long long> basis(60, 0);
    vector<int> pos(60, 0);
    vector<bool> ans(Q, false);

    for (int r = 1; r <= N; ++r) {
        long long cur_val = A[r];
        int cur_pos = r;

        for (int b = 59; b >= 0; --b) {
            if ((cur_val >> b) & 1) {
                if (basis[b] == 0) {
                    basis[b] = cur_val;
                    pos[b] = cur_pos;
                    break;
                }
                if (pos[b] < cur_pos) {
                    swap(basis[b], cur_val);
                    swap(pos[b], cur_pos);
                }
                cur_val ^= basis[b];
            }
        }

        for (const auto& q : queries_at[r]) {
            long long rem = q.x;
            for (int b = 59; b >= 0; --b) {
                if ((rem >> b) & 1) {
                    if (basis[b] != 0 && pos[b] >= q.l) {
                        rem ^= basis[b];
                    }
                }
            }
            if (rem == 0) {
                ans[q.id] = true;
            }
        }
    }

    for (int i = 0; i < Q; ++i) {
        if (ans[i]) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

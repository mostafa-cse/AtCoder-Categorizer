# Problem Analysis: AtCoder-agc058_c — C - Planar Tree

**Problem ID**: `AtCoder-agc058_c`  
**Contest**: `agc058`  
**Rating / Difficulty**: 2991  
**URL**: https://atcoder.jp/contests/agc058/tasks/agc058_c  
**VJudge Tag**: `[problem:AtCoder-agc058_c]`  
**Category File**: [`../categories/basics/circular_stack_reduction_planar_tree_invariant.md`](../categories/basics/circular_stack_reduction_planar_tree_invariant.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Standard Template Library (STL)`  
- **Topic (Skill)**: `Stack`  

---

## 1. Problem Statement & Key Idea
Given a circular sequence of vertex degrees A_1, ..., A_N in {1, 2, 3, 4}, determine if there exists a planar tree embedded in the plane with these cyclic boundary degrees.

## 2. Core Observation & Invariant
A planar tree embedding allows contractible boundary leaves. Consecutive duplicate values merge. A degree-1 leaf adjacent to 2 can be contracted, and a degree-4 node adjacent to 3 can be contracted. Repeatedly simulating these reductions on the circular sequence using a circular doubly-linked list / stack until no further operations are possible reveals that a valid tree exists if and only if the reduced cycle satisfies count(2) > count(4) and count(3) > count(1).

## 3. Step-by-Step Algorithm
1. 1. Represent the circular sequence using doubly linked list arrays (prv, nxt, val, active).
2. 2. Push candidates for adjacent identical values, 1-2 pairs, and 4-3 pairs into a processing queue.
3. 3. Process reductions: merge duplicates; eliminate 1 adjacent to 2; eliminate 4 adjacent to 3. Update links and re-enqueue affected neighbors.
4. 4. Once stabilized, count frequencies of 1, 2, 3, 4 in the active circular component.
5. 5. Output Yes if cnt[2] > cnt[4] and cnt[3] > cnt[1], otherwise No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<int> prev_node(N), next_node(N);
    vector<bool> deleted(N, false);

    for (int i = 0; i < N; ++i) {
        prev_node[i] = (i - 1 + N) % N;
        next_node[i] = (i + 1) % N;
    }

    queue<int> q; // stores index of node that might be deleted, or pair check

    // Check if node u can be deleted due to neighbor v
    auto check_delete = [&](int u, int v) -> bool {
        if (deleted[u] || deleted[v]) return false;
        if (A[u] == A[v]) return true; // u can be deleted
        if (A[u] == 1 && A[v] == 2) return true;
        if (A[u] == 4 && A[v] == 3) return true;
        return false;
    };

    // We can push nodes that should be deleted
    // To be clean: check all directed edges (u, next[u])
    for (int i = 0; i < N; ++i) {
        int nxt = next_node[i];
        if (check_delete(i, nxt)) {
            q.push(i);
        } else if (check_delete(nxt, i)) {
            q.push(nxt);
        }
    }

    int remaining = N;
    while (!q.empty() && remaining > 1) {
        int u = q.front();
        q.pop();
        if (deleted[u]) continue;

        int p = prev_node[u];
        int n = next_node[u];

        if (!check_delete(u, p) && !check_delete(u, n)) {
            continue;
        }

        // Delete u
        deleted[u] = true;
        remaining--;
        next_node[p] = n;
        prev_node[n] = p;

        if (remaining <= 1) break;

        // Check if p or n can be deleted now
        if (check_delete(p, n)) q.push(p);
        else if (check_delete(n, p)) q.push(n);

        int pp = prev_node[p];
        if (check_delete(p, pp)) q.push(p);
        int nn = next_node[n];
        if (check_delete(n, nn)) q.push(n);
    }

    int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    for (int i = 0; i < N; ++i) {
        if (!deleted[i]) {
            if (A[i] == 1) c1++;
            else if (A[i] == 2) c2++;
            else if (A[i] == 3) c3++;
            else if (A[i] == 4) c4++;
        }
    }

    if (c2 > c4 && c3 > c1) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

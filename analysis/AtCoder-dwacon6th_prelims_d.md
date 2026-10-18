# Problem Analysis: AtCoder-dwacon6th_prelims_d — D - Arrangement

**Problem ID**: `AtCoder-dwacon6th_prelims_d`  
**Contest**: `dwacon6th_prelims`  
**Rating / Difficulty**: 2589  
**URL**: https://atcoder.jp/contests/dwacon6th_prelims/tasks/dwacon6th_prelims_d  
**VJudge Tag**: `[problem:AtCoder-dwacon6th_prelims_d]`  
**Category File**: [`../categories/graph_theory/arrangement_halls_marriage_greedy.md`](../categories/graph_theory/arrangement_halls_marriage_greedy.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Halls Theorem`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest permutation $P$ of $(1, 2, \dots, N)$ such that $P_{i+1} \ne a_{P_i}$ for all $1 \le i \le N-1$.

## 2. Core Observation & Invariant
Consider the directed complement graph where forbidden transitions $u \to a_u$ are deleted. We need a Hamiltonian path in this graph. By Hall's Marriage Theorem / Tutte's criterion, a valid continuation exists from current vertex $u$ iff no unvisited vertex $v$ has in-degree $|V_{\text{remaining}}| - 1$ in the forbidden graph (i.e. is forbidden from all remaining vertices). Thus, we can greedily select the smallest available candidate that preserves Hall's condition.

## 3. Step-by-Step Algorithm
1. 1. Maintain the frequency of incoming forbidden edges for all remaining vertices.
2. 2. At each position $i = 1 \dots N$, iterate over available candidates $c$ in ascending numerical order.
3. 3. Check if placing $c$ is valid ($c \ne a_{\text{prev}}$) and if the remaining subproblem satisfies Hall's condition (no vertex has in-degree equal to remaining count).
4. 4. Select the first valid $c$ and update degree counts.
5. 5. If at any step no valid candidate exists, report -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    if (N == 2) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> in_deg(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        in_deg[A[i]]++;
    }

    set<int> V;
    for (int i = 1; i <= N; ++i) V.insert(i);

    auto can_start = [&](int s) -> bool {
        int sz = V.size();
        if (sz == 1) return true;
        if (sz == 2) {
            int other = (s == *V.begin() ? *V.rbegin() : *V.begin());
            return A[s] != other;
        }
        if (sz == 3) {
            vector<int> others;
            for (int x : V) if (x != s) others.push_back(x);
            int u = others[0], v = others[1];
            if (A[u] == v && A[v] == u) return false;
            int in_u = (A[s] == u ? 1 : 0) + (A[v] == u ? 1 : 0);
            int in_v = (A[s] == v ? 1 : 0) + (A[u] == v ? 1 : 0);
            if (in_u == 2 || in_v == 2) return false;
            return true;
        }

        // sz > 3:
        for (int w : V) {
            if (w != s) {
                // If w is A[s], its in-degree inside V without s would be in_deg[w] - 1
                int d = in_deg[w] - (A[s] == w ? 1 : 0);
                if (d == sz - 1) return false;
            }
        }
        return true;
    };

    int start_v = -1;
    for (int s = 1; s <= N; ++s) {
        if (can_start(s)) {
            start_v = s;
            break;
        }
    }

    if (start_v == -1) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> path;
    int cur = start_v;
    path.push_back(cur);
    V.erase(cur);
    in_deg[A[cur]]--;

    while (!V.empty()) {
        int nxt = -1;
        for (int cand : V) {
            if (A[cur] != cand && can_start(cand)) {
                nxt = cand;
                break;
            }
        }
        if (nxt == -1) {
            cout << -1 << "\n";
            return 0;
        }
        cur = nxt;
        path.push_back(cur);
        V.erase(cur);
        in_deg[A[cur]]--;
    }

    for (int i = 0; i < N; ++i) {
        cout << path[i] << (i + 1 == N ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

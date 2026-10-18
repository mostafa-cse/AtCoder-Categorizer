# Problem Analysis: AtCoder-abc319_f — F. Fighter Takahashi

**Problem ID**: `AtCoder-abc319_f`  
**Contest**: `abc319`  
**Rating / Difficulty**: 2480  
**URL**: https://atcoder.jp/contests/abc319/tasks/abc319_f  
**VJudge Tag**: `[problem:AtCoder-abc319_f]`  
**Category File**: [`../categories/dynamic_programming_dp/fighter_takahashi_tree_bitmask_pq_dp.md`](../categories/dynamic_programming_dp/fighter_takahashi_tree_bitmask_pq_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Explore a rooted tree with enemies (add strength $g_u$ if $\ge s_u$) and $\le 10$ medicines (multiply strength by $g_u$). Determine if all enemies can be defeated.

## 2. Core Observation & Invariant
Greedy rule: Always defeat all currently defeatable enemies before consuming any medicine (addition before multiplication strictly dominates). Since there are at most $K \le 10$ medicines, perform bitmask DP over the subset of consumed medicines. From state $mask$, greedily expand reachable enemies via a min-priority queue, then transition to $mask \mid (1 \ll m)$ for each accessible medicine $m$.

## 3. Step-by-Step Algorithm
1. 1. Extract the $K \le 10$ medicine vertices and index them $0 \dots K-1$.
2. 2. Define $DP[mask]$ as the maximum strength achieved with medicine subset $mask$.
3. 3. From each valid state, pop all enemies from the min-heap with requirement $\le \text{strength}$, adding $g_u$ to strength (capped at $10^9$) and discovering new neighbors.
4. 4. If all enemies are defeated, output `Yes`.
5. 5. For each accessible unused medicine, take the medicine and transition to the new mask.
6. 6. If no state defeats all enemies, output `No`.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^K (N \log N))`
- **Space Complexity**: `O(2^K + N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct State {
    long long strength;
    int defeated_count;
    vector<pair<long long, int>> pq;
    vector<int> meds;
    vector<uint8_t> visited;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> type_v(n + 1, 0);
    vector<long long> s_v(n + 1, 0), g_v(n + 1, 0);
    vector<int> med_list;
    vector<int> med_idx(n + 1, -1);

    int total_enemies = 0;
    for (int i = 2; i <= n; ++i) {
        int p, t;
        long long s, g;
        cin >> p >> t >> s >> g;
        adj[p].push_back(i);
        type_v[i] = t;
        s_v[i] = s;
        g_v[i] = g;
        if (t == 2) {
            med_idx[i] = med_list.size();
            med_list.push_back(i);
        } else {
            total_enemies++;
        }
    }

    int K = med_list.size();

    auto expand = [&](long long strength, vector<uint8_t> visited,
                      priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq,
                      vector<int> meds, int def_count) {
        while (!pq.empty() && pq.top().first <= strength) {
            auto top = pq.top();
            pq.pop();
            int u = top.second;
            strength = min((long long)1e9, strength + g_v[u]);
            def_count++;
            visited[u] = 1;
            for (int v : adj[u]) {
                if (!visited[v]) {
                    if (type_v[v] == 1) {
                        pq.push({s_v[v], v});
                    } else {
                        meds.push_back(v);
                    }
                }
            }
        }
        return make_tuple(strength, visited, pq, meds, def_count);
    };

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> init_pq;
    vector<int> init_meds;
    vector<uint8_t> init_vis(n + 1, 0);
    init_vis[1] = 1;
    for (int c : adj[1]) {
        if (type_v[c] == 1) init_pq.push({s_v[c], c});
        else init_meds.push_back(c);
    }

    auto initial = expand(1, init_vis, init_pq, init_meds, 0);
    long long s0 = get<0>(initial);
    int cnt0 = get<4>(initial);
    if (cnt0 == total_enemies) {
        cout << "Yes\n";
        return 0;
    }

    vector<long long> dp(1 << K, -1);
    vector<bool> has_state(1 << K, false);
    vector<State> states(1 << K);

    dp[0] = s0;
    has_state[0] = true;
    auto pq0 = get<2>(initial);
    vector<pair<long long, int>> pq0_vec;
    while (!pq0.empty()) {
        pq0_vec.push_back(pq0.top());
        pq0.pop();
    }
    states[0] = {s0, cnt0, pq0_vec, get<3>(initial), get<1>(initial)};

    for (int mask = 0; mask < (1 << K); ++mask) {
        if (!has_state[mask]) continue;
        const auto &cur = states[mask];
        if (cur.defeated_count == total_enemies) {
            cout << "Yes\n";
            return 0;
        }

        for (int m_vert : cur.meds) {
            int b = med_idx[m_vert];
            if (!(mask & (1 << b))) {
                int nxt_mask = mask | (1 << b);
                long long nxt_s = min((long long)1e9, cur.strength * g_v[m_vert]);
                vector<uint8_t> nxt_vis = cur.visited;
                nxt_vis[m_vert] = 1;
                priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> nxt_pq;
                for (auto &item : cur.pq) nxt_pq.push(item);
                vector<int> nxt_meds;
                for (int m : cur.meds) if (m != m_vert) nxt_meds.push_back(m);
                for (int v : adj[m_vert]) {
                    if (!nxt_vis[v]) {
                        if (type_v[v] == 1) nxt_pq.push({s_v[v], v});
                        else nxt_meds.push_back(v);
                    }
                }

                auto res = expand(nxt_s, nxt_vis, nxt_pq, nxt_meds, cur.defeated_count);
                long long exp_s = get<0>(res);
                int exp_cnt = get<4>(res);
                if (exp_cnt == total_enemies) {
                    cout << "Yes\n";
                    return 0;
                }

                if (exp_s > dp[nxt_mask]) {
                    dp[nxt_mask] = exp_s;
                    has_state[nxt_mask] = true;
                    auto res_pq = get<2>(res);
                    vector<pair<long long, int>> res_pq_vec;
                    while (!res_pq.empty()) {
                        res_pq_vec.push_back(res_pq.top());
                        res_pq.pop();
                    }
                    states[nxt_mask] = {exp_s, exp_cnt, res_pq_vec, get<3>(res), get<1>(res)};
                }
            }
        }
    }

    cout << "No\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

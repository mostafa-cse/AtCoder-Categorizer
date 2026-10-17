# Problem Analysis: AtCoder-abc365_g — G. AtCoder Office

**Problem ID**: `AtCoder-abc365_g`  
**Contest**: `abc365`  
**Rating / Difficulty**: 2254  
**URL**: https://atcoder.jp/contests/abc365/tasks/abc365_g  
**VJudge Tag**: `[problem:AtCoder-abc365_g]`  
**Category File**: [`../categories/data_structures/sqrt_decomposition_light_heavy_interval_overlap.md`](../categories/data_structures/sqrt_decomposition_light_heavy_interval_overlap.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Splitting Objects into Light and Heavy / Case Processing`  

---

## 1. Problem Statement & Key Idea
Given $M$ entry/exit timestamps for $N$ people at an office. Answer $Q$ queries: total duration during which both person $A$ and person $B$ were simultaneously inside the office.

## 2. Core Observation & Invariant
Each person has a collection of disjoint inside intervals. The sum of interval counts across all people is $M / 2 \le 10^5$. We partition people into Heavy ($> B$ intervals) and Light ($\le B$ intervals) with threshold $B \approx 700$. There are at most $M / (2B) \approx 140$ Heavy people. For each Heavy person, we precompute their overlap with all other people in $O(M)$ time via a single chronological sweep. For pairs of Light people, two pointers computes the intersection in $O(B)$ time.

## 3. Step-by-Step Algorithm
1. Group entry/exit records into disjoint intervals for each person.
2. Identify Heavy people with interval count $> 700$.
3. For each Heavy person, compute overlap with all people by sweeping event records in $O(M)$ time and store in a table.
4. For each query $(u, v)$: if either $u$ or $v$ is Heavy, answer in $O(1)$ from the precomputed table; otherwise, run two pointers over their intervals in $O(|I_u| + |I_v|) \le O(B)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \cdot \frac{M}{B} + Q \cdot B) = O(M \sqrt{M} + Q \sqrt{M})`
- **Space Complexity**: `O(N \cdot \frac{M}{B} + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int THRESHOLD = 700;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<pair<int, int>> records(M);
    for (int i = 0; i < M; ++i) {
        cin >> records[i].first >> records[i].second;
        records[i].second--; // 0-indexed
    }

    vector<vector<pair<int, int>>> inside_office(N);
    {
        vector<int> in_time(N, 0);
        for (const auto& [T, P] : records) {
            if (in_time[P]) {
                inside_office[P].emplace_back(in_time[P], T);
                in_time[P] = 0;
            } else {
                in_time[P] = T;
            }
        }
    }

    vector<int> heavy_list;
    vector<int> heavy_id(N, -1);
    for (int i = 0; i < N; ++i) {
        if ((int)inside_office[i].size() > THRESHOLD) {
            heavy_id[i] = heavy_list.size();
            heavy_list.push_back(i);
        }
    }

    int H = heavy_list.size();
    vector<vector<int>> heavy_ans(H, vector<int>(N, 0));

    for (int h = 0; h < H; ++h) {
        int target = heavy_list[h];
        vector<int> sum(N, 0);
        int prev_t = 0, i_sum = 0;
        bool i_inside = false;

        for (const auto& [T, P] : records) {
            if (P == target) {
                if (i_inside) {
                    i_sum += (T - prev_t);
                }
                prev_t = T;
                i_inside = !i_inside;
            }
            int cur_time = i_sum + (i_inside ? (T - prev_t) : 0);
            sum[P] = cur_time - sum[P];
        }

        heavy_ans[h] = move(sum);
    }

    int Q;
    if (!(cin >> Q)) return 0;

    while (Q--) {
        int u, v;
        cin >> u >> v;
        u--; v--;

        if (heavy_id[u] != -1) {
            cout << heavy_ans[heavy_id[u]][v] << "\n";
        } else if (heavy_id[v] != -1) {
            cout << heavy_ans[heavy_id[v]][u] << "\n";
        } else {
            // Both are light: two pointers
            const auto& list_u = inside_office[u];
            const auto& list_v = inside_office[v];
            int i = 0, j = 0;
            int total_overlap = 0;
            int sz_u = list_u.size();
            int sz_v = list_v.size();

            while (i < sz_u && j < sz_v) {
                int L = max(list_u[i].first, list_v[j].first);
                int R = min(list_u[i].second, list_v[j].second);
                if (L < R) {
                    total_overlap += (R - L);
                }
                if (list_u[i].second < list_v[j].second) {
                    i++;
                } else {
                    j++;
                }
            }
            cout << total_overlap << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc388_f — Dangerous Sugoroku

**Problem ID**: `AtCoder-abc388_f`  
**Contest**: `abc388`  
**Rating / Difficulty**: 2214  
**URL**: https://atcoder.jp/contests/abc388/tasks/abc388_f  
**VJudge Tag**: `[problem:AtCoder-abc388_f]`  
**Category File**: [`../categories/number_theory/chicken_mcnugget_dangerous_sugoroku_interval_compression.md`](../categories/number_theory/chicken_mcnugget_dangerous_sugoroku_interval_compression.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Euclidean Algorithm`  
- **Topic (Skill)**: `Chicken McNugget Theorem`  

---

## 1. Problem Statement & Key Idea
Determine whether square N can be reached from square 1 with jump lengths in [A, B] avoiding M dangerous intervals of length <= B on a line of size N <= 10^18.

## 2. Core Observation & Invariant
By the Chicken McNugget Theorem / Frobenius coin problem, any safe distance w >= B^2 - 3B + 2 <= 342 can always be represented as a non-negative combination of steps in {B-1, B} <= [A, B]. Thus, safe gaps between bad intervals longer than ~400 allow complete reachability across the gap. Only boundaries of safe intervals within distance B matter, reducing N <= 10^18 to O(MB^2) transitions.

## 3. Step-by-Step Algorithm
1. 1. If A == B: check if (N - 1) % A == 0 and verify no 1 + k*A falls in any bad interval.
2. 2. If A < B: precompute reachability for distances up to 1000 using standard coin DP; all distances >= 400 are unconditionally reachable.
3. 3. Segment safe squares into intervals [S_i, T_i]. For each interval, record points within distance B of S_i and within distance B of T_i.
4. 4. Propagate reachability within safe intervals using the precomputed reachability table.
5. 5. Propagate reachability between distinct safe intervals for jumps in [A, B].
6. 6. Check if destination N is reachable.

## 4. Complexity Analysis
- **Time Complexity**: `O(M B^2 + B^3)`
- **Space Complexity**: `O(M B)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    int M;
    long long A, B;
    if (!(cin >> N >> M >> A >> B)) return 0;

    vector<pair<long long, long long>> bad(M);
    for (int i = 0; i < M; i++) {
        cin >> bad[i].first >> bad[i].second;
    }

    if (A == B) {
        if ((N - 1) % A != 0) {
            cout << "No\n";
            return 0;
        }
        for (auto p : bad) {
            long long L = p.first, R = p.second;
            // check if any 1 + k * A in [L, R]
            // L <= 1 + k * A <= R
            // L - 1 <= k * A <= R - 1
            long long k_min = (L - 1 + A - 1) / A;
            long long k_max = (R - 1) / A;
            if (k_min <= k_max && 1 + k_min * A <= N) {
                cout << "No\n";
                return 0;
            }
        }
        cout << "Yes\n";
        return 0;
    }

    // A < B
    // Frobenius bound: any distance >= 400 is reachable
    const int MAX_D = 1000;
    vector<bool> can(MAX_D + 1, false);
    can[0] = true;
    for (int i = 0; i <= MAX_D; i++) {
        if (can[i]) {
            for (long long step = A; step <= B; step++) {
                if (i + step <= MAX_D) can[i + step] = true;
            }
        }
    }

    auto is_dist_can = [&](long long d) {
        if (d < 0) return false;
        if (d >= 400) return true;
        return (bool)can[d];
    };

    // Safe intervals: [S_i, T_i]
    vector<pair<long long, long long>> safe;
    long long cur = 1;
    for (int i = 0; i < M; i++) {
        if (cur <= bad[i].first - 1) {
            safe.push_back({cur, bad[i].first - 1});
        }
        cur = bad[i].second + 1;
    }
    if (cur <= N) {
        safe.push_back({cur, N});
    }

    // For each safe interval, we maintain reachable squares in:
    // X_i: head (up to B elements)
    // Y_i: tail (up to B elements)
    // Actually, to handle transitions between X_i and Y_i accurately:
    // X_i has up to B elements: [S_i, min(T_i, S_i + B - 1)]
    // Y_i has up to B elements: [max(S_i, T_i - B + 1), T_i]
    // If length of safe interval <= 2 * B, just store all elements.
    
    // We can store a map or vector of (pos, is_reachable) for active candidate points.
    // Notice only points within B of the start or end of each safe interval matter!
    // Let's store vector<pair<long long, bool>> for each safe interval.

    int num_safe = safe.size();
    vector<vector<pair<long long, bool>>> nodes(num_safe);
    for (int i = 0; i < num_safe; i++) {
        long long S = safe[i].first;
        long long T = safe[i].second;
        if (T - S + 1 <= 2 * B) {
            for (long long p = S; p <= T; p++) nodes[i].push_back({p, false});
        } else {
            for (long long p = S; p < S + B; p++) nodes[i].push_back({p, false});
            for (long long p = T - B + 1; p <= T; p++) nodes[i].push_back({p, false});
        }
    }

    // Starting point 1 is in safe[0]
    for (auto& item : nodes[0]) {
        if (item.first == 1) item.second = true;
    }

    for (int i = 0; i < num_safe; i++) {
        long long S = safe[i].first;
        long long T = safe[i].second;

        // Reachability inside interval i:
        // Any reachable point in nodes[i] can reach another point in nodes[i] if dist is_dist_can.
        // Also note: if an earlier point in nodes[i] can reach a later point in nodes[i].
        for (size_t u = 0; u < nodes[i].size(); u++) {
            if (!nodes[i][u].second) continue;
            long long pos_u = nodes[i][u].first;
            for (size_t v = u + 1; v < nodes[i].size(); v++) {
                if (!nodes[i][v].second) {
                    long long pos_v = nodes[i][v].first;
                    if (is_dist_can(pos_v - pos_u)) {
                        nodes[i][v].second = true;
                    }
                }
            }
        }

        // Transition from interval i to subsequent intervals j > i:
        for (int j = i + 1; j < num_safe; j++) {
            if (nodes[j].empty() || nodes[j][0].first - nodes[i].back().first > B) {
                // If even the closest point is > B, further intervals will also be > B
                // But wait, nodes[i] has elements up to nodes[i].back().
                // Let's just check if nodes[j][0].first - nodes[i].back().first > B, break.
                if (nodes[j][0].first - nodes[i].back().first > B) break;
            }
            for (auto& u : nodes[i]) {
                if (!u.second) continue;
                for (auto& v : nodes[j]) {
                    long long diff = v.first - u.first;
                    if (diff >= A && diff <= B) {
                        v.second = true;
                    }
                }
            }
        }
    }

    bool ans = false;
    for (auto& item : nodes.back()) {
        if (item.first == N && item.second) ans = true;
    }

    cout << (ans ? "Yes\n" : "No\n");
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

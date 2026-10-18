# Problem Analysis: AtCoder-abc320_g — G. Slot Strategy 2 (Hard)

**Problem ID**: `AtCoder-abc320_g`  
**Contest**: `abc320`  
**Rating / Difficulty**: 2575  
**URL**: https://atcoder.jp/contests/abc320/tasks/abc320_g  
**VJudge Tag**: `[problem:AtCoder-abc320_g]`  
**Category File**: [`../categories/graph_theory/slot_strategy_2_bipartite_matching.md`](../categories/graph_theory/slot_strategy_2_bipartite_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Halls Theorem`  

---

## 1. Problem Statement & Key Idea
Find the minimum time $T$ to stop $N$ slot reels at identical digits, where at most one reel can be stopped at any time $t$.

## 2. Core Observation & Invariant
Since there are only $N \le 100$ reels, each reel needs to consider at most its first $N$ occurrences of digit $d$ in the periodic reel. Across all reels, at most $N^2 \le 10000$ candidate times exist. Bipartite matching with binary search on candidate times $T$ verifies solvability.

## 3. Step-by-Step Algorithm
1. 1. Iterate over each target digit $d \in \{0, \dots, 9\}$.
2. 2. For each reel, collect its first $N$ timestamps displaying $d$.
3. 3. Collect and sort all candidate timestamps.
4. 4. Binary search over candidate timestamps: construct bipartite graph of reels to available timestamps $\le T$ and check if maximum matching equals $N$ via Kuhn's algorithm.
5. 5. Return minimum $T$ over all digits.

## 4. Complexity Analysis
- **Time Complexity**: `O(10 \cdot N^3 \log(N^2))`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;
    vector<string> S(N);
    for (int i = 0; i < N; ++i) cin >> S[i];

    long long INF = 1e18;
    long long best_ans = INF;

    for (int d = 0; d < 10; ++d) {
        char digit_char = '0' + d;
        vector<vector<long long>> reel_times(N);
        bool possible = true;

        vector<vector<int>> reels_pos(N);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (S[i][j] == digit_char) {
                    reels_pos[i].push_back(j);
                }
            }
            if (reels_pos[i].empty()) {
                possible = false;
                break;
            }
        }
        if (!possible) continue;

        vector<long long> all_times;
        for (int i = 0; i < N; ++i) {
            long long cycle = 0;
            while ((int)reel_times[i].size() < N) {
                for (int p : reels_pos[i]) {
                    reel_times[i].push_back(cycle * M + p);
                    all_times.push_back(cycle * M + p);
                    if ((int)reel_times[i].size() == N) break;
                }
                cycle++;
            }
        }

        sort(all_times.begin(), all_times.end());
        all_times.erase(unique(all_times.begin(), all_times.end()), all_times.end());

        auto can_match = [&](long long T) -> bool {
            vector<vector<int>> adj(N);
            for (int i = 0; i < N; ++i) {
                for (long long t : reel_times[i]) {
                    if (t <= T) {
                        int idx = lower_bound(all_times.begin(), all_times.end(), t) - all_times.begin();
                        adj[i].push_back(idx);
                    }
                }
            }

            int num_times = all_times.size();
            vector<int> match(num_times, -1);
            vector<bool> vis(num_times, false);

            auto dfs = [&](auto& self, int u) -> bool {
                for (int v : adj[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        if (match[v] == -1 || self(self, match[v])) {
                            match[v] = u;
                            return true;
                        }
                    }
                }
                return false;
            };

            for (int i = 0; i < N; ++i) {
                fill(vis.begin(), vis.end(), false);
                if (!dfs(dfs, i)) return false;
            }
            return true;
        };

        int low = 0, high = (int)all_times.size() - 1;
        long long res = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (can_match(all_times[mid])) {
                res = all_times[mid];
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        if (res != -1) {
            best_ans = min(best_ans, res);
        }
    }

    if (best_ans == INF) cout << -1 << "\n";
    else cout << best_ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-digitalarts_3 — C. Chokutter

**Problem ID**: `AtCoder-digitalarts_3`  
**Contest**: `digitalarts2012`  
**Rating / Difficulty**: 2179  
**URL**: https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_3  
**VJudge Tag**: `[problem:AtCoder-digitalarts_3]`  
**Category File**: [`../categories/basics/event_snapshot_difference_timeline_aggregation.md`](../categories/basics/event_snapshot_difference_timeline_aggregation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Range Queries Without Updates`  
- **Topic (Skill)**: `Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Track an SNS timeline network with N users, M events (tweet, mutual follow, mutual unfollow). Determine the K-th largest timeline tweet count. Tweets of user v during an active mutual follow period [start, end] contribute T_v(end) - T_v(start) to user u timeline.

## 2. Core Observation & Invariant
Instead of updating timelines naively on every tweet, store a snapshot of (T_u, T_v) whenever u and v follow each other. When they unfollow (or at the end of the simulation), add T_v - snap_v to u and T_u - snap_u to v. Since there are at most M follow events, an adjacency map tracks all active friendships in O(M log M) time.

## 3. Step-by-Step Algorithm
1. Maintain an array T[1..N] of cumulative tweet counts for each user, and gained[1..N] for tweets received from followed friends.
2. Maintain an active friendship map mapping pair (min(j, k), max(j, k)) to (T[j], T[k]) snapshots.
3. Process events: on "t j", increment T[j]; on "f j k", record snapshot (T[j], T[k]); on "u j k", retrieve snapshot, add (T[k] - s_k) to gained[j] and (T[j] - s_j) to gained[k], and erase from active map.
4. After all events, flush all remaining active friendships: add differences to both endpoints.
5. Compute total[i] = T[i] + gained[i] for all 1 <= i <= N. Sort descending and print total[K - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M + N log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<long long> T(N + 1, 0);
    vector<long long> gained(N + 1, 0);

    // Map pair (u, v) with u < v to pair (snapshot_u, snapshot_v)
    map<pair<int, int>, pair<long long, long long>> active;

    for (int i = 0; i < M; ++i) {
        char type;
        cin >> type;
        if (type == 't') {
            int j;
            cin >> j;
            T[j]++;
        } else if (type == 'f') {
            int j, k;
            cin >> j >> k;
            if (j > k) swap(j, k);
            active[{j, k}] = {T[j], T[k]};
        } else if (type == 'u') {
            int j, k;
            cin >> j >> k;
            if (j > k) swap(j, k);
            auto it = active.find({j, k});
            if (it != active.end()) {
                long long s_j = it->second.first;
                long long s_k = it->second.second;
                gained[j] += T[k] - s_k;
                gained[k] += T[j] - s_j;
                active.erase(it);
            }
        }
    }

    for (auto const& [edge, snaps] : active) {
        int j = edge.first;
        int k = edge.second;
        long long s_j = snaps.first;
        long long s_k = snaps.second;
        gained[j] += T[k] - s_k;
        gained[k] += T[j] - s_j;
    }

    vector<long long> total(N);
    for (int i = 1; i <= N; ++i) {
        total[i - 1] = T[i] + gained[i];
    }

    sort(total.rbegin(), total.rend());

    cout << total[K - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-abc264_g — G. String Fair

**Problem ID**: `AtCoder-abc264_g`  
**Contest**: `abc264`  
**Rating / Difficulty**: 2348  
**URL**: https://atcoder.jp/contests/abc264/tasks/abc264_g  
**VJudge Tag**: `[problem:AtCoder-abc264_g]`  
**Category File**: [`../categories/graph_theory/debruijn_spfa_negative_cycle_longest_path.md`](../categories/graph_theory/debruijn_spfa_negative_cycle_longest_path.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Bellman Ford`  

---

## 1. Problem Statement & Key Idea
Find the maximum beauty of a string scored by matches of patterns of length $\le 3$. Construct a de Bruijn graph on 703 2-letter states; detect positive cycles and find the longest path via SPFA / Bellman-Ford in $O(V \cdot E)$.

## 2. Core Observation & Invariant
Because all patterns $T_i$ have length $\le 3$, substring matches depend solely on the 2-character suffix of the current string. Constructing a de Bruijn state graph on strings of length $\le 2$ (703 states) maps the maximum beauty problem to the longest walk in a directed graph. A reachable positive cycle yields Infinity; otherwise, the longest walk is finite.

## 3. Step-by-Step Algorithm
1. Define 703 states (empty string, 26 1-char strings, 676 2-char strings).
2. For each state $u$ and transition character $c \in ['a'..'z']$, evaluate bonus points gained from matched patterns, and create directed edge $u \to v$ with weight $-gain$.
3. Run Bellman-Ford or SPFA from the empty state.
4. If a negative cycle is reachable, output Infinity; otherwise output $-\min_{u \ne 0} dist[u]$ in $O(V \cdot E) \approx 703 \times 18278$ operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(V \cdot E)`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int encode_state(const string& s) {
    if (s.empty()) return 0;
    if (s.size() == 1) return (s[0] - 'a' + 1);
    return 27 + (s[0] - 'a') * 26 + (s[1] - 'a');
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<string, long long>> rules(N);
    for (int i = 0; i < N; ++i) {
        cin >> rules[i].first >> rules[i].second;
    }

    // States:
    // 0: empty
    // 1..26: 1 letter
    // 27..702: 2 letters
    int total_states = 703;
    vector<string> state_str(total_states);
    state_str[0] = "";
    for (int c = 0; c < 26; ++c) {
        state_str[c + 1] = string(1, (char)('a' + c));
    }
    for (int c1 = 0; c1 < 26; ++c1) {
        for (int c2 = 0; c2 < 26; ++c2) {
            int id = 27 + c1 * 26 + c2;
            state_str[id] = string(1, (char)('a' + c1)) + (char)('a' + c2);
        }
    }

    struct Edge {
        int to;
        long long cost; // negative of gain
    };

    vector<vector<Edge>> adj(total_states);

    for (int u = 0; u < total_states; ++u) {
        for (char next_ch = 'a'; next_ch <= 'z'; ++next_ch) {
            string next_full = state_str[u] + next_ch;
            long long gain = 0;
            for (const auto& r : rules) {
                if (next_full.size() >= r.first.size()) {
                    if (next_full.substr(next_full.size() - r.first.size()) == r.first) {
                        gain += r.second;
                    }
                }
            }
            string next_s = next_full.substr(max(0, (int)next_full.size() - 2));
            int v = encode_state(next_s);
            adj[u].push_back({v, -gain});
        }
    }

    // SPFA / Bellman-Ford from state 0
    vector<long long> dist(total_states, INF);
    vector<int> cnt(total_states, 0);
    vector<bool> in_queue(total_states, false);
    queue<int> q;

    dist[0] = 0;
    q.push(0);
    in_queue[0] = true;
    cnt[0] = 1;

    bool has_cycle = false;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        in_queue[u] = false;

        for (const auto& e : adj[u]) {
            if (dist[e.to] > dist[u] + e.cost) {
                dist[e.to] = dist[u] + e.cost;
                if (!in_queue[e.to]) {
                    q.push(e.to);
                    in_queue[e.to] = true;
                    cnt[e.to]++;
                    if (cnt[e.to] > total_states) {
                        has_cycle = true;
                        break;
                    }
                }
            }
        }
        if (has_cycle) break;
    }

    if (has_cycle) {
        cout << "Infinity\n";
    } else {
        long long min_cost = INF;
        for (int u = 1; u < total_states; ++u) {
            min_cost = min(min_cost, dist[u]);
        }
        cout << -min_cost << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc086_c — E - Smuggling Marbles

**Problem ID**: `AtCoder-arc086_c`  
**Contest**: `arc086`  
**Rating / Difficulty**: 2814  
**URL**: https://atcoder.jp/contests/arc086/tasks/arc086_c  
**VJudge Tag**: `[problem:AtCoder-arc086_c]`  
**Category File**: [`../categories/dynamic_programming/marble_merging_tree_dp_depth_groups.md`](../categories/dynamic_programming/marble_merging_tree_dp_depth_groups.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Each node in a rooted tree independently starts with a marble with probability 1/2. Marbles move to parents each step, and colliding marbles vanish. Find the expected number of marbles that reach the root, times 2^(N+1) mod 1000000007.

## 2. Core Observation & Invariant
Marbles starting at different depths never interact because they are always at different depths at every time step. For a fixed depth d, exactly 1 marble reaches the root iff at each ancestor node, exactly 1 child sends a marble. This can be tracked using tree DP with states (c_0, c_1, c_2) representing 0, 1, or >= 2 marbles from the subtree. Merging children's deques small-to-large achieves O(N) total complexity.

## 3. Step-by-Step Algorithm
1. 1. Compute depths of all nodes via BFS.
2. 2. In post-order traversal, maintain a deque<State> for each node representing depths below it.
3. 3. Merge sibling deques by small-to-large merging using state convolution: n0 = a0*b0, n1 = a1*b0 + a0*b1, n2 = total - n0 - n1.
4. 4. Any marbles >= 2 vanish at the parent node: c0 += c2, c2 = 0.
5. 5. Prepend state (1, 1, 0) for the current node.
6. 6. Multiply root state c_1 at each depth by 2^(N+1 - depth_count) and sum modulo 1000000007.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

struct State {
    long long c0, c1, c2;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> children(n + 1);
    for (int i = 1; i <= n; i++) {
        int p;
        cin >> p;
        children[p].push_back(i);
    }

    // BFS to get levels
    vector<vector<int>> levels;
    vector<int> current_level = {0};
    levels.push_back(current_level);
    while (true) {
        vector<int> next_level;
        for (int u : levels.back()) {
            for (int v : children[u]) {
                next_level.push_back(v);
            }
        }
        if (next_level.empty()) break;
        levels.push_back(next_level);
    }

    vector<int> level_node_count;
    for (const auto& lvl : levels) {
        level_node_count.push_back(lvl.size());
    }

    // Process from deepest level to root
    vector<deque<State>> balls(n + 1);

    for (int lvl_idx = (int)levels.size() - 1; lvl_idx >= 0; lvl_idx--) {
        for (int node : levels[lvl_idx]) {
            if (children[node].empty()) {
                balls[node].push_back({1, 1, 0});
            } else if (children[node].size() == 1) {
                int child = children[node][0];
                balls[node] = move(balls[child]);
                balls[node].push_front({1, 1, 0});
            } else {
                // Multiple children
                vector<int> cn = children[node];
                sort(cn.begin(), cn.end(), [&](int a, int b) {
                    return balls[a].size() < balls[b].size();
                });

                int largest_child = cn.back();
                deque<State>& bs_res = balls[largest_child];

                for (size_t i = 0; i + 1 < cn.size(); i++) {
                    int c = cn[i];
                    deque<State>& bs_small = balls[c];
                    for (size_t j = 0; j < bs_small.size(); j++) {
                        long long a0 = bs_small[j].c0;
                        long long a1 = bs_small[j].c1;
                        long long a2 = bs_small[j].c2;

                        long long b0 = bs_res[j].c0;
                        long long b1 = bs_res[j].c1;
                        long long b2 = bs_res[j].c2;

                        long long tot_a = (a0 + a1 + a2) % MOD;
                        long long tot_b = (b0 + b1 + b2) % MOD;

                        long long n0 = (a0 * b0) % MOD;
                        long long n1 = (a1 * b0 + a0 * b1) % MOD;
                        long long n2 = (tot_a * tot_b - n0 - n1) % MOD;
                        if (n2 < 0) n2 += MOD;

                        bs_res[j] = {n0, n1, n2};
                    }
                }

                // Any marbles >= 2 vanish at node
                size_t second_largest_len = balls[cn[cn.size() - 2]].size();
                for (size_t j = 0; j < second_largest_len; j++) {
                    bs_res[j].c0 = (bs_res[j].c0 + bs_res[j].c2) % MOD;
                    bs_res[j].c2 = 0;
                }

                bs_res.push_front({1, 1, 0});
                balls[node] = move(bs_res);
            }
        }
    }

    vector<long long> pow2(n + 5, 1);
    for (int i = 1; i < n + 5; i++) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    long long ans = 0;
    const deque<State>& root_balls = balls[0];
    for (size_t i = 0; i < root_balls.size() && i < level_node_count.size(); i++) {
        long long c1 = root_balls[i].c1;
        int nodes_at_depth = level_node_count[i];
        int rem = (n + 1) - nodes_at_depth;
        long long term = c1 * pow2[rem] % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

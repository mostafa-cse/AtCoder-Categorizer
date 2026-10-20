# Problem Analysis: AtCoder-arc101_d — D. Robots and Exits

**Problem ID**: `AtCoder-arc101_d`  
**Contest**: `arc101`  
**Rating / Difficulty**: 2930  
**URL**: https://atcoder.jp/contests/arc101/tasks/arc101_d  
**VJudge Tag**: `[problem:AtCoder-arc101_d]`  
**Category File**: [`../categories/dynamic_programming/robot_exit_coordinate_compression_prefix_bit_dp.md`](../categories/dynamic_programming/robot_exit_coordinate_compression_prefix_bit_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
N robots and M exits on a line. In each step, all robots move 1 unit left or 1 unit right. A robot exits when reaching an exit. Count the number of possible sets of which robot exits where.

## 2. Core Observation & Invariant
Each robot between exit A and exit B exits through A iff the left movement reaches x_i - A before the right movement reaches B - x_i. This assigns each robot a threshold pair (a_i, b_i). A subset of robots choosing A vs B corresponds to non-dominated paths in the (a, b) plane. Sorting points by a_i ascending and b_i descending reduces the problem to counting strictly increasing subsequences, solvable via coordinate compression and a Binary Indexed Tree (BIT).

## 3. Step-by-Step Algorithm
1. 1. For each robot, find its adjacent left and right exits and compute distance pair (a_i, b_i).
2. 2. Filter out robots uniquely trapped into an exit; normalize remaining pairs.
3. 3. Sort pairs by coordinate a_i ascending, and by b_i descending for tie-breaking.
4. 4. Run DP with Fenwick tree / BIT: dp[y] = 1 + sum_{y' < y} dp[y'].
5. 5. Total answer is 1 + sum dp[y] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

struct Node {
    int x, y;
    bool operator<(const Node& other) const {
        if (x != other.x) return x < other.x;
        return y > other.y;
    }
    bool operator==(const Node& other) const {
        return x == other.x && y == other.y;
    }
};

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) {
            tree[i] = (tree[i] + delta) % MOD;
        }
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) {
            sum = (sum + tree[i]) % MOD;
        }
        return sum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> X(N);
    for (int i = 0; i < N; ++i) cin >> X[i];

    vector<int> Y(M);
    for (int i = 0; i < M; ++i) cin >> Y[i];

    vector<Node> pts;
    vector<int> vals_y;

    for (int i = 0; i < N; ++i) {
        if (X[i] > Y[0] && X[i] < Y[M - 1]) {
            int pos = lower_bound(Y.begin(), Y.end(), X[i]) - Y.begin();
            int l_dist = X[i] - Y[pos - 1];
            int r_dist = Y[pos] - X[i];
            pts.push_back({l_dist, r_dist});
            vals_y.push_back(r_dist);
        }
    }

    if (pts.empty()) {
        cout << 1 << "\n";
        return 0;
    }

    sort(vals_y.begin(), vals_y.end());
    vals_y.erase(unique(vals_y.begin(), vals_y.end()), vals_y.end());

    for (auto& pt : pts) {
        pt.y = lower_bound(vals_y.begin(), vals_y.end(), pt.y) - vals_y.begin() + 1;
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    int sz = vals_y.size();
    Fenwick bit(sz);

    int ans = 1;
    for (const auto& pt : pts) {
        int ways = (bit.query(pt.y - 1) + 1) % MOD;
        ans = (ans + ways) % MOD;
        bit.add(pt.y, ways);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

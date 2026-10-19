# Problem Analysis: AtCoder-agc026_d — D - Histogram Coloring

**Problem ID**: `AtCoder-agc026_d`  
**Contest**: `agc026`  
**Rating / Difficulty**: 2742  
**URL**: https://atcoder.jp/contests/agc026/tasks/agc026_d  
**VJudge Tag**: `[problem:AtCoder-agc026_d]`  
**Category File**: [`../categories/dynamic_programming_dp/histogram_coloring_cartesian_tree_dp.md`](../categories/dynamic_programming_dp/histogram_coloring_cartesian_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Given a histogram with N columns of heights h_1, ..., h_N, we want to color each 1x1 square red or blue such that in every 2x2 square completely contained in the histogram, there are exactly two red squares and two blue squares. Find the number of valid colorings modulo 10^9 + 7.

## 2. Core Observation & Invariant
In any 2x2 square, having two red and two blue squares implies that if two adjacent cells in a row have the same color, the entire column above and below them must alternate colors vertically. Columns naturally form blocks organized in a Cartesian tree by height. For a histogram segment of width w and common baseline height offset x, we define two DP states: dp1 (number of colorings where all columns alternate vertically) and dp2 (colorings where at least one pair of adjacent columns does not alternate vertically). For a block with children c_1, ..., c_k, the transitions are: dp1 = 2^x * prod(dp1_{c_i}), and dp2 = 2^w * prod(dp1_{c_i} + dp2_{c_i}) + (2^x - 2) * prod(dp1_{c_i}).

## 3. Step-by-Step Algorithm
1. 1. Build the Cartesian tree on the column heights H_1, ..., H_N.
2. 2. Perform a post-order traversal (bottom-up tree DP) on the Cartesian tree.
3. 3. At each node representing a range [L, R] with base height subtracted by its parent's height x = h_{min} - h_{parent}:
4.    a. Compute dp1 = 2^x * prod_{c} dp1_c.
5.    b. Compute dp2 = 2^(R - L + 1) * prod_{c} (dp1_c + dp2_c) + (2^x - 2) * prod_{c} dp1_c.
6. 4. The total valid colorings for the root node is (dp1_{root} + dp2_{root}) mod (10^9 + 7).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

struct Result {
    long long dp1;
    long long dp2;
};

vector<long long> H;

Result rec(int l, int r, long long base) {
    if (l > r) {
        return {1, 1};
    }

    long long min_val = H[l];
    for (int i = l + 1; i <= r; i++) {
        if (H[i] < min_val) min_val = H[i];
    }

    long long x = min_val - base;

    vector<Result> children;
    long long w = 0;
    int i = l;
    while (i <= r) {
        if (H[i] == min_val) {
            w++;
            i++;
        } else {
            int j = i;
            while (j <= r && H[j] > min_val) {
                j++;
            }
            children.push_back(rec(i, j - 1, min_val));
            i = j;
        }
    }

    long long prod_dp1 = 1;
    long long prod_sum = 1;
    for (const auto& child : children) {
        prod_dp1 = (prod_dp1 * child.dp1) % MOD;
        prod_sum = (prod_sum * ((child.dp1 + child.dp2) % MOD)) % MOD;
    }

    long long p2x = power(2, x);
    long long p2w = power(2, w);

    long long dp1 = (p2x * prod_dp1) % MOD;
    long long dp2 = (p2w * prod_sum + (p2x - 2 + MOD) * prod_dp1) % MOD;

    return {dp1, dp2};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    H.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> H[i];
    }

    Result res = rec(0, n - 1, 0);
    cout << res.dp2 << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

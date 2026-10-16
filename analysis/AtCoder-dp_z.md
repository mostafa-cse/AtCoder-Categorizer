# Problem Analysis: AtCoder-dp_z — Frog 3

**Problem ID**: `AtCoder-dp_z`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 2200  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_z  
**VJudge Tag**: `[problem:AtCoder-dp_z]`  
**Category File**: [`../categories/dp/convex_hull_trick.md`](../categories/dp/convex_hull_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Convex Hull Trick (CHT)`  
- **Topic (Skill)**: `Convex Hull Trick (CHT) and Dynamic CHT`  

---

## 1. Problem Statement & Key Idea
Jump from stone i to j with quadratic cost (h_j - h_i)^2 + C where heights are strictly increasing.

**Core Idea**: Expand (h_j - h_i)^2 + C = h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. For fixed j, this is min_i (m_i * x + b_i) with slope m_i = -2 * h_i and x = h_j.

## 2. Core Observation & Invariant
Since heights h_i are strictly increasing, slopes are strictly decreasing and query points are strictly increasing. A deque maintains the lower convex hull in O(1) amortized time per query.

## 3. Step-by-Step Algorithm
1. Deque stores lines.
2. For stone j: pop front while line[0].eval(h_j) >= line[1].eval(h_j).
3. dp[j] = deque.front().eval(h_j) + h_j^2 + C.
4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping non-convex lines.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

struct Line {
    long long m, b;
    long long eval(long long x) const {
        return m * x + b;
    }
};

// Check if l2 is made redundant by l1 and l3
bool redundant(const Line& l1, const Line& l2, const Line& l3) {
    // Intersection of l1 and l2 vs l2 and l3
    return (double)(l2.b - l1.b) * (l2.m - l3.m) >= (double)(l3.b - l2.b) * (l1.m - l2.m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long C;
    if (!(cin >> n >> C)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, 0);
    deque<Line> hull;

    // Line for stone 0: m = -2*h[0], b = h[0]^2 + dp[0]
    hull.push_back({-2 * h[0], h[0] * h[0]});

    for (int j = 1; j < n; ++j) {
        long long x = h[j];
        // Pop suboptimal lines from front
        while (hull.size() >= 2 && hull[0].eval(x) >= hull[1].eval(x)) {
            hull.pop_front();
        }

        dp[j] = hull.front().eval(x) + x * x + C;

        Line cur = {-2 * h[j], dp[j] + h[j] * h[j]};
        // Maintain convexity at back
        while (hull.size() >= 2 && redundant(hull[hull.size() - 2], hull.back(), cur)) {
            hull.pop_back();
        }
        hull.push_back(cur);
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Canonical Convex Hull Trick with monotonic slopes and queries.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.
- **Reusable Pattern**: `Monotonic Convex Hull Trick (CHT).`

---
Back to [Convex Hull Trick (CHT) and Dynamic CHT](../categories/dp/convex_hull_trick.md) | [Categories Directory](../categories/README.md)
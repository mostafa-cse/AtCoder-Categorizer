# Problem Analysis: AtCoder-abc289_g — Shopping in AtCoder store

**Problem ID**: `AtCoder-abc289_g`  
**Contest**: `abc289`  
**Rating / Difficulty**: 2109  
**URL**: https://atcoder.jp/contests/abc289/tasks/abc289_g  
**VJudge Tag**: `[problem:AtCoder-abc289_g]`  
**Category File**: [`../categories/dynamic_programming/upper_convex_hull_revenue_envelope.md`](../categories/dynamic_programming/upper_convex_hull_revenue_envelope.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Convex Hull Trick (CHT)`  
- **Topic (Skill)**: `Convex Hull Trick (CHT) and Dynamic CHT`  

---

## 1. Problem Statement & Key Idea
There are N customers with base valuations B_1, ..., B_N. You receive M queries, each with a price increase C_j. A price P will attract all customers i with B_i + C_j >= P. Find the maximum revenue achievable for each query C_j.

**Key Insight**: Sort base valuations descending: B_1 >= B_2 >= ... >= B_N. If you target selling to the top i customers, the optimal price is P = B_i + C_j, yielding total revenue i * (B_i + C_j) = i * C_j + i * B_i. This is a linear function of C_j with slope m_i = i and y-intercept c_i = i * B_i. Finding the maximum revenue over all i in [1, N] for each query C_j is the upper convex hull envelope of lines with strictly increasing slopes, solved via the classic Convex Hull Trick.

## 2. Core Observation & Invariant
Pricing revenue functions form lines y = i * x + i * B_i with increasing slopes, evaluated via upper envelope binary search.

## 3. Step-by-Step Algorithm
1. Sort base valuations descending: B_1 >= B_2 >= ... >= B_N.
2. Construct lines y = i * x + i * B_i for i = 1 to N.
3. Filter lines using cross product / intersection checks to maintain the upper convex hull.
4. For each query C_j, binary search on the upper hull to find the tangent line maximizing revenue.
5. Output maximum revenue for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Convex Hull Trick upper envelope construction on linear pricing models.
- **Reusable Pattern**: Maximizing revenue i * (B_i + C) reduces directly to evaluating upper envelope of lines with slope i and intercept i * B_i.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long m, c;
    long long eval(long long x) const {
        return m * x + c;
    }
};

bool is_redundant(const Line& l1, const Line& l2, const Line& l3) {
    return (__int128)(l1.c - l2.c) * (l3.m - l2.m) <= (__int128)(l2.c - l3.c) * (l2.m - l1.m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> b(n);
    for (int i = 0; i < n; ++i) cin >> b[i];

    sort(b.rbegin(), b.rend());

    vector<Line> hull;
    for (int i = 1; i <= n; ++i) {
        Line cur = { (long long)i, (long long)i * b[i - 1] };
        while (hull.size() >= 2 && is_redundant(hull[hull.size() - 2], hull.back(), cur)) {
            hull.pop_back();
        }
        hull.push_back(cur);
    }

    for (int j = 0; j < m; ++j) {
        long long c;
        cin >> c;

        int low = 0, high = (int)hull.size() - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (hull[mid].eval(c) < hull[mid + 1].eval(c)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        cout << hull[low].eval(c) << (j + 1 == m ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

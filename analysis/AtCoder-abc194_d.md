# Problem Analysis: AtCoder-abc194_d — Journey

**Problem ID**: `AtCoder-abc194_d`  
**Contest**: `abc194`  
**Rating / Difficulty**: 1078  
**URL**: https://atcoder.jp/contests/abc194/tasks/abc194_d  
**VJudge Tag**: `[problem:AtCoder-abc194_d]`  
**Category File**: [`../categories/math/coupon_collector_expectation.md`](../categories/math/coupon_collector_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probability & Expectation`  
- **Topic (Skill)**: `Coupon Collector's Problem / Geometric Distribution Linearity of Expectation`  

---

## 1. Problem Statement & Key Idea
Start at vertex 1 of a graph with N vertices. At each step, pick an integer uniformly at random from 1..N and add an edge between the current vertex and the chosen vertex, then move to it. Find the expected number of steps until all N vertices are connected.

**Key Idea**: This is precisely the classical Coupon Collector's Problem.

## 2. Core Observation & Invariant
When k distinct vertices have already been visited, the probability of picking an unvisited vertex in the next step is p = (N - k) / N. The number of steps to pick the next new vertex follows a Geometric Distribution with mean 1 / p = N / (N - k). By Linearity of Expectation, total expected steps is sum_{k=1}^{N-1} N / (N - k).

## 3. Step-by-Step Algorithm
1. Initialize expected_steps = 0.0.
2. For k = 1 to N - 1: expected_steps += (double)N / (N - k).
3. Print expected_steps with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    double ans = 0.0;
    for (int i = 1; i < n; ++i) {
        ans += (double)n / (n - i);
    }

    cout << fixed << setprecision(10) << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Coupon collector expectation using geometric distribution summation.
- **Reusable Pattern**: `Coupon collector expected time: sum_{i=1}^{N-1} N / i.`

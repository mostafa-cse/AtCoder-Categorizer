# Coupon Collector's Problem / Geometric Distribution Linearity of Expectation

**Domain**: `Math`  
**Subtopic**: `Probability & Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **Coupon Collector's Problem / Geometric Distribution Linearity of Expectation**.

---

## Curated Problems

### [problem:AtCoder-abc194_d] — Journey
- **Contest**: `abc194`
- **Rating / Difficulty**: 1078
- **Specific Skill**: Coupon Collector's Problem / Geometric Distribution Linearity of Expectation
- **Individual Analysis**: [`../../analysis/AtCoder-abc194_d.md`](../../analysis/AtCoder-abc194_d.md)
- **Problem Statement Summary**: Start at vertex 1 of a graph with N vertices. At each step, pick an integer uniformly at random from 1..N and add an edge between the current vertex and the chosen vertex, then move to it. Find the expected number of steps until all N vertices are connected.
- **Core Insight**: When k distinct vertices have already been visited, the probability of picking an unvisited vertex in the next step is p = (N - k) / N. The number of steps to pick the next new vertex follows a Geometric Distribution with mean 1 / p = N / (N - k). By Linearity of Expectation, total expected steps is sum_{k=1}^{N-1} N / (N - k).
- **Complexity**: Time: `O(N)` | Space: `O(1)`
- **Verified C++ Implementation**:
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

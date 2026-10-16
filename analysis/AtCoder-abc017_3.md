# Problem Analysis: AtCoder-abc017_3 — High Score

**Problem ID**: `AtCoder-abc017_3`  
**Contest**: `abc017`  
**Rating / Difficulty**: 1607  
**URL**: https://atcoder.jp/contests/abc017/tasks/abc017_3  
**VJudge Tag**: `[problem:AtCoder-abc017_3]`  
**Category File**: [`../categories/basics/complementary_segment_imos_piercing.md`](../categories/basics/complementary_segment_imos_piercing.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Prefix Sums`  
- **Topic (Skill)**: `Complementary Segment Imos / Minimum Cost Interval Piercing`  

---

## 1. Problem Statement & Key Idea
N ruins, each with score s_i and containing jewels of types l_i through r_i (jewels labeled 1..M). Collect ruins to maximize total score such that AT LEAST ONE jewel type is NEVER collected.

**Key Insight**: Invert the condition: pick which single jewel type j in 1..M is omitted. Any ruin containing jewel j cannot be used. We want to minimize the score of ruins containing jewel j.

## 2. Core Observation & Invariant
A ruin with jewel range [l_i, r_i] and score s_i contributes s_i loss to every jewel in [l_i, r_i]. Use an Imos (difference) array over jewel positions 1..M. Answer is (total score of all ruins) - min_{j=1..M} (loss at jewel j).

## 3. Step-by-Step Algorithm
1. Compute total_score = sum s_i.
2. Initialize difference array diff[M + 2] = 0.
3. For each ruin (l_i, r_i, s_i):
4.   diff[l_i] += s_i, diff[r_i + 1] -= s_i.
5. Compute prefix sums of diff to obtain loss[j] for j = 1..M.
6. min_loss = min_{j=1..M} loss[j].
7. Print total_score - min_loss.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> diff(m + 2, 0);
    long long total_score = 0;

    for (int i = 0; i < n; ++i) {
        int l, r;
        long long s;
        cin >> l >> r >> s;
        total_score += s;
        diff[l] += s;
        diff[r + 1] -= s;
    }

    long long cur_loss = 0;
    long long min_loss = 2e18;

    for (int j = 1; j <= m; ++j) {
        cur_loss += diff[j];
        min_loss = min(min_loss, cur_loss);
    }

    cout << total_score - min_loss << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Condition inversion to identify a single blocking pivot combined with 1D difference array.
- **Reusable Pattern**: `Omit at least one feature: total_sum - min_feature(sum_cost_covering_feature).`

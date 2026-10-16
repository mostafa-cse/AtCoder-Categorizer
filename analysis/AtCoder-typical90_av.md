# Problem Analysis: AtCoder-typical90_av — I will not drop out

**Problem ID**: `AtCoder-typical90_av`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 048)  
**Rating / Difficulty**: 800 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_av  
**VJudge Tag**: `[problem:AtCoder-typical90_av]`  
**Category File**: [`../categories/basics/greedy_splitting.md`](../categories/basics/greedy_splitting.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns`  

---

## 1. Problem Statement & Key Idea
N problems, time limit K minutes. Problem i awards B_i points for first minute, and additional A_i - B_i points for second minute. Maximize total score.

**Core Idea**: Since A_i > B_i > A_i - B_i, the first minute yields strictly more points than the second minute.

## 2. Core Observation & Invariant
Because points are diminishing (B_i >= A_i - B_i), any greedy algorithm that picks the largest available bonus will ALWAYS pick B_i before A_i - B_i! The prerequisite dependency is automatically satisfied.

## 3. Step-by-Step Algorithm
1. Create a list of 2N elements: B_i and A_i - B_i for each problem.
2. Sort all 2N elements descending.
3. Sum the top K elements.

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> scores;
    scores.reserve(2 * n);

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        scores.push_back(b);
        scores.push_back(a - b);
    }

    sort(scores.rbegin(), scores.rend());

    long long total = 0;
    for (int i = 0; i < k; ++i) {
        total += scores[i];
    }

    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Splitting dependent tasks into independent rewards using concavity / diminishing returns.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Eliminating dependency constraints in greedy selection when incremental rewards are concave/diminishing.
- **Reusable Pattern**: `Greedy Task Splitting with Diminishing Returns.`

---
Back to [Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns](../categories/basics/greedy_splitting.md) | [Categories Directory](../categories/README.md)
# Problem Analysis: AtCoder-abc160_e — Red and Green Apples

**Problem ID**: `AtCoder-abc160_e`  
**Contest**: `abc160`  
**Rating / Difficulty**: 1036  
**URL**: https://atcoder.jp/contests/abc160/tasks/abc160_e  
**VJudge Tag**: `[problem:AtCoder-abc160_e]`  
**Category File**: [`../categories/basics/top_k_greedy_unification.md`](../categories/basics/top_k_greedy_unification.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Top-(X+Y) Greedy Unification via Candidate Filtering`  

---

## 1. Problem Statement & Key Idea
You need to eat X red apples and Y green apples. You have A red apples (values p_i), B green apples (values q_i), and C colorless apples (values r_i) that can be eaten as either red or green. Maximize the total deliciousness.

**Key Idea**: Colorless apples can replace either red or green apples. But to get the maximum deliciousness, we should initially take the top X red apples and top Y green apples.

## 2. Core Observation & Invariant
Any chosen colorless apple should replace the smallest currently selected apple (whether red or green). Thus, we can pool the top X red apples, top Y green apples, and ALL C colorless apples into a single pool of X + Y + C items, and simply pick the largest X + Y items overall!

## 3. Step-by-Step Algorithm
1. Sort red apples descending, take the top X.
2. Sort green apples descending, take the top Y.
3. Pool the top X red, top Y green, and all C colorless apples into one vector.
4. Sort the combined vector descending.
5. Sum the first X + Y elements.
6. Output the sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(A log A + B log B + (X + Y + C) log(X + Y + C))`
- **Space Complexity**: `O(A + B + C)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y, a, b, c;
    if (!(cin >> x >> y >> a >> b >> c)) return 0;

    vector<long long> p(a), q(b), r(c);
    for (int i = 0; i < a; ++i) cin >> p[i];
    for (int i = 0; i < b; ++i) cin >> q[i];
    for (int i = 0; i < c; ++i) cin >> r[i];

    sort(p.rbegin(), p.rend());
    sort(q.rbegin(), q.rend());

    vector<long long> pool;
    pool.reserve(x + y + c);

    for (int i = 0; i < x; ++i) pool.push_back(p[i]);
    for (int i = 0; i < y; ++i) pool.push_back(q[i]);
    for (int i = 0; i < c; ++i) pool.push_back(r[i]);

    sort(pool.rbegin(), pool.rend());

    long long sum = 0;
    for (int i = 0; i < x + y; ++i) {
        sum += pool[i];
    }

    cout << sum << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Simplifying wildcard substitution problems by candidate pool unification.
- **Reusable Pattern**: `Wildcard replacements: select best quotas of fixed items, pool with wildcards, take top K overall.`

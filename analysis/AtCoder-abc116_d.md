# Problem Analysis: AtCoder-abc116_d — Various Sushi

**Problem ID**: `AtCoder-abc116_d`  
**Contest**: `abc116`  
**Rating / Difficulty**: 1712  
**URL**: https://atcoder.jp/contests/abc116/tasks/abc116_d  
**VJudge Tag**: `[problem:AtCoder-abc116_d]`  
**Category File**: [`../categories/basics/greedy_exchange_diversity_score.md`](../categories/basics/greedy_exchange_diversity_score.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Greedy Exchange Argument with Two Compensating Quantities`  

---

## 1. Problem Statement & Key Idea
Given N sushi pieces, sushi i has type t_i and deliciousness d_i. Choose K sushi pieces. Total score is sum(d_i) + (number of distinct types)^2. Maximize the total score.

**Key Insight**: Start with the top K most delicious sushi. This maximizes sum(d_i). To increase diversity x to x+1, exchange the least delicious duplicate sushi in our chosen set with the most delicious unused sushi of a new type.

## 2. Core Observation & Invariant
Since replacing an element decreases the sum of deliciousness, we should greedily sacrifice the smallest duplicate. Trying all possible distinct type counts x from initial count up to K guarantees finding the global maximum.

## 3. Step-by-Step Algorithm
1. Sort all sushi by deliciousness descending.
2. Select top K sushi. Track distinct types and push duplicate sushi into a stack (sorted by deliciousness ascending).
3. Collect the best sushi for each type not yet selected in candidates.
4. Calculate initial score.
5. While stack has duplicates and candidates has new types:
6.   Pop smallest duplicate, pop best new type, update score and max_score.
7. Print max_score.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

struct Sushi {
    int t;
    long long d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Sushi> sushi(n);
    for (int i = 0; i < n; ++i) {
        cin >> sushi[i].t >> sushi[i].d;
    }

    sort(sushi.begin(), sushi.end(), [](const Sushi& a, const Sushi& b) {
        return a.d > b.d;
    });

    unordered_set<int> chosen_types;
    vector<long long> duplicates;
    long long current_sum = 0;

    for (int i = 0; i < k; ++i) {
        current_sum += sushi[i].d;
        if (chosen_types.count(sushi[i].t)) {
            duplicates.push_back(sushi[i].d);
        } else {
            chosen_types.insert(sushi[i].t);
        }
    }

    vector<Sushi> unused_distinct;
    for (int i = k; i < n; ++i) {
        if (!chosen_types.count(sushi[i].t)) {
            chosen_types.insert(sushi[i].t);
            unused_distinct.push_back(sushi[i]);
        }
    }

    long long distinct_count = chosen_types.size() - unused_distinct.size();
    long long max_score = current_sum + distinct_count * distinct_count;

    int dup_idx = duplicates.size() - 1;
    int unused_idx = 0;

    while (dup_idx >= 0 && unused_idx < (int)unused_distinct.size()) {
        current_sum -= duplicates[dup_idx--];
        current_sum += unused_distinct[unused_idx++].d;
        distinct_count++;
        long long score = current_sum + distinct_count * distinct_count;
        max_score = max(max_score, score);
    }

    cout << max_score << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy exchange argument balancing linear sum with quadratic diversity bonus.
- **Reusable Pattern**: `Base Greedy + Exchange Argument: Optimize dual metric by single-swap step-ladder.`

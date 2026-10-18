# Problem Analysis: AtCoder-donuts_2015_4 — D. ドーナツの箱詰め

**Problem ID**: `AtCoder-donuts_2015_4`  
**Contest**: `donuts-2015`  
**Rating / Difficulty**: 2383  
**URL**: https://atcoder.jp/contests/donuts-2015/tasks/donuts_2015_4  
**VJudge Tag**: `[problem:AtCoder-donuts_2015_4]`  
**Category File**: [`../categories/basics/nested_box_buffer_difference_multiset.md`](../categories/basics/nested_box_buffer_difference_multiset.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Pack K donuts into N nested boxes, minimizing total buffer material C_i - C_j across Q box crush events. Nesting into K chains equates to partitioning sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences. Maintaining differences with two multisets answers each query in O(log N) time.

## 2. Core Observation & Invariant
Using all active boxes to package K donuts partitions the boxes into K nesting chains, where buffer material is sum (C_{outer} - C_{inner}). This is mathematically equivalent to partitioning the sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences.

## 3. Step-by-Step Algorithm
1. Sort all initial box capacities and compute all adjacent differences.
2. Maintain two multisets: top_diffs containing the K-1 largest differences (with running sum) and bot_diffs containing the rest.
3. For each box crush event, remove the box from the active set; update adjacent differences by erasing old differences and adding the merged difference.
4. Answer each query in O(log N) as (max_elem - min_elem) - sum_top (or 0 if remaining boxes <= K).

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> C(n + 1);
    set<int> active;
    for (int i = 1; i <= n; ++i) {
        cin >> C[i];
        active.insert(C[i]);
    }
    int q;
    cin >> q;
    vector<int> D(q);
    for (int i = 0; i < q; ++i) {
        cin >> D[i];
    }

    multiset<int> top_diffs;
    multiset<int> bot_diffs;
    long long sum_top = 0;
    int k_drop = k - 1;

    auto add_diff = [&](int diff) {
        if (k_drop == 0) return;
        if ((int)top_diffs.size() < k_drop) {
            top_diffs.insert(diff);
            sum_top += diff;
        } else if (diff > *top_diffs.begin()) {
            int smallest = *top_diffs.begin();
            top_diffs.erase(top_diffs.begin());
            sum_top -= smallest;
            bot_diffs.insert(smallest);

            top_diffs.insert(diff);
            sum_top += diff;
        } else {
            bot_diffs.insert(diff);
        }
    };

    auto erase_diff = [&](int diff) {
        if (k_drop == 0) return;
        auto it = bot_diffs.find(diff);
        if (it != bot_diffs.end()) {
            bot_diffs.erase(it);
        } else {
            auto it2 = top_diffs.find(diff);
            if (it2 != top_diffs.end()) {
                top_diffs.erase(it2);
                sum_top -= diff;
                if (!bot_diffs.empty()) {
                    auto it_max = prev(bot_diffs.end());
                    int val = *it_max;
                    bot_diffs.erase(it_max);
                    top_diffs.insert(val);
                    sum_top += val;
                }
            }
        }
    };

    // Initialize diffs
    auto it = active.begin();
    int prev_val = *it;
    it++;
    for (; it != active.end(); ++it) {
        add_diff(*it - prev_val);
        prev_val = *it;
    }

    auto get_ans = [&]() -> long long {
        if ((int)active.size() <= k) return 0;
        int span = *active.rbegin() - *active.begin();
        return span - sum_top;
    };

    cout << get_ans() << "\n";
    for (int i = 0; i < q; ++i) {
        int val = C[D[i]];
        auto it_cur = active.find(val);
        bool has_prev = (it_cur != active.begin());
        bool has_next = (next(it_cur) != active.end());

        if (has_prev && has_next) {
            int p = *prev(it_cur);
            int s = *next(it_cur);
            erase_diff(val - p);
            erase_diff(s - val);
            add_diff(s - p);
        } else if (has_prev) {
            int p = *prev(it_cur);
            erase_diff(val - p);
        } else if (has_next) {
            int s = *next(it_cur);
            erase_diff(s - val);
        }
        active.erase(it_cur);
        cout << get_ans() << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

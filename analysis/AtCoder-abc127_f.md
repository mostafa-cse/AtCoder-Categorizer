# Problem Analysis: AtCoder-abc127_f — Absolute Minima

**Problem ID**: `AtCoder-abc127_f`  
**Contest**: `abc127`  
**Rating / Difficulty**: 2003  
**URL**: https://atcoder.jp/contests/abc127/tasks/abc127_f  
**VJudge Tag**: `[problem:AtCoder-abc127_f]`  
**Category File**: [`../categories/data_structures/online_running_median_two_heaps.md`](../categories/data_structures/online_running_median_two_heaps.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Queue & Priority Queue`  
- **Topic (Skill)**: `Online Running Median and Dynamic Absolute Deviation via Two Heaps`  

---

## 1. Problem Statement & Key Idea
Maintain a dynamic function f(x) initially 0. Query 1 a b: update f(x) <- f(x) + |x - a| + b. Query 2: output the integer x that minimizes f(x) (smallest in case of tie) and the minimum value of f(x).

**Key Idea**: The sum of absolute deviations sum |x - a_i| is minimized at the median of the multiset {a_1, ..., a_k}. With two balanced heaps (max-heap left for elements <= median, min-heap right for elements > median), the median is always left.top(). By maintaining sum_left and sum_right of elements in both heaps, the minimum value is (x * |left| - sum_left) + (sum_right - x * |right|) + sum_b.

## 2. Core Observation & Invariant
L1 norm minimization dynamically tracks the median, decomposable into two half-sums maintained by dual priority queues in O(log Q) per addition.

## 3. Step-by-Step Algorithm
1. Maintain max-heap 'left' (size (k+1)/2) and min-heap 'right' (size k/2), with their sum_left and sum_right.
2. For Query 1 (a, b):
3.   Add b to sum_b.
4.   Insert a into left or right depending on a <= left.top().
5.   Rebalance heaps so |left| == |right| or |left| == |right| + 1.
6. For Query 2:
7.   Let x = left.top().
8.   min_val = (x * left.size() - sum_left) + (sum_right - x * right.size()) + sum_b.
9.   Print x and min_val.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log Q)`
- **Space Complexity**: `O(Q)`

## 5. Core Algorithmic Skill & Learning Takeaway
Dynamic median and prefix/suffix deviation maintenance via balanced dual priority queues.

**Reusable Pattern**: Dual Heap Median Tracker: Max-heap left and min-heap right maintaining balanced partition and running element sums.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    priority_queue<long long> left_max;
    priority_queue<long long, vector<long long>, greater<long long>> right_min;
    long long sum_left = 0, sum_right = 0, sum_b = 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            long long a, b;
            cin >> a >> b;
            sum_b += b;

            if (left_max.empty() || a <= left_max.top()) {
                left_max.push(a);
                sum_left += a;
            } else {
                right_min.push(a);
                sum_right += a;
            }

            // Rebalance: left_max has size (total + 1) / 2
            while (left_max.size() > right_min.size() + 1) {
                long long val = left_max.top();
                left_max.pop();
                sum_left -= val;
                right_min.push(val);
                sum_right += val;
            }
            while (left_max.size() < right_min.size()) {
                long long val = right_min.top();
                right_min.pop();
                sum_right -= val;
                left_max.push(val);
                sum_left += val;
            }
        } else {
            long long x = left_max.top();
            long long ans = (x * (long long)left_max.size() - sum_left) +
                            (sum_right - x * (long long)right_min.size()) + sum_b;
            cout << x << " " << ans << "\n";
        }
    }

    return 0;
}
```

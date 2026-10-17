# Problem Analysis: AtCoder-abc155_d — Pairs

**Problem ID**: `AtCoder-abc155_d`  
**Contest**: `abc155`  
**Rating / Difficulty**: 1845  
**URL**: https://atcoder.jp/contests/abc155/tasks/abc155_d  
**VJudge Tag**: `[problem:AtCoder-abc155_d]`  
**Category File**: [`../categories/basics/binary_search_kth_pair_product.md`](../categories/basics/binary_search_kth_pair_product.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on K-th Pair Product with Sign-Partitioned Two Pointers`  

---

## 1. Problem Statement & Key Idea
Given array A of N integers (positive, negative, and zero). Find the K-th smallest product among all N(N - 1) / 2 pairs A_i * A_j (1 <= i < j <= N).

**Key Insight**: Binary search on product value P in [-10^{18}, 10^{18}]. To count pairs with A_i * A_j <= P, split array into negative, zero, and positive elements, and count valid pairs in O(N) using two pointers.

## 2. Core Observation & Invariant
For positive P, count includes all neg*pos and zero pairs, plus two-pointer count on pos*pos and neg*neg. For negative P, only neg*pos pairs can be <= P, counted with two pointers. For P = 0, includes neg*pos and all pairs with 0.

## 3. Step-by-Step Algorithm
1. Sort A.
2. Binary search on P in [-10^{18}, 10^{18}].
3. Function count_le(P):
4.   cnt = 0;
5.   For i = 0 to N - 1:
6.     Use two pointers or binary search to find j > i with A_i * A_j <= P.
7.   Return cnt.
8. If count_le(mid) >= K: ans = mid, high = mid - 1; else low = mid + 1.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max_val) * log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    auto count_le = [&](long long x) -> long long {
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] > 0) {
                int l = i + 1, r = n - 1, pos = i;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    if (a[i] * a[mid] <= x) {
                        pos = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                total += (pos - i);
            } else if (a[i] < 0) {
                int l = i + 1, r = n - 1, pos = n;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    if (a[i] * a[mid] <= x) {
                        pos = mid;
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }
                total += (n - pos);
            } else {
                if (x >= 0) {
                    total += (n - 1 - i);
                }
            }
        }
        return total;
    };

    long long low = -1e18, high = 1e18, ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting pair products <= P across mixed sign categories using binary search on answer.
- **Reusable Pattern**: `K-th Pair Product Search: Binary search product P + two-pointer pair count with sign handling.`

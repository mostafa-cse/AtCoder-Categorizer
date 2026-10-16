# Problem Analysis: AtCoder-abc184_f — Programming Contest

**Problem ID**: `AtCoder-abc184_f`  
**Contest**: `abc184`  
**Rating / Difficulty**: 1423  
**URL**: https://atcoder.jp/contests/abc184/tasks/abc184_f  
**VJudge Tag**: `[problem:AtCoder-abc184_f]`  
**Category File**: [`../categories/basics/meet_in_the_middle_subset_sum.md`](../categories/basics/meet_in_the_middle_subset_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Meet-in-the-Middle`  
- **Topic (Skill)**: `Meet-in-the-Middle on Subset Sum N <= 40`  

---

## 1. Problem Statement & Key Idea
Given N problems (N <= 40) where problem i takes A_i minutes to solve. You have at most T minutes (T <= 10^9). Find the maximum total time of a subset of problems that can be solved in at most T minutes.

**Key Insight**: Split the N problems into two halves of size <= 20. Generate all 2^(N/2) subset sums for each half, sort one half, and binary search for each sum in the first half.

## 2. Core Observation & Invariant
2^40 is ~ 10^12 (impossible), but 2^20 is ~ 10^6. Generating 10^6 values for each half and using binary search takes O(2^(N/2) * log(2^(N/2))) ~ 2 * 10^7 operations.

## 3. Step-by-Step Algorithm
1. Divide array A into left half (size n1 = N/2) and right half (size n2 = N - n1).
2. Generate all 2^n1 subset sums for the left half, keeping only sums <= T.
3. Generate all 2^n2 subset sums for the right half, keeping only sums <= T.
4. Sort the right subset sums and remove duplicates.
5. For each sum s in left subset sums:
6.   Use std::upper_bound to find the largest sum r in right subset sums such that s + r <= T.
7.   Update max_ans = max(max_ans, s + r).
8. Print max_ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^(N/2) * N)`
- **Space Complexity**: `O(2^(N/2))`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generate_sums(const vector<long long>& a, vector<long long>& res, long long T) {
    res.push_back(0);
    for (long long x : a) {
        int sz = res.size();
        for (int i = 0; i < sz; ++i) {
            if (res[i] + x <= T) {
                res.push_back(res[i] + x);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int mid = n / 2;
    vector<long long> left_a(a.begin(), a.begin() + mid);
    vector<long long> right_a(a.begin() + mid, a.end());

    vector<long long> left_sums, right_sums;
    generate_sums(left_a, left_sums, T);
    generate_sums(right_a, right_sums, T);

    sort(right_sums.begin(), right_sums.end());
    right_sums.erase(unique(right_sums.begin(), right_sums.end()), right_sums.end());

    long long best = 0;
    for (long long s : left_sums) {
        auto it = upper_bound(right_sums.begin(), right_sums.end(), T - s);
        if (it != right_sums.begin()) {
            --it;
            best = max(best, s + *it);
        }
    }

    cout << best << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Meet-in-the-middle subset sum enumeration and two-pointer/binary search recombination.
- **Reusable Pattern**: `Subset Sum N <= 40: split into 2^20 halves, sort second half, binary search for complement.`

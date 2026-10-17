# Problem Analysis: AtCoder-abc027_d — Robot Movement

**Problem ID**: `AtCoder-abc027_d`  
**Contest**: `abc027`  
**Rating / Difficulty**: 2081  
**URL**: https://atcoder.jp/contests/abc027/tasks/abc027_d  
**VJudge Tag**: `[problem:AtCoder-abc027_d]`  
**Category File**: [`../categories/basics/future_contribution_greedy_sorting.md`](../categories/basics/future_contribution_greedy_sorting.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
You are given a string S containing 'M', '+', and '-'. An integer variable x starts at 0. At 'M', your score increases by x. At each '+' or '-', you must choose to either increment x or decrement x. The total number of increments must equal the total number of decrements (so x ends at 0). Find the maximum possible final score.

**Key Insight**: Each operation (+ or -) performed at index i affects all subsequent 'M' characters. Specifically, choosing +1 at index i contributes +1 * (number of 'M' after index i) to the score, and -1 contributes -1 * (number of 'M' after index i). Thus, the i-th non-'M' position has an intrinsic coefficient c_i = count of 'M's in S[i+1..|S|]. To maximize the total sum sum c_i * sign_i with exactly half chosen as +1 and half as -1, we simply sort the coefficients c_i in ascending order, assign -1 to the smaller half, and +1 to the larger half.

## 2. Core Observation & Invariant
Cumulative sum scores can be decoupled into individual coefficient contributions of future 'M' occurrences, turning the problem into greedy sorting.

## 3. Step-by-Step Algorithm
1. Compute suffix counts of 'M' for the entire string S.
2. For each position where S[i] != 'M', record c_i = suffix_M[i + 1].
3. Sort all recorded coefficients c in ascending order.
4. Assign -1 to the first half and +1 to the second half.
5. Output the resulting sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| log |S|)`
- **Space Complexity**: `O(|S|)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Decoupling cumulative state increments into independent future contribution coefficients and greedy sign pairing.
- **Reusable Pattern**: When choices at step i additively affect all subsequent evaluation steps, reframe the score as sum (sign_i * future_events) and sort greedily.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<int> suffix_m(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suffix_m[i] = suffix_m[i + 1] + (s[i] == 'M' ? 1 : 0);
    }

    vector<int> coeffs;
    for (int i = 0; i < n; ++i) {
        if (s[i] != 'M') {
            coeffs.push_back(suffix_m[i + 1]);
        }
    }

    sort(coeffs.begin(), coeffs.end());

    int k = coeffs.size();
    long long ans = 0;
    for (int i = 0; i < k / 2; ++i) {
        ans -= coeffs[i];
    }
    for (int i = k / 2; i < k; ++i) {
        ans += coeffs[i];
    }

    cout << ans << "\n";
    return 0;
}
```

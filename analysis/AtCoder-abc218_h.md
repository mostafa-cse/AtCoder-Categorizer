# Problem Analysis: AtCoder-abc218_h — H - Red and Blue Lamps

**Problem ID**: `AtCoder-abc218_h`  
**Contest**: `abc218`  
**Rating / Difficulty**: 2805  
**URL**: https://atcoder.jp/contests/abc218/tasks/abc218_h  
**VJudge Tag**: `[problem:AtCoder-abc218_h]`  
**Category File**: [`../categories/dynamic_programming/red_blue_lamps_aliens_trick_convexity.md`](../categories/dynamic_programming/red_blue_lamps_aliens_trick_convexity.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Aliens Trick / WQS Binary Search`  

---

## 1. Problem Statement & Key Idea
Given N lamps in a line with adjacent difference rewards A_i, choose exactly R lamps to color red and N - R to color blue to maximize total reward.

## 2. Core Observation & Invariant
Choosing red lamps is equivalent to selecting items from an array where adjacent selections lose their mutual boundary reward. The optimal score as a function of the number of chosen red lamps k is strictly concave. This allows applying the Aliens Trick (WQS Binary Search / Lagrangian relaxation): introduce a penalty lambda per chosen red lamp, solve the unconstrained maximum weight problem with O(N) DP, and binary search lambda to find the slope matching R.

## 3. Step-by-Step Algorithm
1. 1. If R > N / 2, replace R with N - R by color symmetry.
2. 2. Binary search penalty lambda in [0, 2e9].
3. 3. In each check, run 2-state DP: dp[i][0/1] = (max_score, min_count) for prefix i with lamp i unchosen / chosen.
4. 4. Find the threshold lambda where the optimal count matches R.
5. 5. Recover the exact maximum answer as score + R * lambda.
6. 6. Output the maximum total reward.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct State {
    long long val;
    int cnt;
    bool operator<(const State& other) const {
        if (val != other.val) return val < other.val;
        return cnt < other.cnt; // prefer larger count
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long R;
    if (!(cin >> N >> R)) return 0;

    vector<long long> A(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        cin >> A[i];
    }

    R = min(R, (long long)N - R);
    if (R == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> B(N, 0);
    B[0] = A[0];
    B[N - 1] = A[N - 2];
    for (int i = 1; i < N - 1; ++i) {
        B[i] = A[i - 1] + A[i];
    }

    auto check = [&](long long lam) -> State {
        State dp0 = {0, 0};
        State dp1 = {B[0] - lam, 1};
        for (int i = 1; i < N; ++i) {
            State new_dp0 = max(dp0, dp1);
            State new_dp1 = {dp0.val + B[i] - lam, dp0.cnt + 1};
            dp0 = new_dp0;
            dp1 = new_dp1;
        }
        return max(dp0, dp1);
    };

    long long low = 0, high = 2e9 + 7;
    long long best_lam = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        State res = check(mid);
        if (res.cnt >= R) {
            best_lam = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    State res = check(best_lam);
    long long ans = res.val + R * best_lam;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

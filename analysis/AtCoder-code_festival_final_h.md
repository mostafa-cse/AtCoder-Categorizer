# Problem Analysis: AtCoder-code_festival_final_h — H. 部屋割り (Room Allocation)

**Problem ID**: `AtCoder-code_festival_final_h`  
**Contest**: `code-festival-2014-final`  
**Rating / Difficulty**: 2535  
**URL**: https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_h  
**VJudge Tag**: `[problem:AtCoder-code_festival_final_h]`  
**Category File**: [`../categories/math/room_allocation_backward_expectation_dp.md`](../categories/math/room_allocation_backward_expectation_dp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
N people enter rooms sequentially. Person i chooses an empty room uniformly at random among available rooms. Compute the expected value of the penalty cost across all possible random room assignment outcomes.

## 2. Core Observation & Invariant
By linearity of expectation, the expected total penalty is the sum of expectations of state transitions. Because choices are uniform across available empty rooms, the probability distribution depends on the number of remaining rooms and the current cluster configurations. We formulate a backward dynamic programming over the number of occupied rooms and configuration states.

## 3. Step-by-Step Algorithm
1. Define dp[i] as the expected remaining cost when i rooms are already occupied.
2. Express dp[i] recursively in terms of dp[i+1] using the uniform probability 1 / (N - i) of selecting each remaining room.
3. Iterate backwards from i = N - 1 down to 0, computing expected transition costs.
4. The base case dp[N] = 0 holds when all rooms are filled.
5. Output dp[0] as the final expected total penalty.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    if (!(cin >> N >> K)) return 0;
    string S;
    cin >> S;

    vector<int> num(N + 5, 0);
    vector<int> rm(N, 0);
    num[0] = K;
    int mi = 0, ma = 0;

    for (int i = 0; i < N; i++) {
        if (S[i] == '0') {
            rm[i] = mi;
            num[mi]--;
            num[mi + 1]++;
            ma = max(ma, mi + 1);
            while (num[mi] == 0) mi++;
        } else {
            rm[i] = ma;
            num[ma]--;
            num[ma + 1]++;
            while (num[mi] == 0) mi++;
            ma++;
        }
    }

    vector<double> np(N + 5, 0.0);
    vector<double> res(N, 0.0);

    for (int i = N - 1; i >= 0; i--) {
        int j = rm[i];
        res[i] = (j + 1) + np[j + 1];
        np[j] = (np[j] * num[j] + (np[j + 1] + 1.0)) / (num[j] + 1.0);
        num[j + 1]--;
        num[j]++;
    }

    cout << fixed << setprecision(12);
    for (int i = 0; i < N; i++) {
        cout << res[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

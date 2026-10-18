# Problem Analysis: AtCoder-agc013_c — C. Ants on a Circle

**Problem ID**: `AtCoder-agc013_c`  
**Contest**: `agc013`  
**Rating / Difficulty**: 2462  
**URL**: https://atcoder.jp/contests/agc013/tasks/agc013_c  
**VJudge Tag**: `[problem:AtCoder-agc013_c]`  
**Category File**: [`../categories/miscellaneous/ants_on_a_circle_cyclic_shift_invariant.md`](../categories/miscellaneous/ants_on_a_circle_cyclic_shift_invariant.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Permutations and Permutation Cycles`  

---

## 1. Problem Statement & Key Idea
Determine the final positions of $N$ ants moving on a circle of circumference $L$ after time $T$, reversing directions upon collisions. Colliding ants can be viewed as passing through each other, so the multiset of final coordinates is exactly $\{(X_i \pm T) \bmod L\}$. Because ants cannot jump over each other on a circle, their cyclic order is strictly preserved. Tracking total counterclockwise zero-crossings identifies the exact cyclic permutation shift.

## 2. Core Observation & Invariant
When two ants collide, their identity swap is equivalent to maintaining cyclic ordering. Each ant crossing coordinate 0 in the positive direction shifts the cyclic permutation offset by $+1$, while crossing in the negative direction shifts by $-1$. Total net shift modulo $N$ identifies which ant in the sorted array corresponds to ant 1.

## 3. Step-by-Step Algorithm
1. 1. For each ant $i$, compute its ghost final position: $X_i' = (X_i + T) \bmod L$ if clockwise, or $(X_i - T) \bmod L$ if counterclockwise.
2. 2. Calculate the net number of times ant $i$ crosses coordinate 0: $\lfloor (X_i + T) / L \rfloor$ for clockwise, and $-\lceil (T - X_i) / L \rceil$ for counterclockwise.
3. 3. Sum all crossing counts and reduce modulo $N$ to find the net cyclic shift $S$.
4. 4. Sort the $N$ final positions in increasing order.
5. 5. The final position of ant $i$ (0-indexed) is given by $final\_pos[(i + S) \bmod N]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long L, T;
    if (!(cin >> N >> L >> T)) return 0;

    vector<long long> X(N);
    vector<int> W(N);
    vector<long long> final_pos(N);
    long long shift = 0;

    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> W[i];
        if (W[i] == 1) {
            final_pos[i] = (X[i] + T) % L;
            shift += (X[i] + T) / L;
        } else {
            final_pos[i] = ((X[i] - T) % L + L) % L;
            long long temp = X[i] - T;
            if (temp < 0) {
                shift -= (-temp + L - 1) / L;
            } else {
                shift += temp / L;
            }
        }
    }

    sort(final_pos.begin(), final_pos.end());

    shift = (shift % N + N) % N;
    vector<long long> ans(N);
    for (int i = 0; i < N; ++i) {
        ans[i] = final_pos[(i + shift) % N];
    }

    for (int i = 0; i < N; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

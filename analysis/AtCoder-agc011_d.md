# Problem Analysis: AtCoder-agc011_d — D. Half Reflector

**Problem ID**: `AtCoder-agc011_d`  
**Contest**: `agc011`  
**Rating / Difficulty**: 2931  
**URL**: https://atcoder.jp/contests/agc011/tasks/agc011_d  
**VJudge Tag**: `[problem:AtCoder-agc011_d]`  
**Category File**: [`../categories/miscellaneous/half_reflector_deque_state_periodicity_simulation.md`](../categories/miscellaneous/half_reflector_deque_state_periodicity_simulation.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Invariants and Monovariants`  

---

## 1. Problem Statement & Key Idea
A sequence of N half-reflectors 'A' and 'B'. A ball enters from the left K times (K <= 10^9). Determine the final configuration of reflectors.

## 2. Core Observation & Invariant
An entering ball travels through the device. If the first reflector is 'A', it flips to 'B' and reflects the ball out to the left in 1 step. If the first reflector is 'B', it flips to 'A', lets the ball pass, and by induction, passing through a sequence of reflectors inverts every encountered reflector and shifts the pattern left by 1 position, appending an 'A' at the right end! Thus the string evolution is a deque pop-front, invert, push-back. After at most 2N steps, the string enters a periodic cycle of length 1 or 2.

## 3. Step-by-Step Algorithm
1. 1. Represent the N reflectors in a deque with a lazy global flip flag.
2. 2. Simulate each ball entry: if front is 'A', flip it; if 'B', pop front, invert lazy flag, push 'A' to back.
3. 3. After 2N operations, detect cycle period (period <= 2).
4. 4. Fast-forward remaining steps using K mod period.
5. 5. Output final string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    string S;
    cin >> S;

    deque<char> dq(S.begin(), S.end());
    int inv = 0;

    long long steps = min(K, 2LL * N);
    long long K_rem = K - steps;

    for (long long step = 0; step < steps; ++step) {
        char front_char = ((dq.front() == 'B') ^ inv) ? 'B' : 'A';
        if (front_char == 'A') {
            dq.front() = (dq.front() == 'A') ? 'B' : 'A';
        } else {
            dq.pop_front();
            inv ^= 1;
            dq.push_back(inv == 1 ? 'B' : 'A');
        }
    }

    if (K_rem > 0) {
        int cycle_len = (N % 2 == 0) ? 1 : 2;
        int extra = K_rem % cycle_len;
        for (int step = 0; step < extra; ++step) {
            char front_char = ((dq.front() == 'B') ^ inv) ? 'B' : 'A';
            if (front_char == 'A') {
                dq.front() = (dq.front() == 'A') ? 'B' : 'A';
            } else {
                dq.pop_front();
                inv ^= 1;
                dq.push_back(inv == 1 ? 'B' : 'A');
            }
        }
    }

    string ans = "";
    ans.reserve(N);
    for (char c : dq) {
        char actual = ((c == 'B') ^ inv) ? 'B' : 'A';
        ans.push_back(actual);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

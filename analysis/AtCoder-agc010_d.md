# Problem Analysis: AtCoder-agc010_d — D - Decrementing

**Problem ID**: `AtCoder-agc010_d`  
**Contest**: `agc010`  
**Rating / Difficulty**: 2795  
**URL**: https://atcoder.jp/contests/agc010/tasks/agc010_d  
**VJudge Tag**: `[problem:AtCoder-agc010_d]`  
**Category File**: [`../categories/game_theory/decrement_gcd_game_parity_reduction.md`](../categories/game_theory/decrement_gcd_game_parity_reduction.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Two players play a game with an array of positive integers A where gcd(A_1, ..., A_N) = 1. A move consists of choosing an element A_i > 1, decrementing it by 1, and dividing all elements by their new GCD. The first player who cannot move loses. Determine if the first player has a winning strategy.

## 2. Core Observation & Invariant
Analyze parity. If the number of even elements cnt_even is odd, the first player can decrement an even element to make it odd, leaving an even number of even elements and no GCD division can occur (since at least one odd element remains odd). If cnt_even is even and cnt_odd > 1, any move leaves an odd number of even elements, and GCD cannot divide out 2, so the opponent wins. The only non-trivial case is when cnt_even is even and cnt_odd == 1: the player must decrement the single odd element (if > 1), after which all elements become even and GCD is divided by an even number >= 2. This recursive division can happen at most O(log(max A)) times.

## 3. Step-by-Step Algorithm
1. 1. Count even elements cnt_even and odd elements cnt_odd in A.
2. 2. If cnt_even is odd, return First.
3. 3. If cnt_odd > 1, return Second.
4. 4. If cnt_odd == 1: find the single odd element A[idx]. If A[idx] == 1, return Second.
5. 5. Decrement A[idx] by 1, divide all elements by gcd(A_1, ..., A_N), and invert the turn recursively.
6. 6. Print 'First' if first player wins, else 'Second'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

bool can_win(vector<long long>& A) {
    while (true) {
        int cnt_even = 0;
        int n = A.size();
        for (int i = 0; i < n; ++i) {
            if (A[i] % 2 == 0) cnt_even++;
        }
        int cnt_odd = n - cnt_even;

        if (cnt_even % 2 == 1) {
            return true; // First wins
        }

        // cnt_even is even
        if (cnt_odd > 1) {
            return false; // Second wins
        }

        // Exactly 1 odd element
        int odd_idx = -1;
        for (int i = 0; i < n; ++i) {
            if (A[i] % 2 == 1) {
                odd_idx = i;
                break;
            }
        }

        if (A[odd_idx] == 1) {
            return false; // Cannot decrement the single odd element
        }

        // Decrement the single odd element
        A[odd_idx]--;
        long long g = 0;
        for (int i = 0; i < n; ++i) {
            g = gcd(g, A[i]);
        }
        for (int i = 0; i < n; ++i) {
            A[i] /= g;
        }

        // Turn passes to the opponent
        return !can_win(A);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    if (can_win(A)) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

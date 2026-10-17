# Problem Analysis: AtCoder-arc148_d — mod M Game

**Problem ID**: `AtCoder-arc148_d`  
**Contest**: `arc148`  
**Rating / Difficulty**: 2009  
**URL**: https://atcoder.jp/contests/arc148/tasks/arc148_d  
**VJudge Tag**: `[problem:AtCoder-arc148_d]`  
**Category File**: [`../categories/game_theory/modular_pairing_invariants_symmetric_game.md`](../categories/game_theory/modular_pairing_invariants_symmetric_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Combinatorial Games`  
- **Topic (Skill)**: `Modular Pairing Invariants and Symmetric Strategy in Mod-M Sum Games`  

---

## 1. Problem Statement & Key Idea
Given a sequence A of 2N integers and a positive integer M. Alice and Bob take turns choosing an element from A (Alice first). Bob wins if sum(A) = sum(B) mod M, else Alice wins. Determine the winner under optimal play.

**Key Idea**: Bob wants the final sum difference sum(A) - sum(B) = 0 mod M. Identical elements can be symmetrically paired (if Bob copies Alice's choice, their contribution cancels to 0). After cancelling all identical pairs: if M is odd, any unpaired element allows Alice to force sum(A) != sum(B) mod M, so Bob wins iff all elements pair up identically. If M is even, elements with difference M/2 can also pair up, because two such pairs yield difference 0 or M = 0 mod M. Thus Bob wins iff all remaining elements pair up into pairs (x, x + M/2) and the number of such pairs is even.

## 2. Core Observation & Invariant
Cancellation of symmetric components isolates essential game degrees of freedom down to half-period modular pairs.

## 3. Step-by-Step Algorithm
1. Compute frequency of each value a[i] mod M.
2. Remove all complete pairs of identical values (keep count % 2).
3. Collect leftover elements into a multiset/map.
4. If leftover is empty: Bob wins.
5. If M % 2 != 0: Alice wins.
6. If M % 2 == 0:
7.   For each leftover value x: it must pair with (x + M/2) % M.
8.   Count how many such pairs exist.
9.   If all leftover elements pair up into (x, x + M/2) and the number of pairs is even: Bob wins.
10.   Else: Alice wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Modular game theory symmetric reduction and half-period pairing invariants.

**Reusable Pattern**: Symmetric Game Reduction: Cancel identical elements; when parity/modulus permits, match elements with difference M/2.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    map<long long, int> freq;
    for (int i = 0; i < 2 * n; ++i) {
        long long a;
        cin >> a;
        freq[a % m]++;
    }

    map<long long, int> rem;
    for (const auto& [val, cnt] : freq) {
        if (cnt % 2 != 0) {
            rem[val] = 1;
        }
    }

    if (rem.empty()) {
        cout << "Bob\n";
        return 0;
    }

    if (m % 2 != 0) {
        cout << "Alice\n";
        return 0;
    }

    long long half = m / 2;
    int pair_count = 0;

    while (!rem.empty()) {
        auto it = rem.begin();
        long long x = it->first;
        long long target = (x + half) % m;

        if (rem.find(target) == rem.end()) {
            cout << "Alice\n";
            return 0;
        }

        rem.erase(x);
        rem.erase(target);
        pair_count++;
    }

    if (pair_count % 2 == 0) {
        cout << "Bob\n";
    } else {
        cout << "Alice\n";
    }

    return 0;
}
```

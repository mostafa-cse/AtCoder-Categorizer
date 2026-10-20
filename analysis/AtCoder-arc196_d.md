# Problem Analysis: AtCoder-arc196_d — D - Roadway

**Problem ID**: `AtCoder-arc196_d`  
**Contest**: `arc196`  
**Rating / Difficulty**: 2973  
**URL**: https://atcoder.jp/contests/arc196/tasks/arc196_d  
**VJudge Tag**: `[problem:AtCoder-arc196_d]`  
**Category File**: [`../categories/basics/laminar_interval_potential_zobrist_two_pointers.md`](../categories/basics/laminar_interval_potential_zobrist_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
Given M directed trips (S_i, T_i) along a linear road of N cities, count pairs (L, R) (1 <= L <= R <= M) such that the subset of trips with indices in [L, R] can be executed simultaneously without traffic conflict.

## 2. Core Observation & Invariant
A subset of trips on a line has no conflicts iff: (1) all forward trips form a laminar family, (2) all reverse trips form a laminar family, and (3) no forward trip and reverse trip share an endpoint or overlap in conflicting direction. The validity of a range [L, R] is monotonic. We maintain the laminar family condition and endpoint disjointness using two pointers on R, checking validity using Zobrist hashing and a Binary Indexed Tree (BIT) to detect crossing intervals in O(log N).

## 3. Step-by-Step Algorithm
1. 1. Maintain a two-pointer window [L, R] over the M trips.
2. 2. As R expands, insert trip R into the active set.
3. 3. Check laminar compatibility: interval [S_R, T_R] must not cross any existing interval of the same direction (testable via BIT range queries).
4. 4. Check endpoint disjointness with opposing direction trips using hash tables.
5. 5. While [L, R] is invalid, advance L and remove trip L.
6. 6. Add (R - L + 1) to total answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <random>
#include <chrono>

using namespace std;

typedef unsigned long long ull;

const int MAXC = 500005;

struct BIT {
    ull bit[MAXC];
    void add(int e, ull v) {
        e++;
        while (e < MAXC) {
            bit[e - 1] ^= v;
            e += e & -e;
        }
    }
    ull query(int e) {
        if (e < 0) return 0;
        ull s = 0;
        e++;
        while (e > 0) {
            s ^= bit[e - 1];
            e -= e & -e;
        }
        return s;
    }
};

BIT bt[2];
int SS[2][MAXC], ST[2][MAXC];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    mt19937_64 rng(1337);

    vector<int> S(m), T(m);
    vector<ull> hv(m);

    for (int i = 0; i < m; ++i) {
        int s, t;
        cin >> s >> t;
        if (s < t) {
            S[i] = s * 2 + 1;
            T[i] = t * 2;
        } else {
            S[i] = s * 2;
            T[i] = t * 2 + 1;
        }
        hv[i] = rng();
    }

    vector<int> ok(m);
    int L = 0, R = 0;

    for (L = 0; L < m; ++L) {
        while (R < m) {
            int x = (S[R] < T[R]);
            if (SS[x][S[R]]) break;
            if (ST[x][T[R]]) break;
            if (ST[x ^ 1][S[R]]) break;
            if (SS[x ^ 1][T[R]]) break;
            if (bt[x].query(S[R]) != bt[x].query(T[R])) break;

            SS[x][S[R]]++;
            ST[x][T[R]]++;
            bt[x].add(S[R], hv[R]);
            bt[x].add(T[R], hv[R]);
            R++;
        }
        ok[L] = R;
        int x = (S[L] < T[L]);
        SS[x][S[L]]--;
        ST[x][T[L]]--;
        bt[x].add(S[L], hv[L]);
        bt[x].add(T[L], hv[L]);
    }

    while (q--) {
        int ql, qr;
        cin >> ql >> qr;
        if (ok[ql - 1] >= qr) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

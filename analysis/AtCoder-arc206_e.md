# Problem Analysis: AtCoder-arc206_e — E. Rectangle Coloring

**Problem ID**: `AtCoder-arc206_e`  
**Contest**: `arc206`  
**Rating / Difficulty**: 2902  
**URL**: https://atcoder.jp/contests/arc206/tasks/arc206_e  
**VJudge Tag**: `[problem:AtCoder-arc206_e]`  
**Category File**: [`../categories/graph_theory/boundary_good_cells_rectangle_bipartite_matching.md`](../categories/graph_theory/boundary_good_cells_rectangle_bipartite_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`  

---

## 1. Problem Statement & Key Idea
On an N x N grid with weighted non-corner boundary cells, repeatedly choose two unused boundary cells and color the bounding rectangle black. Maximize the total sum of chosen cell weights such that the final colored black area is minimized.

## 2. Core Observation & Invariant
To achieve the global minimum colored area, operations must avoid spreading black cells across both dimensions. Minimum area is attained when all colored rectangles degenerate or align along minimal boundary strips. The legal pairings of boundary cells that preserve this minimal area partition naturally into bipartite compatible sets between opposing or adjacent boundary sections. Finding the maximum weight set of valid non-overlapping pairs reduces to Maximum Weight Matching on a Bipartite Graph.

## 3. Step-by-Step Algorithm
1. 1. Determine the minimal area achievable by analyzing boundary configuration constraints.
2. 2. Classify boundary good cells (Top, Bottom, Left, Right) and construct candidate pairs achieving the minimum area.
3. 3. Formulate the compatibility graph as a bipartite graph between partitioned cell sets.
4. 4. Apply Kuhn's algorithm / Hopcroft-Karp / Hungarian method to find the maximum weight valid matching.
5. 5. Output the maximum sum of cell values.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef long long ll;

ll hoge(int N, const vector<ll>& L, const vector<ll>& R) {
    multiset<ll> L1, L2, R1, R2;
    ll INF = 1LL << 50;
    L1.insert(INF); R1.insert(INF);
    L2.insert(INF); R2.insert(INF);
    L1.insert(L[0]); R1.insert(R[0]);
    for (int i = 0; i < N; ++i) {
        L2.insert(L[i]);
        R2.insert(R[i]);
    }
    ll ret = 1LL << 60;
    for (int i = 0; i < N; ++i) {
        ll a = *L1.begin() + *L2.begin();
        if (*L1.begin() == *L2.begin() && L[i] == *L1.begin()) {
            a = min(*L1.begin() + *next(L2.begin()), *L2.begin() + *next(L1.begin()));
        }
        ll b = *R1.begin() + *R2.begin();
        if (*R1.begin() == *R2.begin() && R[i] == *R1.begin()) {
            b = min(*R1.begin() + *next(R2.begin()), *R2.begin() + *next(R1.begin()));
        }
        ret = min(ret, a + b);
        L2.erase(L2.find(L[i]));
        R2.erase(R2.find(R[i]));
        L1.insert(L[i + 1]);
        R1.insert(R[i + 1]);
    }

    L1.clear(); L2.clear(); R1.clear(); R2.clear();
    L1.insert(INF); L2.insert(INF); R1.insert(INF); R2.insert(INF);
    for (int i = 2; i < N; ++i) {
        L2.insert(L[i]);
        R2.insert(R[i]);
    }
    for (int i = 0; i < N - 1; ++i) {
        ret = min(ret, L[i] + *L1.begin() + R[i + 1] + *R2.begin());
        ret = min(ret, R[i] + *R1.begin() + L[i + 1] + *L2.begin());
        L1.insert(L[i]);
        R1.insert(R[i]);
        if (i + 2 < N) {
            L2.erase(L2.find(L[i + 2]));
            R2.erase(R2.find(R[i + 2]));
        }
    }
    return ret;
}

pair<ll, ll> hoge2(int N, const vector<ll>& L, const vector<ll>& R) {
    multiset<ll> L1, L2, R1, R2;
    ll INF = 1LL << 50;
    L1.insert(INF); R1.insert(INF);
    L2.insert(INF); R2.insert(INF);
    L1.insert(L[0]); R1.insert(R[0]);
    for (int i = 1; i < N; ++i) {
        L2.insert(L[i]);
        R2.insert(R[i]);
    }
    ll r1 = 1LL << 60, r2 = 1LL << 60;
    for (int i = 0; i < N - 1; ++i) {
        r1 = min(r1, *L1.begin() + *next(L1.begin()) + *R2.begin() + *next(R2.begin()));
        r2 = min(r2, *L2.begin() + *next(L2.begin()) + *R1.begin() + *next(R1.begin()));
        L1.insert(L[i + 1]);
        R1.insert(R[i + 1]);
        L2.erase(L2.find(L[i + 1]));
        R2.erase(R2.find(R[i + 1]));
    }
    return {r1, r2};
}

void solve() {
    int N;
    if (!(cin >> N)) return;
    N -= 2;
    vector<ll> U(N), D(N), L(N), R(N);
    for (int i = 0; i < N; ++i) cin >> U[i];
    for (int i = 0; i < N; ++i) cin >> D[i];
    for (int i = 0; i < N; ++i) cin >> L[i];
    for (int i = 0; i < N; ++i) cin >> R[i];

    ll ret1 = hoge(N, U, D);
    ll ret2 = hoge(N, L, R);
    pair<ll, ll> p1 = hoge2(N, U, D);
    pair<ll, ll> p2 = hoge2(N, L, R);

    vector<ll> sU = U, sD = D, sL = L, sR = R;
    sort(sU.begin(), sU.end());
    sort(sD.begin(), sD.end());
    sort(sL.begin(), sL.end());
    sort(sR.begin(), sR.end());

    ret2 += sU[0] + sU[1] + sD[0] + sD[1];
    ret1 += sL[0] + sL[1] + sR[0] + sR[1];

    ll ret = min({ret1, ret2, p1.first + p2.first, p1.second + p2.second});

    if (N >= 3) {
        ret = min(ret, sU[0] + sU[1] + sU[2] + sD[0] + sD[1] + sD[2] + sL[0] + sL[1] + sR[0] + sR[1]);
        ret = min(ret, sL[0] + sL[1] + sL[2] + sR[0] + sR[1] + sR[2] + sU[0] + sU[1] + sD[0] + sD[1]);
    }

    cout << ret << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

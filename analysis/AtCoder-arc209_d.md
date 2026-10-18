# Problem Analysis: AtCoder-arc209_d — D. A_A_i

**Problem ID**: `AtCoder-arc209_d`  
**Contest**: `arc209`  
**Rating / Difficulty**: 2583  
**URL**: https://atcoder.jp/contests/arc209/tasks/arc209_d  
**VJudge Tag**: `[problem:AtCoder-arc209_d]`  
**Category File**: [`../categories/miscellaneous/a_a_i_functional_graphs.md`](../categories/miscellaneous/a_a_i_functional_graphs.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Functional Graphs`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N with elements in {1, ..., N} U {-1}, replace all -1 with integers in {1, ..., N} to make the sequence B defined by B_i = A_{A_i} lexicographically smallest.

## 2. Core Observation & Invariant
In the optimal assignment, Snuke only ever writes at most two distinct values: 1 and p, where p is the minimum index such that A_p = 1. If A_1 can be 1 (either A_1 = 1 or A_1 = -1), setting p = 1 and all -1 to 1 achieves B_i = 1 everywhere possible with zero penalty. When A_1 > 1, setting A_i = p makes B_i = A_p = 1, while the chosen pivot index p suffers B_p = A_1 > 1. To make B lexicographically smallest, we delay choosing p as late as possible, until some index i has B_i = p (requiring p to be minimized immediately).

## 3. Step-by-Step Algorithm
1. If count of -1 is 0: output A[A[i]] directly.
2. If count of -1 is 1: find the single index k with A_k = -1, test all N candidate replacements for A_k in O(N), and pick the lexicographically smallest B.
3. If count of -1 >= 2 and A[1] in {1, -1}: set all -1 to 1 and output A[A[i]].
4. Otherwise (A[1] > 1): simulate evima's 3-phase state machine:
5. Phase 1 (delaying p): set -1 to placeholder p; if A[i] != -1 points to placeholder p, transition to Phase 2; if A[i] points to -1, set that target to 1.
6. Phase 2 (minimizing p): the very next -1 encountered is set to 1 and determines p.
7. Phase 3 (after p determined): all remaining -1 are set to p.
8. If p remains undetermined at the end, set p to the last available -1 (or last locked placeholder).
9. Output B_i = A[A[i]] for all i in 1..N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;
    vector<int> A(N + 1);
    vector<int> neg_indices;
    neg_indices.reserve(N);

    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        if (A[i] == -1) neg_indices.push_back(i);
    }

    if (neg_indices.empty()) {
        for (int i = 1; i <= N; i++) {
            cout << A[A[i]] << (i == N ? "" : " ");
        }
        cout << "\n";
        return;
    }

    if (neg_indices.size() == 1) {
        int k = neg_indices[0];
        vector<int> S;
        S.push_back(k);
        for (int i = 1; i <= N; i++) {
            if (A[i] == k) S.push_back(i);
        }
        sort(S.begin(), S.end());
        S.erase(unique(S.begin(), S.end()), S.end());

        int best_x = 1;
        vector<int> best_tuple;
        for (int x = 1; x <= N; x++) {
            vector<int> cand_tuple;
            cand_tuple.reserve(S.size());
            for (int idx : S) {
                int val = (idx == k) ? (x == k ? x : A[x]) : x;
                cand_tuple.push_back(val);
            }
            if (best_tuple.empty() || cand_tuple < best_tuple) {
                best_tuple = cand_tuple;
                best_x = x;
            }
        }
        A[k] = best_x;
        for (int i = 1; i <= N; i++) {
            cout << A[A[i]] << (i == N ? "" : " ");
        }
        cout << "\n";
        return;
    }

    // neg_indices.size() >= 2
    if (A[1] == 1 || A[1] == -1) {
        for (int i = 1; i <= N; i++) {
            if (A[i] == -1) A[i] = 1;
        }
        for (int i = 1; i <= N; i++) {
            cout << A[A[i]] << (i == N ? "" : " ");
        }
        cout << "\n";
        return;
    }

    const int P_PLACE = -2;
    int p = -1;
    int phase = 1; // 1: delaying p, 2: minimizing p, 3: p determined
    vector<int> locked_p;
    locked_p.reserve(N);

    for (int i = 1; i <= N; i++) {
        if (phase == 1) {
            if (A[i] == 1) {
                p = i;
                phase = 3;
            } else if (A[i] == -1) {
                A[i] = P_PLACE;
                locked_p.push_back(i);
            } else {
                int target = A[i];
                if (A[target] == P_PLACE) {
                    phase = 2;
                } else if (A[target] == -1) {
                    A[target] = 1;
                }
            }
        } else if (phase == 2) {
            if (A[i] == 1) {
                p = i;
                phase = 3;
            } else if (A[i] == -1) {
                A[i] = 1;
                p = i;
                phase = 3;
            } else {
                int target = A[i];
                if (A[target] == -1) {
                    A[target] = 1;
                }
            }
        } else if (phase == 3) {
            if (A[i] == -1) {
                A[i] = p;
            } else {
                int target = A[i];
                if (A[target] == -1) {
                    A[target] = 1;
                }
            }
        }
    }

    if (p == -1) {
        int first_1 = -1;
        for (int i = 1; i <= N; i++) {
            if (A[i] == 1) {
                first_1 = i;
                break;
            }
        }
        if (first_1 != -1) {
            p = first_1;
        } else if (phase == 2) {
            int rem = -1;
            for (int i = 1; i <= N; i++) {
                if (A[i] == -1) {
                    rem = i;
                    break;
                }
            }
            if (rem != -1) {
                p = rem;
            } else {
                p = locked_p.back();
            }
        } else {
            for (int i = N; i >= 1; i--) {
                if (A[i] == P_PLACE) {
                    p = i;
                    break;
                }
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        if (A[i] == P_PLACE || A[i] == -1) {
            A[i] = (i == p) ? 1 : p;
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << A[A[i]] << (i == N ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

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

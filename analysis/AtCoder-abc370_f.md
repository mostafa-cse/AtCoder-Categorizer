# Problem Analysis: AtCoder-abc370_f — Cake Division

**Problem ID**: `AtCoder-abc370_f`  
**Contest**: `abc370`  
**Rating / Difficulty**: 2102  
**URL**: https://atcoder.jp/contests/abc370/tasks/abc370_f  
**VJudge Tag**: `[problem:AtCoder-abc370_f]`  
**Category File**: [`../categories/data_structures/binary_lifting_circular_array_partition.md`](../categories/data_structures/binary_lifting_circular_array_partition.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Sparse Table`  
- **Topic (Skill)**: `Sparse Table`  

---

## 1. Problem Statement & Key Idea
You have a circular cake divided into N pieces with weights A_1, ..., A_N. You want to make K cuts along piece boundaries to divide the cake into K contiguous pieces, maximizing the minimum piece weight. Find this maximum possible weight W, and count how many of the N cut lines never appear in any optimal cut set of size K.

**Key Insight**: Binary search on the minimum piece weight W. For a fixed W, duplicate the array to length 2N to handle circularity. Using two pointers, compute for each position i the earliest right boundary r such that the piece weight sum is at least W. Build a binary lifting table up[j][i] to simulate making K greedy jumps in O(log K). A cut position i can successfully produce K pieces of weight >= W if and only if up[K][i] <= i + N. To count how many cut positions never appear in ANY optimal cut partition, we trace the forward jumps of all valid starting cuts and mark all visited boundaries.

## 2. Core Observation & Invariant
Circular greedy partitioning reduces to functional graphs under binary lifting; doubling table up[j][i] checks K contiguous jumps in O(log K).

## 3. Step-by-Step Algorithm
1. Duplicate array A to 2N and compute prefix sums.
2. Binary search W in [1, sum(A) / K]:
3.   Compute two pointers nxt[i] = earliest r with pref[r] - pref[i] >= W.
4.   Build binary lifting table up[18][2N].
5.   Check if there exists i in [0, N-1] with up[K][i] <= i + N.
6. For optimal W, identify all valid starting cuts i with up[K][i] <= i + N.
7. Trace and mark all cut boundaries visited along chains of length K from valid starting positions.
8. Output optimal W and the count of unmarked cut lines.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(sum A) + N log K)`
- **Space Complexity**: `O(N log K)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Binary lifting on circular arrays combined with binary search on partition bounds.
- **Reusable Pattern**: Circular partition feasibility verification using duplicated array doubling table up[log K][2N].

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(2 * n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i + n] = a[i];
    }

    vector<long long> pref(2 * n + 1, 0);
    for (int i = 0; i < 2 * n; ++i) {
        pref[i + 1] = pref[i] + a[i];
    }

    auto check = [&](long long W) {
        vector<int> nxt(2 * n + 1, 2 * n);
        int r = 0;
        for (int i = 0; i < 2 * n; ++i) {
            while (r <= 2 * n && pref[r] - pref[i] < W) {
                r++;
            }
            nxt[i] = r;
        }

        int LOG = 18;
        vector<vector<int>> up(LOG, vector<int>(2 * n + 1, 2 * n));
        for (int i = 0; i <= 2 * n; ++i) up[0][i] = nxt[i];
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i <= 2 * n; ++i) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }

        for (int i = 0; i < n; ++i) {
            int cur = i;
            for (int j = 0; j < LOG; ++j) {
                if ((k >> j) & 1) {
                    cur = up[j][cur];
                }
            }
            if (cur <= i + n) return true;
        }
        return false;
    };

    long long low = 1, high = pref[n] / k, optW = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            optW = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    int LOG = 18;
    vector<vector<int>> up(LOG, vector<int>(2 * n + 1, 2 * n));
    int r = 0;
    for (int i = 0; i < 2 * n; ++i) {
        while (r <= 2 * n && pref[r] - pref[i] < optW) {
            r++;
        }
        up[0][i] = r;
    }
    for (int j = 1; j < LOG; ++j) {
        for (int i = 0; i <= 2 * n; ++i) {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    vector<bool> can_start(n, false);
    for (int i = 0; i < n; ++i) {
        int cur = i;
        for (int j = 0; j < LOG; ++j) {
            if ((k >> j) & 1) {
                cur = up[j][cur];
            }
        }
        if (cur <= i + n) can_start[i] = true;
    }

    vector<bool> used_cut(n, false);
    for (int i = 0; i < n; ++i) {
        if (can_start[i]) {
            int cur = i;
            for (int step = 0; step < k; ++step) {
                used_cut[cur % n] = true;
                cur = up[0][cur];
            }
        }
    }

    int unused_cuts = 0;
    for (int i = 0; i < n; ++i) {
        if (!used_cut[i]) unused_cuts++;
    }

    cout << optW << " " << unused_cuts << "\n";
    return 0;
}
```

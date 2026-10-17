# Problem Analysis: AtCoder-agc048_c — Penguin Skating

**Problem ID**: `AtCoder-agc048_c`  
**Contest**: `agc048`  
**Rating / Difficulty**: 2120  
**URL**: https://atcoder.jp/contests/agc048/tasks/agc048_c  
**VJudge Tag**: `[problem:AtCoder-agc048_c]`  
**Category File**: [`../categories/basics/coordinate_shifted_cluster_two_pointers.md`](../categories/basics/coordinate_shifted_cluster_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
N penguins stand on a line at A_1 < A_2 < ... < A_N on a board of length L. Sliding a penguin moves it until it hits another penguin or the boundary. Given target positions B_1 < B_2 < ... < B_N, find the minimum operations to reach B, or -1 if impossible.

**Key Insight**: Shift coordinates by setting a_i = A_i - i and b_i = B_i - i. When penguins slide and cluster, contiguous blocks in a become equal to the anchor penguin's value! Therefore, the target sequence b can be formed if and only if each b_i can be matched to an occurrence of the identical value in a. Since penguins move either strictly leftward (b_i < a_i) or rightward (b_i > a_i), we can use two pointers to match each b_i with the closest matching value in a, accumulating total move steps.

## 2. Core Observation & Invariant
Penguin sliding collapses differences A_i - i into contiguous constant blocks, reducing the problem to two-pointer matching on monotonic transformed coordinates.

## 3. Step-by-Step Algorithm
1. Set a_i = A_i - i and b_i = B_i - i with boundary sentinels.
2. Verify matching via two pointers j_left and j_right:
3.   If b_i < a_i: advance j_left to find a[j_left] == b_i, add (i - j_left) moves.
4.   If b_i > a_i: advance j_right to find a[j_right] == b_i, add (j_right - i) moves.
5.   If any value cannot be matched, output -1.
6. Output total moves.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Coordinate shift invariant mapping cluster sliding to constant blocks and two-pointer matching.
- **Reusable Pattern**: Compressing contiguous sliding collisions into constant value blocks on offset coordinates A_i - i.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<long long> A(n + 2), B(n + 2);
    A[0] = 0; B[0] = 0;
    for (int i = 1; i <= n; ++i) cin >> A[i];
    for (int i = 1; i <= n; ++i) cin >> B[i];
    A[n + 1] = L + 1; B[n + 1] = L + 1;

    vector<long long> a(n + 2), b(n + 2);
    for (int i = 0; i <= n + 1; ++i) {
        a[i] = A[i] - i;
        b[i] = B[i] - i;
    }

    long long ans = 0;
    int j_left = 0, j_right = 0;

    for (int i = 1; i <= n; ++i) {
        if (a[i] == b[i]) continue;

        if (b[i] < a[i]) {
            while (j_left < i && a[j_left] < b[i]) {
                j_left++;
            }
            if (a[j_left] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (i - j_left);
        } else {
            j_right = max(j_right, i);
            while (j_right <= n + 1 && a[j_right] < b[i]) {
                j_right++;
            }
            if (a[j_right] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (j_right - i);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

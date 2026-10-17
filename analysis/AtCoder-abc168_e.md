# Problem Analysis: AtCoder-abc168_e — ∙ (Bullet)

**Problem ID**: `AtCoder-abc168_e`  
**Contest**: `abc168`  
**Rating / Difficulty**: 1896  
**URL**: https://atcoder.jp/contests/abc168/tasks/abc168_e  
**VJudge Tag**: `[problem:AtCoder-abc168_e]`  
**Category File**: [`../categories/combinatorics/orthogonal_vector_slope_equivalence_classes.md`](../categories/combinatorics/orthogonal_vector_slope_equivalence_classes.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Slope Equivalence Classes`  
- **Topic (Skill)**: `Orthogonal Vector Slope Pairing with Mutually Exclusive Subset Combinatorics`  

---

## 1. Problem Statement & Key Idea
Given N fish with characteristics (A_i, B_i). Two fish i and j fight iff A_i * A_j + B_i * B_j = 0. Find the number of non-empty subsets of fish that contain no fighting pairs, modulo 10^9 + 7.

**Key Insight**: Two vectors (A_1, B_1) and (A_2, B_2) are orthogonal iff their slopes are negative reciprocals. Reduce each vector by dividing by gcd(|A|, |B|) and canonicalizing to the upper half-plane. Vectors partition into orthogonal pairs of classes with counts c_1 and c_2.

## 2. Core Observation & Invariant
For an orthogonal pair of classes, you can choose any non-empty subset from class 1 (2^{c_1} - 1 ways) or class 2 (2^{c_2} - 1 ways), or neither (1 way), giving (2^{c_1} + 2^{c_2} - 1) choices. Zero vectors (0, 0) fight with nobody and can be appended at the end.

## 3. Step-by-Step Algorithm
1. Handle (0, 0) vectors: count zero_count.
2. Canonicalize each non-zero vector (A, B):
3.   g = gcd(|A|, |B|); A /= g; B /= g;
4.   Ensure canonical orientation: if B < 0 || (B == 0 && A < 0): A = -A, B = -B.
5.   Orthogonal partner of (A, B) is canonical form of (-B, A).
6. Group orthogonal classes into pairs (c_1, c_2).
7. Total ways = (product over pairs (2^{c_1} + 2^{c_2} - 1) + zero_count - 1) mod MOD.
8. Print total ways.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max_val))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

const int MOD = 1000000007;

long long gcd(long long a, long long b) {
    return b == 0 ? abs(a) : gcd(b, a % b);
}

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int zero_count = 0;
    map<pair<long long, long long>, int> counts;

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a == 0 && b == 0) {
            zero_count++;
            continue;
        }

        long long g = gcd(a, b);
        a /= g;
        b /= g;

        if (b < 0 || (b == 0 && a < 0)) {
            a = -a;
            b = -b;
        }

        counts[{a, b}]++;
    }

    map<pair<long long, long long>, bool> visited;
    long long total_ans = 1;

    for (auto& [vec, count1] : counts) {
        if (visited[vec]) continue;

        long long a = vec.first, b = vec.second;
        // Orthogonal vector: (-b, a) canonicalized
        long long oa = -b, ob = a;
        if (ob < 0 || (ob == 0 && oa < 0)) {
            oa = -oa;
            ob = -ob;
        }

        visited[vec] = true;
        int count2 = 0;
        if (counts.count({oa, ob})) {
            count2 = counts[{oa, ob}];
            visited[{oa, ob}] = true;
        }

        long long ways1 = power(2, count1);
        long long ways2 = power(2, count2);
        long long combined = (ways1 + ways2 - 1 + MOD) % MOD;

        total_ans = (total_ans * combined) % MOD;
    }

    total_ans = (total_ans - 1 + zero_count + MOD) % MOD;
    cout << total_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pairing mutually exclusive orthogonal equivalence classes under dot product constraints.
- **Reusable Pattern**: `Orthogonal Equivalence Partition: Multiply (2^{c_1} + 2^{c_2} - 1) across orthogonal pairs.`

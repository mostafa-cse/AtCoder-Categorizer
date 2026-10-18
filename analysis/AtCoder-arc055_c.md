# Problem Analysis: AtCoder-arc055_c — C. ABCAC

**Problem ID**: `AtCoder-arc055_c`  
**Contest**: `arc055`  
**Rating / Difficulty**: 2392  
**URL**: https://atcoder.jp/contests/arc055/tasks/arc055_c  
**VJudge Tag**: `[problem:AtCoder-arc055_c]`  
**Category File**: [`../categories/strings/abcac_decomposition_lcp_lcs_z_algorithm.md`](../categories/strings/abcac_decomposition_lcp_lcs_z_algorithm.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Z Algorithm`  

---

## 1. Problem Statement & Key Idea
Fix the split index between ABC and AC. The length of A is bounded above by LCP and below by L - LCS. Computing both via Z-algorithm on S and S^R counts valid decompositions in O(|S|) time.

## 2. Core Observation & Invariant
In any decomposition S = ABCAC with non-empty A, B, C, let L = |AC| = |S| - i, where i is the start index of the suffix AC. A must be a common prefix of S and S[i..], so 1 <= |A| <= min(LCP(S, S[i..]), L-1). C must be a common suffix of S[..i-1] and S, so |AC| - |A| <= LCS(S[..i-1], S), giving max(1, L - LCS) <= |A| <= min(LCP, L-1).

## 3. Step-by-Step Algorithm
1. Run the Z-algorithm on S to compute forward LCP values z_fwd.
2. Run the Z-algorithm on the reversed string S^R to compute reverse LCS values z_rev.
3. Iterate over split index i from 1 to N-1 with L = N - i >= 2 and i > L (ensuring |B| >= 1).
4. Set lcp = min(z_fwd[i], L - 1) and lcs = min(z_rev[N - i], L - 1).
5. Valid lengths of A lie in [max(1, L - lcs), min(lcp, L - 1)], contributing max(0, high - low + 1) in O(1) per index, total O(|S|) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

vector<int> z_algorithm(const string& s) {
    int n = s.size();
    vector<int> z(n);
    z[0] = n;
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    if (!(cin >> S)) return 0;
    int N = S.size();

    vector<int> z_fwd = z_algorithm(S);
    string S_rev = S;
    reverse(S_rev.begin(), S_rev.end());
    vector<int> z_rev = z_algorithm(S_rev);

    ll ans = 0;
    for (int i = 1; i < N; i++) {
        int L = N - i;
        if (L < 2) continue;
        if (i <= L) continue; // need |B| = i - L >= 1

        int lcp = min(z_fwd[i], L - 1);
        int rev_idx = N - i;
        int lcs = min(z_rev[rev_idx], L - 1);

        int low = max(1, L - lcs);
        int high = min(lcp, L - 1);
        if (low <= high) {
            ans += (high - low + 1);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

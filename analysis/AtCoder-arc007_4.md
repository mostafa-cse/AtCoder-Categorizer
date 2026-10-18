# Problem Analysis: AtCoder-arc007_4 — D - 破れた宿題

**Problem ID**: `AtCoder-arc007_4`  
**Contest**: `arc007`  
**Rating / Difficulty**: 2491  
**URL**: https://atcoder.jp/contests/arc007/tasks/arc007_4  
**VJudge Tag**: `[problem:AtCoder-arc007_4]`  
**Category File**: [`../categories/miscellaneous/torn_homework_ap_reconstruction.md`](../categories/miscellaneous/torn_homework_ap_reconstruction.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Heavy Implementation Problems`  

---

## 1. Problem Statement & Key Idea
Given a torn concatenated prefix string $S$ of an arithmetic progression $(A, D)$, find the lexicographically minimal $(A, D)$ with $A, D \ge 1$.

## 2. Core Observation & Invariant
If $S$ starts with $k$ zeros, the first term $A$ must have been severed, with minimal $A = 10^k$. If $S$ starts with a non-zero digit, $A$ can be any prefix $S[0 \dots \text{lenA}-1]$. In both cases, the remaining string $R$ begins with the second term $T_2 = A + D$. Either $R$ is entirely a prefix of $T_2$ (in which case $T_2$ is formed by padding $R$ with zeros until $T_2 > A$), or $T_2$ is a proper prefix of $R$, determining $D = T_2 - A$. In the latter case, we verify that subsequent terms $A + 2D, A + 3D, \dots$ match the rest of $S$. Using BigInt string arithmetic, we test all valid prefixes.

## 3. Step-by-Step Algorithm
1. 1. If $S$ starts with '0', count $k$ leading zeros and fix $A = 10^k$. If $k = N$, set $D = 1$.
2. 2. Otherwise, iterate over all possible prefix lengths for $A$ from $1$ to $N$.
3. 3. For each choice of $A$, let $R$ be the remaining suffix. Check candidates where $R$ is a prefix of $T_2$, padding $R$ to be the minimal number $> A$.
4. 4. For all split points of $R$ into $T_2$ and remainder, compute $D = T_2 - A$ and verify subsequent progression terms match the remaining string.
5. 5. Maintain and output the minimal $(A, D)$ using lexicographical string comparison.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Comparison for large numbers as strings
bool str_less(const string& a, const string& b) {
    if (a.length() != b.length()) return a.length() < b.length();
    return a < b;
}

// Addition of large numbers
string str_add(const string& a, const string& b) {
    string res = "";
    int carry = 0;
    int i = (int)a.length() - 1;
    int j = (int)b.length() - 1;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        res += to_string(sum % 10);
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

// Subtraction of large numbers a - b (assuming a >= b)
string str_sub(const string& a, const string& b) {
    string res = "";
    int borrow = 0;
    int i = (int)a.length() - 1;
    int j = (int)b.length() - 1;
    while (i >= 0) {
        int sub = (a[i] - '0') - borrow;
        if (j >= 0) sub -= (b[j--] - '0');
        if (sub < 0) {
            sub += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        res += to_string(sub);
        i--;
    }
    while (res.length() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

bool check_progression(const string& A, const string& D, const string& S, int start_idx) {
    string curr = str_add(A, str_add(D, D));
    int idx = start_idx;
    int n = S.length();
    while (idx < n) {
        for (char c : curr) {
            if (idx == n) return true;
            if (S[idx] != c) return false;
            idx++;
        }
        curr = str_add(curr, D);
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    if (!(cin >> S)) return 0;
    int N = S.length();

    string best_A = "";
    string best_D = "";

    auto update = [&](const string& A, const string& D) {
        if (D == "0" || D.empty()) return;
        if (best_A.empty()) {
            best_A = A;
            best_D = D;
        } else if (str_less(A, best_A)) {
            best_A = A;
            best_D = D;
        } else if (A == best_A && str_less(D, best_D)) {
            best_D = D;
        }
    };

    if (S[0] == '0') {
        int k = 0;
        while (k < N && S[k] == '0') k++;
        string A_str = "1" + string(k, '0');
        if (k == N) {
            update(A_str, "1");
        } else {
            string R = S.substr(k);
            if (str_less(A_str, R)) {
                update(A_str, str_sub(R, A_str));
            } else {
                string cand = R;
                if (cand.length() < A_str.length()) cand += string(A_str.length() - cand.length(), '0');
                if (str_less(A_str, cand)) {
                    update(A_str, str_sub(cand, A_str));
                } else {
                    cand += "0";
                    update(A_str, str_sub(cand, A_str));
                }
            }

            for (int len2 = 1; len2 < (int)R.length(); ++len2) {
                string T2_str = R.substr(0, len2);
                if (T2_str[0] == '0') continue;
                if (str_less(A_str, T2_str)) {
                    string D_str = str_sub(T2_str, A_str);
                    if (check_progression(A_str, D_str, S, k + len2)) {
                        update(A_str, D_str);
                    }
                }
            }
        }
    } else {
        for (int lenA = 1; lenA <= N; ++lenA) {
            string A_str = S.substr(0, lenA);
            if (lenA == N) {
                update(A_str, "1");
                continue;
            }
            if (S[lenA] == '0') continue;
            string R = S.substr(lenA);
            if (str_less(A_str, R)) {
                update(A_str, str_sub(R, A_str));
            } else {
                string cand = R;
                if (cand.length() < A_str.length()) cand += string(A_str.length() - cand.length(), '0');
                if (str_less(A_str, cand)) {
                    update(A_str, str_sub(cand, A_str));
                } else {
                    cand += "0";
                    update(A_str, str_sub(cand, A_str));
                }
            }

            for (int len2 = 1; len2 < (int)R.length(); ++len2) {
                string T2_str = R.substr(0, len2);
                if (T2_str[0] == '0') continue;
                if (str_less(A_str, T2_str)) {
                    string D_str = str_sub(T2_str, A_str);
                    if (check_progression(A_str, D_str, S, lenA + len2)) {
                        update(A_str, D_str);
                    }
                }
            }
        }
    }

    cout << best_A << " " << best_D << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

# Problem Analysis: AtCoder-arc127_c — Binary String

**Problem ID**: `AtCoder-arc127_c`  
**Contest**: `arc127`  
**Rating / Difficulty**: 2087  
**URL**: https://atcoder.jp/contests/arc127/tasks/arc127_c  
**VJudge Tag**: `[problem:AtCoder-arc127_c]`  
**Category File**: [`../categories/data_structures/lexicographical_preorder_binary_trie.md`](../categories/data_structures/lexicographical_preorder_binary_trie.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
Consider all non-empty binary strings of length at most N that do not start with '0'. When ordered lexicographically, find the X-th string, where X is given as a binary string.

**Key Insight**: The set of valid non-empty binary strings not starting with '0' correspond to the preorder traversal of a complete binary trie rooted at prefix '1' of depth up to N. At any prefix of length L: 1) the prefix itself is visited first (1 string); 2) then all strings extending with '0' (a complete binary subtree of depth N - L - 1 having 2^{N-L} - 1 strings); 3) then all strings extending with '1'. To find the X-th string, we maintain X as a large binary integer. At each step, after visiting the node, we compare X with the size of the left branch (2^{N-L-1} strings). If X <= left_subtree_size, we append '0' and descend; otherwise, we subtract left_subtree_size from X, append '1', and descend.

## 2. Core Observation & Invariant
Lexicographical order of binary strings corresponds exactly to preorder traversal on a binary trie.

## 3. Step-by-Step Algorithm
1. Let string start with '1'. Decrement X by 1. If X == 0, output '1'.
2. For length L from 1 to N - 1:
3.   The left branch ('0') contains subtree size S = 2^{N - L} - 1.
4.   Left branch has S nodes. The root of left branch is 1 node.
5.   Compare X with 2^{N - L - 1}:
6.   If X <= 2^{N - L - 1} - 1 (or 1 + left subtrees):
7.     Append '0', decrement X by 1.
8.     If X == 0, break.
9.   Else:
10.     Append '1', subtract 2^{N - L - 1} from X, decrement X by 1.
11.     If X == 0, break.
12. Output the constructed binary string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Big-integer navigation and preorder rank decomposition on complete binary tries.
- **Reusable Pattern**: Translating lexicographical K-th string queries into big-integer prefix branch comparison on virtual digital tries.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // Convert s to binary array of size n+1 (big integer)
    vector<int> x(n + 1, 0);
    int len = s.size();
    for (int i = 0; i < len; ++i) {
        x[n - len + 1 + i] = s[i] - '0';
    }

    auto dec = [&]() {
        for (int i = n; i >= 1; --i) {
            if (x[i] == 1) {
                x[i] = 0;
                break;
            } else {
                x[i] = 1;
            }
        }
    };

    auto is_zero = [&]() {
        for (int i = 1; i <= n; ++i) {
            if (x[i] != 0) return false;
        }
        return true;
    };

    dec();
    string ans = "1";

    for (int l = 1; l < n; ++l) {
        if (is_zero()) break;

        // Compare X with 2^(n - l - 1)
        // Bit position is (n - l) from right, corresponding to x[l + 1]
        if (x[l + 1] == 1) {
            ans += '1';
            x[l + 1] = 0; // subtract 2^(n - l - 1)
            dec();
        } else {
            ans += '0';
            dec();
        }
    }

    cout << ans << "\n";
    return 0;
}
```

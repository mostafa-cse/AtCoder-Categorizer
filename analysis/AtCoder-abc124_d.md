# Problem Analysis: AtCoder-abc124_d — Handstand

**Problem ID**: `AtCoder-abc124_d`  
**Contest**: `abc124`  
**Rating / Difficulty**: 1138  
**URL**: https://atcoder.jp/contests/abc124/tasks/abc124_d  
**VJudge Tag**: `[problem:AtCoder-abc124_d]`  
**Category File**: [`../categories/basics/run_length_sliding_window_expansion.md`](../categories/basics/run_length_sliding_window_expansion.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Sliding Window`  
- **Topic (Skill)**: `Run-Length Compression Sliding Window Expansion`  

---

## 1. Problem Statement & Key Idea
Given a binary string S. In one operation, flip a contiguous segment of '0's into '1's. At most K operations. Maximize consecutive '1's in the resulting string.

**Key Idea**: Compress S into alternating run-length segments of '1's and '0's.

## 2. Core Observation & Invariant
Flipping K segments of '0's allows taking a contiguous sequence of runs containing at most K '0'-runs and their intervening/adjacent '1'-runs. This corresponds to a sliding window of length at most 2*K + 1 on the alternating run-length array.

## 3. Step-by-Step Algorithm
1. Run-length encode S into pairs (char, count).
2. Slide a window [L, R] over the run array: expand R while count of '0' blocks <= K.
3. Maintain the sum of lengths in window and track maximum.
4. Print the maximum length.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Block {
    char c;
    int len;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    string s;
    if (!(cin >> n >> k >> s)) return 0;

    vector<Block> blocks;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        blocks.push_back({s[i], j - i});
        i = j;
    }

    int max_len = 0;
    int cur_len = 0;
    int zero_blocks = 0;
    int r = 0;

    for (int l = 0; l < (int)blocks.size(); ++l) {
        while (r < (int)blocks.size()) {
            if (blocks[r].c == '0' && zero_blocks == k) break;
            if (blocks[r].c == '0') zero_blocks++;
            cur_len += blocks[r].len;
            r++;
        }

        max_len = max(max_len, cur_len);

        if (blocks[l].c == '0') zero_blocks--;
        cur_len -= blocks[l].len;
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sliding window over run-length encoded compressed segments.
- **Reusable Pattern**: `Run-length sliding window: expand window maintaining at most K inverted blocks.`

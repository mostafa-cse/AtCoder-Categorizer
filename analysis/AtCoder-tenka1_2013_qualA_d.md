# Problem Analysis: AtCoder-tenka1_2013_qualA_d — D - 天下一展開

**Problem ID**: `AtCoder-tenka1_2013_qualA_d`  
**Contest**: `tenka1_2013_qualA`  
**Rating / Difficulty**: 2507  
**URL**: https://atcoder.jp/contests/tenka1_2013_qualA/tasks/tenka1_2013_qualA_d  
**VJudge Tag**: `[problem:AtCoder-tenka1_2013_qualA_d]`  
**Category File**: [`../categories/miscellaneous/tenka1_expansion_ast_range_extraction.md`](../categories/miscellaneous/tenka1_expansion_ast_range_extraction.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Expression Parsing`  

---

## 1. Problem Statement & Key Idea
Extract a substring of length $L \le 10^5$ starting at 0-indexed position $B$ from an EBNF run-length compressed string $S$ with decompressed length up to $10^{15}$.

## 2. Core Observation & Invariant
The compressed string grammar consists of literals, blocks, and repetition expressions `(expr)K`. Parse the expression into an Abstract Syntax Tree (AST) where each node computes its decompressed length using 64-bit integers. If $B < 0$, wrap to $M + B$ where $M$ is root length. Querying character by character takes too long when $L = 10^5$, but querying the continuous range $[B, B + L - 1]$ recursively through the AST intersects at most 2 periods per repetition node, yielding $O(L + \text{depth})$ efficient extraction.

## 3. Step-by-Step Algorithm
1. 1. Parse input string $S$ using a recursive descent parser into an AST with `LIT`, `REP`, and `BLOCK` nodes.
2. 2. Bottom-up compute the decompressed length of each node.
3. 3. Adjust negative start index $B \gets B + M$ where $M$ is root length.
4. 4. Recursively extract range $[B, B + L - 1]$: for `REP` nodes, query first partial period, repeat full periods if any, and query last partial period.
5. 5. Print the extracted substring of length $L$.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + L)`
- **Space Complexity**: `O(|S| + L)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

enum NodeType { LIT, REP, BLOCK };

struct Node {
    NodeType type;
    string text;
    long long count;
    vector<Node> children;
    long long len;
};

Node parse_block(const string& S, int& i) {
    Node node;
    node.type = BLOCK;
    node.len = 0;
    while (i < (int)S.length() && S[i] != ')') {
        if (S[i] == '(') {
            i++; // skip '('
            Node inner = parse_block(S, i);
            i++; // skip ')'
            long long cnt = 0;
            while (i < (int)S.length() && isdigit(S[i])) {
                cnt = cnt * 10 + (S[i] - '0');
                i++;
            }
            Node rep_node;
            rep_node.type = REP;
            rep_node.count = cnt;
            rep_node.children.push_back(inner);
            rep_node.len = inner.len * cnt;
            node.children.push_back(rep_node);
            node.len += rep_node.len;
        } else {
            string lit = "";
            while (i < (int)S.length() && isalpha(S[i])) {
                lit += S[i];
                i++;
            }
            Node lit_node;
            lit_node.type = LIT;
            lit_node.text = lit;
            lit_node.len = lit.length();
            node.children.push_back(lit_node);
            node.len += lit_node.len;
        }
    }
    return node;
}

void extract_range(const Node& node, long long ql, long long qr, string& out) {
    if (ql > qr) return;
    if (node.type == LIT) {
        out += node.text.substr(ql, qr - ql + 1);
    } else if (node.type == BLOCK) {
        long long cur = 0;
        for (const auto& ch : node.children) {
            long long nxt = cur + ch.len;
            if (max(ql, cur) <= min(qr, nxt - 1)) {
                extract_range(ch, max(0LL, ql - cur), min(ch.len - 1, qr - cur), out);
            }
            cur = nxt;
        }
    } else if (node.type == REP) {
        long long inner_len = node.children[0].len;
        long long k_start = ql / inner_len;
        long long k_end = qr / inner_len;
        if (k_start == k_end) {
            extract_range(node.children[0], ql % inner_len, qr % inner_len, out);
        } else {
            extract_range(node.children[0], ql % inner_len, inner_len - 1, out);
            if (k_end - k_start > 1) {
                string full = "";
                extract_range(node.children[0], 0, inner_len - 1, full);
                for (long long k = k_start + 1; k < k_end; ++k) {
                    out += full;
                }
            }
            extract_range(node.children[0], 0, qr % inner_len, out);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long B, L, N;
    string S;
    if (!(cin >> B >> L >> N >> S)) return 0;

    int idx = 0;
    Node root = parse_block(S, idx);

    long long M = root.len;
    if (B < 0) {
        B += M;
    }

    string ans = "";
    extract_range(root, B, B + L - 1, ans);

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

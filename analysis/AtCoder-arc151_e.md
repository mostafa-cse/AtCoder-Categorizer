# Problem Analysis: AtCoder-arc151_e — E - Keep Being Substring

**Problem ID**: `AtCoder-arc151_e`  
**Contest**: `arc151`  
**Rating / Difficulty**: 2713  
**URL**: https://atcoder.jp/contests/arc151/tasks/arc151_e  
**VJudge Tag**: `[problem:AtCoder-arc151_e]`  
**Category File**: [`../categories/strings/keep_being_substring_automata.md`](../categories/strings/keep_being_substring_automata.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Automaton`  

---

## 1. Problem Statement & Key Idea
Given an integer sequence A of length N, and two contiguous subsequences X of length P and Y of length Q, we can add/delete elements from the front or back of X such that X remains a non-empty contiguous subsequence of A at all times. We want to find the minimum number of operations to transform X into Y.

## 2. Core Observation & Invariant
Each operation either increments or decrements the length of X by 1. If X and Y share a common contiguous substring S, we can shrink X to S and expand S to Y in |P| + |Q| - 2|S| operations. To minimize this, we seek the Longest Common Substring (LCS) of X and Y, which can be found in O(P + Q) using a Suffix Automaton built on X. If X and Y have no common substring (LCS = 0), X must shrink to a single element u, transition along adjacent elements in A to an element v in Y via a shortest path of distance d in the value adjacency graph of A (costing 2d operations), and expand to Y. The total operations in this case is |P| + |Q| - 2 + 2d, computed via multi-source BFS.

## 3. Step-by-Step Algorithm
1. 1. Build a Suffix Automaton on sequence X in O(P log(sigma)) time.
2. 2. Feed sequence Y through the Suffix Automaton to find the length L of the longest common substring between X and Y.
3. 3. If L > 0, return P + Q - 2 * L.
4. 4. If L == 0, construct the undirected adjacency graph on the values 1..N where an edge connects A[i] and A[i+1] for all 1 <= i < N.
5. 5. Run a multi-source BFS starting with all distinct values in X at distance 0 to find the minimum distance d to any value in Y.
6. 6. Return P + Q - 2 + 2 * d.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + P log P + Q log P)`
- **Space Complexity**: `O(N + P)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct State {
    int len;
    int link;
    map<int, int> next;
};

const int MAXLEN = 200005;
State st[MAXLEN * 2];
int sz, last;

void sam_init() {
    st[0].len = 0;
    st[0].link = -1;
    st[0].next.clear();
    sz = 1;
    last = 0;
}

void sam_extend(int c) {
    int cur = sz++;
    st[cur].len = st[last].len + 1;
    st[cur].link = -1;
    st[cur].next.clear();

    int p = last;
    while (p != -1 && !st[p].next.count(c)) {
        st[p].next[c] = cur;
        p = st[p].link;
    }
    if (p == -1) {
        st[cur].link = 0;
    } else {
        int q = st[p].next[c];
        if (st[p].len + 1 == st[q].len) {
            st[cur].link = q;
        } else {
            int clone = sz++;
            st[clone].len = st[p].len + 1;
            st[clone].next = st[q].next;
            st[clone].link = st[q].link;
            while (p != -1 && st[p].next.count(c) && st[p].next[c] == q) {
                st[p].next[c] = clone;
                p = st[p].link;
            }
            st[q].link = clone;
            st[cur].link = clone;
        }
    }
    last = cur;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int P;
    cin >> P;
    vector<int> X(P);
    for (int i = 0; i < P; ++i) {
        cin >> X[i];
    }

    int Q;
    cin >> Q;
    vector<int> Y(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> Y[i];
    }

    sam_init();
    for (int x : X) {
        sam_extend(x);
    }

    int v = 0, cur_len = 0;
    int max_lcs = 0;
    for (int y : Y) {
        while (v > 0 && !st[v].next.count(y)) {
            v = st[v].link;
            cur_len = st[v].len;
        }
        if (st[v].next.count(y)) {
            v = st[v].next[y];
            cur_len++;
        } else {
            v = 0;
            cur_len = 0;
        }
        if (cur_len > max_lcs) {
            max_lcs = cur_len;
        }
    }

    if (max_lcs > 0) {
        long long ans = 1LL * P + Q - 2LL * max_lcs;
        cout << ans << "\n";
        return 0;
    }

    // Graph BFS
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u = A[i], w = A[i + 1];
        adj[u].push_back(w);
        adj[w].push_back(u);
    }

    vector<bool> is_target(N + 1, false);
    for (int y : Y) {
        is_target[y] = true;
    }

    vector<int> dist(N + 1, -1);
    queue<int> q;
    for (int x : X) {
        if (dist[x] == -1) {
            dist[x] = 0;
            q.push(x);
        }
    }

    int min_d = -1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (is_target[u]) {
            min_d = dist[u];
            break;
        }

        for (int nxt : adj[u]) {
            if (dist[nxt] == -1) {
                dist[nxt] = dist[u] + 1;
                q.push(nxt);
            }
        }
    }

    long long ans = 1LL * P + Q - 2LL + 2LL * min_d;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

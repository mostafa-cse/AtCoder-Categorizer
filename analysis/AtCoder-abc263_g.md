# Problem Analysis: AtCoder-abc263_g — G. Erasing Prime Pairs

**Problem ID**: `AtCoder-abc263_g`  
**Contest**: `abc263`  
**Rating / Difficulty**: 2261  
**URL**: https://atcoder.jp/contests/abc263/tasks/abc263_g  
**VJudge Tag**: `[problem:AtCoder-abc263_g]`  
**Category File**: [`../categories/graph_theory/bipartite_matching_prime_pairs_ternary_search.md`](../categories/graph_theory/bipartite_matching_prime_pairs_ternary_search.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`  

---

## 1. Problem Statement & Key Idea
Given $N$ distinct values $A_i$ with frequencies $B_i$. In each operation, choose two numbers summing to a prime and erase them. Find the maximum number of operations.

## 2. Core Observation & Invariant
Except for $1 + 1 = 2$, every prime sum must be odd, which requires pairing one odd integer and one even integer. The conflict graph between odd and even integers is bipartite. If $k$ pairs of $(1, 1)$ are reserved, $2k$ ones are removed, and the remaining ones participate in the bipartite matching with the even numbers. The total operations $f(k) + k$ is concave in $k$, allowing ternary search over $k \in [0, \lfloor B_1 / 2 \rfloor]$.

## 3. Step-by-Step Algorithm
1. If 1 is present, ternary search over $k \in [0, \lfloor B_1 / 2 \rfloor]$.
2. For each $k$, construct a bipartite flow network with Source to Odd numbers, Even numbers to Sink, and edges for pairs summing to prime.
3. Evaluate max flow $f(k)$ using Dinic and compute $f(k) + k$.
4. Output the maximum over all tested $k$.

## 4. Complexity Analysis
- **Time Complexity**: `O(E \sqrt{V} \log(\max B))`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Dinic {
    struct Edge {
        int to;
        long long cap;
        long long flow;
        int rev;
    };
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            long long tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, 1e18)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

bool is_prime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N), B(N);
    long long count_one = 0;
    int idx_one = -1;

    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> B[i];
        if (A[i] == 1) {
            count_one = B[i];
            idx_one = i;
        }
    }

    auto eval = [&](long long k) -> long long {
        // Reserve 2k ones. Remaining ones = count_one - 2k.
        // Node 0: S, Node N + 1: T
        // Odd numbers connected from S
        // Even numbers connected to T
        Dinic dinic(N + 2);
        int S = 0, T = N + 1;

        for (int i = 0; i < N; ++i) {
            if (A[i] % 2 == 1) {
                long long cap = B[i];
                if (A[i] == 1) {
                    cap = count_one - 2 * k;
                }
                dinic.add_edge(S, i + 1, cap);
            } else {
                dinic.add_edge(i + 1, T, B[i]);
            }
        }

        for (int i = 0; i < N; ++i) {
            if (A[i] % 2 == 1) {
                for (int j = 0; j < N; ++j) {
                    if (A[j] % 2 == 0 && is_prime(A[i] + A[j])) {
                        dinic.add_edge(i + 1, j + 1, 1e18);
                    }
                }
            }
        }

        long long f = dinic.max_flow(S, T);
        return f + k;
    };

    if (idx_one == -1) {
        cout << eval(0) << "\n";
        return 0;
    }

    long long low = 0, high = count_one / 2;
    while (high - low > 3) {
        long long m1 = low + (high - low) / 3;
        long long m2 = high - (high - low) / 3;
        if (eval(m1) < eval(m2)) {
            low = m1;
        } else {
            high = m2;
        }
    }

    long long ans = 0;
    for (long long k = low; k <= high; ++k) {
        ans = max(ans, eval(k));
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*

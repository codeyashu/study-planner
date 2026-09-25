---
title: DSA question bank
track: dsa
slug: questions
tags: [dsa, questions]
last_reviewed: 2026-09-25
---

# DSA question bank

Cross-topic conceptual and complexity questions, interview-communication scripts, and a 30-question rapid-fire round. Topic-specific L1-L4 questions live on each pattern page. Return to the [DSA overview](index.md).

!!! tip "How to use"
    Answer aloud first (60-90 seconds), then open the answer. Anything you miss goes on your spaced-repetition sheet (see the [tracker](problem-tracker.md)).

## Conceptual and complexity questions (45)

### Complexity

??? question "Q1. What is the difference between O, Theta and Omega, and which do interviewers mean by 'Big-O'?"
    ??? success "Answer"
        O is an upper bound, Omega a lower bound, Theta a tight bound. In interviews 'Big-O' almost always means the tight worst-case bound. Say Theta or 'tight' when it matters, and state the case (worst, average, amortised).

??? question "Q2. Why is building a heap O(n) but heapsort O(n log n)?"
    ??? success "Answer"
        Bottom-up heapify costs the sum of node heights, which is O(n). Heapsort then performs n extract-max operations of O(log n) each, so O(n log n) overall.

??? question "Q3. Explain amortised analysis with dynamic array append."
    ??? success "Answer"
        Doubling capacity costs O(n) copies but happens after n appends since the last resize, so total cost of n appends is O(n) and O(1) per append amortised. The aggregate method sums 1 + 2 + 4 + ... < 2n.

??? question "Q4. What is the complexity of recursive DFS on a graph, counting stack space?"
    ??? success "Answer"
        Time O(V + E). Stack space O(V) worst case (a path graph), so state that recursion depth can hit the Python limit.

??? question "Q5. Why can comparison sorting not beat O(n log n)?"
    ??? success "Answer"
        A decision tree with n! leaves needs height at least log2(n!) which is Theta(n log n). Non-comparison sorts (counting, radix) escape by using key structure.

??? question "Q6. When is hash table lookup not O(1)?"
    ??? success "Answer"
        Adversarial or poor hashes cause collisions (O(n) worst case), resizing spikes, very long keys (hash cost O(L)), and memory or cache effects. Python randomises str hashes to defend against flooding.

??? question "Q7. Derive the complexity of `T(n) = 2T(n/2) + n` and `T(n) = T(n/2) + 1`."
    ??? success "Answer"
        By the master theorem, the first is O(n log n) (merge sort) and the second O(log n) (binary search).

??? question "Q8. What is the space complexity of merge sort and quicksort?"
    ??? success "Answer"
        Merge sort O(n) auxiliary for arrays (O(1) for linked lists with care). Quicksort O(log n) expected stack, O(n) worst case without tail-call handling on the larger partition.

### Hashing

??? question "Q9. Compare open addressing and chaining."
    ??? success "Answer"
        Chaining: simple deletes, tolerates load above 1, pointer overhead. Open addressing (Python dict): cache friendly, needs tombstones and load below about 2/3, clustering issues. Both resize by rehashing.

??? question "Q10. What makes a good hash function and what breaks a dict key?"
    ??? success "Answer"
        Deterministic, uniform, cheap, consistent with equality. Keys must be hashable and their hash must not change: mutable lists cannot be keys, tuples of hashables can.

??? question "Q11. Bloom filter: guarantees and sizing?"
    ??? success "Answer"
        No false negatives, tunable false positives. With m bits, n items and k hashes, the false-positive rate is about (1 - e^(-kn/m))^k, and k = (m/n) ln 2 is optimal. Deletion needs counting Bloom filters.

### Arrays

??? question "Q12. When do you use prefix sums vs a sliding window?"
    ??? success "Answer"
        Prefix sums handle arbitrary values including negatives and arbitrary range queries. Sliding windows need monotonic conditions (typically non-negative values) but use O(1) space.

??? question "Q13. What is an in-place algorithm, and what does it cost you?"
    ??? success "Answer"
        O(1) extra space, mutating the input. Costs: destroys the original (unsafe with shared data), often harder code, and sometimes stability. State it explicitly in interviews.

### Sorting

??? question "Q14. Stable vs unstable sort and why it matters?"
    ??? success "Answer"
        Stable keeps equal keys in original order, enabling multi-key sorts by sorting on secondary keys first. Python's Timsort is stable. Quicksort and heapsort are not.

??? question "Q15. When would you choose counting or radix sort?"
    ??? success "Answer"
        Keys are integers in a small range (counting O(n + k)) or fixed-width (radix O(d(n + k))). Also useful for sorting a huge number of ages, scores or timestamps bucketed by day.

### Binary search

??? question "Q16. What predicate shapes make binary search valid?"
    ??? success "Answer"
        Monotone (F...F T...T). It does not need sorted data per se. Peak finding and answer-space search rely only on monotonicity of a decision function.

### Recursion

??? question "Q17. Recursion vs iteration vs memoisation vs tabulation: when each?"
    ??? success "Answer"
        Recursion for tree-shaped structure. Memoisation when subproblems overlap and only some are reachable. Tabulation for full-table dependency order and space optimisation. Iteration when depth is a risk.

??? question "Q18. How do you convert recursive DFS to iterative?"
    ??? success "Answer"
        Use an explicit stack of frames (node, state). For post-order, push a marker or use two-phase visits. The transformation removes stack-depth risk but complicates state carrying.

### Trees

??? question "Q19. Why are B-trees used in databases rather than binary trees?"
    ??? success "Answer"
        High fan-out reduces height (log_B n) and matches block I/O, so a lookup costs a few page reads. Binary trees have too many levels and pointer hops for disk.

??? question "Q20. AVL vs red-black tree?"
    ??? success "Answer"
        AVL is more strictly balanced (faster lookups, more rotations on update). Red-black does fewer rotations (faster insert/delete), and is the common library choice.

??? question "Q21. What is a segment tree and when do you need it over prefix sums?"
    ??? success "Answer"
        A tree over an array supporting range queries and point or range updates in O(log n). Prefix sums only handle static arrays (updates cost O(n)).

??? question "Q22. Fenwick tree vs segment tree?"
    ??? success "Answer"
        Fenwick (BIT): compact, simple, prefix aggregates with invertible operations (sum). Segment tree: any associative operation (min, max, gcd), lazy propagation for range updates.

### Heaps

??? question "Q23. Why can heapq not do decrease-key and how do you cope?"
    ??? success "Answer"
        It has no position index. Push a new entry and skip stale ones on pop (lazy deletion), or implement an indexed heap. Dijkstra usually uses lazy deletion.

??? question "Q24. Heap vs balanced BST for a priority queue?"
    ??? success "Answer"
        Heap: simpler, O(1) peek, better constants, array layout. BST: ordered iteration, rank queries, arbitrary delete in O(log n), predecessor/successor. Choose by needed operations.

### Graphs

??? question "Q25. BFS vs DFS: which for which problems?"
    ??? success "Answer"
        BFS for shortest paths in unweighted graphs and level-based problems. DFS for reachability, components, cycle detection, topological order, backtracking, and low memory on wide graphs.

??? question "Q26. Adjacency list vs matrix: trade-offs?"
    ??? success "Answer"
        List O(V+E) space, fast neighbour iteration, best for sparse graphs. Matrix O(V^2) space, O(1) edge test, best for dense graphs or Floyd-Warshall.

??? question "Q27. How do you detect a cycle in a directed graph using DFS?"
    ??? success "Answer"
        Colour nodes white/grey/black. An edge to a grey node is a back edge, so there is a cycle. Kahn's algorithm is the alternative: nodes left with nonzero in-degree indicate a cycle.

??? question "Q28. Why does Dijkstra require non-negative weights, and what replaces it otherwise?"
    ??? success "Answer"
        Finalising nodes on pop assumes no later cheaper path. With negatives use Bellman-Ford (O(VE)), or Johnson's reweighting for all-pairs. Negative cycles make shortest paths undefined.

??? question "Q29. Explain union-find with path compression and union by rank."
    ??? success "Answer"
        Each set is a tree of parent pointers. Find compresses paths, union attaches the smaller tree under the larger. Amortised O(alpha(n)) per operation.

??? question "Q30. MST: Kruskal vs Prim, and the cut property?"
    ??? success "Answer"
        Kruskal sorts edges and uses DSU (best sparse). Prim grows a tree with a heap, or an array for dense graphs. Cut property: the lightest edge across any cut is in some MST.

??? question "Q31. What is a topological order and when does one exist?"
    ??? success "Answer"
        A linear order where every edge goes forward. It exists iff the graph is a DAG. It is not unique in general.

### DP

??? question "Q32. How do you recognise DP versus greedy versus backtracking?"
    ??? success "Answer"
        Overlapping subproblems plus optimal substructure suggests DP. A provable local choice (exchange argument) suggests greedy. Enumerating all solutions with pruning suggests backtracking. Try small counterexamples for greedy.

??? question "Q33. Explain why 0/1 knapsack in 1-D iterates capacity downward."
    ??? success "Answer"
        To use each item at most once, dp[c - w] must reflect the state before this item. Upward iteration would reuse the item (unbounded knapsack).

??? question "Q34. What is the difference between memoisation and tabulation in practice?"
    ??? success "Answer"
        Memoisation is lazy, uses recursion and a cache (hit only reachable states, recursion limits). Tabulation is eager, iterative, and allows rolling arrays.

??? question "Q35. How do you reduce DP space, and what do you lose?"
    ??? success "Answer"
        Keep only the rows or variables the transition needs. You lose the ability to reconstruct the solution path unless you use Hirschberg or store parent pointers separately.

??? question "Q36. LIS in O(n log n): why does patience sorting work?"
    ??? success "Answer"
        tails[k] holds the smallest possible tail of an increasing subsequence of length k+1. It stays sorted, so each new value replaces the first tail >= it via binary search. The array length is the LIS length, not the sequence.

### Greedy

??? question "Q37. How do you prove a greedy algorithm correct?"
    ??? success "Answer"
        Exchange argument (transform any optimal solution into the greedy one without loss), greedy stays ahead, or a matroid argument. Also test against brute force on small inputs.

### Strings

??? question "Q38. KMP vs Rabin-Karp vs Z-algorithm?"
    ??? success "Answer"
        All find patterns in O(n + m) expected or exact. KMP uses a failure function (deterministic), Z uses prefix matches, Rabin-Karp uses rolling hashes (simple, multi-pattern friendly, probabilistic).

??? question "Q39. When do you use a trie vs a hash set vs a sorted array for string sets?"
    ??? success "Answer"
        Trie for prefix queries and wildcard or grid search. Hash set for exact membership. Sorted array plus bisect for static prefix search with low memory.

### Design

??? question "Q40. Why do LRU caches use a hash map plus doubly linked list?"
    ??? success "Answer"
        Hash map gives O(1) lookup of the node, the DLL gives O(1) move-to-front and evict-tail. Either alone leaves one operation O(n).

### Concurrency

??? question "Q41. What is a race condition versus a deadlock versus a livelock?"
    ??? success "Answer"
        Race: outcome depends on interleaving of unsynchronised access. Deadlock: threads wait cyclically forever. Livelock: threads keep changing state in response to each other without progress.

??? question "Q42. Explain the GIL and what the free-threaded Python build changes."
    ??? success "Answer"
        The GIL lets one thread run Python bytecode at a time, so CPU-bound threads do not parallelise. Free-threaded builds (3.14t, officially supported per PEP 779) remove it, so races on compound operations become real and locks matter more. I/O-bound code already benefits from threads under the GIL.

??? question "Q43. Mutex vs semaphore vs condition variable vs event?"
    ??? success "Answer"
        Mutex: exclusive ownership. Semaphore: counted permits (resource pools, ping-pong). Condition: wait for a predicate under a lock. Event: one-shot or resettable flag broadcast.

### Systems

??? question "Q44. How do amortised and worst-case latency differ for a service?"
    ??? success "Answer"
        Amortised hides rare expensive operations (a resize, a compaction). A service with p99 targets cares about worst-case per request, so use incremental resizing, background work, or pre-sizing.

??? question "Q45. Why might an O(n log n) algorithm beat O(n) in practice?"
    ??? success "Answer"
        Constants and cache behaviour: sequential array sorts beat pointer-chasing or hash-heavy linear passes for moderate n. Measure before optimising.

## Interview communication scripts

Adapt the wording to your own voice, but keep the structure. Each script has a job: it keeps the interviewer informed and gives them hooks to help you.

??? question "Script 1. Opening: clarify and restate"
    ??? success "Script"
        "Let me restate to make sure I've got it: given X, return Y, and Z should hold. A few questions: how large can n get, can values be negative or duplicated, is the input sorted, and what should I return for empty input? I'll write two examples, including an edge case."

??? question "Script 2. Naming the brute force"
    ??? success "Script"
        "The straightforward approach is to check every pair, which is O(n^2) time and O(1) space. With n up to 10^5 that's about 10^10 operations, too slow, so I'll look for repeated work. Each inner loop is really asking 'have I seen the complement?', which a hash map answers in O(1)."

??? question "Script 3. Proposing the optimised approach"
    ??? success "Script"
        "I'll use a sliding window because the condition is monotone: adding elements can only violate it and removing can only restore it, so both pointers move forward once, giving O(n) time and O(k) space for the character counts. Does that direction sound good before I code?"

??? question "Script 4. Narrating while coding"
    ??? success "Script"
        "I'm using a deque of indices, decreasing by value, so the front is always the window maximum. I pop from the back while the new element is larger, because those can never be a maximum again. I'll expire the front index once it leaves the window."

??? question "Script 5. Tracing your own code"
    ??? success "Script"
        "Let me trace it with nums = [2,7,11,15], target 9. i=0: need 7, map empty, store 2->0. i=1: need 2, found at index 0, so return [0,1]. Now an edge case: duplicates [3,3], target 6. i=0 stores 3, i=1 finds 3, returns [0,1], correct."

??? question "Script 6. When you find a bug"
    ??? success "Script"
        "I see the issue: I update `best` before restoring the invariant, so it can record an invalid window. I'll move that line after the shrink loop and re-run the trace." (Calm, specific, fixed. Do not apologise repeatedly.)

??? question "Script 7. When you are stuck"
    ??? success "Script"
        "I'm stuck on how to avoid rescanning here. Let me think about what information I'd need at index i to answer in O(1)... Can I ask whether the input can be sorted? Or shall I first write the O(n log n) version so we have a correct baseline, and optimise after?"

??? question "Script 8. Stating complexity"
    ??? success "Script"
        "Time is O(n log n): sorting dominates, then a linear scan. Space is O(n) for the output plus the sort's auxiliary space (Timsort uses up to n/2). Recursion depth is not an issue here because it's iterative."

??? question "Script 9. Handling a hint"
    ??? success "Script"
        "That hint suggests the answer is monotone in the capacity, so I can binary search the answer and check feasibility greedily in O(n). Let me define the feasibility function and confirm it's monotone before writing the search."

??? question "Script 10. Staff follow-up: scale it"
    ??? success "Script"
        "At 10^9 items I'd stop thinking in-memory. I'd partition by hash into shards that fit in RAM, solve each independently, and merge. The merge cost and skewed keys are the risks, so I'd salt hot keys and monitor partition sizes."

??? question "Script 11. Staff follow-up: stream it"
    ??? success "Script"
        "For a stream I need one pass and bounded memory: a fixed-size window with running aggregates, or a sketch (Count-Min, HyperLogLog) if exactness is negotiable. I'd state the error bound and what happens on restart, likely checkpoint plus replay."

??? question "Script 12. Staff follow-up: concurrency"
    ??? success "Script"
        "With multiple threads, the check-then-act sequence needs a lock over the whole invariant. I'd start with one lock, measure, then shard by key. The cost is that multi-key operations must acquire shards in a fixed order to avoid deadlock. I'd inject the clock so the tests are deterministic."

??? question "Script 13. Wrapping up"
    ??? success "Script"
        "To summarise: hash map for O(n) time and O(n) space, edge cases handled for empty and duplicate input. Trade-off: if memory mattered I'd sort and use two pointers at O(n log n) and O(1) extra. Follow-ups I'd consider: streaming input and returning all pairs. Happy to go into any of them."

??? question "Script 14. Pushing back politely on an ambiguous spec"
    ??? success "Script"
        "The statement doesn't say whether touching intervals count as overlapping. I'll assume half-open ranges so [1,2] and [2,3] don't conflict, and I'll note that in a comment. If closed ranges are intended it's a one-character change from < to <=."

## Rapid-fire (30)

Target: each answer in under 10 seconds.

??? question "R1. Time to build a heap from n items?"
    ??? success "Answer"
        O(n) with heapify.

??? question "R2. Time for `x in list` versus `x in set`?"
    ??? success "Answer"
        O(n) versus O(1) average.

??? question "R3. Cost of `list.pop(0)`?"
    ??? success "Answer"
        O(n), use `deque.popleft()` at O(1).

??? question "R4. `bisect_left` returns what?"
    ??? success "Answer"
        First index i with a[i] >= x.

??? question "R5. Complexity of BFS on a graph?"
    ??? success "Answer"
        O(V + E) time, O(V) space.

??? question "R6. Complexity of Dijkstra with a binary heap?"
    ??? success "Answer"
        O((V + E) log V).

??? question "R7. Bellman-Ford complexity and special use?"
    ??? success "Answer"
        O(VE), negative edges and K-limited paths, detects negative cycles.

??? question "R8. Floyd-Warshall complexity?"
    ??? success "Answer"
        O(V^3) time, O(V^2) space.

??? question "R9. Kruskal complexity?"
    ??? success "Answer"
        O(E log E) due to sorting, plus DSU near-constant.

??? question "R10. Topological sort exists iff?"
    ??? success "Answer"
        The directed graph is acyclic.

??? question "R11. Union-find amortised cost?"
    ??? success "Answer"
        O(alpha(n)) per operation, effectively constant.

??? question "R12. Quicksort worst case and how to avoid it?"
    ??? success "Answer"
        O(n^2), avoid with a random pivot or median-of-three.

??? question "R13. Merge sort space?"
    ??? success "Answer"
        O(n) auxiliary for arrays.

??? question "R14. Quickselect average and worst?"
    ??? success "Answer"
        O(n) average, O(n^2) worst.

??? question "R15. Trie insert/search cost?"
    ??? success "Answer"
        O(L) in key length.

??? question "R16. Number of subsets of n items?"
    ??? success "Answer"
        2^n.

??? question "R17. Number of permutations of n items?"
    ??? success "Answer"
        n!.

??? question "R18. Catalan number counts what (parentheses)?"
    ??? success "Answer"
        Valid parenthesis strings of n pairs, C_n = C(2n, n)/(n+1).

??? question "R19. Power of two test?"
    ??? success "Answer"
        x > 0 and x & (x - 1) == 0.

??? question "R20. Lowest set bit?"
    ??? success "Answer"
        x & -x.

??? question "R21. XOR of a number with itself?"
    ??? success "Answer"
        0.

??? question "R22. Python recursion limit default?"
    ??? success "Answer"
        About 1000 frames.

??? question "R23. Difference between `//` and `int(a / b)` for negatives?"
    ??? success "Answer"
        `//` floors toward negative infinity, `int()` truncates toward zero.

??? question "R24. Two heaps for streaming median: which holds what?"
    ??? success "Answer"
        Max-heap for the lower half, min-heap for the upper half, sizes differ by at most 1.

??? question "R25. Sliding window maximum structure?"
    ??? success "Answer"
        Monotonic decreasing deque of indices, O(n).

??? question "R26. When does a sliding window fail?"
    ??? success "Answer"
        When values can be negative (sum conditions), so monotonicity breaks. Use prefix sums.

??? question "R27. Kadane's algorithm idea?"
    ??? success "Answer"
        Best sum ending here = max(x, previous + x). Track the global best.

??? question "R28. Floyd's cycle detection space?"
    ??? success "Answer"
        O(1).

??? question "R29. Binary search on answer: three steps?"
    ??? success "Answer"
        Define the answer range, prove the predicate is monotone, write a greedy feasibility check.

??? question "R30. Token bucket vs leaky bucket?"
    ??? success "Answer"
        Token bucket allows bursts up to capacity, leaky bucket smooths output to a constant rate.

## Checklist

- [ ] I answered the conceptual questions aloud and logged misses
- [ ] I rehearsed the scripts on a recorded mock
- [ ] I can clear the rapid-fire round with at most 3 misses

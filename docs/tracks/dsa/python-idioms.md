---
title: Python idioms for interviews
track: dsa
slug: python-idioms
priority: P0
complexity: 1
est_hours: 1
phase: 0
tags: [dsa, P0]
last_reviewed: 2026-09-25
---

# Python idioms for interviews

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 1/5 · **Est. time:** 1 h · **Phase:** 0 · **Prereqs:** [Approach & complexity](approach-complexity.md)
    **You're done when:** you can write BFS, a heap-based top-k, binary search with `bisect`, and memoised DFS from memory with no reference, and name the complexity of every stdlib call you used.

## Why it matters

Python is the fastest interview language when you use its standard library fluently: `collections`, `heapq`, `bisect`, `functools`, `itertools`. It is a liability when you don't, because hidden O(n) calls, recursion limits and mutable-default bugs cost time. You already write production Python. This page is the interview-specific subset: the 30 idioms that save 5–10 minutes per round, plus the traps.

## Core concepts

### The interview toolbox

| Need | Idiom | Complexity | Note |
|---|---|---|---|
| Frequency count | `Counter(s)`, `cnt.most_common(k)` | O(n), O(n log k) | `Counter` subtraction drops non-positive counts |
| Default values | `defaultdict(list)`, `defaultdict(int)` | O(1) | Graph adjacency: `g = defaultdict(list)` |
| Queue / deque | `deque()`, `append`, `popleft`, `appendleft` | O(1) | Never use `list.pop(0)` (O(n)) |
| Min-heap | `heapq.heappush(h, x)`, `heappop(h)`, `heapify(a)` | O(log n), O(n) heapify | Max-heap: push `-x`. Tie-break with tuples `(prio, idx, obj)` |
| Top-k | `heapq.nlargest(k, it, key=)` | O(n log k) | Fine for one-shot use |
| Sorted search | `bisect_left(a, x)`, `bisect_right`, `insort` | O(log n), insort O(n) | `key=` supported since 3.10 |
| Memoisation | `@functools.cache` (3.9+) / `@lru_cache(None)` | per-call O(1) lookup | Args must be hashable, so convert lists to tuples |
| Sorting | `a.sort(key=lambda x: (x[1], -x[0]))` | O(n log n), stable | Custom comparator: `functools.cmp_to_key` |
| Combinatorics | `permutations`, `combinations`, `product`, `accumulate`, `pairwise` (3.10+) | output-sized | `accumulate` gives prefix sums |
| Infinity | `float('inf')`, `math.inf` | | |
| Integer tricks | `divmod`, `//` floors toward -inf, `int(a / b)` truncates | | RPN division needs truncation |
| Bits | `x.bit_count()` (3.10+), `x & -x` lowest bit, `x.bit_length()` | O(1)-ish | Python ints are arbitrary precision, so mask with `& 0xFFFFFFFF` |
| Grid neighbours | `for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):` | | Bounds check `0 <= r < R` |
| Swap | `a, b = b, a` | | |
| Enumerate/zip | `for i, (x, y) in enumerate(zip(a, b)):` | | `zip(strict=True)` in 3.10+ |
| Sorted container | `sortedcontainers.SortedList` | O(log n) | **Not stdlib.** Available on LeetCode; ask before using in other environments |

### Reusable templates

=== "BFS (grid / graph)"

    ```python
    from collections import deque

    def bfs(start, neighbours):
        q = deque([start])
        seen = {start}
        dist = 0
        while q:
            for _ in range(len(q)):          # process one level
                node = q.popleft()
                # if node is target: return dist
                for nxt in neighbours(node):
                    if nxt not in seen:
                        seen.add(nxt)        # mark on push, not on pop
                        q.append(nxt)
            dist += 1
        return -1
    ```

=== "Heap top-k"

    ```python
    import heapq

    def top_k(nums, k):
        h = []
        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)             # keep k largest; h[0] = kth largest
        return h                             # O(n log k) time, O(k) space
    ```

=== "Memoised DFS"

    ```python
    from functools import cache

    def solve(nums):
        @cache
        def dp(i, remaining):                # args must be hashable
            if i == len(nums):
                return 0 if remaining == 0 else float('-inf')
            return max(dp(i + 1, remaining), nums[i] + dp(i + 1, remaining - 1))
        return dp(0, 3)
    ```

=== "bisect / lower bound"

    ```python
    from bisect import bisect_left, bisect_right

    a = [1, 2, 2, 2, 5]
    bisect_left(a, 2)   # 1 -> first index with a[i] >= 2
    bisect_right(a, 2)  # 4 -> first index with a[i] > 2
    # count of 2s = bisect_right - bisect_left = 3
    ```

### Traps that cost interviews

| Trap | Symptom | Fix |
|---|---|---|
| `[[0] * m] * n` | All rows alias the same list | `[[0] * m for _ in range(n)]` |
| Mutable default arg `def f(x, acc=[])` | State leaks between calls | `acc=None` |
| Recursion depth > 1000 | `RecursionError` on deep DFS | Iterative stack or `sys.setrecursionlimit` |
| Appending `path` itself in backtracking | All results identical and empty | `res.append(path[:])` |
| `heapq` with un-comparable objects | `TypeError` on tie | `(priority, counter, obj)` |
| `-7 // 2 == -4` | Wrong truncation in RPN or digit math | `int(-7 / 2) == -3` |
| String building in a loop | Quadratic time | List plus `"".join` |
| `@cache` on a method with `self` or list args | Unhashable, or memory leak | Nested function or tuple args |
| Modifying a dict while iterating | `RuntimeError` | Iterate `list(d.items())` |

### Senior-level nuance

- **Readability is scored.** Prefer `for i, x in enumerate(a)` to index gymnastics. Extract helpers (`in_bounds(r, c)`, `neighbours(node)`).
- **Know when *not* to use a one-liner.** `sorted(Counter(a).items(), key=...)[:k]` is fine, but explain the O(n log n) cost versus a heap or bucket sort.
- **Python 3.14 free-threaded builds** (PEP 779, officially supported as of Sept 2026) change the concurrency story. See [concurrency & LLD](concurrency-lld.md). For DSA rounds, nothing changes.
- **Type hints are optional** in interviews. Use them for function signatures only if it helps readability.

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [collections docs](https://docs.python.org/3/library/collections.html) | docs | `deque`, `Counter`, `defaultdict`, `OrderedDict` APIs (official) | intermediate | free |
| [heapq docs](https://docs.python.org/3/library/heapq.html) | docs | Includes the priority-queue implementation notes with entry-counter tie-breaks | intermediate | free |
| [bisect docs](https://docs.python.org/3/library/bisect.html) | docs | `key=` parameter and search recipes | intermediate | free |
| [functools docs](https://docs.python.org/3/library/functools.html) | docs | `cache`, `lru_cache`, `cmp_to_key` | intermediate | free |
| [itertools docs](https://docs.python.org/3/library/itertools.html) | docs | Combinatoric iterators and `accumulate`/`pairwise` | intermediate | free |
| [Python Sorting HOWTO](https://docs.python.org/3/howto/sorting.html) | docs | Key functions, stability, multi-key sorts | intermediate | free |
| [Python TimeComplexity wiki](https://wiki.python.org/moin/TimeComplexity) | docs | Cost of every built-in container operation | intermediate | free |
| [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/) :gem: | docs | Pure-Python sorted list/dict available on LeetCode, great for interval and calendar problems | advanced | free |
| [Fluent Python 2e](https://www.fluentpython.com/) | book | Data model depth; the chapters on sequences and dicts explain the costs above | advanced | paid |

## Hands-on lab

**Goal:** muscle memory (45 min). With no references, in a blank file:

1. Write BFS shortest path on a grid with obstacles (`0` open, `1` wall). Test on a 5×5 grid.
2. Write top-k frequent words using `Counter` + `heapq` with tie-break by lexicographic order (LC 692 style).
3. Write `lower_bound` by hand, then verify against `bisect_left` on 1,000 random arrays with `assert`.
4. Write memoised `coin_change(coins, amount)` with `@cache`, then convert it to a bottom-up table.
5. Run `python -X importtime` (optional) and `timeit` to compare `list.pop(0)` with `deque.popleft()` for n=10^5 and record the numbers.

**Expected output:** `idioms.py` with all five passing asserts, committed to your practice repo, plus a note on the timing comparison (expect orders of magnitude difference).

## Questions

### L1 — Recall

??? question "Q1. How do you implement a max-heap with `heapq`?"
    ??? success "Answer"
        Push negated keys: `heappush(h, -x)` and read `-h[0]`. For tuples: `(-priority, tiebreak, item)`. For objects, define `__lt__` or wrap them in a dataclass with `order=True`.

??? question "Q2. What is the difference between `bisect_left` and `bisect_right`?"
    ??? success "Answer"
        `bisect_left(a, x)` returns the first index i with `a[i] >= x` (lower bound). `bisect_right` returns the first index with `a[i] > x` (upper bound). With duplicates, `right - left` is the count of x.

??? question "Q3. Why is `deque` preferred over `list` for BFS?"
    ??? success "Answer"
        `deque.popleft()` is O(1). `list.pop(0)` shifts all elements, which is O(n) and turns BFS into O(V^2).

### L2 — Apply

??? question "Q4. Group anagrams in one idiomatic function. State its complexity."
    ??? success "Answer"
        ```python
        from collections import defaultdict
        def group_anagrams(strs):
            groups = defaultdict(list)
            for s in strs:
                key = [0] * 26
                for ch in s:
                    key[ord(ch) - 97] += 1
                groups[tuple(key)].append(s)
            return list(groups.values())
        ```
        O(N·K) time for N strings of max length K (versus O(N·K log K) with a sorted-string key). O(N·K) space.

??? question "Q5. Fix this backtracking bug."
    ```python
    def subsets(nums):
        res, path = [], []
        def bt(i):
            if i == len(nums):
                res.append(path); return
            path.append(nums[i]); bt(i + 1); path.pop(); bt(i + 1)
        bt(0); return res
    ```
    ??? success "Answer"
        `res.append(path)` stores a reference to the same list, which is empty at the end. Use `res.append(path[:])` (or `list(path)`).

??? question "Q6. Sort intervals by start ascending, ties by end descending, in one line."
    ??? success "Answer"
        `intervals.sort(key=lambda iv: (iv[0], -iv[1]))`. Python's sort is stable, so you could also do two passes (secondary key first).

### L3 — Design & trade-offs

??? question "Q7. `@cache` vs an explicit dp table: which do you write first in an interview?"
    ??? success "Answer"
        Top-down `@cache` first. It mirrors the recurrence, is fast to write, and computes only reachable states. Risks: recursion depth (n > ~1000) and memory held by the cache. Then offer bottom-up if asked about space optimisation (rolling arrays) or recursion limits. Some interviewers ask you to avoid `@cache` to see the table, so be fluent in both.

??? question "Q8. When would you use `sortedcontainers.SortedList` and what do you say to the interviewer?"
    ??? success "Answer"
        Use it when you need ordered insert/delete plus rank/neighbour queries: sliding window median, calendar booking, "count smaller after self". Say: "Python has no built-in balanced BST. `SortedList` gives O(log n) insert/remove (amortised; it's a list of sorted sublists). If it's not allowed, I'd use two heaps with lazy deletion or a Fenwick tree over compressed coordinates." Ask permission first.

??? question "Q9. Recursion vs an explicit stack for tree DFS in Python?"
    ??? success "Answer"
        Recursion is clearer and fine when height ≤ ~1000 (balanced trees, typical LC constraints where n ≤ 10^4 but trees may be skewed, so check). An explicit stack avoids `RecursionError` and is required for post-order variants on deep trees. Say which you picked and why.

### L4 — Staff-level ambiguity

??? question "Q10. Your team debates banning `@lru_cache` on instance methods in production code. What's your position?"
    ??? success "Answer"
        Support the ban with an exception process. `lru_cache` on a method keys on `self`, which keeps instances alive (a memory leak) and shares one cache across instances with confusing eviction. Alternatives: `functools.cached_property` for per-instance values, a module-level cache keyed on explicit ids, or an injected cache object with TTL and metrics. The general principle: memoisation is a data structure with a lifecycle, so make it explicit and observable.

??? question "Q11. The interviewer says 'no libraries: implement the heap yourself'. How do you manage time?"
    ??? success "Answer"
        Confirm the scope (just push/pop?). Write an array-backed binary heap with `_sift_up` / `_sift_down` (about 20 lines, 5–7 minutes). Parent `(i-1)//2`, children `2i+1`, `2i+2`. Test with a quick sequence. Mention that `heapify` is O(n) by sifting down from `n//2 - 1` and explain why (the sum of heights is O(n)).

## Real-world use cases

- **Job schedulers:** `heapq` with `(run_at, seq, job)` tuples is exactly how simple in-process schedulers (and `sched`) work.
- **Rate limiting:** a `deque` of timestamps for sliding-window-log limiters in API gateways.
- **Analytics:** `Counter.most_common` for top error codes, `bisect` for bucketing latencies into histogram bins.
- **Config/rule engines:** `defaultdict(list)` adjacency lists for rule dependency graphs, with topological order for evaluation.

## Pitfalls & anti-patterns

- Reaching for `sortedcontainers` or `numpy` without asking.
- Using `list` as a queue, or `in list` for membership.
- Returning references to mutable accumulators in backtracking.
- Writing heavy OOP (classes for everything) when a function is enough.
- Relying on dict ordering for correctness without saying so (insertion order has been guaranteed since 3.7, so it's fine, but state it).

## Checklist

- [ ] I can write BFS, top-k heap, lower_bound and memoised DFS without references
- [ ] I know the complexity of every `collections`, `heapq` and `bisect` call I use
- [ ] I can list five Python traps and their fixes
- [ ] I answered all L3 questions out loud in < 3 min each

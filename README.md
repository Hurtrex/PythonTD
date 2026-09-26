# 📚 Python Data Structures & Algorithms — Study Notes

> Covers lectures **L01 → L06** and their corresponding TDs.  
> Use this to study concepts, understand the code, and review before exams.

---

## 📋 Table of Contents

- [L01 — Python OOP](#l01--python-oop)
- [L02 — Complexity Analysis](#l02--complexity-analysis)
- [L03 — Recursion](#l03--recursion)
- [L04 — ADT List](#l04--adt-list)
- [L05 — ADT Stack](#l05--adt-stack)
- [L06 — ADT Queue](#l06--adt-queue)
- [Project Structure](#project-structure)
- [Complexity Cheat Sheet](#-complexity-cheat-sheet)

---

## L01 — Python OOP

> 📁 `src/TD1/` &nbsp;|&nbsp; 🎥 [Python OOP in 4 hours](https://www.youtube.com/watch?v=Ej_02ICOIgs)

### The Class

A class is a blueprint. An **object** is an instance of that blueprint.

```python
class Animal:
    species = "Unknown"          # class variable — shared by ALL instances

    def __init__(self, name):    # constructor
        self.name = name         # instance variable — unique per object

    def speak(self):             # instance method
        print(f"{self.name} speaks")
```

> `self` in Python = `this` in Java/C#. Always the first parameter of instance methods.

---

### Access Modifiers

| Syntax | Access | Convention |
|--------|--------|------------|
| `name` | Public | Anyone can read/write |
| `_name` | Protected | "Don't touch from outside" (not enforced) |
| `__name` | Private | Name-mangled, truly hidden |

```python
class Person:
    def __init__(self):
        self.public = "anyone"
        self._protected = "subclasses"
        self.__private = "this class only"
```

---

### Key Dunder Methods

Special methods Python calls automatically. You override them to customize behavior.

| Method | When called | Example use |
|--------|-------------|-------------|
| `__init__` | Object created | Initialize attributes |
| `__str__` | `print(obj)` | Human-readable string |
| `__repr__` | `repr(obj)`, debugger | Developer string |
| `__eq__` | `obj1 == obj2` | Compare by value |
| `__lt__` | `obj1 < obj2` | Sorting, heaps |
| `__del__` | Object garbage collected | Cleanup |

```python
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __lt__(self, other):       # needed to use in a MinHeap
        return self.year < other.year
```

---

### Inheritance

```python
class Animal:
    def speak(self): print("...")

class Dog(Animal):               # Dog inherits from Animal
    def speak(self):             # override
        print("Woof!")

class GuideDog(Dog, Animal):     # Python supports MULTIPLE inheritance
    pass
```

> All classes implicitly inherit from `object`. Writing `class Foo(object)` is optional.

---

### Class vs Static Methods

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):          # cls = the class itself
        cls.count += 1

    @staticmethod
    def description():           # no self, no cls — just a utility
        return "Counts things"
```

---

### Layered Architecture (TD1)

The BMI app splits responsibility into layers. Each layer only talks to the one below it.

```
UI (ConsoleUI)
    ↓ calls
Service (BodyMassIndexService)
    ↓ calls
DAO (CategoryDAO)
    ↓ queries
Data (MockDB)  ←  Model (Category)
```

> **Why?** You can swap `MockDB` for a real SQL database without touching the UI or service at all.

---

### Singleton Pattern (`MockDB`)

Guarantees **only one instance** of a class ever exists — useful for shared resources like a database connection.

```python
class MockDB:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MockDB()
        return cls._instance      # always the same object
```

---

### Python Collections Quick Reference

| Collection | Ordered | Mutable | Duplicates | Syntax |
|------------|---------|---------|------------|--------|
| `list` | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| `tuple` | ✅ | ❌ | ✅ | `(1, 2, 3)` |
| `set` | ❌ | ✅ | ❌ | `{1, 2, 3}` |
| `dict` | ✅ (3.7+) | ✅ | keys: ❌ | `{"a": 1}` |

---

## L02 — Complexity Analysis

> 📁 `src/TD2/` &nbsp;|&nbsp; 🎥 [Big-O Notation explained](https://www.youtube.com/watch?v=MyeV2_tGqvw)

### What is Complexity?

Complexity measures how many **elementary operations** an algorithm performs as input size `n` grows.  
We don't care about the exact count — we care about the **order of magnitude** (the shape of the curve).

> **Elementary operation** = one comparison, one assignment, one arithmetic op, one array access.

---

### How to Count Operations

| Structure | Rule |
|-----------|------|
| Sequence of statements | **Sum** the costs |
| `if/else` | **Max** of the two branches |
| Loop | **Sum** of each iteration |
| Recursive function | Solve a **recurrence equation** |

---

### Simplification Rules (Big-O)

1. **Drop constants:** `O(3n)` → `O(n)`
2. **Drop lower-order terms:** `O(n² + n)` → `O(n²)`
3. **Keep only the dominant term**

```
T(n) = n³ + 2n² + 4n + 2   →  O(n³)
T(n) = n·log(n) + 12n + 2  →  O(n log n)
T(n) = 4x² + 3x + 6·3ˣ    →  O(3ˣ)   ← exponential always dominates polynomial
```

---

### Orders of Magnitude (slowest → fastest growing)

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

| Notation | Name | Real example |
|----------|------|--------------|
| O(1) | Constant | Array index `arr[3]` |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | All subsets of a set |
| O(n!) | Factorial | All permutations |

---

### Execution Time Reality Check

For a machine doing **1 million ops/sec**:

| n | O(n) | O(n²) | O(2ⁿ) |
|---|------|-------|-------|
| 10 | < 1s | < 1s | < 1s |
| 100 | < 1s | < 1s | 10¹⁷ years |
| 1 000 | < 1s | 1s | ∞ |
| 10 000 | < 1s | 2 min | ∞ |
| 100 000 | < 1s | 3 hours | ∞ |

> 🔑 This is why algorithm choice matters. Going from O(n²) to O(n log n) on 100k elements = **from 3 hours to 2 seconds**.

---

### Cases: Best / Average / Worst

- **Best case** — ideal input (e.g. searching for the first element)
- **Average case** — typical input
- **Worst case** — most expensive input — **the default when we say O(n)**

---

### Step-by-Step Examples

The method is always the same:
1. **Identify the structure** (sequence / loop / nested loop / recursive)
2. **Count operations** per iteration
3. **Multiply** by how many times each block runs
4. **Sum everything** up, then **drop constants and lower terms**

---

#### 🟢 Easy — Single assignment block

```python
def swap(a, b):
    tmp = a      # 1 op
    a = b        # 1 op
    b = tmp      # 1 op
    return a, b  # 1 op
```

**Count:**
```
T(n) = 1 + 1 + 1 + 1 = 4
```
**Drop constant → O(1)**

> The input size doesn't affect how many operations run. Always 4 ops no matter what.

---

#### 🟢 Easy — Single loop

```python
def print_all(arr):          # arr has n elements
    for i in range(len(arr)):   # runs n times
        print(arr[i])            # 1 op per iteration
```

**Count:**
```
T(n) = n × 1 = n
```
**Drop constant → O(n)**

> The loop runs exactly `n` times, doing 1 thing each time → linear.

---

#### 🟢 Easy — Loop with constant work inside

```python
def sum_array(arr):
    total = 0                    # 1 op
    for x in arr:                # runs n times
        total += x               # 1 op
        print(total)             # 1 op  ← still constant per iteration
    return total                 # 1 op
```

**Count:**
```
T(n) = 1 + n × (1 + 1) + 1
     = 1 + 2n + 1
     = 2n + 2
```
**Drop constants → O(n)**

> The 2 multiplier and +2 don't matter. The shape is still linear.

---

#### 🟡 Medium — Two separate loops

```python
def two_loops(arr):
    for x in arr:        # loop 1: runs n times
        print(x)         # 1 op

    for x in arr:        # loop 2: runs n times
        print(x * 2)     # 1 op
```

**Count:**
```
T(n) = n × 1  +  n × 1
     = n + n
     = 2n
```
**Drop constant → O(n)**

> Two separate loops are **not** O(n²). They add, not multiply. O(n) + O(n) = O(n).

---

#### 🟡 Medium — Nested loops

```python
def print_pairs(arr):
    for i in range(len(arr)):        # outer: n times
        for j in range(len(arr)):    # inner: n times for EACH i
            print(arr[i], arr[j])    # 1 op
```

**Count:**
```
T(n) = n × n × 1
     = n²
```
**→ O(n²)**

> Every outer iteration triggers n inner iterations. That's n × n = n².

```
i=0: j runs 0,1,2,...,n-1   → n ops
i=1: j runs 0,1,2,...,n-1   → n ops
...
i=n-1: j runs 0,...,n-1     → n ops
Total: n × n = n²
```

---

#### 🟡 Medium — Nested loop, inner depends on outer

```python
def print_upper_triangle(arr):
    for i in range(len(arr)):        # outer: n times
        for j in range(i, len(arr)): # inner: starts at i, NOT 0
            print(arr[i], arr[j])
```

**Count:**
```
i=0: inner runs n   times
i=1: inner runs n-1 times
i=2: inner runs n-2 times
...
i=n-1: inner runs 1 time

T(n) = n + (n-1) + (n-2) + ... + 1
     = n(n+1)/2
     = n²/2 + n/2
```
**Drop lower term and constant → O(n²)**

> Even though the inner loop does less work each time, it's still quadratic. The triangle shape = n²/2 which is still O(n²).

---

#### 🔴 Hard — Loop that halves each time

```python
def count_halvings(n):
    i = n
    while i > 1:      # how many times can we halve before reaching 1?
        print(i)
        i = i // 2    # halve i each iteration
```

**Count — think about it differently:**

```
n=16: i → 16 → 8 → 4 → 2 → 1   (4 steps)
n=32: i → 32 → 16 → 8 → 4 → 2 → 1   (5 steps)
n=64: i → 64 → ... → 1   (6 steps)
```

Each time n doubles, we only add 1 more step.  
Number of steps = how many times you divide n by 2 until you reach 1 = **log₂(n)**

**→ O(log n)**

> Any loop where the variable is **divided** (not decremented) per iteration is O(log n).

---

#### 🔴 Hard — Mixed: loop + nested halving

```python
def mixed(arr):                      # arr has n elements
    for i in range(len(arr)):        # outer: n times
        j = len(arr)
        while j > 1:                 # inner: log n times
            print(arr[i], j)
            j = j // 2
```

**Count:**
```
Outer loop:  n iterations
Inner loop:  log n iterations per outer step

T(n) = n × log n
```
**→ O(n log n)**

> This is the complexity of the best sorting algorithms (merge sort, heap sort). The outer "touches every element" (n), and the inner "halves each time" (log n).

---

#### 🔴 Hard — Recursive function (recurrence equation)

```python
def merge_sort(arr, start, end):
    if start >= end:          # base case: 1 element → O(1)
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)    # recurse LEFT half  → T(n/2)
    merge_sort(arr, mid+1, end)    # recurse RIGHT half → T(n/2)
    merge(arr, start, end, mid)    # merge both halves  → O(n)
```

**Build the recurrence equation:**
```
T(1) = 1                         ← base case
T(n) = 2 × T(n/2) + n           ← two halves + merge cost
```

**Expand it (substitution method):**
```
T(n) = 2T(n/2) + n
     = 2[2T(n/4) + n/2] + n  =  4T(n/4) + n + n
     = 2[2[2T(n/8) + n/4] + n/2] + n  =  8T(n/8) + n + n + n
     ...
     = 2^k × T(n/2^k) + k×n
```

When `2^k = n` → `k = log₂(n)`, and `T(1) = 1`:
```
T(n) = n × T(1) + log(n) × n
     = n + n log n
```
**Drop lower term → O(n log n)**

> Recurrence equations look scary but the pattern is: split in half + linear work = O(n log n). This is the **master theorem** in action.

---

#### 🔴 Hard — Two recursive calls (Fibonacci)

```python
def fib(n):
    if n <= 1:          # base case
        return n
    return fib(n-1) + fib(n-2)   # TWO recursive calls
```

**Recurrence:**
```
T(1) = 1
T(n) = T(n-1) + T(n-2) + 1
```

**Visualize the call tree for fib(5):**
```
                    fib(5)
                 /          \
            fib(4)          fib(3)
           /      \         /    \
       fib(3)   fib(2)  fib(2)  fib(1)
       /    \   /    \
   fib(2) fib(1) fib(1) fib(0)
   /    \
fib(1) fib(0)
```

Each level roughly doubles the calls. With `n` levels → **≈ 2ⁿ total nodes**.

**→ O(2ⁿ)**

> This is why naive recursive Fibonacci is catastrophically slow. fib(46) takes 19 seconds. The fix is **memoization** (cache results) → brings it down to O(n).

---

#### Quick Pattern Recognition

| Code pattern | Complexity |
|---|---|
| `x = arr[i]` | O(1) |
| `for i in range(n)` | O(n) |
| `for i in range(n): for j in range(n)` | O(n²) |
| `for i in range(n): for j in range(i, n)` | O(n²) |
| `while i > 1: i //= 2` | O(log n) |
| `for i in range(n): while j > 1: j //= 2` | O(n log n) |
| One recursive call on half: `f(n/2)` | O(log n) |
| Two recursive calls on halves: `f(n/2) + f(n/2) + O(n)` | O(n log n) |
| Two recursive calls full: `f(n-1) + f(n-2)` | O(2ⁿ) |

---

### TD2 Algorithms Breakdown

| Function | Complexity | Why |
|----------|-----------|-----|
| `find_v1` | O(n) | Single loop through array |
| `exist` | O(n) | Single loop |
| `remove_duplicates_v1` | O(n²) | `exist()` called inside a loop |
| `check_array_v1` | O(n) | Single pass |
| `check_array_v2` | O(n²) | `sort_selection` is O(n²), dominates |
| `sort_selection` | O(n²) | Two nested loops |
| `binary_search_iterative` | O(log n) | Halves search space each time |
| `binary_search_recursive` | O(log n) | Same logic, recursive |

---

## L03 — Recursion

> 📁 `src/TD3/` &nbsp;|&nbsp; 🎥 [Recursion in 5 minutes](https://www.youtube.com/watch?v=ngCos392W4w) &nbsp;|&nbsp; 🎥 [Recursion vs Iteration](https://hackernoon.com/recursion-vs-looping-in-python-9261442f70a5)

### The Concept

A function is **recursive** if it calls itself. Every recursive function has:

1. **Base case** — the stopping condition (no more recursion)
2. **Recursive case** — the problem broken into a smaller version of itself

```python
def factorial(n):
    if n == 0:          # ← base case
        return 1
    return n * factorial(n - 1)   # ← recursive case, smaller n

# factorial(4) = 4 × factorial(3)
#                    = 3 × factorial(2)
#                          = 2 × factorial(1)
#                                = 1 × factorial(0)
#                                      = 1
# Result: 4 × 3 × 2 × 1 × 1 = 24
```

---

### The Call Stack

Every function call is **pushed** onto the call stack. When it returns, it's **popped**.

```
factorial(4)  ← pushed first
  factorial(3)
    factorial(2)
      factorial(1)
        factorial(0) ← base case, starts returning
      returns 1
    returns 2
  returns 6
returns 24
```

> ⚠️ Too many recursive calls = **Stack Overflow**. Python's default limit is ~1000 calls.

---

### Two Types of Recursion

**Functional recursion** — returns a computed value  
```python
def sum_recursive(n):
    if n == 0: return 0
    return n + sum_recursive(n - 1)
```

**Structural recursion** — traverses a recursive data structure (tree, linked list)
```python
def tree_size(node):
    if node is None: return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
```

---

### TD3 Examples

| Problem | Base case | Recursive step | Complexity |
|---------|-----------|----------------|-----------|
| Count to limit | `counter == limit-1` | `count(limit, counter+1)` | O(n) |
| Mult table (2 loops) | `i >= limitfori` | increment `j`, then `i` | O(n×m) |
| Reverse string | `len(msg) == 0` | `reverse(msg[1:]) + msg[0]` | O(n) |
| String length | `len(msg) == 0` → `0` | `length(msg[1:]) + 1` | O(n) |
| Binary search | `start > end` → `-1` | search left or right half | O(log n) |

---

### Binary Search — The Most Important Recursive Algorithm

Works **only on sorted arrays**. Cuts the search space in half each time → O(log n).

```
Array: [1, 3, 5, 7, 9, 11]   Target: 7

Step 1: middle = index 2 → value 5.  7 > 5 → search RIGHT half
Step 2: [7, 9, 11] → middle = index 1 → value 9.  7 < 9 → search LEFT half
Step 3: [7] → middle = index 0 → value 7.  FOUND ✅
```

```python
def binary_search_recursive(values, start, end, key):
    if end >= start:
        middle = (start + end) // 2
        if values[middle] == key:
            return middle
        elif values[middle] > key:
            return binary_search_recursive(values, start, middle, key)   # go left
        else:
            return binary_search_recursive(values, middle+1, end, key)  # go right
    return -1   # base case: not found
```

---

### Recursion vs Iteration

| | Recursion | Iteration |
|-|-----------|-----------|
| Readability | ✅ More elegant | ❌ Can be verbose |
| Memory | ❌ Uses call stack | ✅ Constant stack |
| Speed | ❌ Slightly slower (stack overhead) | ✅ Faster |
| Best for | Trees, graphs, divide & conquer | Simple loops |

> Fibonacci recursively for n=46 takes **19 seconds**. Iteratively: **< 1ms**. This is because naive recursion recomputes the same values repeatedly. Fix: **Dynamic Programming** (memoization).

---

## L04 — ADT List

> 📁 `src/TD4/` &nbsp;|&nbsp; 🎥 [Linked Lists explained](https://www.youtube.com/watch?v=njTh_OwMljA)

### What is an ADT?

An **Abstract Data Type (ADT)** defines *what* operations exist, not *how* they're implemented. Like an interface/contract.

`IList` in Python uses `ABC` (Abstract Base Class):

```python
from abc import ABC, abstractmethod

class IList(ABC):
    @abstractmethod
    def add(self, element): pass

    @abstractmethod
    def get(self, index): pass
    # ... etc
```

Any class that inherits `IList` **must** implement all abstract methods or Python will raise a `TypeError`.

---

### Implementation 1 — ArrayList (Contiguous)

Backed by a Python `list` (a resizable array). Elements sit **next to each other in memory**.

```
Index:  0    1    2    3
       [10] [20] [30] [40]
```

| Operation | Complexity | Reason |
|-----------|-----------|--------|
| `get(i)` | **O(1)** | Direct index access |
| `add` (end) | **O(1)** amortized | Append to end |
| `add_at(i)` | **O(n)** | Must shift all elements right of `i` |
| `remove(i)` | **O(n)** | Must shift all elements left of `i` |
| `contains` | **O(n)** | Linear scan |

> ✅ Use when you **read a lot** and **rarely insert/delete** in the middle.

---

### Implementation 2 — Singly Linked List

Each **Node** stores data + a pointer (`next`) to the next node. Nodes are scattered in memory.

```
head
 ↓
[10 | •]──→[20 | •]──→[30 | •]──→ None
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None       # pointer to next node
```

| Operation | Complexity | Reason |
|-----------|-----------|--------|
| `get(i)` | **O(n)** | Must walk from head |
| `add` (end) | **O(n)** | Must walk to tail first |
| `add_at(0)` | **O(1)** | Just update head |
| `remove(0)` | **O(1)** | Just update head |
| `remove(i)` | **O(n)** | Must walk to position |

> ✅ Use when you **insert/delete at the front** frequently.

---

### Implementation 3 — Doubly Linked List

Each Node has **both** `next` and `prev` pointers. The list tracks both `head` and `tail`.

```
     head                        tail
      ↓                           ↓
None←[10|•]⇄[20|•]⇄[30|•]⇄[40|•]→None
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None       # ← extra pointer
```

| Operation | Complexity | Reason |
|-----------|-----------|--------|
| `add` (end) | **O(1)** | Direct tail access |
| `add` (front) | **O(1)** | Direct head access |
| `remove` (known node) | **O(1)** | Use prev/next to bypass |
| `get(i)` | **O(n)** | Still must walk |
| Traverse backwards | ✅ | Follow `prev` pointers |

> ✅ Use when you need **O(1) at both ends** and sometimes traverse backwards.

---

### Full Comparison

| Operation | Array | Singly Linked | Doubly Linked |
|-----------|-------|---------------|---------------|
| Access by index | O(1) ✅ | O(n) | O(n) |
| Add at front | O(n) | O(1) ✅ | O(1) ✅ |
| Add at end | O(1) ✅ | O(n) | O(1) ✅ |
| Add in middle | O(n) | O(n) | O(n) |
| Remove at front | O(n) | O(1) ✅ | O(1) ✅ |
| Remove at end | O(1) ✅ | O(n) | O(1) ✅ |
| Memory overhead | Low | +1 pointer/node | +2 pointers/node |
| Traverse backwards | ❌ | ❌ | ✅ |

---

### Dynamic Resizing (TD5 ArrayList)

The TD5 `ArrayList` uses Python's `ctypes` to build a true low-level array with manual resizing:

```
Initial capacity: 4   → [_, _, _, _]
Add 4 items:          → [A, B, C, D]   ← full!
Add 1 more:           → resize to 8 → [A, B, C, D, E, _, _, _]
```

**Why double the size?** If you grew by 1 each time, every `add_back` would trigger a copy → O(n) always.  
Doubling makes `add_back` **O(1) amortized** (occasional O(n) copy, but rare).

---

## L05 — ADT Stack

> 🎥 [Stack Data Structure](https://www.youtube.com/watch?v=I37kGX-nZEI)

### The Concept — LIFO

A **Stack** is a linear structure where the **last element added is the first removed**.  
Think of a stack of plates — you can only take from the top.

```
push(A) → [A]
push(B) → [A, B]
push(C) → [A, B, C]
pop()   → C    stack: [A, B]
pop()   → B    stack: [A]
pop()   → A    stack: []
```

---

### Core Operations

| Operation | Description | Complexity |
|-----------|-------------|-----------|
| `push(e)` | Add element to top | O(1) |
| `pop()` | Remove & return top element | O(1) |
| `peek()` / `top()` | Return top without removing | O(1) |
| `is_empty()` | Check if empty | O(1) |
| `size()` | Number of elements | O(1) |

> All stack operations are **O(1)**. This is what makes a stack powerful.

---

### Stack vs Queue

| | Stack | Queue |
|-|-------|-------|
| Order | **LIFO** — Last In First Out | **FIFO** — First In First Out |
| Insert | `push` at **top** | `enqueue` at **rear** |
| Remove | `pop` from **top** | `dequeue` from **front** |
| Real analogy | Stack of plates | Line at a store |

---

### Implementation 1 — Array-based Stack

```
top
 ↓
[A, B, C, _, _, _]
 0  1  2
```

```python
class ArrayStack:
    def __init__(self, max_size):
        self._data = [None] * max_size
        self._top = 0

    def push(self, e):
        if self._top >= len(self._data):
            raise OverflowError("Stack full")
        self._data[self._top] = e
        self._top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        self._top -= 1
        return self._data[self._top]

    def peek(self):
        return self._data[self._top - 1]

    def is_empty(self):
        return self._top == 0
```

---

### Implementation 2 — Linked List Stack

Use a **Singly Linked List** where the `head` is the top of the stack.

```
top/head
    ↓
   [C] → [B] → [A] → None
```

**Adapter pattern:** Stack *delegates* to the linked list instead of inheriting from it.

| Stack method | Linked List method |
|-------------|-------------------|
| `push(e)` | `add_first(e)` — O(1) |
| `pop()` | `remove_first()` — O(1) |
| `peek()` | `get(0)` — O(1) |

---

### Applications of Stacks

#### 1. Parentheses Matching
Check if `([{}])` is valid — every opening bracket must close in the correct order.

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
```

#### 2. Program Call Stack
When you call a function, Python pushes a **stack frame** (local variables + return address) onto the call stack. When the function returns, it's popped. Recursive algorithms consume a lot of stack.

#### 3. Undo/Redo in editors
Every action is pushed onto a stack. `Ctrl+Z` pops the last action and reverses it.

#### 4. Convert decimal to binary
```python
def dec_to_bin(n):
    stack = []
    while n > 0:
        stack.append(n % 2)   # push remainder
        n //= 2
    result = ""
    while stack:
        result += str(stack.pop())  # pop in reverse = correct order
    return result
# dec_to_bin(13) → "1101"
```

#### 5. Expression evaluation
Use two stacks (operands + operators) to evaluate `3 + (4 × 2)` without recursion.

---

## L06 — ADT Queue

> 🎥 [Queue Data Structure](https://www.youtube.com/watch?v=XuCbpw6Bj1U) &nbsp;|&nbsp; 🎥 [Priority Queue & Heap](https://www.youtube.com/watch?v=wptevk0bshY)

### The Concept — FIFO

A **Queue** is a linear structure where the **first element added is the first removed**.  
Think of a line at a store — you join at the back, leave from the front.

```
enqueue(A) →      [A]
enqueue(B) →      [A, B]
enqueue(C) →      [A, B, C]
              front^       ^rear
dequeue()  → A,   [B, C]
dequeue()  → B,   [C]
```

---

### Core Operations

| Operation | Description | 
|-----------|-------------|
| `enqueue(e)` | Add to the **rear** |
| `dequeue()` | Remove from the **front** |
| `peek()` / `front()` | See front without removing |
| `is_empty()` | Check if empty |
| `size()` | Number of elements |

---

### Four Implementations (from TD5)

#### 1. `ArrayQueue` — Simple array
```python
def enqueue(self, item):   # O(1) — append to end
    self.__items.append(item)

def dequeue(self):         # ❌ O(n) — pop(0) shifts ALL elements left
    return self.__items.pop(0)
```

#### 2. `LinkedQueue` — Singly Linked List (head only)
```python
def enqueue(self, item):   # ❌ O(n) — must walk to tail
    self.add(item)

def dequeue(self):         # O(1) — remove head
    return self.remove(0)
```

#### 3. `LinkedQueueHT` — Linked List with Head & Tail ✅
```python
def enqueue(self, item):   # O(1) — direct tail access
    new_node = self.Node(item)
    self.tail.next = new_node
    self.tail = new_node

def dequeue(self):         # O(1) — direct head access
    removed = self.head.data
    self.head = self.head.next
    return removed
```

#### 4. `DequeQueue` — Python `collections.deque` ✅
```python
from collections import deque

def enqueue(self, item):   # O(1)
    self.__items.append(item)

def dequeue(self):         # O(1) — deque is optimized for this
    return self.__items.popleft()
```

---

### Complexity Comparison

| Implementation | `enqueue` | `dequeue` | Notes |
|----------------|-----------|-----------|-------|
| `ArrayQueue` | O(1) | ❌ **O(n)** | `pop(0)` shifts everything |
| `LinkedQueue` | ❌ **O(n)** | O(1) | No tail pointer |
| `LinkedQueueHT` | ✅ O(1) | ✅ O(1) | Best linked version |
| `DequeQueue` | ✅ O(1) | ✅ O(1) | Easiest, use this in practice |

> 🔑 The trick for O(1) on both ends: keep a **tail pointer**. Never walk the list.

---

### Circular Queue

A fixed-size array used as a ring to avoid the O(n) shift problem.

```
Indices:  0    1    2    3    4
         [C]  [D]  [ ]  [A]  [B]
               ↑              ↑
              rear           front
```

Formulas:
- `front = (front + 1) % capacity`
- `rear = (rear + 1) % capacity`

This wraps around — when rear reaches the end of the array, it goes back to index 0.

---

### Priority Queue & Min-Heap

A **Priority Queue** is a queue where dequeue always returns the **highest-priority element**, not the oldest.

**Implemented with a Heap** — a complete binary tree where every parent is ≤ its children (min-heap).

```
         1          ← always the minimum
       /   \
      3     2
     / \   /
    7   4  5

Array representation: [1, 3, 2, 7, 4, 5]
Index:                  0  1  2  3  4  5
```

#### Index Formulas (0-based)

```
Parent of i   →  (i - 1) // 2
Left child    →  2i + 1
Right child   →  2i + 2
```

#### Insert — `enqueue` — O(log n)

1. Append new element to end of array
2. **Bubble up:** swap with parent while `child < parent`

```
Insert 0:  [1, 3, 2, 7, 4, 5, 0]
                              ↑ new
Bubble up: 0 < 2 → swap  →  [1, 3, 0, 7, 4, 5, 2]
           0 < 1 → swap  →  [0, 3, 1, 7, 4, 5, 2]  ← done
```

#### Remove minimum — `dequeue` — O(log n)

1. Swap root with last element
2. Remove last (the old min)
3. **Bubble down:** swap with smallest child while `parent > child`

```
Remove min (0): swap root with last → [2, 3, 1, 7, 4, 5]
Bubble down: 2 > 1 → swap → [1, 3, 2, 7, 4, 5]  ← done
```

#### Priority Queue with custom objects

Objects need comparison operators so the heap can order them:

```python
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __lt__(self, other):      # older year = higher priority
        return self.year < other.year

    def __repr__(self):
        return f"Movie({self.title}, {self.year})"

pq = PriorityQueue()
pq.enqueue(Movie("Inception", 2010))
pq.enqueue(Movie("The Godfather", 1972))
pq.enqueue(Movie("Parasite", 2019))

pq.dequeue()  # → The Godfather (1972) — oldest = most prioritized
pq.dequeue()  # → Inception (2010)
pq.dequeue()  # → Parasite (2019)
```

#### Heap Operations Summary

| Operation | Complexity | How |
|-----------|-----------|-----|
| `enqueue` | O(log n) | Append + bubble up |
| `dequeue` | O(log n) | Swap + pop + bubble down |
| `peek` | **O(1)** | Root is always minimum |
| Height of heap | O(log n) | `h = log₂(n+1) - 1` |

#### Applications of Priority Queues

- 🏥 Hospital triage — most critical patient seen first
- 🖨️ Print queue — shortest job first
- 🌐 Network packet routing — by urgency
- 💻 OS task scheduler — critical before interactive before background
- 📦 Compression algorithms (Huffman coding)

---

## Project Structure

```
src/
├── TD1/    OOP, layered architecture, Singleton, BMI calculator
│   ├── Model/      Category.py
│   ├── Data/       MockDB.py
│   ├── Dao/        CategoryDAO.py
│   ├── Service/    BodyMassIndexService.py
│   └── UI/         ConsoleUI.py, Main.py
│
├── TD2/    Big-O, linear search, duplicate removal, selection sort
│   └── Exercice.py
│
├── TD3/    Recursion, binary search
│   └── Exercice.py
│
├── TD4/    IList interface, ArrayList, SinglyLinkedList, DoublyLinkedList
│   ├── IList.py
│   ├── ArrayList.py
│   ├── SingleLinkedList.py
│   └── DoubleLinkedList.py
│
└── TD5/    Queue variants, dynamic ArrayList, MinHeap, PriorityQueue
    ├── ArrayList.py          (dynamic with ctypes)
    ├── DoublyLinkedList.py
    ├── DoublyLinkedNode.py
    └── TD5/
        ├── ArrayQueue.py
        ├── Queue.py
        ├── LinkedQueue.py
        ├── LinkedQueueHT.py
        ├── DequeQueue.py
        ├── MinHeap.py
        └── Movie.py          (Priority Queue demo)
```

---

## 📊 Complexity Cheat Sheet

### Data Structures

| Structure | Access | Search | Insert (front) | Insert (end) | Delete |
|-----------|--------|--------|----------------|--------------|--------|
| Array (contiguous) | **O(1)** | O(n) | O(n) | O(1)* | O(n) |
| Singly Linked List | O(n) | O(n) | **O(1)** | O(n) | O(1) head |
| Doubly Linked List | O(n) | O(n) | **O(1)** | **O(1)** | O(1) if node known |
| Stack | O(n) | O(n) | — | **O(1)** push/pop | **O(1)** |
| Queue (deque/HT) | O(n) | O(n) | — | **O(1)** | **O(1)** |
| Min-Heap | — | — | — | O(log n) | O(log n) |

*amortized

### Sorting Preview

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

---

*Last updated: L01 → L06*

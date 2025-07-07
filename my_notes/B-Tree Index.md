## What Is B-Tree?

A B-tree is a [data structure](https://builtin.com/data-science/data-structures) that provides [sorted data](https://builtin.com/machine-learning/fastest-sorting-algorithm) and allows searches, sequential access, attachments and removals in sorted order. The B-tree is highly capable of storing systems that write large blocks of data. The B-tree simplifies the [binary search tree](https://builtin.com/data-science/binary-search-implementation-python) by allowing nodes with more than two children. Below is a B-tree example.
![Illustration of a b-tree](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/1_b-tree-indexing.jpg)

Illustration of a B-tree index. | Image: Dhanushka Madushan

B-tree stores data such that each node contains keys in ascending order. Each of these keys has two references to another two child nodes. The left-side child node keys are less than the current keys, and the right-side child node keys are more than the current keys. If a single node has “n” number of keys, then it can have maximum “n+1” child nodes.

When we think about the performance of a [database](https://builtin.com/data-science/database), indexing is the first thing that comes to mind. Here, we’ll look into how database indexing works on a database.

## B-Tree Indexing Explained
B-tree indexing is the process of sorting large blocks of data such that each node contains keys in ascending order. Its goal is to make searching through data faster and easier, and its search time is O(log(n)).
operation_perf.py - Provides the source code for measuring the performance of different methods of removing elements from a list and reversing a list.

operation_practice.py - Used to test/practice a series of Python list operations.

performance-comparison.png - Output of running operation_perf.py which shows two plots comparing the performance of methods of removing and element and reversing a list, respectively.

python-practice.png - Output of operation_practice.py

------Observations------
As N (size of the list L) increases, the time taken by each operation increases. When removing an element from a list with pop(), removing the first element with L.pop(0) leads to a significantly higher execution time at higher N values, while the time for removing the last element with L.pop() stays relatively constant.
Thus, it is reasonable to assume that removing the last element of a list is much faster than removing the first element, especially at higher list sizes.

Similarly, out-of-place list reversal is significantly slower at high N values, while in-place reversal has a much less drastic increase in time. Thus, it is reasonable to assume that in-place list reverasal is more performant than out-of-place reversal at higher list sizes.
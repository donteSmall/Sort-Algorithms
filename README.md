  ### Sort-Algorithms

`A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.`

`An in-place algorithm is an algorithm which transforms input using no auxiliary data structure`


| Sort Type     | Av.Complexity |  Worst Case    |   Stable      |  Inplace      |      Note     |
| ------------- | ------------- |  ------------- | ------------- | ------------- | ------------- |
|    Quick      |  O(n log n)   |   O(n^2)       |     Yes       |      Yes      | O(n^2) in best case  |
|    Merge      |  O(n log n)   |   O(n log n)   |     Yes       |      No       |               |
|    Heap       |  O(n log n)   |   O(n log n)   |     No        |      Yes      |               |
|    Select     |  O(n^2)       |   O(n^2)       |     No        |      Yes      |               |
|    Bubble     |  O(n^2)       |   O(n^2)       |     Yes       |      Yes      |               |
|    Insert     |  O(n^2)       |   O(n^2)       |     Yes       |      Yes      | O(n) in best case
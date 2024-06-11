# NP-hard-time-analysis

This is my try on the famous NP hard problem which goes like this:

Find all the subsets from a set of numbers whose sum is zero.
Constraint: Subset size must be 5
Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

This is a smaller version of how it goes.

#solution 1
a famous solution for this is randomization. we randomly choose a subet of size 5 
and hope for the best.
The thing with NP hard problems is they're very long to solve so what we do is give it
a condition, lets say 10000 iterations to find as many subsets that total to 0 as possible.

#solution 2
The solution that comes to mind is making all possible subsets and then filtering the ones that 
total to 0. I did this to show why this solution is not viable for bigger sets.
I wrote a python code that finds subsets that total to 0 in a particular set, and then add 5
more random values between -50 and 50 to increase the size of the set. I did this over 20 iterations
and stored the time taken into a .csv file and wrote an R code to make the graph of time taken

This is how the graph looks
![image](https://github.com/ArmaanChahal/NP-hard-time-analysis/assets/121849483/4e3bc793-5ccb-459c-a004-eada150ab345)

Analysis:
Time Complexity Explanation
To determine the time complexity of finding all subsets of a given size 
𝑘
k that sum to zero, we need to consider the following steps:

Generating Combinations:
The number of combinations of 
𝑛
n elements taken 
𝑘
k at a time is given by the binomial coefficient:

𝐶
(
𝑛
,
𝑘
)
=
𝑛
!
𝑘
!
(
𝑛
−
𝑘
)
!
C(n,k)= 
k!(n−k)!
n!
​
 
For a subset size 
𝑘
k, the number of combinations is 
𝑂
(
𝐶
(
𝑛
,
𝑘
)
)
=
𝑂
(
𝑛
!
𝑘
!
(
𝑛
−
𝑘
)
!
)
O(C(n,k))=O( 
k!(n−k)!
n!
​
 ).

Checking Subset Sums:
For each combination, we need to check if the sum of the elements is zero. The time complexity for summing 
𝑘
k elements is 
𝑂
(
𝑘
)
O(k). Since 
𝑘
k is a constant, this can be considered 
𝑂
(
1
)
O(1).

Overall Time Complexity
Combining the two steps, the overall time complexity for finding all subsets of size 
𝑘
k whose sum is zero can be approximated as:

𝑂
(
𝑛
!
𝑘
!
(
𝑛
−
𝑘
)
!
)
⋅
𝑂
(
1
)
O( 
k!(n−k)!
n!
​
 )⋅O(1)
For large 
𝑛
n, this can be approximated as:

𝑂
(
𝑛
𝑘
)
O(n 
k
 )
Specific Case: Subset Size 6
For a subset size of 6, the number of combinations is:

𝐶
(
𝑛
,
6
)
=
𝑛
!
6
!
(
𝑛
−
6
)
!
C(n,6)= 
6!(n−6)!
n!
​
 
Thus, the time complexity for generating and checking all combinations of size 6 is:

𝑂
(
𝑛
!
6
!
(
𝑛
−
6
)
!
)
≈
𝑂
(
𝑛
6
)
O( 
6!(n−6)!
n!
​
 )≈O(n 
6
 )
Summary
The time complexity for generating and checking all subsets of size 
𝑘
k is 

O(n^k).

 
For a subset size of 6, the time complexity is 


O(n^6).

Thus, this is not a viable option.

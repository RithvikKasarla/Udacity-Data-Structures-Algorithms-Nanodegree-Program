For this problem I used a manipulated binary search algorithm. Starting out, I made my pivot the middle of array like a typical binary search. 

This is where is diverges from regular binary search. By checking if the number is greater or less than the middle, then checking how it compares with the first or last element of the section, respectively I am able to determine on what side of the pivot the number will fall. Continuing this pattern I was able make it so it works like binary search.

Space complexity is O(n) andthe time complexityis O(logn).
For the union function I used a set data structure in order to ensure when I added the data from list 1 and 2 there will only be unique data in it. Then I added the data from the set into a new linked list.

The worst case time complexity os O(2n) and the worst case space complexity is O(2n)

For the intersection I created a set for list1 so I know none of the numbers is repeated. Then Then I created an empty set for list 2. As I traverese list 2 if the value isnt already in the lsit 2 set then I add it and check if the value is in list1's set. If both are true then I add it to my intersection linked list and retrun that.

This time complexity is O(2n) and its worst case space complexity is O(n).
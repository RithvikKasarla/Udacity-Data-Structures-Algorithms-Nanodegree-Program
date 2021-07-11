In problem 3 for the encoding, first I used a dictionary to associate each charcter with its respective chracter count, as a dictionary is representative of a table. Once this "table" is created I sorted the keys in an array based on their values. Then build the tree using recursion as I noticed the same process repeating itself- you have a node which tells the count of all characters below it, you put the largest character on the left and the new count on the right and repeat. 

Once the tree was built I used recursion again to create the conversion values. I used recurion again as we were just traversing the tree, which is a repeated process. I used a dictionary to hold these conversions as it acts like a conversion table where each character key has its own associated code.

Finally I converted the data.

For the decoding process, I used regression to traverse the tree and recrease the conversions of each letter, the converstions were held using a dictionary with key value pairs. Once I had this dictionary created, I went through the encoded message and used basic code to split it to the numbers and put each in the decoding dictionary to get the final message.

The time complexity of the encoding is O(nlogn) and the time complexity for the decoding is O(n). As in both we effectively go through the message once either to decode all the values back to letters or vice versa. The space complexity for both functions is O(n).
For the trie problem, I just coded a classic trie. The trie node includes a dictionary holding its childrens nodes and whether or not that node is the last node of the word.Its insert function is O(1) and space comlexityis O(1).

The trie class then uses the Trie node class. Its insert function having a time complexity of O(n) and a space complexity of O(n). The find function has a time complexity O(n) and a space complexity of O(1).

In the rewritten trie node there is a suffix function which has a time and space complexiy of O(n). This function utilizes recursion as the problem consists of traversing all paths in the trie below a certain node.
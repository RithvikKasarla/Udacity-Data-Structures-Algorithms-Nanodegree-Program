# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, node,handle):
        # Insert the node as before
        self.children[node] = RouteTrieNode(handle)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler
    def insert(self, p,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        #print("INSERING ...")
        cur = self.root
        #print("INSERTING")
        #print(p)
        for node in p:
            #print("\t", node)
            if node not in cur.children:
                cur.insert(node, None)
            cur = cur.children[node]
        cur.handler = handler
        #print(cur.handler)
    def find(self, p):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        #print("FINDING")
        cur = self.root
        for path_ in p:
            #print("\t",path_)
            #for x  in cur.children:
                #print('\t\t',x)
            if path_ in cur.children:
                cur = cur.children[path_]
            else:
                return None
        return cur.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler,NotFoundHander = "404 Not Found"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.TrieRoot = RouteTrie(handler)
        self.notFound = NotFoundHander

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        p = self.split_path(path)
        #print("SPLIT ",path, " to ",p)
        self.TrieRoot.insert(p, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == None or path == "":
            return self.notFound
        p = self.split_path(path)
        #print("-------> split", path, "into ", p)

        if p == [""]:
            return self.TrieRoot.handler
        cur = self.TrieRoot
        handle = cur.find(p)
        if handle == None:
            return self.notFound
        else:
            return handle

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split_path = path.split('/')
        if path == None:
            return None
        if split_path[0] == '':
            split_path =  split_path[1:]
        if split_path[len(split_path)-1] == "":
            split_path = split_path[:len(split_path)-1]
        return split_path
        



# Here are some test cases and expected outputs you can use to test your implementation
print("Ex.1")
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

#--------------------------------------------------------
print("Ex. 2")
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler") 
router.add_handler("/home", "home handler") 

print(router.lookup("/")) # should print 'root handler
print(router.lookup("/home")) #home handler
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/me")) # not found handler

print("Ex. 3")
router = Router("root handler", "not found handler")
router.add_handler("/home/about/", "about handler") 
router.add_handler("/home/", "home handler") 

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) #home handler
print(router.lookup("+home+about+me")) # not found handler
print(router.lookup(None)) # not found handler
print(router.lookup("")) # not found handler
import sys
import operator
class node:
    
    def __init__(self,char, freq):
        self.left = None
        self.right = None
        self.char = char
        self.freq = freq

def huffman_encoding(data):
    if data == "":
        return "0" , node(None,0)
    count = {}
    for ch in data:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    sortedvalues = sorted(count, key=lambda k: count[k], reverse=True)
    head = node(None, len(data))
    buildTree(len(data), count, sortedvalues, head)
    conversions = createconversions(head,"")
    return convert(data, conversions), head

def buildTree(count, freq, sortedvals, head):
    if (len(sortedvals) > 2):
        head.left = node(sortedvals[0], freq[sortedvals[0]])
        head.right = node(None, count - freq[sortedvals[0]])
        buildTree(head.right.freq, freq, sortedvals[1:], head.right)
        return
    else:
        head.left = node(sortedvals[0], freq[sortedvals[0]])
        try:
            head.right = node(sortedvals[1], freq[sortedvals[1]])
        except:
            pass
        return

def createconversions(head, code):
    converstions = {}
    if head.left == None and head.right == None:
        converstions[head.char] = code + "1"
        return converstions
    else:
        converstions.update(createconversions(head.left,code))
        if head.right != None:
            converstions.update(createconversions(head.right,code + "0"))
    return converstions 

def convert(data, conversions):
    characters = list(data)
    converted = []
    for character in characters:
        converted.append(conversions[character])
    return "".join(converted)

def huffman_decoding(data,tree):
    if data == "0":
        return ""
    conversions = createconversions(tree,"")
    decode_converstions = dict([(value, key) for key, value in conversions.items()])
    splits = data.split("1")
    message = ""
    for split in range(0,len(splits)):
        splits[split] += '1'
        message += decode_converstions[splits[split]]
    return message



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #------- TEST 2 -----
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    #------- TEST 3 -----
    a_great_sentence = "AAAAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
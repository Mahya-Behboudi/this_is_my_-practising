from testing12 import test
import time

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
def linear_search(X,target):
    co =0
    for(I,V) in enumerate(X):
        co +=1
        if V == target:
            return I
    return -1
def found_unknown_words(vocab,words):
        listi =[]
        for w in words:
            if (linear_search(vocab,w)<0):
                listi.append(w)
        return listi
def load_word_from_file(filename):
    f = open(filename,"r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds
def translatee(thefile):
    ff = open(thefile ,"r")
    d = ff.read()
    w = d.maketrans(
    # If you find any of these
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
    # Replace them by these
    "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = d.translate(w)
    return cleaned_text
def te():
    pass
#     test(linear_search(friends,"Joe") ==0)
#     test(linear_search(friends,"amhya") == 9)
#     test(linear_search(friends,"Brad")==2)
    #   test(found_unknown_words(vocab,book_words) ==["from","to"])
    #   test(found_unknown_words([],book_words) == book_words)
    #   test(found_unknown_words(vocab,["the","boy","fell"])==[])
# te()
loag = load_word_from_file("alice_sory.txt")
print("there are {0} words in the alice's story,starting with\n {1}".format(len(loag),loag[:6]))
load = load_word_from_file("word_list.txt")
print("there are {0} words in the list of words ,ending with {1} word !".format(len(load),load[19400:]))
t0 = time.time()
the_result = translatee("yu.txt")
t1 = time.time()
print(the_result)
print("this is the prossesor {0:.4f}".format(t1-t0))



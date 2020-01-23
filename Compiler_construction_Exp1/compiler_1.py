from termcolor import colored


S = "#include xyz \nint  i =    2 + 3; \ncout<<i; /*jhgjghjg*/ \ni = (a<b)?(a:b); //ggg "

D = {"keywords":[], "constants":[], "id":[], "operators":[], "assignment":[], "comparisons":[]}


def print_D(D):
    print("_______________________________________________", )
    for key, value in D.items():
        if key != "comparisons" and key!="prepocessors" and key!="id":
            print(colored(key, "blue", attrs=["bold"]), "\t\t\t\t", value)
        elif key == 'id':
            print(colored(key, "blue", attrs=["bold"]), '\t\t\t\t\t\t', value)
        else:
            print(colored(key, "blue", attrs=["bold"]), "\t\t\t", value)
    print("_______________________________________________")


def remove_comments_single(S):
    f = 0
    S0 = ""
    for i_ in range(len(S)):
        i = S[i_]

        if f == 0:
            if i == "/" and S[i_+1] == "/":
                f = 1
            else:
                S0 = S0 + i


        else:

            if S[i_:i_+1:] == "\n":
                f =0



    return S0

def remove_comment_multi(S):
    f = 0
    S0 = ""
    for i_ in range(len(S)):
        i = S[i_]

        if f == 0:
            if i == "/" and S[i_ + 1] == "*":
                f = 1
            else:
                S0 = S0 + i
        elif f== 2:
            f =0
        else:
            if S[i_] == "*" and S[i_+1] == '/':
                f = 2

    return S0

def remove_comments(S):
    S0 = remove_comments_single(S)
    # print(S0)
    S1 = remove_comment_multi(S0)
    # print(S1)
    print(colored("\n\nRemoving comments we get:", "green", attrs=["bold"]))
    print(S1)
    return S1




def add_operator(S, j, L):
    if len(S) != j+1:
        if S[j+1] == " ":
            L.append(S[j])
    else:
        L.append(S[j])
    return L

def replace_new_line(S):
    S = S.replace('\r', '').replace('\n', '')
    return S

def remove_sapces(S):
    print(colored("\n\nRemoving spaces and new-line characters, we get:", "green", attrs=["bold"]))
    S0 = ""
    S = replace_new_line(S)
    index_space= []
    for i in range(len(S)):

        if S[i] == " ":
            index_space.append(i)
        else:
            S0 = S0 + S[i]

    i = 0
    index_space2 = []
    while i < len(index_space):


        if i == len(index_space)-1:
            if index_space[i] == len(S)-1:
                break
            if index_space[i - 1] == index_space[i]-1:

                index_space2.append(index_space[i])
            else:
                index_space2.append(index_space[i])

        elif index_space[i+1] != index_space[i]+1 :

            if index_space[i - 1] == index_space[i]-1:

                index_space2.append(index_space[i])
            else:
                index_space2.append(index_space[i])

        i = i+1

    index_space = index_space2
    S1 = S

    S2 = ""

    for i in range(len(S1)):
        if S1[i] == " ":
            if i in index_space:
                S2 = S2 + S1[i]
        else:
            S2 = S2 +S1[i]
    print(S2)
    return S2

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def add_space_before_equal(S):
    L = list(find_all(S, "="))
    S0 = ""
    for i in range(0, len(S)):
        if i in L:
            S0 = S0 + " " + S[i]
        else:
            S0 = S0 + S[i]
    # print(S0)
    return S0


def add_space_before(S, ch):
    return S.replace(ch, " "+ch +" ")

def add_space_before_assignment(S):

    S0 = add_space_before(S, "==")
    S1 = S0.replace("= =", " ==")
    S2 = add_space_before(S1, ";")
    S3 = add_space_before(S2, "{")
    S4 = add_space_before(S3, "}")
    S5 = add_space_before(S4, "(")
    # print("S5", S5)
    S6 = add_space_before(S5, ")")
    # print("S6", S6)

    S7 = add_space_before(S6, "%")
    S8 = add_space_before(S7, "/")
    S9 = add_space_before(S8, "*")
    S10 = add_space_before(S9, "-")
    S11 = add_space_before(S10, "+")
    S12 = add_space_before(S11, ":")
    # print(S12, S12)
    S13 = add_space_before(S12, "?")
    S14 = add_space_before(S13, "<<")
    # S14 = add_space_before(S13, "<")
    S15 = S14.replace("< <", " <<")


    S_ = remove_sapces(S15)

    # print(S_)


    return S_





def add_spaces(S):
    S = remove_sapces(S)



    return S

def get_entities(S):
    # S =

    S = add_space_before_assignment(S)
    # print(S, "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
    L=[]
    i = 0
    x = ""

    while i < len(S):
        # print(i, len(S), S[i])
        # L.append(S[i])
        if S[i] == " ":
            L.append(x)
            x = ""

        else:
            x = x+S[i]
        # print(x)
        i = i+1


    print(colored("\n\nSeperating Different entities:", "green", attrs=["bold"]))
    return L


# entities_list = []
# def find_entities(S):
#     L = []
#     i = 0
#     # for i in range(len(S)):
#     while i < len(S):
#         print(i, "$$$$$$$$$$$$$$$$$$$$$$")
#         x = ""
#         for j in range(i, len(S)):
#             if S[j] == " ":
#                 i = j
#                 break
#             if S[j] in "=<>!;+-*/":
#                 i=j
#                 print("Get Operators")
#                 L = add_operator(S, j, L)
#                 break
#
#             x = x+S[j]
#             print(x, "*************", S[j])
#         print(x, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n ___________________________________")
#         # if x!= "":
#         L.append(x)
#
#         i = i+1
#     print(L)
#
# # add_keyword("int", 0, 2)
# # print_D(D)
# print(get_entities(S))


def check_for_function(i_, L):
    if L[i_+1] == "(":
        return True

def check_for_preprocessor(i_, L):
    if L[i_-1] == "#":
        return True


def get_types(S):
    S = remove_comments(S)
    L = get_entities(S)
    # print(L, "\n", S, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    L0 = []
    preproc = []

    for i_ in range(len(L)):
        i = L[i_]
        #print(i, "+============================================")
        if i in ['int', 'cout'] and i[0]!="#":
            print("found keyword:", i)
            D["keywords"].append(i)
            # print(D)
        elif i in ['+', '-', '*', '/', '%', ':', '?', '(', ')', ';']:
            print("operator found:", i)
            D["operators"].append(i)
        elif i in ['==', '<']:
            print("coparison found:", i)
            D["comparisons"].append(i)

        elif i in ['=']:
            print("assignment found:", i)
            D["assignment"].append(i)

        else:
            try:
                x = int(i)
                D['constants'].append(x)
            except:
                try:
                    if check_for_function(i_, L):
                        print("function found:", i)
                except:
                    pass
                if check_for_preprocessor(i_, L):
                    print("preprocessor part found:", str(i) + str(L[i_+1]))
                else:
                    D["id"].append(i)

                    print("variable found:", i)
        # print(D)
        new_id = []
        f = 0
        for i_ in range(len(D['id'])):
            # print(i)
            i = D['id'][i_]
            try:
                # print("try", i)
                if i == "#include":
                    # D['id'][i_] = i + " " + D['id'][i_+1]
                    # D['id']
                    preproc.append(i + " " + D['id'][i_+1])
                    # print('###########################################################################3', preproc)
                    D['prepocessors'] = preproc
                    # print(D)
                    f = 1
                elif f==1:
                    f = 0
                    # pass
                else:
                    new_id.append(i)

            except:
                new_id.append(i)
                pass
        # print(new_id, preproc, "+++++++++++++++++++++++++++++++++++++++++++++")
        D['id'] = new_id
        D['prepocessors'] = preproc
        # print(D)

    return L, D



print(colored("\n\nOriginal String:\n", "green", attrs=["bold"]), S, "\n")



G=get_types(S)
print(colored("\n\nFollowing is the dictionary:", "green", attrs=["bold"]))
print_D(G[1])

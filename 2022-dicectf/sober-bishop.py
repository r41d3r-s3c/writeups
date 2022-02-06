freq = [[' ',0],['.',1],['o',2],['+',3],['=',4],['*',5],['B',6],['O',7],['X',8],['@',8],['%',9],['&',9],['#',9],['/',9],['^',9],['S','S'],['E','E']]

def test_program(word):
    possible_phrases = [word]

    print(possible_phrases[0])

    same_list = []

    prev_list = []

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789_}'

    current_loc = 76

    code = []

    original = "          E               +               B               = .               S                                                                            "

    # test if randomart is wrong 
    def test_if_wrong(x,y):
        same_count = 0
        state = "Same"
        for i in range(0, len(x)):
            if y[i] > x[i]:
                return['Greater',same_count]
            
            if y[i] < x[i]:
                state = "Lesser"
            if y[i] == x[i]:
                same_count = same_count + 1
        return [state, same_count]

    def find_current_loc_index(x,y):
        for i in range(0,len(code)):
            if x[i][0] == y[0]:
                if x[i][1] == y[1]:
                    return i

    # make bishop move
    def move_bishop(code,letter,current_loc):
        a = 0
        b = 16
        c = 153-17
        d = 153
        T = 0
        B = 8
        R = 16
        L = 0

        if current_loc == a:    
            if letter == '00':
                current_loc = current_loc
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc +1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 18
                code[current_loc][2] = code[current_loc][2] + 1
        elif current_loc == b:    
            if letter == '00':
                current_loc = current_loc - 1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 17
                code[current_loc][2] = code[current_loc][2] + 1
        elif current_loc == c:    
            if letter == '00':
                current_loc = current_loc - 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 1
                code[current_loc][2] = code[current_loc][2] + 1
        elif current_loc == d:    
            if letter == '00':
                current_loc = current_loc - 18
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc - 1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc
                code[current_loc][2] = code[current_loc][2] + 1
        elif code[current_loc][0] == T:    
            if letter == '00':
                current_loc = current_loc - 1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc + 1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 18
                code[current_loc][2] = code[current_loc][2] + 1
        elif code[current_loc][0] == B:    
            if letter == '00':
                current_loc = current_loc - 18
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc - 1
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 1
                code[current_loc][2] = code[current_loc][2] + 1
        elif code[current_loc][1] == R:    
            if letter == '00':
                current_loc = current_loc - 18
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 17
                code[current_loc][2] = code[current_loc][2] + 1
        elif code[current_loc][1] == L:    
            if letter == '00':
                current_loc = current_loc - 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 17
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 18
                code[current_loc][2] = code[current_loc][2] + 1
        else:       
            if letter == '00':
                current_loc = current_loc - 18
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '01':
                current_loc = current_loc - 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '10':
                current_loc = current_loc + 16
                code[current_loc][2] = code[current_loc][2] + 1
            if letter == '11':
                current_loc = current_loc + 18
                code[current_loc][2] = code[current_loc][2] + 1

        return [code,current_loc]

    ### convert original to num_code
    num_code = ''
    for i in range(len(original)):
        for j in range(0,len(freq)):
            if original[i] == freq[j][0]:
                num_code = num_code + str(freq[j][1])

    ### create initial code statement
    def create_initial_state():
        tmp = []
        for i in range(0,9):
            for j in range(0,17):
                tmp.append([i,j,0])
        return tmp

    # create code from phrase
    def test_possible_phrases(possible_phrases):
        possible_phrase = []
        prev_list = possible_phrases
        for phrase in possible_phrases:
            for char in chars:
                code = create_initial_state()
                current_loc = 76
                tmp_phrase = phrase + char
                for i in range(0,len(tmp_phrase)):
                    bin_str = ''.join(format(ord(j), '08b') for j in tmp_phrase[i])
                    a_str = bin_str[6:8]
                    tmp = move_bishop(code,a_str,current_loc)
                    tmp_code = tmp[0]
                    current_loc = tmp[1]
                    b_str = bin_str[4:6]
                    tmp = move_bishop(code,b_str,current_loc)
                    tmp_code = tmp[0]
                    current_loc = tmp[1]
                    c_str = bin_str[2:4]
                    tmp = move_bishop(code,c_str,current_loc)
                    tmp_code = tmp[0]
                    current_loc = tmp[1]
                    d_str = bin_str[0:2]
                    tmp = move_bishop(code,d_str,current_loc)
                    tmp_code = tmp[0]
                    current_loc = tmp[1]

                # place starting key
                for itm in code:
                    if itm[0] == 4: 
                        if itm[1] == 8:
                            itm[2] = 'S'

                # place starting key
                for itm in code:
                    if itm[0] == 1: 
                        if itm[1] == 16:
                            itm[2] = 'E'

                # convert code to same format as num_code
                tmp_code = ''
                for i in range(0,len(code)):
                    tmp_num = code[i][2]
                    if tmp_num != 'S':
                        if tmp_num != 'E':
                            if tmp_num > 9:
                                tmp_num = 9
                    tmp_code = tmp_code + str(tmp_num)

                # print(num_code)
                # print(tmp_code)
                # print(len(original), len(num_code))

                test_answer = test_if_wrong(num_code, tmp_code)
                if test_answer[1] > 152:
                    if tmp_phrase[-1] == '}':
                        print(tmp_phrase,":", test_answer, "Possible Answer")
                   
                if test_answer[0] == "Lesser":                    
                    possible_phrase.append(tmp_phrase)

                if test_answer[0] == "Same":            
                    same_list.append(tmp_phrase)
        return possible_phrase

    while len(possible_phrases) != 0:
        print("Testing: ", len(possible_phrases), "possibles")
        possible_phrases = test_possible_phrases(possible_phrases)

word_list = ['dice{5e', 'dice{5g', 'dice{5m', 'dice{5o', 'dice{5q', 'dice{5s', 'dice{5t', 'dice{5u', 'dice{5w', 'dice{5y', 'dice{55', 'dice{57', 'dice{59', 'dice{5_','dice{ua', 'dice{uc', 'dice{ud', 'dice{uf', 'dice{ug', 'dice{ui', 'dice{uk', 'dice{ul', 'dice{um', 'dice{un', 'dice{uo', 'dice{up', 'dice{uq', 'dice{ur', 'dice{us', 'dice{ut', 'dice{uv', 'dice{uw', 'dice{ux', 'dice{uy', 'dice{uz', 'dice{u0', 'dice{u1', 'dice{u2', 'dice{u3', 'dice{u4', 'dice{u5', 'dice{u6', 'dice{u7', 'dice{u8', 'dice{u9', 'dice{u_']

for test_word in word_list:
    test_program(test_word)

stroka = input()

def tokenize(stroka):

    separators = '\t, \n,\\,;:!?()=[]{}"«»…–—|/'
    dig = "0123456789"
    result = []
    buffer = ''
    gen_res = []


    for i in range(len(stroka)):
        
        if stroka[i] == '.':
            if i == 0 or i == len(stroka):
                result.append(buffer)
                buffer = ''    
                continue

            elif (stroka[i-1] not in dig) or (stroka[i+1] not in dig):
                result.append(buffer)
                buffer = ''
                continue

        if stroka[i] in separators:
            result.append(buffer)
            buffer = ''
            continue
        
        buffer = buffer + stroka[i]

        if i == len(stroka) - 1:
            result.append(buffer)

    for i in range(len(result)):
        if result[i] != '':
            gen_res.append(result[i])

    return gen_res
    
print(tokenize(stroka))
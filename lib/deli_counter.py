def line(deli):
    if(len(deli)==0):
        print('The line is currently empty.')
    else:
        current_line = []; num = 1
        for person in deli:
            if(deli.index(person)==-1):
                current_line.append(f'{num}. {person}.')
            else:
                current_line.append(f'{num}. {person} ')
            num+=1
            new_current_line = ''.join(current_line)
        print(f'The line is currently: {new_current_line}')


def take_a_number(deli, person):
    deli.append(person)
    print(f'Welcome, {person}. You are number {deli.index(person)+1} in line.')
    
# katz_deli = []

# print(take_a_number(katz_deli, 'Ada'))
# print(take_a_number(katz_deli, 'Mike'))
# line(['Ada', 'Grace', 'Kent'])
# line([])
# line(["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"])
#def get_rainbow_color(color_number):
    #color_number_list = [1, 2, 3, 4, 5, 6, 7]
    #if type(color_number) is not int:
        #raise TypeError('Color number must be integer type')
    #if color_number not in color_number_list:
        #raise ValueError('Color number must be in range of integer from 1 to 7 ')

    #if color_number == 1:
        #return 'red'
    #if color_number == 2:
        #return 'orange'
    #if color_number == 3:
        #return 'yellow'
    #if color_number == 4:
        #return 'green'
    #if color_number == 5:
        #return 'blue'
    #if color_number == 6:
        #return 'indigo'
    #if color_number == 7:
        #return 'violet'


#color = get_rainbow_color('hi')
#print(color)


def colorize_text(color_number, text):
    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if type(color_number) is not int:
        raise TypeError('Parameter color number must be integer type')
    if color_number not in color_number_list:
        raise ValueError('Parameter color_number must be in range of integer from 1 to 7 ')
    if type(text) is not str:
        raise TypeError('Parameter text must be string type')

    if color_number == 1:
        print('red ' + text)
    if color_number == 2:
        print('orange ' + text)
    if color_number == 3:
        print('yellow ' + text)
    if color_number == 4:
        print('green ' + text)
    if color_number == 5:
        print('blue ' + text)
    if color_number == 6:
        print('indigo ' + text)
    if color_number == 7:
        print('violet ' + text)


colorize_text(4, 'True')
colorize_text(4, True)


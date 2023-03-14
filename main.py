import logic

if __name__ == '__main__':

    mat = logic.start_game()
    for i in range(4):
        print(mat[i][0], mat[i][1], mat[i][2], mat[i][3])
 
while(True):
 

    x = input("Press the command : ")

    if(x == 'W' or x == 'w'):

        mat, flag = logic.move_up(mat)
 
        status = logic.get_current_state(mat)
        print(status)
 

        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    elif(x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
 
    # to move left
    elif(x == 'A' or x == 'a'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
 
    # to move right
    elif(x == 'D' or x == 'd'):
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    else:
        print("Invalid Key Pressed")
	
    for i in range(4):
        print(mat[i][0], mat[i][1], mat[i][2], mat[i][3])
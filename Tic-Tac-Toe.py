#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Display a board


# In[32]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])


# In[ ]:


#Sample board


# In[40]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[41]:


#Assign X and O to players


# In[65]:


def player_input():
    marker=""
    while marker !="X" and marker!="O":
        marker=input("Choose X or O").upper()
    if marker=="X":
        return("X","O")
    else:
        return("O","X")
    


# In[66]:


player_1_marker,player_2_marker=player_input()


# In[67]:


player_1_marker


# In[68]:


player_2_marker


# In[49]:


#Place markers


# In[50]:


def place_marker(board,marker,position):
    board[position]=marker
    


# In[51]:


place_marker(test_board,"@",7)
display_board(test_board)


# In[ ]:


#CONDITIONS TO WIN THE GAME 


# In[63]:


def win_check(board,mark):
    return (board[7] ==board[8] ==board[9] == mark) or (board[4] ==board[5] ==board[6] == mark) or (board[1] ==board[2] ==board[3] == mark) or (board[7] ==board[4] ==board[1] == mark) or (board[8] ==board[5] == board[2] == mark) or (board[9] ==board[6] == board[3] == mark) or (board[7] ==board[5] == board[3] == mark) or (board[9] ==board[5] == board[1] == mark)

#WIN THE GAME

#ROWS #COLUMNS # 2 DIAGONAL


# In[64]:


display_board(test_board)
win_check(test_board,"X")


# In[ ]:


# tossup to start first


# In[69]:


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player_1"
    else:
        return "Player_2"


# In[77]:


def space_check(board,position):
    return board[position]==""
    


# In[78]:


space_check(test_board,1)


# In[85]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[86]:


def player_choice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check:
        position=int(input("Choose a position:(1-9)"))
    return position
    
    


# In[87]:


def replay():
    choice="Wrong"
    while choice not in ["Y","N"]:
        choice=input("Do you want to replay? (Y or N)")
    if choice=="Y":
        return True 
    else:
        return False
    


# In[88]:


#Using logic and connecting the loops


# In[ ]:


print("Welcome to Tic Tac Toe")
while True:
    
    #Game board
    game_board=[""]*10
    
    #Players choose their markers
    player_1_marker,player_2_marker=player_input()
    
    #Tossup to start first
    turn=choose_first()
    print(turn+"will"+"start"+"first")
    
    #Check if Players are ready or not?
    play_game=input("Are you ready to play? y or n?")
    if play_game=="y":
        game_on=True
    else:
        game_on=False
    
    #player_1 senario
    while game_on:
        if turn=="Player 1":
            
            display_board(game_board)
            
            position=player_choice(game_board)
            
            place_marker(game_board,player_1_marker,position)
            
            if win_check(game_board,player_1_marker):
                display_board(game_board)
                print("Player 1 has won!!")
                game_on=False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie Game!!")
                    break
                else:
                    turn="Player 2"
        #Player_2 senario
        else:
         
            display_board(game_board)
          
            position=player_choice(game_board)
         
            place_marker(game_board,player_2_marker,position)
          
            if win_check(game_board,player_2_marker):
                display_board(game_board)
                print("Player 2 has won!!")
                game_on=False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie Game!!")
                    game_on=False
                else:
                    turn="Player 1"
    #break out if players choose N 
    if not replay():
        break



# In[ ]:





# In[ ]:





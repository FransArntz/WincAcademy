# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Opdracht python strings
tekst_kop = 'In de EK finale 1988'
player_0 = 'Hans van Breukelen'
player_1 = 'Berry van Aerle'
player_2 = 'Frank Rijkaard'
player_3 = 'Ronald Koeman'
player_4 = 'Adri van Tiggelen'
player_5 = 'Gerald Vanenburg'
player_6 = 'Jan Wouters'
player_7 = 'Arnold Mühren'
player_8 = 'Erwin Koeman'
player_9 = 'Ruud Gullit'
player_10 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_9 +' '+ str(goal_0) +' '+ player_10 +' '+ str(goal_1)
score_0 = player_9 +' '+'scored in the' +' ' + str(goal_0) + 'nd minute' 
score_1 = player_10 +' '+'scored in the' +' ' + str(goal_1) + 'th minute'
report = score_0 + '\n' + score_1 
player = player_3 # player that played in the soccer match and store his name as a string in the variable player
first_name = player[player.find('Ronald'):6] # use slicing and the find-method (help) to isolate and store the player's first name
last_name_len = len(player[player.find('Koeman'):100]) # use find, slicing and len to isolate and store the length of their last name
name_short = first_name[0] + '.' + ' ' + (player[player.find('Koeman'):100]) # isolate and store the player's name in this format G. von Examplestein
chant = (first_name+'!'+' ')*(len(first_name)-1) + (first_name+'!') #chant: their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the last character of this string is not a space! 
good_chant = (chant[-1] !=' ') #good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=).
print (tekst_kop)
print (report)
print (first_name)
print (last_name_len)
print (name_short)
print (chant)
print (good_chant)

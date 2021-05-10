# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Opdracht python strings
# Correctie 1

player_9 = 'Ruud Gullit'
player_10 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_9 +' '+ str(goal_0) +', '+ player_10 +' '+ str(goal_1)
score_0 = player_9 +' scored in the ' + str(goal_0) + 'nd minute' 
score_1 = (f'{player_10} scored in the {str(goal_1)}th minute')
report = (f'{score_0} \n{score_1}') 
player = player_10 
first_name = player[0:player.find(' ')] 
last_name_len = len(player[player.find(' '):-1]) 
name_short = first_name[0] + '.' + (player[player.find(' '):100]) 
chant = (first_name+'!'+' ')*(len(first_name)-1) + (first_name+'!') 
good_chant = (chant[-1] !=' ') 

print (scorers)
print (report)
print (first_name)
print (last_name_len)
print (name_short)
print (chant)
print (good_chant)

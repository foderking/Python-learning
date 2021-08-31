subjects = ('Maths','Chemistry','Physics','English','Futher Maths')
Database = {'ope':[10,14,14,14013,24],'jamie':[13,14,14,14,24]}

for S in subjects:
    for score_ in Database['ope']:
        print( S + ' is ' + str(score_ ))
        break

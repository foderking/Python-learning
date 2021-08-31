import random
import os

os.chdir('C:\\users\\foderking\\downloads\\Test')
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



quizFile = open('capitalsquiz.txt', 'w')
answerFile = open('capitalsquiz_answers.txt', 'w')

quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
quizFile.write((' '*20) + 'STATE CAPITAL QUIZ' )
quizFile.write('\n\n')
answerFile.write('ANSWERS'.center(50) + '\n')
answerFile.write(''.center(50, '=') + '\n\n' )


states = list(capitals.keys())
caps = list(capitals.values())
random.shuffle(states)

for no_ in range(1, 36) :
    Q = states[0]
    ans = capitals[Q]

    quizFile.write('%s. What is the capital of %s?\n' % ( no_ , Q  ) )

    states.remove(Q)
    caps.remove(ans)

    rest = random.sample(caps, 3)
    opts = [ans] + rest
    random.shuffle(opts)

    for i in  range(4) :
        quizFile.write('    %s. %s\n' % ('ABCD'[i], opts[i]))
    quizFile.write('\n')
    answerFile.write('%s %s' % (str(no_).ljust(3, '.'), 'ABCD'[opts.index(ans)] ))
    answerFile.write('\n')

 
quizFile.close()
answerFile.close()

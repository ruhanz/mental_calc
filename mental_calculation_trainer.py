import random,datetime
def calculator():
    input('ready? ')
    now=datetime.datetime.now()
    wrong_counter, counter = 0,1
    while counter <=20:
        symbol = random.choice(['+','-'])
        if symbol == '/':
            n=int(random.random()*10)
            n2 = int(random.random()*10)
            if int(input(f'{n*n2} : {n} = ')) != n2:
                print(f'wrong, {n2}')
                wrong_counter += 1
        elif symbol == '+' or symbol == '-':
            n = random.randint(1,9 if symbol == '*' else 100)
            n2 = random.randint(1,100)
            if int(input(f'{n} {symbol} {n2} = ')) != eval(f'{n} {symbol} {n2}'):
                print(f'wrong, {eval(f'{n} {symbol} {n2}')}')
                wrong_counter+=1
        counter += 1
    av_time = (datetime.datetime.now() - now)/20
    m = int(av_time.seconds/60)
    print(f'Time for each question: {'' if not m else (str(m) + 'm')} {av_time.seconds}s {int(av_time.microseconds/1000)}ms')
    print(f'Accuracy: {round((20-wrong_counter)/20,4)*100}%')
while 1:
    calculator()

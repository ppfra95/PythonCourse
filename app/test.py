import requests, json, pprint, random, time, html

from os import system


play=True

def printQuestion(q):
    print(("Category:  "+str(q['results'][0]['category'])).center(80,"="))
    print(html.unescape(str(q['results'][0]['question']).center(80,"-")))
    answers=q['results'][0]['incorrect_answers']
    answers.append(q['results'][0]['correct_answer'])
    answers=random.sample(answers,k=4)

    return answers

def printAnswers(answers):
    n=0
    for x in answers:
        n+=1
        print(n,": ",html.unescape(x))


while play:
    r=""
    try:
        r=requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
    except:
        print("fail")
        play=False

    question = json.loads(r.text)
    #print(html.unescape(r.text))
    pprint.pprint(question)
    answers=printQuestion(question)

    ans=0
    e=0
    while e<3:
        printAnswers(answers)

        try:
            ans=int(input("Answer: "))
        except:
            print("This a not number")
            e+=1
            ans=0

        if ans!=0:
            if ans>4 or ans<0:
                print("This a not opcion")
                e+=1
            elif answers[ans-1]==question['results'][0]['correct_answer']:
                print("Correct Answer")
                break
            else:
                print("Incorrect Answer")
                break

        time.sleep(1)
        system("clear")

    e2=0
    while e<3 and e2<3:
        print("Do you play again? Y/N: ")
        ans2=""
        try:
            ans2=str(input("Answer: "))
        except:
            print("This a not opcion")
            e2+=1
            play=False

        if ans2 == "Y" or ans2 == "y":
            break
        elif ans2 == "N" or ans2 == "n":
            play=False
            break
        else:
            print("This a not opcion")
            e2+=1

        time.sleep(1)
        system("clear")

    if e>2 or e2>2:
        play=False

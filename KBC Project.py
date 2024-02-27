questions=[["Where was India’s first national Museum opened?","Delhi","Hyedrabad","Rajasthan","Mumbai","None",4],

["Which of the three banks will be merged with the other two to create India's tird largest bank? ","Punjab national bank","Indian bank","Bank of baroda","Dena bank","None",2],

["What is the name of the weak zone of the earth’s crust?","Seismic","Cosmic","Formic","Anemic","None",1],
[" In 2019, Which popular singer was awarded the Bharat Ratna award?","Lata mangeshkar","Asha bhosle","Bhupen hazarika","Manna dey","None",3],
 ["The world’s nation 5G mobile network was launched by which country?","japan","asia","malysia","south korea","none",4],
["Which language was used in making fb?","Python","Javascript","French","Php","None",4],
["The world’s nation 5G mobile network was launched by which country?","2015","2017","2019","2020","None",3],
["Vijay Singh (golf player) is from which country","Fiji","USA","Asia","UK","None",1],
["The green planet in the solar system is?","Mars","Uranus","Venus","Earth","None",2],
["What is the reason behind the Bats flying in the dark?","They produce high pitched sounds called ultrasonics","The light startles them","They have a perfect vision in the dark","None of the above","none",1],
["Which of these is the small-scale industry in India?","Jute industry","Paper industry","Textile industry","Handloom industry","none",4]
          ]
levels=[1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,1250000]
money=0
for i in range(0,len(questions)):
  question=questions[i]
  print(f"\n\nQuestion for Rs.{levels[i]}")
  print(f"Your question is:\n{question[0]}")
  print(f"a. {question[1]}                      c. {question[3]}")
  print(f"b. {question[2]}                      d. {question[4]}")
  reply=int(input("Enter your Answer 1-4:"))
  if(reply==question[-1]):
    print(f"Correct Answer\nYou have won{levels[i]}")
    if(i==4):
      money=10000
    elif(i==9):
      money=320000
    elif(i==11):
      money=1250000
  else:
    print("wrong answer")
    break
print(f"your price is{money}!!")
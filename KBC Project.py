import random
questions = [
    ["Where was India’s first national Museum opened?",
     ["Delhi", "Hyderabad", "Rajasthan", "Mumbai"], 0],

    ["Which of these banks was merged to create India's third largest bank?",
     ["Punjab National Bank", "Indian Bank", "Bank of Baroda", "Dena Bank"], 2],

    ["What is the weak zone of the earth’s crust called?",
     ["Seismic", "Cosmic", "Formic", "Anemic"], 0],

    ["In 2019, which singer received Bharat Ratna?",
     ["Lata Mangeshkar", "Asha Bhosle", "Bhupen Hazarika", "Manna Dey"], 2],

    ["Which country launched the world’s first 5G network?",
     ["Japan", "Asia", "Malaysia", "South Korea"], 3],

    ["Which language was initially used to build Facebook?",
     ["Python", "JavaScript", "French", "PHP"], 3],

    ["In which year was 5G first launched globally?",
     ["2015", "2017", "2019", "2020"], 2],

    ["Vijay Singh (golf player) is from which country?",
     ["Fiji", "USA", "Asia", "UK"], 0],

    ["The green planet in the solar system is?",
     ["Mars", "Uranus", "Venus", "Earth"], 1],

    ["Why can bats fly in the dark?",
     ["Ultrasonic sound navigation", "Light startles them",
      "Perfect night vision", "None"], 0],

    ["Which of these is a small-scale industry in India?",
     ["Jute industry", "Paper industry", "Textile industry", "Handloom industry"], 3]
]

levels = [1000, 2000, 5000, 10000, 20000,
          40000, 80000, 160000, 320000, 640000, 1250000]

checkpoints = {4: 10000, 9: 320000, 10: 1250000}


random.shuffle(questions)

money = 0

print("\n⭐ WELCOME TO KAUN BANEGA CROREPATI! ⭐")
print("----------------------------------------")

for i in range(len(questions)):
    q_text = questions[i][0]
    options = questions[i][1]
    correct_index = questions[i][2]

    
    option_list = list(enumerate(options))
    random.shuffle(option_list)

   
    new_correct_index = None
    for idx, (original_index, option_value) in enumerate(option_list):
        if original_index == correct_index:
            new_correct_index = idx + 1   # +1 because user sees 1-4
            break

    print(f"\n✅ Question for Rs. {levels[i]}")
    print(q_text)

   
    for num, (_, option_value) in enumerate(option_list, start=1):
        print(f"{num}. {option_value}")

    user_input = input("\nEnter your answer (1-4) or 'quit' to exit: ")

    if user_input.lower() == "quit":
        print("\nYou quit the game!")
        break

    if not user_input.isdigit():
        print("❌ Invalid input!")
        continue

    reply = int(user_input)

    if reply == new_correct_index:
        print("\n✅ Correct Answer!")
        money = levels[i]

        if i in checkpoints:
            money = checkpoints[i]
            print(f"🎯 Checkpoint reached! Guaranteed Rs. {money}")

    else:
        print("\n❌ Wrong Answer!")
        for cp in sorted(checkpoints.keys(), reverse=True):
            if i > cp:
                money = checkpoints[cp]
                break
        break

print(f"\n💰 Your final winning amount: Rs. {money}")
print("🎉 Thanks for playing KBC! 🎉")

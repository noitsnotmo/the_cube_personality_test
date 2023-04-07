
# This is a personality test program.



print("Welcome to The Cube personality test!")
name = input("What is your name? ")
print("Hello", name, "! Please answer the following questions with your initial gut reaction.")

# Question 1: The Field
field = input("Think of an open field. How big is this field? What is it filled with? What are the surroundings like? ")
print("Great. Let's move on.")

# Question 2: The Cube
cube = input("Think of a cube. How big is the cube? What is it made of and what is the surface like? What color is it? Where in the field is it? Is it transparent? ")
print("Next question.")

# Question 3: The Ladder
ladder = input("Think of a ladder. How long is this ladder and where is it located in your field? What's the distance between the ladder and the cube? ")
print("You're doing great!")

# Question 4: The Horse
horse = input("Think of a horse. What color is the horse? What is the horse doing and where is it in relation to your cube? ")
print("Almost done.")

# Question 5: The Flowers
flowers = input("Now, think of flowers. Where are the flowers in your field, and how many are there? ")
print("Just a few more.")

# Question 6: The Weather
weather = input("Think of what the weather in the field is like. Is it raining? Sunny? Is your field foggy? ")
print("One left!")

# Question 7: The Storm
storm = input("Think of a storm. What is the distance between the storm and the cube? Is it a big storm? It is just passing through? ")
print("That's the last question!")

# Results
print("Now that you have a clear picture of your field and everything in it, it's time to see what it says about who you are! ")

while True:
    results = input("Which do you want to learn about (field/cube/ladder/horse/flowers/weather/storm)? Type 'q' to quit. ").lower()
    if results == "field":
        print("The field represents your mind. Its size is the representation of your knowledge of the world, and how vast your personality is. The condition of the field (dry, grassy, or well-trimmed) is what your personality looks like at first glance.")
        print("If the field condition is: ")
        print("Dry and Dead: You are feeling pessimistic.")
        print("Grassy and Healthy: You are feeling optimistic.")
        print("Well-Trimmed: You are analytical and cautious.")
        print("You responded: ", field, ".")

    elif results == "cube":
        print("The cube represents you. The size of the cube is your ego. The surface of the cube represents what is visibly observable about your personality, or maybe it is what you want others to think about you. The texture of the cube (e.g. smooth, rough, bumpy, etc.) represents your nature.")
        print("If the cube is: ")
        print("Smooth: You are a gentle person who takes care not to hurt others or make them feel uncomfortable.")
        print("Rough: You are more straightforward. You tend to be honest in everything you say, no matter how it might affect the person you're talking to.")
        print("Bumpy or Spiky: You have a tendency to criticize others in an attempt to make them feel inferior to you.")

        print("The color of the cube is a more in-depth analysis of yourself. Each color can represent an emotion, or an entire personality altogether. However, these are the most common:")
        cube_color = input("What color is your cube (red/yellow/blue/violet/grey/black/white)? ").lower()
        if cube_color == "red":
            print("Red means you are physically active and enjoy rich sensory experiences.")
        elif cube_color == "yellow":
            print("Yellow means you are sociable and cherish your individuality.")
        elif cube_color == "blue":
            print("Blue means you are intelligent and respect others' ideals.")
        elif cube_color == "violet":
            print("Violet means you are intelligent and a bit of a perfectionist. You are also mysterious.")
        elif cube_color == "grey":
            print("Grey means you are self-confident, independent, and not easily rattled.")
        elif cube_color == "black":
            print("Black means you have a strong sense of individuality and independence, and you put a high value on alone time.")
        elif cube_color == "white":
            print("White means you are kind, independent, and self-reliant.")
        
        else:
            print("Please enter a valid color (red, yellow, blue, violet, grey, black, or white).")

        print("In some cases, the physical characteristics of the cube are unique:")
        print("Transparent: You tend to let others know how you feel on the inside. You are confident enough to show your inner thoughts, and you are deeply sincere. You know that you are good inside, and guess what--it shows! That's what most people see in you as well.")
        print("Water or Ice: You let external elements influence you completely. Your personality is sensitive to social pressure, relationships, and other environmental factors.")
        print("Hollow: You are primarily concerned with your outside appearance, with far less care for what's going on within. However, this does not mean that you have nothing to offer on the inside.")
        print("Metal or Rock: You have solid integrity. Your personality is so strong that it cannot be bent or influenced by any external force. You are dominant and consistent.")
        
        print("You responded: ", cube, ".")

    elif results == "ladder":
        print("The ladder represents two different aspects of your life—your goals and your friendships. First, let's look at what the ladder says about your goals.")
        print("If the ladder is:")
        print("Short: Your goals are realistic and simple.")
        print("Long: Your goals are more far-fetched and difficult to attain.")
        print("Near: You are putting maximum effort and focus into achieving your goals.")
        print("Far: Your aren't putting much thought or effort into achieving your goals.")
        print("Now, the location and material of your ladder can also tell you how close you are with your friends. You guessed it—the closer the ladder is to the cube and the stronger the ladder is, the better it is for your friendships!")
        print("Near: If your ladder is near the cube, you are very close with your friends. If it's actually leaning on the cube, it means your friends can lean on you for support.")
        print("Far: You have a hard time opening up to people and letting them get close to you.")
        print("Strong: The stronger the material (e.g. stone, metal, etc.), the stronger the bond!")
        print("Weak: A weak ladder indicates a weak bond between you and those around you.")
        print("You responded: ", ladder, ".")

    elif results == "horse":
        print("The horse represents your ideal partner. It could be playing, running around, or grazing right next to your cube or clear across the field.")
        print("If the horse is: ")
        print("Playing: Your ideal partner doesn't take life too seriously and or get bogged down by the little stuff.")
        print("Running: Your ideal partner will respect your space and give you the alone time that you crave.")
        print("Sleeping or Grazing: Your ideal partner is calm and fully committed to you.")
        print("Brown: You prize comfort and reliability above all else. Otherwise, you don't have a specific set of expectations for your partner.")
        print("Black: Your ideal partner is dominant, seductive, and sophisticated.")
        print("White: You value loyalty and trust more than anything else in a relationship.")
        print("NOTE: If your horse is a completely different color than the ones listed above (think Wizard of Oz), it means you value originality and independence in a partner. You want to be with someone who fascinates and challenges you.")
        print("One more factor to consider about the horse is its distance from the cube. If it's very near the cube, it indicates that you prefer relationships where you spend most of your time with your partner. If the horse is a bit further away from the cube, it indicates a need for a partner who will understand and accommodate your desire for alone time.")
        print("You responded: ", horse, ".")

    elif results == "flowers":
        print("The flowers represent your family and friends. The number of flowers reflects your popularity, and their location indicates how close you are with your social groups.")
        print("If the flowers are: ")
        print("Few: You are close with your family and have a small, tight-knit group of friends.")
        print("Everywhere: You're a social butterfly! With family and friends too numerous to count, you'll never be lonely.")
        print("You responded", flowers, ".")

    elif results == "weather":
        print("The weather in your field reflects your general outlook on life. There's a reason we have expressions like: When it rains, it pours!")
        print("If the weather is: ")
        print("Rainy: Rain symbolizes the problems in your life; the harder the rain, the bigger the problems.")
        print("Foggy: You feel uncertainty in life and may be struggling with your identity.")
        print("Windy: Though you tend to worry about future issues, you generally don't let them get you down for long.")
        print("Sunny: You are optimistic and carefree!")
        print("You responded: ", weather, ".")

    elif results == "storm":
        print("The strength and position of the storm reflect the stress you're feeling in life. As you probably guessed, the stronger the storm and the closer to the cube, the higher your stress level! If you imagined a storm raging right above your cube, it might be a good idea to work on reducing stress in your daily life.")
        print("If the storm is: ")
        print("Mild (Just Passing Through): While you aren't immune to stress, you know that all things must pass.")
        print("Strong (In the Eye of the Storm): When you stress, you go all in and have a very hard time pulling yourself out again.")
        print("In the Background: Any obstacles that might be causing you grief are not at the forefront of your mind. You are good at managing your anxiety.")
        print("Right Above Your Cube: You are deeply affected by stress and have a hard time seeing past it to get back to the bigger picture.")
        print("You responded: ", storm, ".")

    elif results == "q":
        break

    else:
        print("Please enter a valid answer.")

review = input("Did you get accurate results (yes/no)? ").lower()
if review == "yes":
    print("Great! I'm glad you enjoyed it!")
else:
    print("I'm sorry you didn't get accurate results! Personality tests are not fool-proof and this test was made for pure entertainment. Thanks for trying it out!")

print("Thank you for taking the test! I hope you enjoyed it!")
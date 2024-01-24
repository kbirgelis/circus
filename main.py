
#KRISTERS KEVINS BIRĢELIS

# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

pozicija1 = 0
pozicija2 = 0
turn = 0

print("Welcome to the circus game!")

choice = input("Are you ready to begin the game? (Y/N): ")

if choice == 'N': #Ja spēlētājs atbild ka nevēlas spēlēt, tad spēle tiek apstādināta.
  
  print("Goodbye!")

if choice == 'Y': #Ja spēlētājs vēlas spēlēt, tad spēle tiek uzsākta.

  print("Starting the game!")
  print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇")

import random

import time

while True:
     
     choice = input("Are you ready to roll (Y/N): ")

     result = (random.randint(1, 6))

     print("★★★ You rolled: " + (str(result)))

     pozicija1 = pozicija1 + result
     print("★ Your current point count is: " + (str(pozicija1)))
     time.sleep(0.5)
         
     print("It is the computers turn!")
     time.sleep(0.5)
     print("Rolling...")
     time.sleep(0.5)
        
     result = (random.randint(1, 6))

     print("✿✿✿The computer rolled: " + (str(result)))
     time.sleep(0.5)
     pozicija2 = pozicija2 + result
     print("✿ Computers current point count is:" + (str(pozicija2)))
     time.sleep(0.5)
     turn = turn + 1
     print("Turn count (out of 25 max): " + (str(turn)))
     print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")


     if pozicija1 == 18: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 - 11
           time.sleep(0.5)
           print("⬇⬇⬇You fell down the blue stairs at square 18!⬇⬇⬇")
           time.sleep(0.5)
           print("Your current position is 7!")

     if pozicija2 == 18: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija2 - 11
           time.sleep(0.5)
           print("⬇⬇⬇Computer fell down the blue stairs at square 18!⬇⬇⬇")
           time.sleep(0.5)
           print("Computer's current position is 7!")

     if pozicija1 == 15: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 + 9 
           time.sleep(0.5)
           print("⬆⬆⬆You took the stairs up to 24!⬆⬆⬆")
           time.sleep(0.5)
           print("Your current position is 24")

     if pozicija2 == 15: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija1 + 9
           time.sleep(0.5)
           print("⬆⬆⬆Computer took the stairs up to 24!⬆⬆⬆")
           time.sleep(0.5)
           print("Computer's current position is 24")

     if pozicija1 == 33: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 + 19
           time.sleep(0.5) #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.) 
           print("⬆⬆⬆You took the stairs up to 52!⬆⬆⬆")
           time.sleep(0.5)
           print("Your current position is 52!")

     if pozicija2 == 33: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija1 + 19
           time.sleep(0.5)
           print("⬆⬆⬆Computer took the stairs up to 52!⬆⬆⬆")
           time.sleep(0.5)
           print("Computer's current position os 52!")

     if pozicija1 == 39: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 + 9
           time.sleep(0.5)
           print("⬆⬆⬆You took the stairs up to 48!⬆⬆⬆")
           time.sleep(0.5)
           print("Your current position is 48!")

     if pozicija2 == 39: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija2 + 9 
           time.sleep(0.5)
           print("⬆⬆⬆Computer took the stairs up to 48!⬆⬆⬆")
           time.sleep(0.5)
           print("Computer's current position is 48!")

     if pozicija1 == 67: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 - 21
           time.sleep(0.5)
           print("⬇⬇⬇You took the stairs down to 46!⬇⬇⬇")
           time.sleep(0.5)
           print("Your current position is 46!")

     if pozicija2 == 67: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija2 - 21
           time.sleep(0.5)
           print("⬇⬇⬇Computer took the stairs down to 46!⬇⬇⬇")
           time.sleep(0.5)
           print("Computer's current position is 46!")

     if pozicija1 == 74: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1  - 11
           time.sleep(0,5)
           print("⬇⬇⬇You took the stairs down to 63!⬇⬇⬇")
           time.sleep(0.5)
           print("Your current position is 63!")

     if pozicija2 == 74: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija2 - 11
           time.sleep(0,5)
           print("⬇⬇⬇Computer took the stairs down to 63!⬇⬇⬇")
           time.sleep(0.5)
           print("Computer's current position is 63!")

     if pozicija1 == 80: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 - 11
           time.sleep(0,5)
           print("⬇⬇⬇You took the stairs down to 69!⬇⬇⬇")
           time.sleep(0.5)
           print("Your current position is 69!")

     if pozicija2 == 80: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija2 - 11
           time.sleep(0,5)
           print("⬇⬇⬇Computer took the stairs down to 69!⬇⬇⬇")
           time.sleep(0.5)
           print("Computer's current position is 69!")

     if pozicija1 == 87: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija1 = pozicija1 + 9
           time.sleep(0.5)
           print("⬆⬆⬆You took the stairs up to 96!⬆⬆⬆")
           time.sleep(0.5)
           print("⬆⬆⬆Your current position is 96!⬆⬆⬆")

     if pozicija2 == 87: #Ja pozicija sakrīt ar trepju sākumu (trigger pointu - zilajām trepēm augša, bet sarkanajām apakša.)
           pozicija2 = pozicija1 + 9
           time.sleep(0.5)
           print("⬆⬆⬆Computer took the stairs up to 96!⬆⬆⬆")
           time.sleep(0.5)
           print("Computer's current position is 96!")

     if pozicija1 >= 100: #Ja spēlētājs ir sasniedzis 100 laukumiņu, tad tiek printēta uzvara!
           print("You won!")

           pass

     if pozicija2 >= 100: #Ja dators ir sasniedzis 100 laukumiņu, tad tiek printēta uzvara!
           print("You lost! Good luck next time!")
           pass
    
     if turn == 25:
           print("Its a tie!")
           pass
        


        

  

        

         

           

    




        



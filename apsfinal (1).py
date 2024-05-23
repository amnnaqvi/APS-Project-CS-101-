# LAST EDIT: RAYYAN AT 9:03 4TH DEC.

import random #to generate random values, where necessary
import ast #to parse through strings and later evaluate them into a dictionary, list or tuple
import os #to interact with the operating system and manipulate the output visuals as required
import time #to incorporate real-time functions in the program

# art list is used to store stick figures for hangman
art = [""" 
                   --------
                   |      |
                   |   
                   |   
                   |    
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     
                   |     
                   |     
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |    
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |       \ 
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \ 
                   |
                   -
                                """,
       """
                   --------
                   |      |
                   |
                   |      O
                   |     \|/
                   |      |
                   |     / \ 
                   -
                                """,
       """
                   --------
                   |      |
                   |      O
                   |
                   |     \|/
                   |      |
                   |     / \ 
                   -
                                """
       ]

# the nested lists below store items relevant to a specific category, arranged in order of easy, medium and hard
movies_h=[['Titanic',
'Jurassic Park',
'The Lion King',
'Harry Potter',
'Avatar',
'The Avengers',
'The Shawshank Redemption',
'Star Wars',
'ET the Extra Terrestrial',
'Finding Nemo',
'The Dark Knight',
'Forrest Gump',
'Frozen',
'The Matrix',
'Pirates of the Caribbean',
'The Sound of Music',
'Jaws',
'Spider-Man',
'The Incredibles',
'Toy Story'], [
'Inception',
'The Grand Budapest Hotel',
'La La Land',
'Interstellar',
'The Departed',
'The Revenant',
'The Social Network',
'Slumdog Millionaire',
'Gladiator',
'Memento',
'The Princess Bride',
'A Beautiful Mind',
'The Sixth Sense',
'The Green Mile',
'American Beauty',
'Million Dollar Baby',
'The Pursuit of Happyness',
'The Truman Show',
'Shutter Island',
'The Prestige'], ['Oldboy',
'Rashomon',
'La Haine',
'A Clockwork Orange',
'Mulholland Drive',
"Pan's Labyrinth",
'City of God',
'The Seventh Seal',
'Breathless A bout de souffle',
'12 Angry Men',
'Stalker',
'Solaris',
'Metropolis',
'The Cabinet of Dr Caligari',
'Persona',
'Akira',
'Amelie',
'8 and a half',
'The 400 Blows Les Quatre Cents Coups',
'Ran']]
movies_b=[['Dilwale Dulhania Le Jayenge',
'Kabhi Khushi Kabhie Gham',
'3 Idiots',
'Sholay',
'Dil To Pagal Hai',
'Kuch Kuch Hota Hai',
'Dhoom',
'Queen',
'Jab Harry Met Sejal',
'Padmaavat',
'Baahubali',
'PK',
'Dangal',
'Chennai Express',
'Lagaan',
'Kabir Singh',
'Bajrangi Bhaijaan',
'Kabhi Alvida Naa Kehna',
'Hera Pheri',
'Andaz Apna Apna'], ['Rock On',
'Barfi',
'Dil Chahta Hai',
'Haider',
'Rang De Basanti',
'Wake Up Sid',
'Andhadhun',
'Talaash',
'Haathi Mere Saathi',
'Mughal e Azam',
'Devdas',
'Piku',
'Badhaai Ho',
'Kapoor & Sons',
'Chak De India',
'Zindagi Na Milegi Dobara',
'Padosan',
'Gangs of Wasseypur',
'Rocket Singh Salesman of the Year',
'Neerja'], ['Ship of Theseus',
'Ankhon Dekhi',
'The Lunchbox',
'Masaan',
'Drishyam',
'Court',
'Kahaani',
'Black Friday',
'Udaan',
'Monsoon Wedding',
'Gully Boy',
'Tumbbad',
'Titli',
'Harishchandrachi Factory',
'Paan Singh Tomar',
'Khosla Ka Ghosla',
'Newton',
'Aligarh',
'Lipstick Under My Burkha',
'Qissa']]
animals=[['Dog',
'Cat',
'Elephant',
'Lion',
'Tiger',
'Giraffe',
'Monkey',
'Horse',
'Dolphin',
'Penguin',
'Rabbit',
'Koala',
'Panda',
'Zebra',
'Kangaroo',
'Bear',
'Owl',
'Penguin',
'Turtle',
'Cheetah'], ['Chimpanzee',
'Polar Bear',
'Gorilla',
'Alligator',
'Ostrich',
'Hippopotamus',
'Rhinoceros',
'Red Panda',
'Koala',
'Komodo Dragon',
'Lemur',
'Peacock',
'Armadillo',
'Platypus',
'Sloth',
'Snow Leopard',
'Tapir',
'Wallaby',
'Chameleon',
'Dingo'], ['Quokka',
'Axolotl',
'Okapi',
'Fossa',
'Narwhal',
'Kakapo',
'Aye-Aye',
'Markhor',
'Tufted Puffin',
'Coelacanth',
'Saola',
'Thorny Devil',
'Quetzal',
'Nudibranch',
'Fennec Fox',
'Pangolin',
'Gerenuk',
'Serval',
'Mantis Shrimp',
'Maned Wolf']]
cities=[['London',
'Paris',
'Rome',
'Tokyo',
'Beijing',
'Moscow',
'New Delhi',
'Cairo',
'Berlin',
'Brasilia',
'Ottawa',
'Buenos Aires',
'Seoul',
'Bangkok',
'Ankara',
'Madrid',
'Canberra',
'Riyadh',
'Pretoria',
'Washington DC'], ['Stockholm',
'Warsaw',
'Lisbon',
'Dublin',
'Hanoi',
'Nairobi',
'Oslo',
'Tehran',
'Bogota',
'Budapest',
'Jakarta',
'Vienna',
'Prague',
'Manila',
'Helsinki',
'Accra',
'Bucharest',
'Warsaw',
'Zagreb',
'Kiev'], ['Ulaanbaatar',
'Bishkek',
'Windhoek',
'Vilnius',
'Quito',
'Rabat',
'Tbilisi',
'Naypyidaw',
'Asmara',
'Suva',
'Podgorica',
'Minsk',
'Dushanbe',
'Tashkent',
'Astana',
'Nouakchott',
'Bamako',
'Apia',
'Vaduz',
'Bissau']]
hu_faculty=[['Ishtiyaq Makda', 'Shama Dossa', 'Zahra Malkari', 'Rakhshaan Qazi', 'Shamsher Ali Seeiro', 'Anzar Khaliq', 'Maleeha Habib', 'Farhan Anwar', 'Nahrain Al-mousawi', 'Sarah Hasnain', 'Ahmed Ali Mustansir', 'Muneer Zafar', 'Abdul Samad', 'Areeba Aziz Rajput', 'Behzad Khosravi Noori', 'Omar Farooq Anjum', 'Qasim Pasta', 'Coline Ferrant', 'Syeda Shaheda Raza', 'Hussnain Qamar Shah', 'Abdullah Mirza', 'Behroz Mirza', 'Aatyka Fatima', 'Sana Rizwan Gondal', 'Noman Baig', 'Inamullah Nadeem', 'Mah Noor Jamil', 'Taha Munir', 'Tufail Camar Shaikh', 'Nighat Chaudhry', 'Mohammad Moeini Feizabadi', 'Muzammil Patel', 'Muhammad Umer Tariq', 'Aqdas Afzal', 'Maria Samad', 'Waqar Saleem', 'Owais Talaat', 'Mirza Muhammad Amir', 'Junaid Ahmed Memon', 'Hassan Furqan Khan', 'Isma Gul Hasan', 'Zain Saeed'], 
['Anum Asi', 'Mohamed Elsayed Orabil', 'Basit Memon', 'Zaineb Makati', 'Naila Pervaiz', 'Saad Umer Baig', 'Zainab Saleem', 'Hasan Habib', 'Ayaz Ul Hassan Khan', 'Aeyaz Jamil Kayani', 'Unaiza Ahsan', 'Shafayat Abrar', 'Bashrat Issa', 'Shah Jamal Alam', 'Yousuf Kerai', 'Zoha Tunio', 'Haniya Habib', 'Uswa Ali Memon', 'Saba Saeed', 'Neelma Bhatti', 'Musabbir Majeed', 'Farhan Khan', 'Faraz Iqbal', 'Christie Marie Lauder', 'Afzal Azim', 'Humaira Qureshi', 'Fayyaz Ali Bhojani', 'Rohama Malik', 'Muhammad Farhan', 'Aamir Hasan', 'Usman Salahuddin', 'Ahsen Ali', 'Aaron Mulvany', 'Nimra Farooq', 'Afzal Ahmed', 'Xiaoxi Zhang', 'Muhammad Nadeem', 'Mehwish Abid', 'Tariq Mumtaz', 'Muneera Batool', 'Daniyal Ahmed', 'Newal Osman'], 
['Najeeb Jan', 'Humaira Jamshed', 'Mehreen Odho', 'Tajreen Midhat', 'Sahaab Bader Sheikh', 'Muntazir Abidi', 'Mohammad Salman', 'Hussain Quintai Shah', 'Paul Woolridge', 'Ahmad Usman', 'Saaed Ur Rehman', 'Shahid Hamid', 'Hira Atif', 'Asma Larik', 'Naimat Zada', 'Rameez Ragheb', 'Muhammad Zulqurnain', 'Haleema Qamar', 'Nauman Naqvi', 'Ana Husain', 'Sajal Rana', 'Syed Muhammad Hur Rizvi', 'Haseeb Shaikh', 'Asad Ur Rehman', 'Muhammad Haris', 'Faisal Alvi', 'Nadia Nasir', 'Irfan Muhammad', 'Muhammad Aatir Khan', 'Haya Fatima Iqbal', 'Sumbul Usman Yousuf', 'Sarah Zaid', 'Mahreen Asif Zuberi', 'Muhammad Ashar', 'Muhammad Mobeen Movania', 'Hamza Bin Sajjad', 'Abdullah Zafar', 'Marcelo Lima', 'Tariq Kamal', 'Sameena Shah Zaman', 'Khan Asif', 'Syeda Khola Adnan Wasti']]
hu_locations=[['Circuits And Electronics Lab', 'Tapal Cafeteria', 'Baithak', 'Cafe 2 Go', 'Soorty Hall', 'Office Of Student Life', 'Nest Cafe', 'Dhabba', 'Gym', 'Yohsin Hall', 'Visualization And Graphics Lab', 'Physics Lab', 'HU Clinic', 'Piano Room', 'Adamjee Math Lab', 'Air Courtyard', 'Tariq Rafi Lecture Theatre', 'Amphitheatre', 'Digital Systems And Instrumentation Lab', 'Atrium'],
['Writing Centre', 'Water Courtyard', 'Chemistry Lab', 'Design Studio', 'Ecology Lab', 'Khwaja Mashooqullah Music Room', 'Faculty Pod', 'Student Wellbeing', 'Mehfil', 'Arif Habib Classroom', 'Playground', 'Student Lounge', 'Grito Juice Bar', 'Female Lounge', 'Courts', 'Wellness Courtyard', 'Amin Issa Tai Classroom', 'Library', 'Student Centre', 'Office Of Academic Performance'],
['Tidal Pod', 'Garden', 'Zen Garden', 'Ehsas Centre', 'Horizon', 'Nariman Kaikhushroo Irani Film Studio', 'Book Pod', 'Swimming Pool', 'Fire Courtyard', 'Projects Lab', 'Engineering Workshop', 'Multi Purpose Room', 'Information Commons', 'Registrar Office', 'Sky Dhabba', 'Earth Courtyard', 'Auditorium', 'Learn Courtyard', 'Office Of Career Services', 'Cassim Computing Lab', 'HU Dukaan', 'Linux And Networking Lab']]

game_dictionary={'Hollywood Movies':movies_h, 'Bollywood Movies':movies_b, 'Animals':animals, 'Cities':cities, 'HU Faculty':hu_faculty, 'HU locations': hu_locations} #utilizing dictionaries for anagram and hangman

# nested list which allows the program to display and manipulate the tictactoe board
ttt=[[' ', ' ', ' ', ' ', ' ', '¦', ' ', ' ', ' ', ' ' , ' ', '¦', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', '1', ' ', ' ', '¦', ' ', ' ', '2', ' ' , ' ', '¦', ' ', ' ', '3', ' ', ' '],
['_', '_', '_', '_', '_', '¦', '_', '_', '_', '_', '_', '¦', '_', '_', '_', '_', '_'],
[' ', ' ', ' ', ' ', ' ', '¦', ' ', ' ', ' ', ' ' , ' ', '¦', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', '4', ' ', ' ', '¦', ' ', ' ', '5', ' ' , ' ', '¦', ' ', ' ', '6', ' ', ' '],
['_', '_', '_', '_', '_', '¦', '_', '_', '_', '_', '_', '¦', '_', '_', '_', '_', '_'],
[' ', ' ', ' ', ' ', ' ', '¦', ' ', ' ', ' ', ' ' , ' ', '¦', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', '7', ' ', ' ', '¦', ' ', ' ', '8', ' ' , ' ', '¦', ' ', ' ', '9', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', '¦', ' ', ' ', ' ', ' ' , ' ', '¦', ' ', ' ', ' ', ' ', ' ']]             #nested lists to hold tictactoe grid

horizontalwin = [[(1, 2), (1, 8), (1, 14)], [(4, 2), (4,8), (4, 14)], [(7, 2), (7, 8), (7, 14)]]        #utilizing nested lists and tuples
verticalwin = [[(1, 2), (4, 2), (7, 2)], [(1, 8), (4, 8), (7, 8)], [(1, 14), (4, 14), (7, 14)]]
diagnolwin = [[(1, 2), (4, 8), (7, 14)], [(1, 14), (4, 8), (7, 2)]]
win_dict = {'hor': horizontalwin, 'ver': verticalwin, 'diag': diagnolwin}       #dictionary that holds coordinates for all possible wins
file_path = 'C://Users/rayya/OneDrive/Documents/Outlook Files/TTT_Dicts.txt'        #file path to follow for tictactoe when reading and/or writing file

def clear_console():        #function to clear console when playing two player anagram/hangman to hide input
    os.system('cls' if os.name == 'nt' else 'clear') #clear output screen, no matter what the OS is
def countdown():              #defining a function that displays fun messages for the user as the program loads
    openinglst = ["Calling Python back from its coffee break... ", "Wow, there's a lot of in bugs here...", "Encouraging the code gremlins to work their magic...",
                    "Sending motivational quotes to the Python code to boost its confidence...", "Offering the code bugs an all-you-can-eat buffet to speed up debugging...", "Asking the Python code nicely to please get its act together...", "Convincing the code hamsters that the faster they run, the sooner we're done...", "Playing soothing elevator music for the Python code—because even code needs a break!", "Deploying a team of code clowns to juggle the bits and bytes for optimal performance..."]
    seconds = 5
    while seconds > -1:
        if seconds == 5:
            print()
            print()             #extra lines to appear cleaner on the console
            print("Your game will begin shortly... ")
        elif seconds == 4:
            print()
            print("Loading up game...")
        elif seconds == 3:
            print()
            print("Debugging...")
        elif seconds == 2:
            print()
            print(openinglst[random.randint(0,8)]) #choosing a random statement from openinglst to avoid being repetitve
        elif seconds == 0:
            print()
            print("OK We're Ready! Let's Begin!")
        time.sleep(1)       #delay execution by one second for visual appeal
        seconds -= 1
    print()

def hangymany(secret, word, temp, attempts, art_index, out, correct):  #a helper function to take letters as input and display the art
        if " ___ " not in temp and attempts >= 0: # base case 1: checks if there are no missing letters and the user still has attempts
                print(art[8])
                print("Congratulations! You won!")
                return True
        elif " ___ " in temp and attempts <= 0: # base case 2: checks if there are missing letters to be guessed and the user is out of attempts
             print(art[9])
             print("You lost... The word was:", secret)
             return False
        else:
             print(art[art_index])  # print the relevant stick figure based on attempts left                       
             print(word) 
             print()
             guess = input("Enter a letter: ")    
             while len(guess) != 1 or guess == " ":             #only only allowing singular characters to be inputs, which are not empty space
                  guess = input("Please only enter a singular letter only: ")
             while guess.upper() in out or guess.lower() in out: #ensuring the letter hasn't already been guessed before
                guess = input("You have already guessed this letter. Please enter a new one: ")

            # using two if conditions to adjust for case-sensitivity and checking if the same letter appears multiple times in different casing
             if guess.upper() in secret:                    
                  for i in range(len(secret)):
                     if guess.upper() == secret[i]:
                          temp[i] = secret[i]
                          correct += 1
                  word = " ".join(temp).strip()             #temp is updated with correctly guessed letter in place of ' ___ '
        
             if guess.lower() in secret:
                  for i in range(len(secret)):
                     if guess.lower() == secret[i]:
                          temp[i] = secret[i]
                          correct += 1
                  word = " ".join(temp).strip()
        
             if guess.upper() not in secret and guess.lower() not in secret:        
                  art_index += 1
                  attempts -= 1
                  print("Incorrect! You have", attempts, "attempt(s) left... ")
        
             out += guess #storing the guessed letter in an empty string for reference if guessed again
        
             hangymany(secret, word, temp, attempts, art_index, out, correct)      #recursive call       
def hangman_categorized(x, n):      #function for categorized hangman n represents consecutive wins and x represents level 0 being easy and 2 being hard
    print()
    print('These are the available categories')
    print('Hollywood Movies: 1'+'\n'+'Bollywood Movies: 2'+'\n'+'Animals: 3'+'\n'+'Cities: 4'+'\n'+'HU Faculty: 5'+'\n'+'HU locations: 6')
    category=int(input('Enter the number corresponding to your category of choice: '))      #number of category
    while category not in range(1, 7):
         print("The chosen category does not exist! Select one of the predefined categories.")
         category=int(input('Enter the number corresponding to your category of choice: '))          #handles misnomers
    if category==1:
        category1='Hollywood Movies'
    elif category==2:
        category1='Bollywood Movies'
    elif category==3:
        category1='Animals'
    elif category==4:
        category1='Cities'
    elif category==6:
        category1='HU locations'
    elif category==5:
        category1='HU Faculty'
    secret = game_dictionary[category1][x][random.randint(0, len(movies_h[x])-1)]      #choosing a random word (as per the difficulty level) from the chosen category
    temp = []                       #to hold and create hangman spaces
    for i in range(len(secret)):
            if secret[i] == " ":
                    temp.append("   ")          #is creating the hangman dashed spaces 
            else:
                    temp.append(" ___ ")        
                    
    if hangymany(secret, " ".join(temp).strip() , temp, 7, 0, "", 0) == True:       #initialising with values which will then be updated during recursion
        n=n+1
        if n==5 and x==0:
            print("These words seem too easy for you. Let's level up!")     #leveling up to medium
            hangman_categorized(1, 0) 
        elif n==3 and x==1:
            print("These words seem too easy for you. Let's level up!")     #leveling up to hard
            hangman_categorized(2, 0) 
    else:
        n=0
    if n>=8 and x==2:           #ends game if several consecutive wins in hard
        print('Game Over')
        return
    hangman_categorized(0, 0)   #recursive call unchanged if no wins
def hangman_randomized(x, n):
    category1=random.choice(list(game_dictionary.keys()))       #selects a random category from the dictionary
    secret = game_dictionary[category1][x][random.randint(0, len(movies_h[x])-1)]       #it then selects a random word from that category 
    temp = []                       #remaining function follows the exact same logic as categorized
    for i in range(len(secret)):                
            if secret[i] == " ":
                    temp.append("   ")
            else:
                    temp.append(" ___ ")
                    
    if hangymany(secret, " ".join(temp).strip() , temp, 7, 0, "", 0) == True:
        n=n+1
        if n==5 and x==0:
            print("These words seem too easy for you. Let's level up!")
            hangman_randomized(1, 0) 
        elif n==3 and x==1:
            print("These words seem too easy for you. Let's level up!")
            hangman_randomized(2, 0) 
    else:
        n=0
    if n>=8 and x==2:
        print('Game Over')
        return
    hangman_randomized(0, 0)
def hangman_twoplayer():
    secret = input("Player 1, please enter the secret word you'd like Player 2 to guess: ")
    clear_console() #clear screen to hide secret input
    temp = []
    for i in range(len(secret)):
            if secret[i] == " ":
                    temp.append("   ")
            else:
                    temp.append(" ___ ")
    
    hangymany(secret, " ".join(temp).strip() , temp, 7, 0, "", 0)
    print()
    
    turn=input('Do you want to play again? ').upper()
    while turn!='YES' and turn!='NO':
        print('Invalid response! Answer with yes or no')
        turn=input('Do you want to play again? ').upper()
    print()
    if turn =='YES':
        hangman_twoplayer()
    elif turn == 'NO':
        print('Game Over...')
        print()
        return 

def iswin(icon): #checks if the icon (X or O) has won tictactoe
    for v in win_dict.values():
        for i in v:
            if ttt[i[0][0]][i[0][1]] == icon and ttt[i[1][0]][i[1][1]] == icon and ttt[i[2][0]][i[2][1]] == icon:
                return True
    return False
def tictactoe_onePlay():
    attempts = 0 #ensuring "Draw" is displayed if necessary
    used = [] #to check if the loci is being used already
    
    for i in range(len(ttt)):
        for j in range(len(ttt[i])):
            print(ttt[i][j], end='') #printing the tictactoe board
        print()
        
    print()   
    icon = input('Would like to play as X or O? ').upper()
    while icon!='X' and icon!='O':
        icon=input('You can only play as either x or o. Please try again: ').upper()
        
    if icon == "X": #icon is what the user will play as, compicon becomes the computer's icon
        compicon = "O"
    else:
        compicon = "X"
        
    while attempts < 9: #to terminate in case of a draw
        
        if attempts%2 == 0: #to alternate between user and computer's moves
            print()
            loci = input('Select which box u want your icon to be placed: ')
            
            try:                                #exception handling to ensure only numbers are added
                while not 1 <= int(loci) <= 9:
                    loci = input('Please select a valid number from the grid above: ') 
            except:
                loci = input("Please only enter a number: ")
                
            while loci in used: 
                loci = input("This region has already been chosen, please select a different region: ")
            print()
            print()
            print("Your Move:") #differentiates between user and computer moves
            print()
            used.append(loci)            
            for i in range(len(ttt)):
                for j in range(len(ttt[i])):
                    if ttt[i][j]==loci:
                        ttt[i][j]=icon
                    print(ttt[i][j], end='')
                print()
                
            if iswin(icon): #if user has won, display congrats and terminate
                print()
                return "Congratulations! You Won!"
            attempts += 1
        
        else:
            temp = []
            myfile = open(file_path, "r") #reading a file to check where computer should make its move
            line = myfile.readline().strip() #reading first line
            while line != "":                   #read until end of file
                lst = ast.literal_eval(line)    #convert string statment into appropriate data type (list)
                if lst[0] != loci:
                    line = myfile.readline().strip() #read next line until user's loci is found in list
                else:
                    target = max(lst[1].values()) #go to the dictionary stored alongside loci numbers and find the maximum of move frequencies
                    for k, v in lst[1].items():
                        if v == target:
                            temp.append(k) #store all possible moves the computer should make, based on statistics from human players
                    break
            myfile.close()
            
            if len(temp) > 1: 
                for n in temp:  #iterating through temp and picking the first one that isnt in used
                    if n not in used:
                        loci = n
                        break
            else:
                loci = temp[0]    #it will make a move in any box that is empty if the loci in temp is already occupied
                index = 1
                while loci in used:
                    loci = str(index)
                    index += 1
            print()
            print()
            print("Computer's Move:", compicon, "at", loci) #displays where the computer has made a move to avoid confusion
            print()
            used.append(loci)
            for i in range(len(ttt)):
                for j in range(len(ttt[i])):
                    if ttt[i][j] == loci:
                        ttt[i][j] = compicon
                    print(ttt[i][j], end='')
                print()

            if iswin(compicon): #if the computer won, display a losing message to user and terminate
                print()
                return "You lost! Better luck next time..."
            attempts += 1
    print()
    return "Draw" #if no win or loss was made, then the game must be a draw
def ttt_win(ttt, p1, p2):   #helper for two player tictactoe, checking for who won 
    for i in win_dict.values():     #checking through the dictionary with predefined indexes
        for v in i:
            if ttt[v[0][0]][v[0][1]] == ttt[v[1][0]][v[1][1]] == ttt[v[2][0]][v[2][1]] == p1:   
                return p1
            elif ttt[v[0][0]][v[0][1]] == ttt[v[1][0]][v[1][1]] == ttt[v[2][0]][v[2][1]] == p2:
                return p2
    return 'no wins'
def tictactoe_twoPlay():
    used = []       #to store the loci where a player has already made a move and prevent another move there 
    temp = []       #to store the data from read file so it can be updated
    player1 = input('Player 1, please enter your name: ').capitalize()
    player2 = input('Player 2, please enter your name: ').capitalize()
    print()
    print('This is your grid, each number represents a loci for a turn.')
    print()
    for row in ttt:
        print("".join(row))   #printing the grid the first time
    print()
    p1=input(player1+', '+'enter what you want to play as: ').upper()
    while p1!='X' and p1!='O':                  #ensuring players only play as x or o
        p1=input('You can only play as either x or o. Choose what you want to play as:').upper()
    if p1=='X':
        p2='O'                              #assigning player 2 the other possible icon
    elif p1=='O':
        p2='X'
    print(player2+', you will play as '+p2)
    for i in range(9):          #looping 9 times because of 9 turns 
        print()                         #extra line again so it looks better on console
        loc1 = input(player1+', enter your loci: ')
        while (not loc1.isdigit() or (int(loc1)>9 or int(loc1)<1)) or loc1 in used: #ensuring players enter only a number in range and one that isnt occupied
            loc1=input('Invalid loci, enter loci again: ')
            print()
        if len(used) >= 1:          #checking if a move was made before 
            with open(file_path, 'r') as myfile:            #reading file and appending to temp 
                line = myfile.readline().strip()
                while line!='':
                    lst = ast.literal_eval(line)
                    temp.append(lst)
                    line = myfile.readline().strip()
            myfile.close()
            with open(file_path, 'w') as myfile:        #file is truncated and then temp's lists are manipulated
                for a in temp:
                    if used[-1] in a:
                        a[1][loc1] += 1
                    myfile.write(str(a)+'\n')       #storing frequncies of moves after a certain move to refer to during one player
            myfile.close()
            temp = []
        used.append(loc1)           #appending used loci to used so it isnt used again
        print()
        for k in range(len(ttt)):
            for j in range(len(ttt[k])):
                if ttt[k][j]==loc1:
                    ttt[k][j]=p1
                print(ttt[k][j], end='')        #printing grid after turn
            print()
        if ttt_win(ttt, p1, p2) == p1:          #checking for win
            print()
            print('Congratulations', player1+',', 'you won!', 'Better luck next time', player2)
            break
        if len(used) == 9:          #checking for a draw before second turn so as to prevent asking for an extra input
            print()
            print("It's a draw! Play again.")
            break
        print()
        loc2 = input(player2+', enter your loci: ')
        while (not loc2.isdigit() or (int(loc2)>9 or int(loc2)<1)) or loc2 in used:
            loc2=input('Invalid loci, enter loci again: ')
            print()
        if len(used) >= 1:
            with open(file_path, 'r', errors = 'ignore') as myfile:
                line = myfile.readline().strip()
                while line!='':
                    lst = ast.literal_eval(line)
                    temp.append(lst)
                    line = myfile.readline().strip()
            myfile.close()
            with open(file_path, 'w', errors = 'ignore') as myfile:
                for a in temp:
                    if used[-1] in a:
                        a[1][loc2] += 1
                    myfile.write(str(a)+'\n')
            myfile.close()
            temp = []
        used.append(loc2)
        print()
        for k in range(len(ttt)):
            for j in range(len(ttt[k])):        #utilizing nested loops
                if ttt[k][j]==loc2:
                    ttt[k][j]=p2
                print(ttt[k][j], end='')
            print()
        if ttt_win(ttt, p1, p2) == p2:
            print()
            print('Congratulations', player2+',', 'you won!', 'Better luck next time', player1)
            break

def anagram_checker(realstring, attempts):      #function to check if anagram is guessed correctly
    guess = input('Enter your guess: ').upper() 
    if guess == realstring.upper():
        print('Congratulations! You guessed the word correctly with', attempts-1, 'attempt(s) remaining')
        return True
    elif attempts==1 and guess!=realstring.upper():
        print('Sorry, you lost! You were not able to guess the word correctly. The correct word was', realstring.upper(), '.')
    else:
        print("That's not correct. Try again! You have", attempts-1, "attempt(s) remaining")
        anagram_checker(realstring, attempts-1)     #utilizing recursions
def anagram_categorized(x, n):      #function for when player chooses to play anagram by category
    anagram = ''    #initializing anagram string
    print()
    print('These are the available categories')
    print()
    print('Hollywood Movies: 1'+'\n'+'Bollywood Movies: 2'+'\n'+'Animals: 3'+'\n'+'Cities: 4'+'\n'+'HU Faculty: 5'+'\n'+'HU locations: 6')
    print()
    category=int(input('Enter the number corresponding to your category of choice: '))
    while category not in range(1, 7):      #check to ensure category exists
         print("The chosen category does not exist! Select one of the predefined categories.")
         category=int(input('Enter the number corresponding to your category of choice: '))
    if category==1:
        category1='Hollywood Movies'
    elif category==2:
        category1='Bollywood Movies'
    elif category==3:
        category1='Animals'
    elif category==4:
        category1='Cities'
    elif category==6:
        category1='HU locations'
    elif category==5:
        category1='HU Faculty'
    realstring=game_dictionary[category1][x][random.randint(0, len(movies_h[x])-1)]     #choosing random word from category
    reallist=realstring.split()         #converting string to list to shuffle better
    for i in reallist:          #shuffling each word so as to not shuffle spaces
        char_list = list(i)
        random.shuffle(char_list)
        temp = ''.join(char_list)
        anagram = anagram + ' ' + temp
    anagram = anagram.strip()
    print()
    attempts=int(input('Enter attempts between 1 and 4: '))
    while attempts>4 or attempts<1:         #restricting attempts
            print('Invalid number of attempts')
            attempts=int(input('Enter attempts between 1 and 4: '))
    print()
    print(anagram)
    print()
    print('Now make your guess!')
    if anagram_checker(realstring, attempts) == True:
        n=n+1       #keeping track of consecutive wins
        if n==5 and x==0:
            print()
            print("These words seem too easy for you. Let's level up!")
            anagram_categorized(1, 0)   #x is 1, representing medium level
        elif n==3 and x==1:
            print()
            print("These words seem too easy for you. Let's level up!")
            anagram_categorized(2, 0)   #x is 2, representing hard level
    else:
        n=0
    if n>=8 and x==2:           #so the game does not run infinitely and ends if u get 8 consecutive from hard correct
        print()
        print('Game Over')
        print()
        return
    anagram_categorized(0, n)       #function is recursive, depending on condition it makes a different call
def anagram_twoplayer():
    anagram=''
    print()
    realstring=input('Please enter the word, name, or sentece you want scrambled for player 2 to guess: ')
    clear_console() #clear screen to hide secret input
    reallist=realstring.split()
    for i in reallist:
        char_list = list(i)
        random.shuffle(char_list)
        temp = ''.join(char_list)
        anagram = anagram + ' ' + temp
    anagram = anagram.strip()
    print()
    attempts=int(input('Enter the number of attempts you want to allow player 2 to guess: '))
    print()
    print("Now it's player 2's turn")
    print(anagram)
    print()
    print('Now make your guess!')
    anagram_checker(realstring, attempts)
    print()
    turn=input('Do you want to play again? ').upper()
    while turn!='YES' and turn!='NO':
        print('Invalid response! Answer with yes or no')
        turn=input('Do you want to play again? ').upper()
    print()
    if turn =='YES':
        anagram_twoplayer()
    elif turn == 'NO':
        print('Game Over')
        return 
def anagram_randomized(x, n, a):        #a is for consistency, it allows for the lets try again statement to be printed when any other turn after 1st
    anagram=''
    category1=random.choice(list(game_dictionary.keys()))
    realstring=game_dictionary[category1][x][random.randint(0, len(movies_h[x])-1)]
    reallist=realstring.split()
    for i in reallist:
        char_list = list(i)
        random.shuffle(char_list)
        temp = ''.join(char_list)
        anagram = anagram + ' ' + temp
    anagram = anagram.strip()
    if a>0: 
        print()
        print("Let's try another word!")
    print()
    attempts=int(input('Enter attempts between 1 and 4: '))
    while attempts>4 or attempts<1:
            print('Invalid number of attempts')
            attempts=int(input('Enter attempts between 1 and 4: '))
    print()
    print(anagram)
    print()
    print('Now make your guess!')
    a+=1
    if anagram_checker(realstring, attempts) == True:
        n=n+1
        if n==5 and x==0:
            print()
            print("These words seem too easy for you. Let's level up!")
            anagram_randomized(1, 0, a) 
        elif n==3 and x==1:
            print()
            print("These words seem too easy for you. Let's level up!")
            anagram_randomized(2, 0, a) 
    else:
        n=0
    if n>=8 and x==2:
        print()
        print('Game Over')
        print()
        return
    anagram_randomized(0, n, a)

# MAIN PROGRAM

print()
print('Hello World...')
print('Do you want to play ANAGRAM SOLVER? Maybe HANGMAN? Or perhaps TICTACTOE?')
print()
game=input('Choose the game you would like to play or enter "random": ').upper() #initiating the game. Random picks any game for you

while game != 'ANAGRAM SOLVER' and game != 'HANGMAN' and game != 'TICTACTOE' and game != 'RANDOM':
    game = input('Game does not exist! Enter one of the existing games: ')          #handles any misnomers
if game == 'RANDOM':
    gamesR = ['ANAGRAM SOLVER', 'HANGMAN', 'TICTACTOE']
    game = gamesR[random.randint(0, len(gamesR)-1)]     #picks a random game from list 
if game == 'ANAGRAM SOLVER':
    band=input('Do you want to play by yourself or with a partner? Enter 1 for single player and 2 for two player: ')
    while not band.isdigit() or (int(band)>2 or int(band)<1):
        band=input('Invalid input! You can only choose 1 or 2. Enter again: ')  #ensures only taking 1 or 2 as input 
    if band =='1':
        types=input('Do you want to play by category or randomized: ').upper()
        while types!='RANDOMIZED' and types!='CATEGORY':
            print('That was an invalid choice. Try again!')
            types=input('Do you want to play by category or randomized: ').upper()          #handling misnomers
            print()
        if types=='CATEGORY':
            countdown()
            anagram_categorized(0, 0)           #initiates function call with 0s for easy level
        elif types=='RANDOMIZED':
            print()
            print('A random word or name from any category will now be presented!')
            countdown()
            anagram_randomized(0, 0, 0)         #initiates function call with 0s for easy level
    elif band =='2':
        countdown()
        anagram_twoplayer()         #calling twoplayer
elif game == 'HANGMAN':
    band=input('Do you want to play by yourself or with a partner? Enter 1 for single player and 2 for two player: ')
    while not band.isdigit() or (int(band)>2 or int(band)<1):
        band=input('Invalid input! You can only choose 1 or 2. Enter again: ') 
    if band =='1':
        types = input('Do you want to play by category or randomized: ').upper()
        while types!='RANDOMIZED' and types!='CATEGORY':
            print('That was an invalid choice. Try again!')
            types=input('Do you want to play by category or randomized: ').upper()
            print()
        if types =='CATEGORY':
            countdown()
            hangman_categorized(0, 0)
        elif types =='RANDOMIZED':
            print()
            print('A random word or name from any category will now be presented!')
            countdown()
            hangman_randomized(0, 0)
    else:
        countdown()
        hangman_twoplayer()
elif game =='TICTACTOE':
    band = input('Do you want to play by yourself or with a partner? Enter 1 for single player and 2 for two player: ')
    while not band.isdigit() or (int(band)>2 or int(band)<1):
        band = input('Invalid input! You can only choose 1 or 2. Enter again: ')
    if band == '1':
        countdown()
        print(tictactoe_onePlay())
    elif band == '2':
        countdown()
        tictactoe_twoPlay()    
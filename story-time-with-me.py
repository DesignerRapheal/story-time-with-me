# Personalized adventure story generator

# Import the required libraries
from colorama import init, Fore, Style

# Initialize colorama
init()

# Print the title and description of the program
print(Fore.BLUE + '====Your Adventure Simulator====' + Style.RESET_ALL)
print('You\'ll be asked a bunch of questions then\nthen we\'ll make you up an amazing story\nwith you has the star')
print()

# Prompt the user for their name, their worst enemy's name, and their superpower
name = input('What is your name? ')
enemy = input('Who is your worst enemy? ')
superpower = input('What is your superpower? ')
print()

# Print the story's introduction and the conflict
print('Our story begins as our hero approaches a castle...')
print(f'Suddenly, a bolt of lightning strikes the ground at the feet of {name} 🎇!')
print(Fore.GREEN + f'"Our final battle begins!"' + Style.RESET_ALL + f' shouts the evil {enemy}, clearly missing the fact that {name} has the power of ' + Fore.YELLOW + f'{superpower}' + Style.RESET_ALL + f' which means they will win quite easily.')


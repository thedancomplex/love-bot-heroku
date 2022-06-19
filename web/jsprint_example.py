from jsConsole import *
#### And now you can use classes like document, window, Math or console from Python!

console.log('jsConsole is ready!')
'jsConsole is ready!'

window.open('https://love-bot.xyz', '_self')
# Opens google.com on the browser #

def hello():
    print('Hello')


    document.getElementsByClassName('RNNXgb')[0].addEventListener('click', hello) ### Adding an event listener to the search bar from google.com which executes hello() when clicked.

    window.kill() # Needed to kill the browser (for it not to stay in the background even with Python quited)

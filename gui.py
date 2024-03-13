import tkinter as tk
from subprocess import Popen, PIPE

def bet_size():
    # Define the command to change directory and then execute the script
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/bet_size && bash test.sh"
    
    # Execute the command in a bash shell, ensuring the correct working directory
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    
    # Optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def stack_decision():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/stack_decision && bash test.sh"

    # Execute the command in a bash shell, ensuring the correct working directory
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
            
    # Optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def pot():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/pot && bash test.sh"

    # execute the command in a bash shell, ensuring the correct working directory
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def dealer():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/dealer && bash test.sh"

    # execute the command in a bash shell, ensuring the correct working directory
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())





app = tk.Tk()
app.title('Poker Game Tracker')

run_button = tk.Button(app, text='Bet Size', command=bet_size)
run_button.pack(pady=20)

run_button = tk.Button(app, text='Stack_decision', command=stack_decision)
run_button.pack(pady=20)

run_button = tk.Button(app, text='Pot', command=pot)
run_button.pack(pady=20)

run_button = tk.Button(app, text='Dealer', command=dealer)
run_button.pack(pady=20)





app.mainloop()

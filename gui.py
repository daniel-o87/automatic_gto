import tkinter as tk
import subprocess
def bet_size():
    # Define the command to change directory and then execute the script
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/bet_size && bash test.sh"
    
    # Execute the command in a bash shell, ensuring the correct working directory
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    # Optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


def stack_decision():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/stack_decision && bash test.sh"

    # Execute the command in a bash shell, ensuring the correct working directory
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
            
    # Optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def pot():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/pot && bash test.sh"

    # execute the command in a bash shell, ensuring the correct working directory
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def dealer():
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/dealer && bash test.sh"

    # execute the command in a bash shell, ensuring the correct working directory
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())


ml_frame = None

def add_ml_buttons():
    global ml_frame

    # Check if ml_frame exists and is mapped (displayed)
    if ml_frame is not None and ml_frame.winfo_ismapped():
        # If ml_frame is visible, hide it
        ml_frame.pack_forget()
        # You might want to also destroy the frame or set ml_frame to None depending on your needs
        # ml_frame.destroy()
        # ml_frame = None
    else:
        # Create ml_frame since it doesn't exist or isn't visible
        ml_frame = tk.Frame(app)
        ml_frame.pack(pady=20)

        # Define commands for new buttons
        def players_command():
            command = "cd /home/do/Desktop/fun_testing/automatic_gto/ml_cards && bash players.sh"

            # execute the command in a bash shell, ensuring the correct working directory
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # optionally, print stdout and stderr to debug
            print(stdout.decode())
            if stderr:
                print(stderr.decode())
        def flop_command():
            command = "cd /home/do/Desktop/fun_testing/automatic_gto/ml_cards && bash flop.sh"

            # execute the command in a bash shell, ensuring the correct working directory
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # optionally, print stdout and stderr to debug
            print(stdout.decode())
            if stderr:
                print(stderr.decode())
        def turn_command():
            command = "cd /home/do/Desktop/fun_testing/automatic_gto/ml_cards && bash turn.sh"

            # execute the command in a bash shell, ensuring the correct working directory
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # optionally, print stdout and stderr to debug
            print(stdout.decode())
            if stderr:
                print(stderr.decode())
        def river_command():
            command = "cd /home/do/Desktop/fun_testing/automatic_gto/ml_cards && bash river.sh"

            # execute the command in a bash shell, ensuring the correct working directory
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # optionally, print stdout and stderr to debug
            print(stdout.decode())
            if stderr:
                print(stderr.decode())

        # Create and pack buttons in the frame
        tk.Button(ml_frame, text='Players', command=players_command).pack(side=tk.LEFT)
        tk.Button(ml_frame, text='Flop', command=flop_command).pack(side=tk.LEFT)
        tk.Button(ml_frame, text='Turn', command=turn_command).pack(side=tk.LEFT)
        tk.Button(ml_frame, text='River', command=river_command).pack(side=tk.LEFT)


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

run_button = tk.Button(app, text="Who has cards", command = add_ml_buttons)
run_button.pack(pady=20)





app.mainloop()

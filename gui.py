import tkinter as tk
from subprocess import Popen, PIPE

def run_script():
    # Define the command to change directory and then execute the script
    command = "cd /home/do/Desktop/fun_testing/automatic_gto/bet_size && bash test.sh"
    
    # Execute the command in a bash shell, ensuring the correct working directory
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    
    # Optionally, print stdout and stderr to debug
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

app = tk.Tk()
app.title('Poker Game Tracker')

run_button = tk.Button(app, text='Run Script', command=run_script)
run_button.pack(pady=20)

app.mainloop()

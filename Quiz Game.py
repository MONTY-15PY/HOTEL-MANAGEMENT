import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Display Box")
root.geometry("1200x600")  # Set the window size to 1200x600 pixels

# Create a frame to hold the questions and answers
frame = tk.Frame(root, bg="d:\Screenshot 2024-12-30 021151.jpg")
frame.pack(pads=50)

# Create a label to display the text
label = tk.Label(frame, text="Welcome to My Quiz Game", font=("Arial", 24), bg="#FFC0CB")
label.grid(row=0, column=0, columns=4, padx=20, pady=20)

# Create a frame to hold the questions and answers
question_frame = tk.Frame(frame, bg="#FFC0CB")
question_frame.grid(row=1, column=0, columns=2, pads=20,)

# Create a frame to hold the answers
answer_frame = tk.Frame(frame, bg="#FFC0CB")
answer_frame.grid(row=1, column=2, columns=2, pady =20, pad=20)

# Create a label and entry for each question
questions = ["Full Form Of GPU", "Full Form Of CPU", "Full Form Of PC", "Full Form Of UI"]
answers = ["Graphics Processing Unit", "Central Processing Unit", "Personal Computer", "User Interface"]
entries = []
for i, (question, answer) in enumerate(zip(questions, answers)):
    label = tk.Label(question_frame, text=question, font=("Arial", 18), bg="#FFC0CB", wraplength=400)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entry = tk.Entry(answer_frame, font=("Arial", 18), bg="#FFC0CB", width=50)
    entry.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entries.append(entry)

# Function to check answers and show score
def check_answers():
    score = 0
    for i, entry in enumerate(entries):
        user_answer = entry.get().lower()
        correct_answer = answers[i].lower()
        if user_answer == correct_answer:
            score += 1
        else:
            print(f"Wrong spelling: {user_answer} should be {correct_answer}")
    messagebox.showinfo("Score", f"Your score is {score} out of {len(questions)}")

# Create a button to submit the answers
button = tk.Button(frame, text="Submit", command=check_answers, bg="#FF69B4", fg="#FFFFFF")
button.grid(row=5, column=0, columnspan=4, padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()
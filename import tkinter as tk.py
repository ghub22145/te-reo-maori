import tkinter as tk
from tkinter import messagebox

# 10 Te Reo Moaori questions
questions = [
    ("Aroha means 'love' in Māori.", True),
    ("Kia ora means 'goodbye' in Māori.", False),
    ("Whānau means 'family' in Māori.", True),
    ("Kai means 'food' in Māori.", True),
    ("Moana means 'sky' in Māori.", False),
    ("Kōrero means 'to speak or talk' in Māori.", True),
    ("Waiata means 'song' in Māori.", True),
    ("Tamariki means 'adults' in Māori.", False),
    ("Kākahu means 'clothes' in Māori.", True),
    ("Roto means 'outside' in Māori.", False),
]

class TeReoQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Te Reo Māori Quiz")

        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
        self.question_label.pack(pady=20)

        self.true_button = tk.Button(root, text="True", command=lambda: self.check_answer(True), width=10)
        self.true_button.pack(side="left", padx=20, pady=10)

        self.false_button = tk.Button(root, text="False", command=lambda: self.check_answer(False), width=10)
        self.false_button.pack(side="right", padx=20, pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q_text, _ = questions[self.q_index]
            self.question_label.config(text=q_text)
        else:
            self.end_quiz()

    def check_answer(self, answer):
        correct = questions[self.q_index][1]
        if answer == correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.q_index += 1
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"You got {self.score}/{len(questions)} correct!")
        self.root.destroy()

# Run thee program
if __name__ == "__main__":
    root = tk.Tk()
    quiz = TeReoQuiz(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
# questions lists for the quiz
original_questions = [
    {"question": "Aroha means 'love' in Māori.", "answer": True},
    {"question": "Kia ora means 'goodbye' in Māori.", "answer": False},
    {"question": "Whānau means 'family' in Māori.", "answer": True},
    {"question": "Kai means 'food' in Māori.", "answer": True},
    {"question": "Moana means 'sky' in Māori.", "answer": False},
    {"question": "Kōrero means 'to speak or talk' in Māori.", "answer": True},
    {"question": "Waiata means 'song' in Māori.", "answer": True},
    {"question": "Tamariki means 'adults' in Māori.", "answer": False},
    {"question": "Kākahu means 'clothes' in Māori.", "answer": True},
    {"question": "Roto means 'outside' in Māori.", "answer": False},
]

class TeReoQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Te Reo Maori Quiz")
        # starting score for the quiz
        self.score = 0
        self.questions = original_questions.copy()
        self.current_question = None
        # font for text size (question)
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
        self.question_label.pack(pady=20)
        # true button
        self.true_button = tk.Button(root, text="True", command=lambda: self.check_answer(True), width=10)
        self.true_button.pack(side="left", padx=20, pady=10)
        # false button
        self.false_button = tk.Button(root, text="False", command=lambda: self.check_answer(False), width=10)
        self.false_button.pack(side="right", padx=20, pady=10)
        # font and font size for the score at the bottom
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.load_question()
    # load question function
    def load_question(self):
        if self.questions:
            self.current_question = self.questions.pop(0) 
            self.question_label.config(text=self.current_question["question"])
        else:
            self.end_quiz()
    # add the proper amount of score per question right
    def check_answer(self, answer):
        if answer == self.current_question["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.questions.append(self.current_question)

        self.load_question()
    # ending message showing how much score you ended with
    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"You got all questions correct!\nFinal Score: {self.score}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    quiz = TeReoQuiz(root)
    root.mainloop()

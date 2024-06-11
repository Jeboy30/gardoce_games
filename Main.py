import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class HistoryBrainTrain:
    def __init__(self, root):
        self.root = root
        self.root.title("Guest Game")
        self.root.geometry("800x600")
        
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        style.configure('TLabel', font=('Helvetica', 14))
        
        self.difficulty_levels = {
            "Easy": {
                "questions": [
                    "Who was the first President of the United States?",
                    "In which year did the Titanic sink?",
                    "Who discovered America in 1492?",
                    "Which ancient civilization built the pyramids?",
                    "Who wrote the play 'Romeo and Juliet'?",
                    "In which year did the Berlin Wall fall?",
                    "What was the name of the ship that brought the Pilgrims to America?",
                    "Who was the British Prime Minister during World War II?",
                    "When was the Declaration of Independence signed?",
                    "Who painted the Mona Lisa?",
                    "Which city was the first capital of the United States?",
                    "Who invented the telephone?",
                    "In which year did the first man land on the moon?",
                    "Who was the first woman to fly solo across the Atlantic Ocean?",
                    "What was the main language spoken in the Roman Empire?",
                    "Who was the first emperor of China?",
                    "What was the primary religion of ancient Greece?",
                    "Who led the Soviet Union during World War II?",
                    "What was the main cause of the American Civil War?",
                    "Who was the longest-reigning British monarch?"
                ],
                "choices": [
                    ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                    ["1912", "1905", "1898", "1915"],
                    ["Christopher Columbus", "Leif Erikson", "Vasco da Gama", "Marco Polo"],
                    ["Egyptians", "Romans", "Greeks", "Mayans"],
                    ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
                    ["1989", "1991", "1987", "1990"],
                    ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                    ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
                    ["1776", "1789", "1801", "1812"],
                    ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
                    ["New York", "Philadelphia", "Washington, D.C.", "Boston"],
                    ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Samuel Morse"],
                    ["1969", "1965", "1972", "1961"],
                    ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Jacqueline Cochran"],
                    ["Latin", "Greek", "Hebrew", "Arabic"],
                    ["Qin Shi Huang", "Liu Bang", "Sun Tzu", "Confucius"],
                    ["Polytheism", "Christianity", "Buddhism", "Islam"],
                    ["Joseph Stalin", "Vladimir Lenin", "Leon Trotsky", "Mikhail Gorbachev"],
                    ["Slavery", "Taxation", "States' rights", "Economic issues"],
                    ["Queen Elizabeth II", "Queen Victoria", "King George III", "King Henry VIII"]
                ],
                "answers": [
                    "George Washington", "1912", "Christopher Columbus", "Egyptians", "William Shakespeare",
                    "1989", "Mayflower", "Winston Churchill", "1776", "Leonardo da Vinci",
                    "New York", "Alexander Graham Bell", "1969", "Amelia Earhart", "Latin",
                    "Qin Shi Huang", "Polytheism", "Joseph Stalin", "Slavery", "Queen Elizabeth II"
                ],
                "time_limit": 30
            },
            "Normal": {
                "questions": [
                    "What event started World War I?",
                    "Who was the British Prime Minister during World War II?",
                    "When was the Magna Carta signed?",
                    "Which treaty ended World War I?",
                    "Who was the first President of the United States?",
                    "Who discovered America in 1492?",
                    "What was the main cause of the American Civil War?",
                    "Who invented the telephone?",
                    "When was the Declaration of Independence signed?",
                    "Who painted the Mona Lisa?",
                    "Which city was the first capital of the United States?",
                    "What was the name of the ship that brought the Pilgrims to America?",
                    "In which year did the first man land on the moon?",
                    "Who was the first woman to fly solo across the Atlantic Ocean?",
                    "What was the main language spoken in the Roman Empire?",
                    "Who was the first emperor of China?",
                    "What was the primary religion of ancient Greece?",
                    "Who led the Soviet Union during World War II?",
                    "Who was the longest-reigning British monarch?",
                    "In what year did the Berlin Wall fall?"
                ],
                "choices": [
                    ["Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Sinking of Lusitania", "Zimmermann Telegram"],
                    ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
                    ["1215", "1066", "1492", "1776"],
                    ["Treaty of Versailles", "Treaty of Paris", "Treaty of Tordesillas", "Treaty of Ghent"],
                    ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                    ["Christopher Columbus", "Leif Erikson", "Vasco da Gama", "Marco Polo"],
                    ["Slavery", "Taxation", "States' rights", "Economic issues"],
                    ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Samuel Morse"],
                    ["1776", "1789", "1801", "1812"],
                    ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
                    ["New York", "Philadelphia", "Washington, D.C.", "Boston"],
                    ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                    ["1969", "1965", "1972", "1961"],
                    ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Jacqueline Cochran"],
                    ["Latin", "Greek", "Hebrew", "Arabic"],
                    ["Qin Shi Huang", "Liu Bang", "Sun Tzu", "Confucius"],
                    ["Polytheism", "Christianity", "Buddhism", "Islam"],
                    ["Joseph Stalin", "Vladimir Lenin", "Leon Trotsky", "Mikhail Gorbachev"],
                    ["Queen Elizabeth II", "Queen Victoria", "King George III", "King Henry VIII"],
                    ["1989", "1991", "1987", "1990"]
                ],
                "answers": [
                    "Assassination of Archduke Franz Ferdinand", "Winston Churchill", "1215", "Treaty of Versailles", 
                    "George Washington", "Christopher Columbus", "Slavery", "Alexander Graham Bell", "1776", "Leonardo da Vinci",
                    "New York", "Mayflower", "1969", "Amelia Earhart", "Latin", 
                    "Qin Shi Huang", "Polytheism", "Joseph Stalin", "Queen Elizabeth II", "1989"
                ],
                "time_limit": 20
            },
            "Hard": {
                "questions": [
                    "Which Roman emperor was the first to convert to Christianity?",
                    "In what year did the Berlin Wall fall?",
                    "What was the original purpose of the Great Wall of China?",
                    "Who was the longest-reigning British monarch?",
                    "Who led the Soviet Union during World War II?",
                    "What event started World War I?",
                    "Who was the first emperor of China?",
                    "What was the main cause of the American Civil War?",
                    "Who invented the telephone?",
                    "Who was the first President of the United States?",
                    "Who discovered America in 1492?",
                    "When was the Declaration of Independence signed?",
                    "Who painted the Mona Lisa?",
                    "Which city was the first capital of the United States?",
                    "What was the main language spoken in the Roman Empire?",
                    "What was the primary religion of ancient Greece?",
                    "What was the name of the ship that brought the Pilgrims to America?",
                    "Who was the British Prime Minister during World War II?",
                    "In which year did the first man land on the moon?",
                    "Who was the first woman to fly solo across the Atlantic Ocean?"
                ],
                "choices": [
                    ["Constantine the Great", "Augustus", "Nero", "Tiberius"],
                    ["1989", "1991", "1987", "1990"],
                    ["Defense against invasions", "Transport", "Trade route", "Boundary marker"],
                    ["Queen Elizabeth II", "Queen Victoria", "King George III", "King Henry VIII"],
                    ["Joseph Stalin", "Vladimir Lenin", "Leon Trotsky", "Mikhail Gorbachev"],
                    ["Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Sinking of Lusitania", "Zimmermann Telegram"],
                    ["Qin Shi Huang", "Liu Bang", "Sun Tzu", "Confucius"],
                    ["Slavery", "Taxation", "States' rights", "Economic issues"],
                    ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Samuel Morse"],
                    ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                    ["Christopher Columbus", "Leif Erikson", "Vasco da Gama", "Marco Polo"],
                    ["1776", "1789", "1801", "1812"],
                    ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
                    ["New York", "Philadelphia", "Washington, D.C.", "Boston"],
                    ["Latin", "Greek", "Hebrew", "Arabic"],
                    ["Polytheism", "Christianity", "Buddhism", "Islam"],
                    ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                    ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
                    ["1969", "1965", "1972", "1961"],
                    ["Amelia Earhart", "Harriet Quimby", "Bessie Coleman", "Jacqueline Cochran"]
                ],
                "answers": [
                    "Constantine the Great", "1989", "Defense against invasions", "Queen Elizabeth II", 
                    "Joseph Stalin", "Assassination of Archduke Franz Ferdinand", "Qin Shi Huang", "Slavery", 
                    "Alexander Graham Bell", "George Washington", "Christopher Columbus", "1776", 
                    "Leonardo da Vinci", "New York", "Latin", "Polytheism", 
                    "Mayflower", "Winston Churchill", "1969", "Amelia Earhart"
                ],
                "time_limit": 10
            }
        }

        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        ttk.Label(self.root, text="Guest Game", font=('Helvetica', 24)).pack(pady=20)
        play_button = ttk.Button(self.root, text="Play", command=self.show_difficulty_selection)
        play_button.pack(pady=10)

        instruction_button = ttk.Button(self.root, text="Instructions", command=self.show_instructions)
        instruction_button.pack(pady=10)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def show_difficulty_selection(self):
        self.clear_screen()
        ttk.Label(self.root, text="Select Difficulty", font=('Helvetica', 24)).pack(pady=20)
        easy_button = ttk.Button(self.root, text="Easy", command=lambda: self.start_game("Easy"))
        easy_button.pack(pady=10)

        normal_button = ttk.Button(self.root, text="Normal", command=lambda: self.start_game("Normal"))
        normal_button.pack(pady=10)

        hard_button = ttk.Button(self.root, text="Hard", command=lambda: self.start_game("Hard"))
        hard_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back", command=self.main_menu)
        back_button.pack(pady=10)

    def start_game(self, difficulty):
        self.clear_screen()
        self.current_difficulty = difficulty
        self.total_questions = 20
        self.current_question_index = 0
        self.correct_streak = 0
        self.questions = self.difficulty_levels[difficulty]["questions"]
        self.choices = self.difficulty_levels[difficulty]["choices"]
        self.answers = self.difficulty_levels[difficulty]["answers"]
        self.time_limit = self.difficulty_levels[difficulty]["time_limit"]
        self.generate_question()

    def generate_question(self):
        if self.current_question_index < self.total_questions:
            question_text = self.questions[self.current_question_index]
            choices = self.choices[self.current_question_index][:]
            random.shuffle(choices)

            self.clear_screen()
            question_label = ttk.Label(self.root, text=f"Question {self.current_question_index + 1}/{self.total_questions}: {question_text}", wraplength=700)
            question_label.pack(pady=20)

            for choice in choices:
                choice_button = ttk.Button(self.root, text=choice, command=lambda c=choice: self.check_answer(c))
                choice_button.pack(pady=5)

            self.timer_label = ttk.Label(self.root, text=f"Time Left: {self.time_limit} seconds")
            self.timer_label.pack(pady=20)
            self.remaining_time = self.time_limit
            self.update_timer()
        else:
            self.end_quiz()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time Left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer("")

    def check_answer(self, user_answer):
        correct_answer = self.answers[self.current_question_index]
        is_correct = user_answer == correct_answer
        self.update_q_table(is_correct)

        if is_correct:
            self.correct_streak += 1
        else:
            self.correct_streak = 0

        self.current_question_index += 1
        self.generate_question()

    def update_q_table(self, is_correct):
        # Q-learning logic would be implemented here
        pass

    def end_quiz(self):
        self.clear_screen()
        messagebox.showinfo("Quiz Ended", "The quiz has ended.")
        self.main_menu()

    def show_instructions(self):
        messagebox.showinfo("Instructions", "Select a difficulty level and answer the history questions within the time limit. Good luck!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HistoryBrainTrain(root)
    root.mainloop()

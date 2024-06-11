
def update_timer(self):
    if self.remaining_time >= 0:
        self.timer_label.config(text=f"Time Left: {self.remaining_time} seconds")
        self.remaining_time -= 1
        self.root.after(1000, self.update_timer)
    else:
        self.check_answer("")

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

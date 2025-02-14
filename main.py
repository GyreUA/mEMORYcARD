from card_layout import (
   app, layout_card,
   lb_Question, lb_Correct, lb_Result,
   rbtn_1, rbtn_2, rbtn_3, rbtn_4,
   btn_OK, show_question, show_result
)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # перемішуватимемо відповіді у картці питання


card_width, card_height = 600, 500 # початкові розміри вікна "картка"
text_wrong = 'Неправильно'
text_correct = 'Правильно'
question_number = 0


# у цій версії напишемо в коді одне запитання та відповіді до нього
# відповідні змінні поля майбутнього об'єкта "form" (тобто. анкета)
questions = [
    {
        "question": "Яблоку",
        "right": "apple",
        "wrongs": ["application", "building", "caterpillar"]
    },
    {
        "question": "Собака",
        "right": "dog",
        "wrongs": ["cat", "mouse", "bunny"]
    },
    {
        "question": "Машина",
        "right": "car",
        "wrongs": ["bicycle", "airplane", "boat"]
    },
    {
        "question": "Книга",
        "right": "book",
        "wrongs": ["pen", "notebook", "lamp"]
    },
    {
        "question": "Сонце",
        "right": "sun",
        "wrongs": ["moon", "star", "planet"]
    },
    {
        "question": "Будинок",
        "right": "house",
        "wrongs": ["apartment", "school", "office"]
    },
    {
        "question": "Молоко",
        "right": "milk",
        "wrongs": ["water", "juice", "tea"]
    }
]
#frm_question = 'Яблуко'
#frm_right = 'apple'
#frm_wrong1 = 'application'
#frm_wrong2 = 'building'
#frm_wrong3 = 'caterpillar'


# Тепер нам потрібно показати ці дані,
# причому відповіді розподілити випадково між радіокнопками, і пам'ятати кнопку з правильною відповіддю.
# Для цього створимо набір посилань на радіокнопки та перемішаємо його
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # ми не знаємо, який це з радіобаттонів, але можемо покласти сюди правильну відповідь і запам'ятати це
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]


def show_data():
    global question_number
   # об'єднаємо у функцію схожі дії
    frm_question = questions[question_number]['question']
    frm_right = questions[question_number]['right']
    frm_wrong1, frm_wrong2, frm_wrong3 = questions[question_number]['wrongs']

    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)


def check_result():
   ''' перевірка, чи правильна відповідь обрана
   якщо відповідь була обрана, то напис "правильно/неправильно" набуває потрібного
   значення і показується панель відповідей
   '''
   correct = answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
   if correct:
       # відповідь вірна, запишемо
       lb_Result.setText(text_correct) # напис "правильно" або "неправильно"
       show_result()
   else:
       incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
       if incorrect:
           # відповідь невірна, запишемо і відобразимо у статистиці
           lb_Result.setText(text_wrong) # напис "правильно" або "неправильно"
           show_result()


def click_OK(self):
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
    global question_number
    if btn_OK.text() != 'Наступне питання':
       check_result()
    else:
        try:
            question_number += 1
            show_question()
            show_data()
        except:
            question_number = 0
            print('Питання закінчилися')



win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')


win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(click_OK)


win_card.show()
app.exec_()

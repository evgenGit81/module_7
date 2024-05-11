# -*- coding: utf-8 -*-
team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команда Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"
#challenge_result = "победа команды Мастера кода!"
print("В команде %s участников: %d" % (team1_name, team1_num))
print("В команде %s участников: %d" % (team2_name, team2_num))
print("Команда {} решила задач: {}!".format(team2_name, score_2))
print("Команда {} решила задач: {}!".format(team1_name, score_1))
print("{} решили задачи за {} с!".format(team1_name, team1_time))
print("{} решили задачи за {} с!".format(team2_name, team2_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решенно {tasks_total} задач, в среднем по "
      f"{((team2_time + team1_time) / (score_2 + score_1)):4.1f} секунд на задачу!")
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунд на задачу!")
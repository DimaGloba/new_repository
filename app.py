import json

from flask import Flask, request, redirect, url_for, render_template#импорт библиотеки Flask

app = Flask(__name__) #экземпляр класса Flask с аргументом __name__

users = {"Дмитрий": "123",
         "Олег": "456",
         "Михаил": "789"
         }

class Users:
    def add_user(self, username, password):
        try:
            if username in users.keys():
                return False
            else:
                users[username] = password
                print(users)
                return True
        except KeyError:
            return False

    def del_user(self):
        pass

    def get_user(self, username, password):
        try:
            if users[username] == password:
                return  True
            else:
                return False
        except KeyError:
            return False

user = Users()

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user.get_user(username, password):
            return render_template('user_window.html', username=username)
        else:
            return "Неверный пароль"

    return render_template('login.html')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/regis', methods=['GET', 'POST'])
def regis():
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user.add_user(username, password):
            return "Пользователь успешно создан"
        else:
            return "Пользователь с таким именем уже зарегестрирован"
        render_template('login.html')
    return render_template('regis.html')


print(users)

if __name__ == "__main__":
    app.run()
    print(users)

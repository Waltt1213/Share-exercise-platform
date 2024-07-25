import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import pytesseract
from PIL import Image
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
from configs import data_base_path



def register_user():
    def register():
        new_user_name = var_new_user_name.get()
        new_password = var_new_password.get()
        new_password_confirm = var_new_password_confirm.get()
        role = 'user'

        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (new_user_name,))
        user = c.fetchone()

        if user:
            tk.messagebox.showinfo('Error', 'This user name has been registered')
        else:
            if new_password != new_password_confirm:
                tk.messagebox.showinfo('Error', 'Password must be the same!')
            else:
                c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                          (new_user_name, new_password, role))
                tk.messagebox.showinfo('Success', 'You have register successfully')
                conn.commit()
                register_window.destroy()
        conn.close()

        """使用文件进行注册
        with open('user_info.pickle', 'rb') as user_file:
            current_user_info = pickle.load(user_file)

        if new_password != new_password_confirm:
            tk.messagebox.showinfo('Error', 'Password must be the same!')
        elif new_user_name in current_user_info:
            tk.messagebox.showinfo('Error', 'This user name has been registered')
        else:
            current_user_info[new_user_name] = new_password
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(current_user_info, user_file)
            tk.messagebox.showinfo('Success', 'You have register successfully')
            register_window.destroy()
        """

    register_window = tk.Toplevel(window)
    register_window.geometry('350x200')
    register_window.title('Register Window')

    var_new_user_name = tk.StringVar()
    var_new_password = tk.StringVar()
    var_new_password_confirm = tk.StringVar()

    tk.Label(register_window, text='User name:').place(x=10, y=10)
    tk.Label(register_window, text='Password:').place(x=10, y=50)
    tk.Label(register_window, text='Confirm Password:').place(x=10, y=90)

    entry_new_user_name = tk.Entry(register_window, textvariable=var_new_user_name)
    entry_new_password = tk.Entry(register_window, textvariable=var_new_password, show='*')
    entry_new_password_confirm = tk.Entry(register_window, textvariable=var_new_password_confirm, show='*')
    entry_new_user_name.place(x=150, y=10)
    entry_new_password.place(x=150, y=50)
    entry_new_password_confirm.place(x=150, y=90)

    confirm_button = tk.Button(register_window, text='Confirm', command=register)
    confirm_button.place(x=150, y=130)


def log_user():
    user_name = var_usr_name.get()
    password = var_password.get()

    conn = sqlite3.connect(data_base_path)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user_name, password))
    user = c.fetchone()

    if user:
        tk.messagebox.showinfo('Welcome', 'Welcome to our shared-exercise platform')
        window.destroy()
        main_window(user)
    else:
        tk.messagebox.showinfo('Error', 'Incorrect username or password!')

    """使用文件进行登录
    if user_name == '':
        tk.messagebox.showinfo('Error', 'Please input')
        return
        
    try:
        with open('user_info.pickle', 'rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file:
            user_info = {user_name: password}
            pickle.dump(user_info, user_file)

    if user_name not in user_info:
        tk.messagebox.showinfo('Error', 'This user name is non-existent, please try other or create one')
    else:
        if password == user_info[user_name]:
            tk.messagebox.showinfo('Welcome', 'Welcome to our shared-exercise platform')
        else:
            tk.messagebox.showinfo('Error', 'The password is wrong, please try again')
    """


def modify_password():
    def modify():
        user_name = var_user_name.get()
        new_password = var_new_password.get()
        new_password_confirm = var_new_password_confirm.get()

        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (user_name,))
        user = c.fetchone()

        if user:
            c.execute('SELECT password FROM users WHERE username = ?', (user_name,))
            old_password = c.fetchone()[0]
            if new_password != new_password_confirm:
                tk.messagebox.showinfo('Error', 'Password must be the same!')
            elif new_password == old_password:
                tk.messagebox.showinfo('Error', 'The new password is the same as the old')
            else:
                tk.messagebox.showinfo('Success', 'You have modified successfully')
                c.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, user_name))
                conn.commit()
                modify_window.destroy()
        else:
            tk.messagebox.showinfo('Error', 'This user name has not been registered')

        conn.close()

        """使用文件修改密码
        with open('user_info.pickle', 'rb') as user_file:
            current_user_info = pickle.load(user_file)

        if user_name not in current_user_info:
            tk.messagebox.showinfo('Error', 'This user name has not been registered')
        elif new_password != new_password_confirm:
            tk.messagebox.showinfo('Error', 'Password must be the same!')
        elif current_user_info[user_name] == new_password:
            tk.messagebox.showinfo('Error', 'The new password is the same as the old')
        else:
            current_user_info[user_name] = new_password
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(current_user_info, user_file)
            tk.messagebox.showinfo('Success', 'You have modified successfully')
            modify_window.destroy()
        """

    modify_window = tk.Toplevel(window)
    modify_window.geometry('350x200')
    modify_window.title('Modify Window')

    var_user_name = tk.StringVar()
    var_new_password = tk.StringVar()
    var_new_password_confirm = tk.StringVar()

    tk.Label(modify_window, text='User name:').place(x=10, y=10)
    tk.Label(modify_window, text='New password:').place(x=10, y=50)
    tk.Label(modify_window, text='Confirm new password:').place(x=10, y=90)

    entry_new_user_name = tk.Entry(modify_window, textvariable=var_user_name)
    entry_new_password = tk.Entry(modify_window, textvariable=var_new_password, show='*')
    entry_new_password_confirm = tk.Entry(modify_window, textvariable=var_new_password_confirm, show='*')
    entry_new_user_name.place(x=150, y=10)
    entry_new_password.place(x=150, y=50)
    entry_new_password_confirm.place(x=150, y=90)

    confirm_button = tk.Button(modify_window, text='Confirm', command=modify)
    confirm_button.place(x=150, y=130)


def main_window(user):
    # 上传问题
    def upload_question():
        file_path = askopenfilename()
        if file_path:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            edit_question(text)
    # 编辑问题
    def edit_question(text):
        correct_answers_list = []
        fill_blank_entries = []

        options = []
        edit_window = tk.Toplevel(main_win)
        edit_window.title("Edit your question")
        options_frame = tk.Frame(edit_window)
        option_entries = [tk.Entry(edit_window, width=50) for _ in range(4)]

        def add_option():
            option_entries_len = len(option_entries)
            option_label = tk.Label(options_frame, text=f"Option {chr(65 + option_entries_len)}:")
            option_label.grid(row=option_entries_len, column=0, sticky=tk.W)
            option_entry = tk.Entry(options_frame, width=50)
            option_entry.grid(row=option_entries_len, column=1)
            option_var = tk.BooleanVar()
            option_check = tk.Checkbutton(options_frame, variable=option_var)
            option_check.grid(row=option_entries_len, column=2)
            option_entries.append(option_entry)
            options.append([option_label, option_entry, option_check])
            correct_answers_list.append(option_var)

        def remove_option():
            if option_entries:
                last_option = options.pop()
                option_entries.pop()
                correct_answers_list.pop()
                for option in last_option:
                    option.grid_remove()

        btn_add_option = tk.Button(edit_window, text='Add Option', command=add_option)
        btn_remove_option = tk.Button(edit_window, text='Remove Option', command=remove_option)

        def show_options():
            # for multi-options
            for widget in options_frame.winfo_children():
                widget.destroy()
            if btn_add_blank.winfo_ismapped():
                btn_add_blank.pack_forget()
            if btn_remove_blank.winfo_ismapped():
                btn_remove_blank.pack_forget()
            options_frame.pack()
            options.clear()
            ans_entries = []
            correct_answers_vars = []
            for i in range(len(option_entries)):
                option_label = tk.Label(options_frame, text=f"Option {chr(65 + i)}:")
                option_label.grid(row=i, column=0, sticky=tk.W)
                option_entry = tk.Entry(options_frame, width=50)
                option_entry.grid(row=i, column=1)
                # if option_entries[i].get():
                #   option_entry.insert(0, option_entries[i].get())
                option_var = tk.BooleanVar()
                option_check = tk.Checkbutton(options_frame, variable=option_var)
                option_check.grid(row=i, column=2)
                options.append([option_label, option_entry, option_check])
                ans_entries.append(option_entry)
                correct_answers_vars.append(option_var)
            # show_options()
            btn_add_option.pack()
            btn_remove_option.pack()

            option_entries.clear()
            option_entries.extend(ans_entries)
            correct_answers_list.clear()
            correct_answers_list.extend(correct_answers_vars)

        def add_fill_blank():
            entry = tk.Entry(options_frame, width=50)
            entry.grid(row=len(fill_blank_entries), column=0)
            fill_blank_entries.append(entry)

        def remove_fill_blank():
            if fill_blank_entries:
                last_entry = fill_blank_entries.pop()
                last_entry.grid_remove()

        # for fill-bank
        btn_add_blank = tk.Button(edit_window, text='Add Blank', command=add_fill_blank)
        btn_remove_blank = tk.Button(edit_window, text='Remove Blank', command=remove_fill_blank)

        def show_fill_in_blanks():
            for widget in options_frame.winfo_children():
                widget.destroy()
            if btn_add_option.winfo_ismapped():
                btn_add_option.pack_forget()
            if btn_remove_option.winfo_ismapped():
                btn_remove_option.pack_forget()
            options_frame.pack()
            fill_blank_entries.clear()
            add_fill_blank()
            btn_add_blank.pack()
            btn_remove_blank.pack()


        tk.Label(edit_window, text="Edit Question Text").pack()
        text_box = tk.Text(edit_window, wrap='word', height=10)
        text_box.insert('1.0', text)
        text_box.pack(expand=True, fill='both')

        answer_type_var = tk.StringVar(value="multiple_choice")
        tk.Radiobutton(edit_window, text="Multiple Choice", variable=answer_type_var, value="multiple_choice",
                       command=show_options).pack(anchor=tk.W)
        tk.Radiobutton(edit_window, text="Fill in the Blanks", variable=answer_type_var, value="fill_in_the_blanks",
                       command=show_fill_in_blanks).pack(anchor=tk.W)

        show_options()
        tk.Label(edit_window, text="Select Group:").pack()
        group_name_var = tk.StringVar()
        group_menu = ttk.Combobox(edit_window, textvariable=group_name_var)
        group_menu.pack()

        def load_groups():
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT group_name FROM question_groups')
            groups = c.fetchall()
            conn.close()
            group_menu['values'] = [group[0] for group in groups]

        def add_new_group():
            new_group = tk.simpledialog.askstring("New Group", "Enter new group name:")
            if new_group:
                load_groups()
                group_name_var.set(new_group)

        load_groups()
        tk.Button(edit_window, text="Add New Group", command=add_new_group).pack()

        def save_question():
            question_text = text_box.get('1.0', 'end-1c')
            question_type = answer_type_var.get()
            group_name = group_name_var.get()
            options_text = ''
            if question_type == "multiple_choice":
                options = [entry.get() for entry in option_entries]
                correct_answers = [options[i] for i in range(len(options)) if correct_answers_list[i].get()]
                if not correct_answers:
                    messagebox.showerror("Error", "Please select at least one correct answer.")
                    return
                options_text = "|".join(options)
                correct_answers_text = "|".join(correct_answers)
            else:
                correct_answers_text = "|".join([entry.get() for entry in fill_blank_entries])

            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT id FROM question_groups WHERE group_name = ?', (group_name, ))
            group = c.fetchone()
            if not group:
                c.execute('INSERT INTO question_groups (group_name) VALUES (?)', (group_name, ))
                conn.commit()
                group_id = c.lastrowid
            else:
                group_id = group[0]
            c.execute('''
                INSERT INTO questions (question_text, question_type, options, correct_answer, group_id) 
                VALUES (?, ?, ?, ?, ?)
                ''', (question_text, question_type, options_text, correct_answers_text, group_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Save", "Question and answer saved successfully!")
            edit_window.destroy()

        tk.Button(edit_window, text='Save', command=save_question).pack(side=tk.BOTTOM)

    def show_question(question):
        question_id, question_text = question
        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute('SELECT question_type, options, correct_answer FROM questions WHERE id = ?', (question_id,))
        question_data = c.fetchone()
        conn.close()

        question_window = tk.Toplevel(main_win)
        question_window.title(f'Question {question_id}')
        question_window.geometry("450x300")
        tk.Label(question_window, text=question_text).pack()
        question_type, options, correct_answers = question_data
        correct_answers_list = correct_answers.split('|')

        if question_type == 'multiple_choice':
            option_vars = [tk.BooleanVar() for op in options.split('|')]
            for i, option in enumerate(options.split('|')):
                tk.Checkbutton(question_window, text=option, variable=option_vars[i]).pack(anchor=tk.W)

            def check_answer():
                op = options.split('|')
                user_answers = [op[j] for j in range(len(option_vars)) if option_vars[j].get()]
                if sorted(user_answers) == sorted(correct_answers_list):
                    messagebox.showinfo("Correct!", "Your answer is correct!")
                else:
                    log_error(question_id)
                    messagebox.showerror("Incorrect!", "Your answer is incorrect.")

        else:
            fill_blank_entries = [tk.Entry(question_window) for _ in correct_answers_list]
            for entry in fill_blank_entries:
                entry.pack()

            def check_answer():
                user_answers = [entry.get() for entry in fill_blank_entries]
                if sorted(user_answers) == sorted(correct_answers_list):
                    messagebox.showinfo("Correct!", "Your answer is correct!")
                else:
                    log_error(question_id)
                    messagebox.showerror("Incorrect!", "Your answer is incorrect.")

        tk.Button(question_window, text='Submit', command=check_answer).pack()

    def log_error(question_id):
        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute('SELECT error_count FROM error_logs WHERE user_id = ? AND question_id = ?',
                  (user[0], question_id))
        result = c.fetchone()
        if result:
            error_count = result[0] + 1
            c.execute('UPDATE error_logs SET error_count = ? WHERE user_id = ? AND question_id = ?',
                      (error_count, user[0], question_id))
        else:
            c.execute('INSERT INTO error_logs (user_id, question_id, error_count) VALUES (?, ?, ?)',
                      (user[0], question_id, 1))
        conn.commit()
        conn.close()
    # 做题
    def start_practice():
        def show_questions(group_id):
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT id, question_text FROM questions WHERE group_id = ?', (group_id,))
            questions = c.fetchall()
            conn.close()

            questions_window = tk.Toplevel(practice_window)
            questions_window.title('Questions')
            if not questions:
                tk.Label(questions_window, text=f"There's no problem here, go take a look elsewhere").pack()
            for question in questions:
                question_id, question_text = question
                tk.Button(questions_window, text=f'{question_id}: {question_text[:20]}',
                          command=lambda q=question: show_question(q)).pack()

        practice_window = tk.Toplevel(main_win)
        practice_window.title('Practice')
        practice_window.geometry("450x300")
        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute('SELECT id, group_name FROM question_groups')
        groups = c.fetchall()
        conn.close()

        for group in groups:
            group_id, group_name = group
            tk.Button(practice_window, text=group_name, command=lambda gid=group_id: show_questions(gid)).pack()
    def create_user_group():
        def create():
            new_group_name = var_new_group_name.get()

            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT * FROM groups WHERE group_name = ?', (new_group_name,))
            group = c.fetchone()

            if group:
                tk.messagebox.showinfo('Error', 'This group has been created')
            else:
                c.execute('INSERT INTO groups (group_name, users) VALUES (?, ?)',
                          (new_group_name, user[1]))
                tk.messagebox.showinfo('Success', 'You have create ' + new_group_name + ' successfully')
                conn.commit()
                create_window.destroy()
            conn.close()

        create_window = tk.Toplevel(main_win)
        create_window.geometry('250x100')
        create_window.title('Create a User Group')

        var_new_group_name = tk.StringVar()

        tk.Label(create_window, text='Group name:').place(x=10, y=10)

        entry_new_group_name = tk.Entry(create_window, textvariable=var_new_group_name)
        entry_new_group_name.place(x=100, y=10)

        confirm_button = tk.Button(create_window, text='Confirm', command=create)
        confirm_button.place(x=100, y=40)

    # 搜索和加入组
    def search_join_user_group():
        def search():
            new_group_name = var_new_group_name.get()
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT * FROM groups WHERE group_name = ?', (new_group_name,))
            group = c.fetchone()

            if group:
                tk.messagebox.showinfo('Info', 'This group is existent')
            else:
                tk.messagebox.showinfo('Error', 'This group has not been created')

            conn.close()

        def join():
            new_group_name = var_new_group_name.get()
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT * FROM groups WHERE group_name = ?', (new_group_name,))
            group = c.fetchone()

            if group:
                c.execute('SELECT * FROM groups WHERE group_name = ? AND users LIKE ?',
                          (new_group_name, f'%{user[1]}%'))
                member = c.fetchone()
                if member:
                    tk.messagebox.showinfo('Error', 'You are already in this group')
                else:
                    c.execute('SELECT users FROM groups WHERE group_name = ?', (new_group_name,))
                    current_users = c.fetchone()[0]
                    updated_users = f'{current_users},{user[1]}' if current_users else user[1]

                    c.execute('UPDATE groups SET users = ? WHERE group_name = ?',
                              (updated_users, new_group_name))
                    conn.commit()
                    tk.messagebox.showinfo('Success', 'You have now joined this group')
            else:
                tk.messagebox.showinfo('Error', 'This group has not been created')

            conn.close()

        search_join_window = tk.Toplevel(main_win)
        search_join_window.geometry('250x100')
        search_join_window.title('Search or join a User Group')

        var_new_group_name = tk.StringVar()

        tk.Label(search_join_window, text='Group name:').place(x=10, y=10)

        entry_new_group_name = tk.Entry(search_join_window, textvariable=var_new_group_name)
        entry_new_group_name.place(x=100, y=10)

        search_button = tk.Button(search_join_window, text='Search', command=search)
        search_button.place(x=20, y=40)
        join_button = tk.Button(search_join_window, text='Join', command=join)
        join_button.place(x=100, y=40)

        # 退出登录
    def exit_log():
        main_win.destroy()

    # 分享题目
    def share_question():
        def send_question():
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT users FROM groups WHERE group_name = ?', (user_group_name_var.get(),))
            users = c.fetchall()
            for user in users[0][0].split(','):
                c.execute('SELECT user_name, question_group_name FROM user_inbox WHERE user_name = ? AND question_group_name = ?',
                          (user, question_group_name_var.get()))
                item = c.fetchone()
                if not item:
                    c.execute('INSERT INTO user_inbox (user_name, question_group_name) VALUES (?, ?)',
                          (user, question_group_name_var.get()))
                    conn.commit()
                tk.messagebox.showinfo('Success', 'You have shared successfully')
            conn.close()

        share_window = tk.Toplevel(main_win)
        share_window.geometry('300x150')
        share_window.title('Share Question')
        tk.Label(share_window, text='Select Question Group:').pack()
        question_group_name_var = tk.StringVar()
        question_group_menu = ttk.Combobox(share_window, textvariable=question_group_name_var)
        question_group_menu.pack()
        tk.Label(share_window, text='Select User Group:').pack()
        user_group_name_var = tk.StringVar()
        user_group_menu = ttk.Combobox(share_window, textvariable=user_group_name_var)
        user_group_menu.pack()

        def load_question_group():
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT group_name FROM question_groups')
            question_groups = c.fetchall()
            conn.close()
            question_group_menu['values'] = [group[0] for group in question_groups]

        def load_user_group():
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT group_name FROM groups')
            user_groups = c.fetchall()
            conn.close()
            if user_groups:
                user_group_menu['values'] = [group[0] for group in user_groups]

        load_question_group()
        load_user_group()

        tk.Button(share_window, text='Send', command=send_question).pack()

    # 接收题目
    def receive_question():
        receive_window = tk.Toplevel(main_win)
        receive_window.geometry('300x150')
        receive_window.title('Receive Question')

        question_group_name_var = tk.StringVar()
        question_group_menu = ttk.Combobox(receive_window, textvariable=question_group_name_var)
        question_group_menu.pack()

        def load_receive_question_group():
            conn = sqlite3.connect(data_base_path)
            c = conn.cursor()
            c.execute('SELECT question_group_name FROM user_inbox')
            question_groups = c.fetchall()
            conn.close()
            question_group_menu['values'] = [group[0] for group in question_groups]

        load_receive_question_group()

    def review_errors():
        conn = sqlite3.connect(data_base_path)
        c = conn.cursor()
        c.execute(
            'SELECT q.id, q.question_text, e.error_count FROM questions q JOIN error_logs e ON q.id = e.question_id '
            'WHERE e.user_id = ? ORDER BY e.error_count DESC',
            (user[0],))
        errors = c.fetchall()
        conn.close()

        errors_window = tk.Toplevel(main_win)
        errors_window.title('Review Errors')
        errors_window.geometry('450x300')

        for question in errors:
            question_id, question_text, error_count = question
            tk.Button(errors_window, text=f'{question_id}: {question_text[:20]} (Errors: {error_count})',
                      command=lambda q=question: show_question((q[0], q[1]))).pack()

    main_win = tk.Tk()
    main_win.title("Shared Exercises Platform")
    main_win.geometry("450x300")
    tk.Label(main_win, text=f"welcome to Shared Exercises, {user[1]}!").pack()

    # upload question
    tk.Button(main_win, text='Upload question and edit', command=upload_question).pack()

    # practice questions
    tk.Button(main_win, text='Start Practice', command=start_practice).pack()
    # create search join user group
    tk.Button(main_win, text='Create a User Group', command=create_user_group).pack()
    tk.Button(main_win, text='Search or join a User Group', command=search_join_user_group).pack()
    # exit log
    tk.Button(main_win, text='Exit', command=exit_log).pack()
    # error logs
    tk.Button(main_win, text="Review Errors", command=review_errors).pack()

    tk.Button(main_win, text='Share Question', command=share_question).pack()
    tk.Button(main_win, text='Receive Question', command=receive_question).pack()
    main_win.mainloop()


if __name__ == '__main__':
    # create sqlite3
    conn = sqlite3.connect(data_base_path)
    c = conn.cursor()

    # create questions table
    c.execute('''
              CREATE TABLE IF NOT EXISTS questions
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              question_text TEXT NOT NULL,
              question_type TEXT NOT NULL,
              options TEXT,
              correct_answer TEXT NOT NULL,
              group_id INTEGER,
              FOREIGN KEY (group_id) REFERENCES question_groups (id))
              ''')
    # create users table
    c.execute('''
              CREATE TABLE IF NOT EXISTS users
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL,
              role TEXT NOT NULL)
              ''')
    # create groups table
    c.execute('''
             CREATE TABLE IF NOT EXISTS groups
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             group_name TEXT NOT NULL,
             users TEXT NOT NULL)
             ''')

    # create questions group table
    c.execute('''
              CREATE TABLE IF NOT EXISTS question_groups
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              group_name TEXT NOT NULL)
              ''')

    c.execute('''
              CREATE TABLE IF NOT EXISTS error_logs
              (user_id TEXT NOT NULL,
              question_id TEXT NOT NULL,
              error_count INTEGER DEFAULT 1,
              PRIMARY KEY (user_id, question_id))
              ''')
    # 收件箱
    c.execute('''
              CREATE TABLE IF NOT EXISTS user_inbox
              (user_name TEXT NOT NULL,
              question_group_name TEXT NOT NULL,
              PRIMARY KEY (user_name, question_group_name))
              ''')

    conn.commit()
    conn.close()

    window = tk.Tk()
    window.title("Welcome!!!")
    window.geometry('450x300')

    tk.Label(window, text="User name").place(x=50, y=150)
    tk.Label(window, text="Password").place(x=50, y=190)

    # user_name and password entry
    var_usr_name = tk.StringVar()
    var_password = tk.StringVar()

    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=150)
    entry_password = tk.Entry(window, textvariable=var_password, show='*')
    entry_password.place(x=160, y=190)

    btn_login = tk.Button(window, text='Login', command=log_user)
    btn_login.place(x=150, y=230)
    btn_sign_up = tk.Button(window, text='register', command=register_user)
    btn_sign_up.place(x=240, y=230)
    btn_sign_up = tk.Button(window, text='modify password', command=modify_password)
    btn_sign_up.place(x=240, y=265)

    window.mainloop()

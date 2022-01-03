from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from random import randint

window = Tk()
window.geometry("600x600")
window.title("Learn It!")
window.iconbitmap("logo.png")

def topic_input():
    if len(topic.get()) == 0:
        er_topic.config(text="Please type in the topic of your material.")
    else:
        er_topic.config(text="")
        synthesize()
# ---------------------------------------------------------------------------------------------------------------------
# window 2
def synthesize():
    global window2
    window2 = Tk()
    window2.geometry("600x600")
    window2.title("Synthesize It!")
    window2.iconbitmap("logo.png")
    window.withdraw()

    topic2 = Label(window2, text=topic.get(), font=("Times", 30), justify="center", width=40)
    topic2.place(x=0, y=20)

    Label(window2, text="Synthesize the information to less than 800 words.",
          font=("Times italic", 20), justify="center").place(x=100, y=65)
    st = Text(window2, width=60, height=30, bg="#F5F1ED", undo=True)
    st.place(x=98, y=130)

    # bold
    def bold():
        bold_font = font.Font(st, st.cget("font"))
        bold_font.configure(weight="bold")
        st.tag_configure("bold", font=bold_font)

        current_tags = st.tag_names("sel.first")
        if "bold" in current_tags:
            st.tag_remove("bold", "sel.first", "sel.last")
        else:
            st.tag_add("bold", "sel.first", "sel.last")
    # italics
    def italic():
        italic_font = font.Font(st, st.cget("font"))
        italic_font.configure(slant="italic")
        st.tag_configure("italic", font=italic_font)

        current_tags = st.tag_names("sel.first")
        if "italic" in current_tags:
            st.tag_remove("italic", "sel.first", "sel.last")
        else:
            st.tag_add("italic", "sel.first", "sel.last")
    #renew
    def renew():
        st.delete("1.0", END)

    # wordcount
    def wordcount():
        num = st.get("1.0", END)
        words = len(num.split())
        wordcount_txt.config(text=str(words) + " / 800")
        # if words exceeds 800
        if words > 800:
            over_msg.config(text="The text is over 800 words.")
        else:
            pass

    def init_wordcount():
        wordcount()
        wordcount_txt.after(1000, init_wordcount)

    # done: move on to next page
    def check_done():
        num = st.get("1.0", END)
        words = len(num.split())
        if words == 0:
            no_msg.config(text="Please type something in the box provided above.")
            over_msg.config(text="")
        elif words > 800:
            over_msg.config(text="The text is over 800 words.")
            no_msg.config(text="")
        else:
            input_words()
            no_msg.config(text="")
            over_msg.config(text="")

    # Go back to home screen
    def back_home():
        window2.withdraw()
        window.deiconify()

    # help button
    def help1():
        window7 = Tk()
        window7.geometry("200x310")
        window7.title("Help")

        def exit_help():
            window7.destroy()

        Label(window7, text="Help", font=("Times", 20)).place(x=75, y=10)
        Label(window7, text="Synthesize or summarize your materials to less than 800 words. "
                            "Then, click the button 'Done' to move on. \n Buttons:"
                            "\n<   Go back to home screen\n←  Undo\n→  Redo",
              anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=18, y=50)
        Label(window7, text="B", anchor="nw", justify="left", font=("Times bold", 15), wraplength=180).place(x=18, y=202)
        Label(window7, text="Bold", anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=40,
                                                                                                             y=202)
        Label(window7, text="I", anchor="nw", justify="left", font=("Times italic", 15), wraplength=180).place(x=18,
                                                                                                             y=220)
        Label(window7, text="Italic", anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=40,
                                                                                                               y=220)
        Label(window7, text="X", anchor="nw", justify="left", font=("Arial", 15), wraplength=180).place(x=18, y=238)
        Label(window7, text="Clear", anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=40, y=238)
        exit = Button(window7, text="Exit", command=exit_help)
        exit.place(x=80, y=275)


    # Buttons
    done = Button(window2, text="Done", font=("Times", 15), command=check_done)
    done.place(x=480, y=555)
    back = Button(window2, text="<", font=("Times", 20), command=back_home)
    back.place(x=100, y=20)
    help = Button(window2, text="?", font=("Times", 20), command=help1)
    help.place(x=485, y=20)

    undo_btn = Button(window2, text="←", font=("Times", 15), command=st.edit_undo)
    undo_btn.place(x=380, y=105)
    redo_btn = Button(window2, text="→", font=("Times", 15), command=st.edit_redo)
    redo_btn.place(x=410, y=105)
    bold_btn = Button(window2, text="B", font=("Times bold", 15), command=bold)
    bold_btn.place(x=440, y=105)
    under_btn = Button(window2, text="I", font=("Times italic", 15), command=italic)
    under_btn.place(x=470, y=105)
    new_btn = Button(window2, text="X", font=("Arial", 15), command=renew)
    new_btn.place(x=500, y=105)

    # word count
    wordcount_txt = Label(window2, text=" ", font=("Times"))
    wordcount_txt.place(x=98, y=530)
    over_msg = Label(window2, text="", font=("Times"), fg="red")
    over_msg.place(x=380, y=530)
    no_msg = Label(window2, text="", font=("Times"), fg="red")
    no_msg.place(x=270, y=530)

    init_wordcount()
# ---------------------------------------------------------------------------------------------------------------------
# window 3
def input_words():
    global window3
    window3 = Tk()
    window3.geometry("600x600")
    window3.title("Input It!")
    window3.iconbitmap("logo.png")

    topic3 = Label(window3, text=topic.get(), font=("Times", 30), justify="center", width=40)
    topic3.place(x=0, y=20)

    # Go back to home screen
    def back_synth():
        window3.withdraw()
        window2.deiconify()

    # help in window 3 (window 8)
    def help2():
        window8 = Tk()
        window8.geometry("200x310")
        window8.title("Help")

        def exit_help2():
            window8.destroy()

        Label(window8, text="Help", font=("Times", 20)).place(x=75, y=10)
        Label(window8, text="Type in the 10 vocabularies you have in your material. You can do so by looking "
                            "at the summarized text you just finished. Once you are done, click the 'Submit' button"
                            " to proceed to the next step. \nButton:\n<  Go back to previous\n    screen",
              anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=12, y=50)
        exit2 = Button(window8, text="Exit", command=exit_help2)
        exit2.place(x=80, y=275)

    def check_submit():
        if len(t1.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t2.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t3.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t4.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t5.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t6.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t7.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t8.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t9.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(t10.get()) == 0:
            err_term.config(text="Please fill in all the terms.")
        elif len(d1.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d2.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d3.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d4.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d5.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d6.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d7.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d8.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d9.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        elif len(d10.get()) == 0:
            err_term.config(text="Please fill in all the definitions.")
        else:
            choose()

    Label(window3, text="Input your 10 vocabularies accordingly.",
          font=("Times italic", 20), justify="center").place(x=140, y=65)
    Label(window3, text="Terms", font=("Times", 15)).place(x=98, y=100)
    Label(window3, text="Definition", font=("Times", 15)).place(x=260, y=100)
    err_term = Label(window3, text=" ", fg="red")
    err_term.place(x=210, y=555)
    err_def = Label(window3, text=" ", fg="red")
    err_def.place(x=190, y=555)

    # number list
    Label(window3, text="1.", font=("Times", 16)).place(x=68, y=122)
    Label(window3, text="2.", font=("Times", 16)).place(x=68, y=162)
    Label(window3, text="3.", font=("Times", 16)).place(x=68, y=202)
    Label(window3, text="4.", font=("Times", 16)).place(x=68, y=242)
    Label(window3, text="5.", font=("Times", 16)).place(x=68, y=282)
    Label(window3, text="6.", font=("Times", 16)).place(x=68, y=322)
    Label(window3, text="7.", font=("Times", 16)).place(x=68, y=362)
    Label(window3, text="8.", font=("Times", 16)).place(x=68, y=402)
    Label(window3, text="9.", font=("Times", 16)).place(x=68, y=442)
    Label(window3, text="10.", font=("Times", 16)).place(x=62, y=482)


    # entries for terms and definitions
    global t1
    global d1
    t1 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t1.place(x=98, y=120)
    d1 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d1.place(x=260, y=120)
    global t2
    global d2
    t2 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t2.place(x=98, y=160)
    d2 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d2.place(x=260, y=160)
    global t3
    global d3
    t3 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t3.place(x=98, y=200)
    d3 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d3.place(x=260, y=200)
    global t4
    global d4
    t4 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t4.place(x=98, y=240)
    d4 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d4.place(x=260, y=240)
    global t5
    global d5
    t5 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t5.place(x=98, y=280)
    d5 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d5.place(x=260, y=280)
    global t6
    global d6
    t6 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t6.place(x=98, y=320)
    d6 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d6.place(x=260, y=320)
    global t7
    global d7
    t7 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t7.place(x=98, y=360)
    d7 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d7.place(x=260, y=360)
    global t8
    global d8
    t8 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t8.place(x=98, y=400)
    d8 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d8.place(x=260, y=400)
    global t9
    global d9
    t9 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t9.place(x=98, y=440)
    d9 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d9.place(x=260, y=440)
    global t10
    global d10
    t10 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=12)
    t10.place(x=98, y=480)
    d10 = Entry(window3, bg="#F5F1ED", font=("Times", 20), width=26)
    d10.place(x=260, y=480)

    # buttons
    submit = Button(window3, text="Submit", command=check_submit)
    submit.place(x=270, y=530)
    help = Button(window3, text="?", font=("Times", 20), command=help2)
    help.place(x=485, y=20)
    back = Button(window3, text="<", font=("Times", 20), command=back_synth)
    back.place(x=100, y=20)

# ---------------------------------------------------------------------------------------------------------------------
# window 4
def choose():
    window4 = Tk()
    window4.geometry("600x600")
    window4.title("Choose It!")
    window4.iconbitmap("logo.png")
    window2.withdraw()
    window3.withdraw()

    # review window
    def review():
        window5 = Tk()
        window5.geometry("600x600")
        window5.title("Review It!")
        window5.iconbitmap("logo.png")
        window4.withdraw()

        # help in window 5 (window 9)
        def help3():
            window9 = Tk()
            window9.geometry("200x310")
            window9.title("Help")

            def exit_help3():
                window9.destroy()

            Label(window9, text="Help", font=("Times", 20)).place(x=75, y=10)
            Label(window9, text="Press the buttons, which displays the terms, provided on the left side. "
                                "The definition will show for the according terms you press. To reset, click the"
                                "'Reset' button at the right corner. Once done, "
                                "press < to go back to choosing the options.",
                  anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=12, y=50)
            exit3 = Button(window9, text="Exit", command=exit_help3)
            exit3.place(x=80, y=275)

        def back():
            window5.destroy()
            window4.deiconify()

        # configure display
        def change_b1():
            def_display.config(text=d1.get())
        def change_b2():
            def_display.config(text=d2.get())
        def change_b3():
            def_display.config(text=d3.get())
        def change_b4():
            def_display.config(text=d4.get())
        def change_b5():
            def_display.config(text=d5.get())
        def change_b6():
            def_display.config(text=d6.get())
        def change_b7():
            def_display.config(text=d7.get())
        def change_b8():
            def_display.config(text=d8.get())
        def change_b9():
            def_display.config(text=d9.get())
        def change_b10():
            def_display.config(text=d10.get())
        def reset_dis():
            def_display.config(text="")

        topic5 = Label(window5, text=topic.get(), font=("Times", 30), justify="center", width=40)
        topic5.place(x=0, y=20)
        Label(window5, text="Learn your vocabs by pressing the buttons.",
              font=("Times italic", 20), justify="center").place(x=134, y=65)
        help = Button(window5, text="?", font=("Times", 20), command=help3)
        help.place(x=485, y=20)
        back = Button(window5, text="<", font=("Times", 20), command=back)
        back.place(x=100, y=20)

        def_display = Label(window5, text=" ", bg="#F5F1ED", width=38, height=24, anchor="nw", justify="left",
                            padx=10, pady=10)
        def_display.place(x=210, y=120)

        # buttons
        b1 = Button(window5, text=t1.get(), width=20, font=("Times", 15), command=change_b1)
        b1.place(x=25, y=130)
        b2 = Button(window5, text=t2.get(), width=20, font=("Times", 15), command=change_b2)
        b2.place(x=25, y=170)
        b3 = Button(window5, text=t3.get(), width=20, font=("Times", 15), command=change_b3)
        b3.place(x=25, y=210)
        b4 = Button(window5, text=t4.get(), width=20, font=("Times", 15), command=change_b4)
        b4.place(x=25, y=250)
        b5 = Button(window5, text=t5.get(), width=20, font=("Times", 15), command=change_b5)
        b5.place(x=25, y=290)
        b6 = Button(window5, text=t6.get(), width=20, font=("Times", 15), command=change_b6)
        b6.place(x=25, y=330)
        b7 = Button(window5, text=t7.get(), width=20, font=("Times", 15), command=change_b7)
        b7.place(x=25, y=370)
        b8 = Button(window5, text=t8.get(), width=20, font=("Times", 15), command=change_b8)
        b8.place(x=25, y=410)
        b9 = Button(window5, text=t9.get(), width=20, font=("Times", 15), command=change_b9)
        b9.place(x=25, y=450)
        b10 = Button(window5, text=t10.get(), width=20, font=("Times", 15), command=change_b10)
        b10.place(x=25, y=490)
        reset = Button(window5, text="Reset", font=("Times", 15), command=reset_dis)
        reset.place(x=532, y=535)
    # -----------------------------------------------------------------------------------------------------------------
    # practice window
    def practice():
        window6 = Tk()
        window6.geometry("600x600")
        window6.title("Practice It!")
        window6.iconbitmap("logo.png")
        window4.withdraw()

        # help in window 6 (window 10)
        def help4():
            window10 = Tk()
            window10.geometry("200x310")
            window10.title("Help")

            def exit_help4():
                window10.destroy()

            Label(window10, text="Help", font=("Times", 20)).place(x=75, y=10)
            Label(window10, text="Click 'Start' to start practicing. Once the definition displays, "
                                 "type in the according term. Next, press ✓ to get answered checked. After reviewing, "
                                 "click 'Done' for the next question. Press < to go back to choosing the options.",
                  anchor="nw", justify="left", font=("Times", 15), wraplength=180).place(x=12, y=50)
            exit3 = Button(window10, text="Exit", command=exit_help4)
            exit3.place(x=80, y=275)

        defs = [d1.get(), d2.get(), d3.get(), d4.get(), d5.get(), d6.get(), d7.get(), d8.get(), d9.get(), d10.get()]

        def done_btn():
            global rand_def
            rand_def = defs[randint(0, 10)]
            def_dis.config(text=rand_def)
            correct_msg.config(text=" ")

        def check():
            print(rand_def)
            if rand_def == d1.get():
                if ans.get() == t1.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t1.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d2.get():
                if ans.get() == t2.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t2.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d3.get():
                if ans.get() == t3.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t3.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d4.get():
                if ans.get() == t4.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t4.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d5.get():
                if ans.get() == t5.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t5.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d6.get():
                if ans.get() == t6.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t6.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d7.get():
                if ans.get() == t7.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t7.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d8.get():
                if ans.get() == t8.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t8.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d9.get():
                if ans.get() == t9.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t9.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")
            elif rand_def == d10.get():
                if ans.get() == t10.get():
                    correct_msg.config(text="Correct!", fg="green")
                    ans.delete(0, END)
                    done2.config(text="Done")
                else:
                    correct_msg.config(text="Correct Answer: " + t10.get(), fg="red")
                    ans.delete(0, END)
                    done2.config(text="Done")

        def back():
            window6.destroy()
            window4.deiconify()

        topic6 = Label(window6, text=topic.get(), font=("Times", 30), justify="center", width=40)
        topic6.place(x=0, y=20)
        Label(window6, text="Type in the definition according to the terms provided.",
              font=("Times italic", 20), justify="center").place(x=90, y=65)
        help = Button(window6, text="?", font=("Times", 20), command=help4)
        help.place(x=485, y=20)
        back = Button(window6, text="<", font=("Times", 20), command=back)
        back.place(x=100, y=20)
        def_dis = Label(window6, text="", font=("Times", 30), justify="center", width=40)
        def_dis.place(x=0, y=280)
        ans = Entry(window6, bg="#F5F1ED", font=("Times", 25), width=29)
        ans.place(x=105, y=470)

        # widgets for checking answers
        check = Button(window6, text="✓", font=("Times", 30), command=check)
        check.place(x=495, y=470)
        correct_msg = Label(window6, text=" ", font=("Times", 15), fg="green")
        correct_msg.place(x=150, y=515)
        done2 = Button(window6, text="Start", font=("Times", 15), command=done_btn)
        done2.place(x=105, y=515)

    # -----------------------------------------------------------------------------------------------------------------


    def finish():
        window.destroy()
        window2.destroy()
        window3.destroy()
        window4.destroy()

    topic4 = Label(window4, text=topic.get(), font=("Times", 30), justify="center", width=40)
    topic4.place(x=0, y=120)
    Label(window4, text="Choose to either review or practice.",
          font=("Times italic", 20), justify="center").place(x=160, y=165)
    review = Button(window4, text="Review", font=("Times", 25), padx=12, pady=7, command=review)
    review.place(x=250, y=220)
    prac = Button(window4, text="Practice", font=("Times", 25), padx=12, pady=7, command=practice)
    prac.place(x=250, y=300)
    finish = Button(window4, text="Finish", font=("Times", 15), command=finish)
    finish.place(x=280, y=380)
# ---------------------------------------------------------------------------------------------------------------------

logo = Image.open("logo.png")
resized_logo = ImageTk.PhotoImage(logo.resize((130,108), Image.ANTIALIAS))
my_logo = Label(window, image=resized_logo).place(x=240, y=50)

Label(window, text="Learn It!", font=("Times", 35)).place(x=245, y=200)
Label(window, text="Learn your materials more efficiently by using Learn It!\n"
                   "You will have to condense your materials to smaller information \nand then "
                   "pick up 10 keywords to study. Happy studying!",
      font=("Times", 20), justify="center").place(x=50, y=250)
Label(window, text="Type in the topic of your material to get started.",
      font=("Times italic", 20), justify="center").place(x=120, y=350)

topic = Entry(window, bg="#F5F1ED", font=("Times", 25))
topic.place(x=180, y=380)

er_topic = Label(window, text=" ", fg="red")
er_topic.place(x=180, y=420)

gs = Button(window, text="Get Started",  font=("Times", 15), command=topic_input)
gs.place(x=275, y=450)


window.mainloop()
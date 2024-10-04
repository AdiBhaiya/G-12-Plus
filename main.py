from tkinter import messagebox as msgbox
import customtkinter as tk
import random
import sqlite3

users = sqlite3.connect("g12plus.db")
cur = users.cursor()
cur.execute(
	"""CREATE TABLE IF NOT EXISTS users (
	fName TEXT,
	lName TEXT,
	phNo TEXT,
	email TEXT UNIQUE,
	passwd TEXT,
	active INTEGER
	)"""
)

tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
tk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = tk.CTk()
root.title("G-12 Plus")
# root.iconbitmap(r".\assets\img\Logo.ico")
root.attributes("-fullscreen", True)
root.resizable(False, False)





pages = {
	"signupPageFrame": False,
	"loginPageFrame": False,
	"profileFrame": False,
	"homePageFrame": False,
	"playPageFrame": False,
	"statsPageFrame": False,
	"gameFPBPageFrame": False,
	"gameGuessPageFrame": False,
	"gameKBCPageFrame": False
}


def destroyOldPages(event=None):
	for x in pages:
		if pages[x] == True:
			eval(x).destroy()  # Converts the string into a global variable and then destroy it.
			pages[x] = False


def showPass(showBut, passField, event=None):
	showBut = eval(showBut)
	passField = eval(passField)
	if showBut._text == "Show":
		passField.configure(show="")
		showBut.configure(text="Hide")
	elif showBut._text == "Hide":
		passField.configure(show="*")
		showBut.configure(text="Show")


def signupPage(event=None):
	def createNewUser():
		if signUpFName.get() == "" or signUpLName.get() == "" or signUpPhNo.get() == "" or signUpEmail.get() == "" or signUpPassword.get() == "":
			msgbox.showerror("INVALID", "One or more text fields are empty.")
		elif "@" not in signUpEmail.get() or "." not in signUpEmail.get():
			msgbox.showerror("INVALID", "Invalid email ID")
		else:
			if signUpPassword.get() != signUpCPassword.get():
				msgbox.showerror("INVALID", "Passwords do not match")
			else:
				cur.execute(
					"INSERT INTO users VALUES (:fName, :lName, :phNo, :email, :passwd, :active)",
					{
						"fName": signUpFName.get(),
						# "mName": signUpMName.get(),
						"lName": signUpLName.get(),
						"phNo": signUpPhNo.get(),
						"email": signUpEmail.get(),
						"passwd": signUpPassword.get(),
						"active": 0
					}
				)
				users.commit()

				userData = {
					"fName": signUpFName.get(),
					"lName": signUpLName.get(),
					"phNo": signUpPhNo.get(),
					"email": signUpEmail.get(),
					"passwd": signUpPassword.get()
				}

				# with open("g12plus.dat", "ab") as gameData:
				# 	pickle.dump(userData, gameData)

				msgbox.showinfo("SUCCESS", "New user created successfully :)")
				loginPage()


	destroyOldPages()
	pages["signupPageFrame"] = True
	global signupPageFrame, signUpShowPassLabel, signUpPassword, signUpShowCPassLabel, signUpCPassword
	signupPageFrame = tk.CTkFrame(root)
	signupPageFrame.pack(fill=tk.BOTH, expand=True)

	signupPageBtnsFrame = tk.CTkFrame(signupPageFrame, fg_color="transparent")
	signupPageBtnsFrame.pack(pady=10, anchor="nw")
	# buttonHome = tk.CTkButton(signupPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100,  corner_radius=15, command=homePage)
	buttonHome = tk.CTkButton(signupPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100,  corner_radius=15, command=homePage)
	buttonHome.grid(row=0, column=1, padx=10, pady=(0, 10))
	signupPageFrameContents = tk.CTkFrame(signupPageFrame, fg_color="transparent")
	signupPageFrameContents.pack(pady=10, anchor="center")

	signUpText = tk.CTkLabel(signupPageFrameContents, text="SIGN UP", font=("Berlin Sans FB Demi", 50))
	signUpText.grid(row=0, column=0, columnspan=3, pady=(0, 50))

	signUpFNameLabel = tk.CTkLabel(signupPageFrameContents, text="First Name", font=("Calibri", 20))
	signUpFNameLabel.grid(row=1, column=0, padx=10, pady=10)
	signUpFName = tk.CTkEntry(signupPageFrameContents, placeholder_text="First Name", font=("Calibri", 20), width=200, height=50)
	signUpFName.grid(row=2, column=0, padx=10, pady=(0, 10))

	signUpLNameLabel = tk.CTkLabel(signupPageFrameContents, text="Last Name", font=("Calibri", 20))
	signUpLNameLabel.grid(row=1, column=2, padx=10, pady=10)
	signUpLName = tk.CTkEntry(signupPageFrameContents, placeholder_text="Last Name", font=("Calibri", 20), width=200, height=50)
	signUpLName.grid(row=2, column=2, padx=10, pady=(0, 10))

	signUpPhNoLabel = tk.CTkLabel(signupPageFrameContents, text="Phone Number", font=("Calibri", 20))
	signUpPhNoLabel.grid(row=3, column=0, columnspan=3, pady=(25, 10))
	signUpPhNo = tk.CTkEntry(signupPageFrameContents, placeholder_text="Phone Number", font=("Calibri", 20), width=350, height=50)
	signUpPhNo.grid(row=4, column=0, columnspan=3, pady=(0, 10))

	signUpEmailLabel = tk.CTkLabel(signupPageFrameContents, text="Email ID", font=("Calibri", 20))
	signUpEmailLabel.grid(row=5, column=0, columnspan=3, pady=(25, 10))
	signUpEmail = tk.CTkEntry(signupPageFrameContents, placeholder_text="Email ID", font=("Calibri", 20), width=350, height=50)
	signUpEmail.grid(row=6, column=0, columnspan=3, pady=(0, 10))

	signUpPasswordLabel = tk.CTkLabel(signupPageFrameContents, text="Password", font=("Calibri", 20))
	signUpPasswordLabel.grid(row=7, column=0, columnspan=3, pady=(25, 10))
	signUpPassword = tk.CTkEntry(signupPageFrameContents, placeholder_text="Password", show="*", font=("Calibri", 20), width=350, height=50)
	signUpPassword.grid(row=8, column=0, columnspan=3, pady=(0, 10))
	signUpShowPassLabel = tk.CTkButton(signupPageFrameContents, text="Show", font=("Calibri", 20), width=20, command=lambda:showPass("signUpShowPassLabel", "signUpPassword"))
	signUpShowPassLabel.grid(row=7, column=1, columnspan=3, pady=(25, 10))

	signUpCPasswordLabel = tk.CTkLabel(signupPageFrameContents, text="Confirm", font=("Calibri", 20))
	signUpCPasswordLabel.grid(row=9, column=0, columnspan=3, pady=(25, 10))
	signUpCPassword = tk.CTkEntry(signupPageFrameContents, placeholder_text="Confirm Password", show="*", font=("Calibri", 20), width=350, height=50)
	signUpCPassword.grid(row=10, column=0, columnspan=3, pady=(0, 10))
	signUpShowCPassLabel = tk.CTkButton(signupPageFrameContents, text="Show", font=("Calibri", 20), width=20, command=lambda:showPass("signUpShowCPassLabel", "signUpCPassword"))
	signUpShowCPassLabel.grid(row=9, column=1, columnspan=3, pady=(25, 10))

	signUpButton = tk.CTkButton(signupPageFrameContents, text="Sign Up", font=("Berlin Sans FB Demi", 20), width=250, height=50, command=createNewUser)
	signUpButton.grid(row=11, column=0, columnspan=3, pady=(30, 0))
	signUpLoginButton = tk.CTkButton(signupPageFrameContents, text="I already have an account\nLogin Instead?", fg_color="transparent", font=("Calibri", 20), width=20, command=loginPage)
	signUpLoginButton.grid(row=12, column=0, columnspan=3, pady=(25, 10))


def loginPage(event=None):
	def loginUser():
		found = 0
		if loginEmail.get() == "" or loginPassword.get() == "":
			msgbox.showerror("INVALID", "One or more text fields are empty")
		elif "@" not in loginEmail.get() or "." not in loginEmail.get():
			msgbox.showerror("INVALID", "Invalid email ID")
		else:
			pswd = ""
			for i in cur.execute("""SELECT * FROM users"""):
				if loginEmail.get() in i:				# If user found
					pswd = i[4]
					found = 1
					break

			if found == 1:
				if loginPassword.get() == pswd:
					cur.execute(
						f"""
						UPDATE users
						SET active = 1
						WHERE email = '{loginEmail.get()}'
						"""
					)
					users.commit()
					msgbox.showinfo("SUCCESS", "Logged in successfully :)")
					homePage()
				else:
					msgbox.showerror("INVALID", "Incorrect credentials")
			else:
				newUserMsgBox = msgbox.askyesno("NOT FOUND", "This user was not found.\n Want to create a new user instead?")
				if newUserMsgBox:
					signupPage()


	destroyOldPages()
	pages["loginPageFrame"] = True
	global loginPageFrame, loginShowPassLabel, loginPassword
	loginPageFrame = tk.CTkFrame(root)
	loginPageFrame.pack(fill=tk.BOTH, expand=True)

	loginPageBtnsFrame = tk.CTkFrame(loginPageFrame, fg_color="transparent")
	loginPageBtnsFrame.pack(pady=10, anchor="nw")
	buttonHome = tk.CTkButton(loginPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100,  corner_radius=15, command=homePage)
	buttonHome.grid(row=0, column=1, padx=10, pady=(0, 10))
	loginPageFrameContents = tk.CTkFrame(loginPageFrame, fg_color="transparent")
	loginPageFrameContents.pack(pady=10, anchor="center")

	loginText = tk.CTkLabel(loginPageFrameContents, text="LOGIN", font=("Berlin Sans FB Demi", 50))
	loginText.grid(row=0, column=0, columnspan=2, pady=(0, 50))

	loginEmailLabel = tk.CTkLabel(loginPageFrameContents, text="Email ID", font=("Calibri", 20))
	loginEmailLabel.grid(row=1, column=0, columnspan=2, pady=(25, 10))
	loginEmail = tk.CTkEntry(loginPageFrameContents, placeholder_text="Email ID", font=("Calibri", 20), width=350, height=50)
	loginEmail.grid(row=2, column=0, columnspan=2, pady=(0, 10))

	loginPasswordLabel = tk.CTkLabel(loginPageFrameContents, text="Password", font=("Calibri", 20))
	loginPasswordLabel.grid(row=3, column=0, columnspan=2, pady=(25, 10))
	loginPassword = tk.CTkEntry(loginPageFrameContents, placeholder_text="Password", show="*", font=("Calibri", 20), width=350, height=50)
	loginPassword.grid(row=4, column=0, columnspan=2, pady=(0, 10))
	loginShowPassLabel = tk.CTkButton(loginPageFrameContents, text="Show", font=("Calibri", 20), width=20, command=lambda:showPass("loginShowPassLabel", "loginPassword"))
	loginShowPassLabel.grid(row=3, column=1, columnspan=2, pady=(25, 10))

	loginButton = tk.CTkButton(loginPageFrameContents, text="Login", font=("Berlin Sans FB Demi", 20), width=250, height=50, command=loginUser)
	loginButton.grid(row=5, column=0, columnspan=2, pady=(30, 0))
	loginsignUpButton = tk.CTkButton(loginPageFrameContents, text="New to this app?\nCreate account", fg_color="transparent", font=("Calibri", 20), width=20, command=signupPage)
	loginsignUpButton.grid(row=6, column=0, columnspan=3, pady=(25, 10))


def profile(event=None):
	def logout():
		cur.execute(
			f"""
			UPDATE users
			SET active = 0
			WHERE active = 1
			"""
		)

		users.commit()

		msgbox.showinfo("SUCCESS", "Logged out successfully\nSayonara, Amigo")
		homePage()

	prof = 0

	x = ()
	for i in cur.execute("""SELECT * FROM users"""):
		if i[5] == 1:
			x = i
			prof = 1
			break

	users.commit()

	if prof == 0:
		loginPage()
	else:
		destroyOldPages()
		pages["profileFrame"] = True
		global profileFrame
		profileFrame = tk.CTkFrame(root)
		profileFrame.pack(fill=tk.BOTH, expand=True)

		profileBtnsFrame = tk.CTkFrame(profileFrame, fg_color="transparent")
		profileBtnsFrame.pack(pady=10, anchor="nw")
		buttonHome = tk.CTkButton(profileBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100, corner_radius=15, command=homePage)
		buttonHome.grid(row=0, column=1, padx=10, pady=(0, 10))
		profileFrameContents = tk.CTkFrame(profileFrame, fg_color="transparent")
		profileFrameContents.pack(pady=10, anchor="center")

		profileText = tk.CTkLabel(profileFrameContents, text="PROFILE", font=("Berlin Sans FB Demi", 50))
		profileText.grid(row=0, column=0, columnspan=2, pady=(0, 50))

		profileNameLabel = tk.CTkLabel(profileFrameContents, text="NAME", font=("Calibri", 20))
		profileNameLabel.grid(row=1, column=0, pady=20, sticky=tk.W)
		profileName = tk.CTkLabel(profileFrameContents, text=(f"{x[0]} {x[1]}"), font=("Calibri", 20))
		profileName.grid(row=1, column=1, padx=100, pady=20, sticky=tk.W)

		profilePhNoLabel = tk.CTkLabel(profileFrameContents, text="PHONE NUMBER", font=("Calibri", 20))
		profilePhNoLabel.grid(row=2, column=0, pady=20, sticky=tk.W)
		profilePhNo = tk.CTkLabel(profileFrameContents, text=x[2], font=("Calibri", 20))
		profilePhNo.grid(row=2, column=1, padx=100, pady=20, sticky=tk.W)

		profileEmailLabel = tk.CTkLabel(profileFrameContents, text="EMAIL ID", font=("Calibri", 20))
		profileEmailLabel.grid(row=3, column=0, pady=20, sticky=tk.W)
		profileEmail = tk.CTkLabel(profileFrameContents, text=x[3], font=("Calibri", 20))
		profileEmail.grid(row=3, column=1, padx=100, pady=20, sticky=tk.W)

		profileButton = tk.CTkButton(profileFrameContents, text="LOGOUT", font=("Berlin Sans FB Demi", 20), width=250, height=50, command=logout)
		profileButton.grid(row=11, column=0, columnspan=3, pady=(30, 0))


def homePage(event=None):
	destroyOldPages()
	pages["homePageFrame"] = True
	global homePageFrame
	homePageFrame = tk.CTkFrame(root)
	homePageFrame.pack(fill=tk.BOTH, expand=True)
	# bkg("homePageFrame")
	# buttonHome = tk.Button(mainCanvas, text="...", width=10, height=4, command=leftNav)
	# buttonHome.place(x=10, y=10)

	# homePageHeadFrame = tk.CTkFrame(homePageFrame, fg_color="transparent")
	# homePageHeadFrame.pack(side=tk.TOP, pady=50)

	buttonHome = tk.CTkButton(homePageFrame, text="User", font=("Berlin Sans FB Demi", 25), width=100, height=100, command=profile, corner_radius=15)
	# buttonHome = tk.CTkButton(homePageFrame, text="_\n(_)\n/|\\\n/\\\n", font=("Consolas", 20, "bold"), width=150, height=150, command=profile, corner_radius=15)
	# buttonHome = tk.CTkButton(homePageFrame, text="", width=50, height=50, command=profile, corner_radius=15, image=tk.CTkImage(dark_image=Image.open(r".\assets\img\user_icon.png")), fg_color="black")
	buttonHome.pack(padx=10, pady=10, anchor="ne")
	buttonPlay = tk.CTkLabel(homePageFrame, text="G-12 Plus", font=("Berlin Sans FB Demi", 125), width=300, height=100, corner_radius=25)
	# buttonPlay.grid(row=0, column=0, pady=10)
	buttonPlay.pack(side=tk.TOP, pady=50)
	# buttonLogin = tk.CTkButton(homePageFrame, text="Login", font=("Berlin Sans FB Demi", 20), width=300, height=100, corner_radius=15, command=loginPage)
	# buttonLogin.pack(side=tk.TOP, pady=50, anchor="ne")

	homePageBtnsFrame = tk.CTkFrame(homePageFrame, fg_color="transparent")
	homePageBtnsFrame.pack(side=tk.BOTTOM, pady=50)
	buttonPlay = tk.CTkButton(homePageBtnsFrame, text="PLAY", font=("Berlin Sans FB Demi", 30), command=playPage, width=350, height=125, hover_color="#144870", corner_radius=25)
	buttonPlay.grid(row=0, column=0, pady=10)
	# buttonStats = tk.Button(homePageBtnsFrame, text="STATS", font=("Berlin Sans FB Demi", 20), command=statsPage, width=350, height=125, , hover_color="#144870", corner_radius=25)
	# buttonStats.grid(row=1, column=0, pady=10)
	buttonQuit = tk.CTkButton(homePageBtnsFrame, text="QUIT GAME", font=("Berlin Sans FB Demi", 30), command=root.destroy, width=350, height=125, hover_color="#144870", corner_radius=25)
	buttonQuit.grid(row=2, column=0, pady=10)


def playPage(event=None):
	destroyOldPages()
	pages["playPageFrame"] = True
	global playPageFrame
	playPageFrame = tk.CTkFrame(root)
	playPageFrame.pack(fill="both", expand=True)
	# root.bind('<Escape>', homePage)
	buttonHome = tk.CTkButton(playPageFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100, command=homePage, corner_radius=15)
	buttonHome.pack(padx=10, pady=10, anchor="nw")

	OptnsFrame = tk.CTkFrame(playPageFrame, fg_color="transparent")
	OptnsFrame.pack(side=tk.TOP, pady=10)
	playPage = tk.CTkLabel(OptnsFrame, text="What do you want to play?", font=("Berlin Sans FB Demi", 50))
	playPage.grid(row=0, column=0, pady=(0, 50))
	game1Button = tk.CTkButton(OptnsFrame, text="FPB", font=("Berlin Sans FB Demi", 25), width=400, height=100, corner_radius=15, command=game1FPB)
	game1Button.grid(row=1, column=0, pady=10)
	game2Button = tk.CTkButton(OptnsFrame, text="Guess the Number", font=("Berlin Sans FB Demi", 25), width=400, height=100, corner_radius=15, command=game2GuessNum)
	game2Button.grid(row=2, column=0, pady=10)
	# game3Button = tk.CTkButton(OptnsFrame, text="KBT", font=("Berlin Sans FB Demi", 25), width=400, height=100, corner_radius=15, command=game3KBC)
	# game3Button.grid(row=3, column=0, pady=10)
	pass


def statsPage(event=None):
	destroyOldPages()
	pages["statsPageFrame"] = True
	global statsPageFrame
	statsPageFrame = tk.CTkFrame(root)
	statsPageFrame.pack(fill="both", expand=True)


# GAMES START


def game1FPB(event=None):
	global ctr, att, n, d, outRow
	ctr = 1
	outRow = 5
	d = 3
	tries = {3: 10, 4: 15, 5: 20, 6: 30, 7: 45, 8: 55, 9: 70, 10: 80}
	att = tries[d]
	letters = random.sample('0123456789', d)
	if letters[0] == '0':
		letters.reverse()
	n = ''.join(letters)
	FPBNumList = []

	# print(n)

	def FPBSubmit(event=None):
		global outRow
		g = FPBInputBox.get()
		if g in FPBNumList:
			FPBOutputShowLabel.configure(text="You guessed the same wrong number again. Try another number.")
		else:
			FPBNumList.append(g)
			if (g.isdigit() == True) and (int(g) >= 100 and int(g) <= 999) and (g[0] != g[1] and g[1] != g[2] and g[2] != g[0]):
				g = str(int(g))
				global ctr
				if ctr <= 10:
					ctr += 1
				FPBInputLabel.configure(text="Guess #" + str(ctr) + ": ")
				FPBOutputShowLabel.configure(text="")
				hint = []
				for i in range(d):
					if g[i] == n[i]:
						hint.append("FERMI")
					elif g[i] in n:
						hint.append("PICO")
				if hint == []:
					hint.append("BAGELS")
				random.shuffle(hint)
				hint = " ".join(hint)
				FPBTriesKeysLabel = tk.CTkLabel(gameFPBPageContentFrame, text=g, font=("Calibri", 20))
				FPBTriesKeysLabel.grid(row=outRow, column=4, pady=10)
				FPBTriesValuesLabel = tk.CTkLabel(gameFPBPageContentFrame, text=hint, font=("Calibri", 20))
				FPBTriesValuesLabel.grid(row=outRow, column=5, pady=10)
				outRow += 1
				if hint == "FERMI FERMI FERMI":
					ctr -= 1
					root.bind('<Return>', game1FPB)
					FPBInputSubmitButton.configure(text="GAME COMPLETED", command=game1FPB, width=300)
					FPBInputBox.delete(0, tk.END)
					FPBInputBox.configure(state="disabled")
					FPBOutputShowLabel.configure(text=("You guessed the right number in " + str(ctr) + " tries."), font=("Berlin Sans FB Demi", 25))
				else:
					FPBOutputShowLabel.configure(text=hint)
				FPBInputBox.delete(0, tk.END)
			else:
				if (g.isdigit() == False):
					FPBOutputShowLabel.configure(text="Input must be an integer only. Try again.")
				elif (int(g) < 100 or int(g) > 999):
					FPBOutputShowLabel.configure(text="Input must have exactly 3 digits. Try again.")
				elif (g[0] == g[1] or g[1] == g[2] or g[2] == g[0]):
					FPBOutputShowLabel.configure(text="Input must not have repetitive digits. Try again.")
				else:
					FPBOutputShowLabel.configure(text="Something went wrong. Try again.")
		if ctr > att:
			root.bind('<Return>', game1FPB)
			FPBInputSubmitButton.configure(text="Game Over", command=game1FPB, width=200)
			FPBOutputShowLabel.configure(text=("The number I thought was: " + n), font=("Berlin Sans FB Demi", 25))

	destroyOldPages()
	pages["gameFPBPageFrame"] = True
	global gameFPBPageFrame
	gameFPBPageFrame = tk.CTkFrame(root)
	gameFPBPageFrame.pack(fill="both", expand=True)

	gameFPBPageBtnsFrame = tk.CTkFrame(gameFPBPageFrame, fg_color="transparent")
	gameFPBPageBtnsFrame.pack(pady=10, anchor="nw")
	# buttonHome = tk.CTkButton(gameFPBPageBtnsFrame, text="Home", font=("Berlin Sans FB Demi", 20), width=100, height=100, corner_radius=15, command=homePage, )
	# buttonHome.grid(row=0, column=0, padx=10, pady=(0,10))
	# root.bind('<Escape>', playPage)
	buttonHome = tk.CTkButton(gameFPBPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100,
							  corner_radius=15, command=playPage)
	buttonHome.grid(row=0, column=0, padx=10, pady=(0, 10))
	FPBTitle = tk.CTkLabel(gameFPBPageBtnsFrame, text="Fermi-Pico-Bagels", font=("Berlin Sans FB Demi", 50))
	FPBTitle.grid(row=0, column=1, pady=10, columnspan=10)

	gameFPBPageContentFrame = tk.CTkFrame(gameFPBPageFrame, fg_color="transparent")
	gameFPBPageContentFrame.pack(pady=10, anchor="center")
	FPBInstructions = tk.CTkLabel(gameFPBPageContentFrame,
								  text="FERMI means 'ONE DIGIT IS CORRECT AND IN THE RIGHT POSITION.'\nPICO means 'ONE DIGIT IS CORRECT BUT IN THE WRONG POSITION.'\nBAGELS means 'NO DIGIT IS CORRECT.'\nThere are no repeated digits in the number.",
								  font=("Calibri", 25))
	FPBInstructions.grid(row=1, column=0, pady=10, columnspan=10)

	FPBInputLabel = tk.CTkLabel(gameFPBPageContentFrame, text=("Guess #" + str(ctr) + ": "),
								font=("Berlin Sans FB Demi", 25))
	FPBInputLabel.grid(row=2, column=4, pady=10)
	FPBInputBox = tk.CTkEntry(gameFPBPageContentFrame, font=("Berlin Sans FB Demi", 25), width=200, height=50)
	FPBInputBox.grid(row=2, column=5, pady=10)
	FPBInputBox.focus()
	# FPBInputSubmitButton = tk.CTkButton(gameFPBPageContentFrame, text="Check", font=("Berlin Sans FB Demi", 25), width=150, height=75, corner_radius=10, , command=lambda:FPBSubmit())
	root.bind('<Return>', FPBSubmit)
	FPBInputSubmitButton = tk.CTkButton(gameFPBPageContentFrame, text="Check", font=("Berlin Sans FB Demi", 25), width=150,
										height=75, corner_radius=10, command=FPBSubmit)
	FPBInputSubmitButton.grid(row=3, column=0, columnspan=10, pady=10)
	FPBOutputShowLabel = tk.CTkLabel(gameFPBPageContentFrame, text="", font=("Calibri", 20), text_color="red")
	FPBOutputShowLabel.grid(row=4, column=0, columnspan=10, pady=10)


def game2GuessNum(event=None):
	global ctr, n
	ctr = 1
	n = random.randint(100, 999)
	# print(n)
	guessNumLst = []

	def GuessSubmit(event=None):
		global ctr
		g = GuessInputBox.get()
		if g in guessNumLst:
			GuessOutputShowLabel.configure(text="You guessed the same wrong number again. Try another number.")
		else:
			if not g.isdigit():
				GuessOutputShowLabel.configure(text="Input must be an integer only. Try again.")
			elif len(g) != 3:
				GuessOutputShowLabel.configure(text="Input must have 3 digits only. Try again.")
			else:
				g = int(g)
				if g < 100 or g > 999:
					GuessOutputShowLabel.configure(text="Input must be in the range of 100 to 999 only. Try again.")
				else:
					ctr += 1
					guessNumLst.append(str(g))
					if len(guessNumLst) % 25 == 0:
						guessNumLst.append("\n")
					if g > n:
						GuessOutputShowLabel.configure(text="Think of a smaller number.")
					elif g < n:
						GuessOutputShowLabel.configure(text="Think of a bigger number.")
					else:
						ctr -= 1
						root.bind('<Return>', game2GuessNum)
						GuessInputSubmitButton.configure(text="GAME COMPLETED", command=game2GuessNum, width=300)
						GuessInputBox.delete(0, tk.END)
						GuessInputBox.configure(state="disabled")
						GuessOutputShowLabel.configure(text=("You guessed the right number in " + str(ctr) + " tries."), font=("Berlin Sans FB Demi", 25))
					GuessInputBox.delete(0, tk.END)
					GuessInputLabel.configure(text=("Guess #" + str(ctr) + ": "))
					GuessOutputShowLstLabel.configure(text=guessNumLst)
		# print()
		if ctr > 15:
			root.bind('<Return>', game2GuessNum)
			GuessInputSubmitButton.configure(text="Game Over", command=game2GuessNum, width=200)
			GuessOutputShowLabel.configure(text=("The number I thought was: " + str(n)), font=("Berlin Sans FB Demi", 25))


	destroyOldPages()
	pages["gameGuessPageFrame"] = True
	global gameGuessPageFrame
	gameGuessPageFrame = tk.CTkFrame(root)
	gameGuessPageFrame.pack(fill="both", expand=True)

	gameGuessPageBtnsFrame = tk.CTkFrame(gameGuessPageFrame, fg_color="transparent")
	gameGuessPageBtnsFrame.pack(pady=10, anchor="nw")
	# buttonHome = tk.CTkButton(gameGuessPageBtnsFrame, text="Home", font=("Berlin Sans FB Demi", 20), width=100, height=100, corner_radius=15, command=homePage, )
	# buttonHome.grid(row=0, column=0, padx=10, pady=(0,10))
	# root.bind('<Escape>', playPage)
	buttonHome = tk.CTkButton(gameGuessPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100, corner_radius=15, command=playPage)
	buttonHome.grid(row=0, column=0, padx=10, pady=(0, 10))
	guessTitle = tk.CTkLabel(gameGuessPageBtnsFrame, text="Guess The Number", font=("Berlin Sans FB Demi", 50))
	guessTitle.grid(row=0, column=1, pady=10, columnspan=10)

	gameGuessPageContentFrame = tk.CTkFrame(gameGuessPageFrame, fg_color="transparent")
	gameGuessPageContentFrame.pack(pady=10, anchor="center")
	GuessInstructions = tk.CTkLabel(gameGuessPageContentFrame,
		text="Guess the number is a puzzle-based number game.\nYou have to guess a 3 digit number, for which certain hints will be provided.\n\nHow to Play:\nYou have to guess the number which is chosen by the computer.\nYou will be given 15 tries to do so.\nYou will be told after each answer that whether the number chosen by the computer is higher or lesser than what you guessed.",
		font=("Calibri", 25))
	GuessInstructions.grid(row=0, column=0, pady=10, columnspan=10)

	GuessInputLabel = tk.CTkLabel(gameGuessPageContentFrame, text=("Guess #" + str(ctr) + ": "), font=("Berlin Sans FB Demi", 25))
	GuessInputLabel.grid(row=1, column=4, pady=10)
	GuessInputBox = tk.CTkEntry(gameGuessPageContentFrame, font=("Berlin Sans FB Demi", 25), width=200, height=50)
	GuessInputBox.grid(row=1, column=5, pady=10)
	GuessInputBox.focus()
	# FPBInputSubmitButton = tk.CTkButton(gameFPBPageContentFrame, text="Check", font=("Berlin Sans FB Demi", 25), width=150, height=75, corner_radius=10, , command=lambda:FPBSubmit())
	root.bind('<Return>', GuessSubmit)
	GuessInputSubmitButton = tk.CTkButton(gameGuessPageContentFrame, text="Check", font=("Berlin Sans FB Demi", 25), width=150,
										  height=75, corner_radius=10, command=GuessSubmit)
	GuessInputSubmitButton.grid(row=2, column=0, columnspan=10, pady=10)
	GuessOutputShowLabel = tk.CTkLabel(gameGuessPageContentFrame, text="", font=("Calibri", 20),
									   text_color="red")
	GuessOutputShowLabel.grid(row=3, column=0, columnspan=10, pady=10)
	GuessOutputShowLstLabel = tk.CTkLabel(gameGuessPageContentFrame, text="", font=("Calibri", 20))
	GuessOutputShowLstLabel.grid(row=4, column=0, columnspan=10, pady=10)


def game3KBC(event=None):
	destroyOldPages()
	pages["gameKBCPageFrame"] = True
	global gameKBCPageFrame
	gameKBCPageFrame = tk.CTkFrame(root)
	gameKBCPageFrame.pack(fill="both", expand=True)

	gameKBCPageBtnsFrame = tk.CTkFrame(gameKBCPageFrame, fg_color="transparent")
	gameKBCPageBtnsFrame.pack(pady=10, anchor="nw")
	# buttonHome = tk.CTkButton(gameKBCPageFrame, text="Home", font=("Berlin Sans FB Demi", 20), width=100, height=100, corner_radius=15, command=homePage, )
	# buttonHome.grid(row=0, column=0, padx=10, pady=(0,10))
	# root.bind('<Escape>', playPage)
	buttonHome = tk.CTkButton(gameKBCPageBtnsFrame, text="Back", font=("Berlin Sans FB Demi", 25), width=100, height=100, corner_radius=15, command=playPage)
	buttonHome.grid(row=0, column=0, padx=10, pady=(0, 10))
	KBCTitle = tk.CTkLabel(gameKBCPageBtnsFrame, text="Kaun Banega Trollpati", font=("Berlin Sans FB Demi", 50))
	KBCTitle.grid(row=0, column=1, pady=10, columnspan=10)

	gameKBCPageContentFrame = tk.CTkFrame(gameKBCPageFrame, fg_color="transparent")
	gameKBCPageContentFrame.pack(pady=10, anchor="center")


# GAMES END


homePage()

root.mainloop()
users.close()

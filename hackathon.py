from tkinter import *

root = Tk()
root.title("College Information Chatbot")
BG_GRAY = "#B6B6B6"
BG_COLOR = "#FFFFFF"
TEXT_COLOR = "#000000"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
	 
	send =  "You:" + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello" or user == "hi" or user == "hii"):
		txt.insert(END, "\n" + "Bot: Hi there, how can I help?\n Here are some frequently asked questions:\n 1- Course offered ? \n2- Admission Related Enquiry \n3- Major recruiters ?\n4- Events ?\n5- Facilities Offered?\n6- Emergency")

	elif (user == "admission" or user == "Admission related enquiry" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot: For admission related enquiries please refer to Official CET Cell website: https://cetcell.mahacet.org\n  You'll be asked to login using your email id on CET CELL\n")

	elif (user == "events" or user == "Could you tell me more about events taking place in college"):
		txt.insert(END, "\n" + "Bot: Welcome to the College Events Information Section \n We have number of events organised by the college \n Some of the Events organised by us are \n 1.The Grant Event Zephrs\n2.Freshers for the new students\n3.Various department level Fests by Every Department\n3.Hackathons\n4.Games Competition\n5.Varioius Events on Festivals\n6.Orientation programs"
      "\n 7.Tantragyan \n 8.Robocon \n 9.Seminars \n 10.Event Calender \n ")
		
	elif (user == "amenities" or user == "What are amenities provided by the college" or user == "Facilities"):
		txt.insert(END, "\n" + "Bot: Numerous amenities are made available for students \n ------------------------------------------------------ \n * Building Area\n* Computing facilities\n* Seminar halls \n* E-library\n* Counselling cell\n*"
      " Training and placement cell\n* Student clubs\n* Student internships\n* Canteen services\n"
      "* sports \n ")

	elif (user == "programs" or user == "Which programs are offered by the college" or user == "Course offered"):
		txt.insert(END, "\n" + "Bot: Programs Offered \n ------------------- \n * U.G (B.E) Program \n    -Computer Engineering\n    -Mechanical Engineering\n    -Electrical Engineering\n    -Electronics & Telecom. Engineering\n    -CSE (Data Science)\n    -CSE (AI & ML)\n    -CSE (IoT and Cyber Security)\n* P.G( M.E) Program    -Computer Engineering\n    -Mechanical Engineering\n* DOCTORATE (PH.D.)Program    -Computer Engineering\n    -Mechanical Engineering\n ")

	elif (user == "emergency" or user == "Where should I contact during emergencies"):
		txt.insert(END, "\n" + "Bot: In case of Emergency services immediately call for \n * Campus security- 022-27541005\n* Police Helpline- 100\n* Ambulance- 102,108\n* Fire Helpline- 101")

	elif (user == "recruiters" or user == "What are major recruiters of college" or user == "Major recruiters"):
		txt.insert(
			END, "\n" + "Bot: Major Recruiters in our college are: \n -> AWS\n -> IBM\n -> Tata Consultancy Services\n -> Infosys\n -> LTI\n -> Jio\n -> Capgemini\n -> accenture\n -> HCl")

	elif (user == "details" or user == "Tell me details about college"):
		txt.insert(END, "\n" + "Bot: \n Our college is located at-\nLokmanya Tilak College of Engineering,Vikas Nagar, Gyan Vikas Sector 4, Kopar Khairane, Navi Mumbai, Maharashtra 400709\nContacts info-\nMobile/Telephone No- +91-022-27541005/+91-022-27541006\nEmail id- principal@ltce.in\nprincipal.ltce@gmail.com")

	else:
		txt.insert(END, "\n" + "Bot: Sorry! I didn't understand that")

	e.delete(0, END)

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()



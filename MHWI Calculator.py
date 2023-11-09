import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

win=tk.Tk()
win.geometry('1030x640')
win.title('傷害計算程式 Ver 0.1')
#f = open(r'C:\Users\brfiveonze\Desktop\pyt\1.txt')
#word=f.read()
#print(word)
#f.close()

#**********************************4捨5入函式***********************************

def FOFI(a):
	b=a-int(a)
	if b<0.5:
		a=int(a)
	else:
		a=int(a)+1
	return a

#******************************Label設定名稱 位置*******************************

lb1=tk.Label(text='武器基礎面板').grid(row=0)
lb2=tk.Label(text='武器種類').grid(row=0,column=1)
lb3=tk.Label(text='物理肉質').grid(row=0,column=2)
lb4=tk.Label(text='屬性肉質').grid(row=2,column=2)
lb5=tk.Label(text='其他增益').grid(row=0,column=4,columnspan=7)
buff=tk.Label(text='貓飯增益').grid(row=0,column=11,columnspan=4)
skill=tk.Label(text='攻擊').grid(row=1,column=7)
skill=tk.Label(text='挑戰者').grid(row=1,column=8)
skill=tk.Label(text='火場怪力').grid(row=1,column=9)
skill=tk.Label(text='怨恨').grid(row=1,column=10)
lb11=tk.Label(text='面板屬性').grid(row=2,column=0)
lb12=tk.Label(text='發怒補正(百分比)').grid(row=0,column=3)
skill=tk.Label(text='無傷').grid(row=3,column=7)
skill=tk.Label(text='轉禍為福').grid(row=3,column=8)
lb16=tk.Label(text='套裝').grid(row=2,column=11,columnspan=2)
lb17=tk.Label(text='斬味').grid(row=2,column=1)
skill=tk.Label(text='超會心').grid(row=3,column=9)
skill=tk.Label(text='屬性強化').grid(row=5,column=7)
skill=tk.Label(text='攻擊守勢').grid(row=5,column=8)
lb19=tk.Label(text='冥赤套(0/3/5)').grid(row=3,column=11,columnspan=2)
lb19=tk.Label(text='冰咒套(0/2/4)').grid(row=3,column=13,columnspan=2)
lb19=tk.Label(text='溟波套(0/2/4)').grid(row=5,column=11,columnspan=2)
lb19=tk.Label(text='煌黑套(0/2/3)').grid(row=5,column=13,columnspan=2)
block=tk.Label(text='物理動作值').grid(row=4,column=0)
block=tk.Label(text='屬性動作值').grid(row=4,column=1)
Damage=tk.Label(text='基礎物理攻擊').grid(row=7,column=0)
Damage=tk.Label(text='物理傷害').grid(row=8,column=0)
Damage=tk.Label(text='基礎屬性攻擊').grid(row=7,column=2)
Damage=tk.Label(text='屬性傷害').grid(row=8,column=2)
Damage=tk.Label(text='總傷害').grid(row=9,column=0)

#lb100=tk.Label(text='貓飯').grid(row=3,column=9)

#***********************Tkinter變量宣告***************************************************

var1 = tk.IntVar()         #鬼人粉
var2 = tk.IntVar()         #鬼人藥大小
var3 = tk.IntVar()         #怪力種 藥
var4 = tk.StringVar()      #面板攻擊
var5 = tk.StringVar()      #屬性攻擊
var6 = tk.StringVar()      #物理肉質
var7 = tk.StringVar()      #屬性肉質
var8 = tk.StringVar()      #物理攻擊
var9 = tk.IntVar()         #力護
var10 = tk.IntVar()        #力爪
var11 = tk.IntVar()        #短催
var12 = tk.StringVar()     #發怒
var13 = tk.StringVar()     #基礎屬性攻擊
var14 = tk.StringVar()     #屬性傷害
var15 = tk.StringVar()     #物理動作值
var16 = tk.StringVar()     #屬性動作值
var17 = tk.IntVar()        #屬會
var18 = tk.IntVar()        #真屬會
var60 = tk.StringVar()     #總傷害
var50 = tk.StringVar()     #物理傷害
var100 = tk.IntVar()       #貓火
var111 = tk.IntVar()       #無屬性強化

var4.set('')
var5.set('')
var6.set('')
var7.set('')
var12.set('')

wpp=[4.8,3.3,1.4,1.4,2.3,2.3,5.2,4.2,3.5,3.6,3.1,1.3,1.5,1.2]       #武器倍率1
wp2=0.0;                                                            #武器倍率2
wapen=['大劍','太刀','片手',\
'雙刀','長槍','銃槍','槌子',\
'狩獵笛','劍斧','盾斧','蟲棍',\
'輕弩','重弩','弓箭']                                               #武器種類
lv3=['無','LV1','LV2','LV3']                                        #技能等級LV3
lv5=['無','LV1','LV2','LV3','LV4','LV5']                            #技能等級LV5
lv6=['無','LV1','LV2','LV3','LV4','LV5','LV6']                      #技能等級LV6
lv7=['無','LV1','LV2','LV3','LV4','LV5','LV6','LV7']                #技能等級LV7
shp=['紅','橙','黃','綠','藍','白','紫']                            #斬位
shpD=[0.5,0.75,1,1.05,1.2,1.32,1.39,0.25,0.5,0.75,1,1.0625,1.125,1.2]  #物理與屬性斬味倍率
CatFood=['無','攻擊小','攻擊中','攻擊大']                           #貓飯
fire=[1,1,1.05,1.05,1.1,1.15,1.25]                                  #人火倍率
skill1=['無','龍脈覺醒','真·龍脈覺醒']                              #冥赤套
sk=[1.6,2.2,2.55,24,12,9,0,8,15]                                    #冥赤套倍率/上限
skill2=['無','屬性會心','寒氣練成']                                 #冰咒套
skill3=['無','屬性加速','真·屬性加速']                              #溟波套
skill4=['無','屬耐轉換','全屬耐強化']                               #煌黑套
ElementPower=[1,1,1,1,1.05,1.1,1.2,0,3,6,10,10,10,10]

#**********************************動態變動元件************************************************

Attack=tk.Entry(width=5,textvariable=var4).grid(row=1)                         #武器面板
ElementAttack=tk.Entry(width=5,textvariable=var5).grid(row=3)                  #屬性面板
PhysicalFleshy=tk.Entry(width=5,textvariable=var6).grid(row=1,column=2)        #物理肉質
ElementFleshy=tk.Entry(width=5,textvariable=var7).grid(row=3,column=2)         #屬性肉質
PhysicalFleshy=tk.Entry(width=5,textvariable=var12).grid(row=1,column=3)       #發怒
en1=tk.Entry(width=5,textvariable=var15).grid(row=5,column=0)                  #物理動作值
en2=tk.Entry(width=5,textvariable=var16).grid(row=5,column=1)                  #屬性動作值

lb61=tk.Label(textvariable=var8).grid(row=7,column=1)                          #基礎物理攻擊
lb63=tk.Label(textvariable=var50).grid(row=8,column=1)                         #物理傷害
lb61=tk.Label(textvariable=var13).grid(row=7,column=3)                         #基礎屬性攻擊
lb63=tk.Label(textvariable=var14).grid(row=8,column=3)                         #屬性傷害
lb61=tk.Label(textvariable=var60).grid(row=9,column=1)                         #總傷害

def Magnification():
	EC=[1.0,-1]
	critical=1.25
	Total=0
	ET=1.6
	ATotal=0.0
	Aadd=0.0
	Apower=1.0
	ETotal=0.0
	Eadd=0.0
	Epower=1.0
	Angry=0
	sk2i=0
#**************判斷參數 技能 是否衝突或錯誤********************************

	ErrorID=[0,0,0,0,0,0,'武器面板',' 屬性面板',' 物理肉質',' 屬性肉質',' 物理動作值',' 屬性動作值',0]
	ErrorStr=''
	if (var4.get()==''):
		ErrorID[0]=1
	if (var5.get()==''):
		ErrorID[1]=1
	if (var6.get()==''):
		ErrorID[2]=1
	if (var7.get()==''):
		ErrorID[3]=1
	if (var15.get()==''):
		ErrorID[4]=1
	if (var16.get()==''):
		ErrorID[5]=1
	for i in range(6):
		if ErrorID[i]==1:
			ErrorID[12]=1
			ErrorStr=ErrorStr + ErrorID[6+i]
	if ErrorID[12]==1:
		messagebox.showerror('參數錯誤', '以下參數未寫入:' + ErrorStr)
		return

	if var12.get()=='0':
		messagebox.showerror('參數錯誤','發怒補正不可為0' + ErrorStr)
		return
	elif var12.get()=='':
		var12.set(1)
		messagebox.showinfo('提示','未輸入發怒補正，此參數將由1來取代')
	if (cb5.get()!='無' and cb6.get()!='無'):
		messagebox.showwarning('注意','「無傷」與「怨恨」無法同時並存 計算傷害將技能加最多的值')

#**************判定武器種類****************************************

	k1=var4.get()                                                #武器物理面板
	k2=var5.get()                                                #武器屬性面板
	k3=float(var6.get())/100                                     #物理肉質
	k4=float(var7.get())/100                                     #屬性肉質
	k5=float(var15.get())/100                                    #物理動作值
	k6=float(var16.get())/100                                    #屬性動作值
	k7=float(var12.get())/100                                    #發怒補正
	nime=cb1.get()
	if (nime==wapen[11] or nime==wapen[12]):
		messagebox.showerror('未開放', '開發中 無法使用!')
		return
	for i,j in zip(wapen,range(13)):
		if nime==i:
			if ((i=='大劍') or (i=='槌子') or (i=='狩獵笛')):
				EC[1]=j
			wp2=wpp[j]
			ATotal=float(k1)/wp2
			ETotal=float(k2)/10
			k1=ATotal                                   #真實物理值
			k2=ETotal                                   #真實屬性值

#*****************無屬性強化點選***************************************
	if var111.get():
		if ETotal<=0:
			ATotal=FOFI(float(k1)*1.05)
		else:
			messagebox.showwarning('注意','武器有屬性，無屬性強化無效')

#***************勾選型BUFF*****************************************

	if var1.get():
		ATotal=ATotal+10             #鬼人粉
	if var9.get():
		ATotal=ATotal+6              #力護
	if var10.get():
		ATotal=ATotal+9              #力爪
	if var11.get():
		ATotal=ATotal+9              #短催
	if var17.get() and var18.get():
		messagebox.showwarning('注意'\
,'真屬會 與 屬會 無法疊加 將取真屬會來計算')
		var17.set(False)             #屬會是否疊加
	if var17.get():
		if EC[1]==0 or EC[1]==6 or EC[1]==7:
			EC[0]=1.5
		else:
			EC[0]=1.35           #屬會
	if var18.get():
		if EC[1]==0 or EC[1]==6 or EC[1]==7:
			EC[0]=1.7
		else:
			EC[0]=1.55           #真屬會
	if var2.get()==1:
		ATotal=ATotal+5              #鬼藥
	elif var2.get()==2:
		ATotal=ATotal+7              #大鬼藥
	if var3.get()==1:
		ATotal=ATotal+10             #種子
	elif var3.get()==2:
		ATotal=ATotal+25             #藥丸

#********************下拉式選單************************************

	for i in range(3):
		if cb12.get()==skill1[i]:
			if k2<sk[i+3]:
				ET=k2+15                                     #屬性上限過低
			else:
				ET=k2*sk[i]                                  #屬性上限不變
			ET=FOFI(ET)
			Eadd=Eadd+sk[6+i]
		#if cb13.get()==skill2[i]:
	for i in range(1,4):
		if cb6.get()==lv3[i]:
			sk2i=sk2i+(5*i)                                      #無傷
			if i==3:
				sk2i=sk2i+5                                  #無傷3
			Aadd=Aadd+sk2i
		if cb9.get()==lv3[i]:
			critical=float(critical)+(0.05*i)
		if cb7.get()==lv3[i]:
			Aadd=Aadd+(9+3*i)                                    #轉福
			if ETotal>0:
				Eadd=Eadd+(3*i)
		if cb120.get()==CatFood[i]:
			Aadd=Aadd+(5*i)                                      #貓飯
	for i in range(1,6):
		if cb5.get()==lv5[i]:
			if sk2i<(5*i):
				Aadd=Aadd+(5*i)-sk2i                         #怨恨
				cb6.current(0)
			else:
				cb5.current(0)
	for i in range(0,7):
		if cb10.get()==lv6[i]:
			ETotal=ETotal*ElementPower[i]+ElementPower[i+7]      #屬性強化
	for i in range(0,8):
		if cb2.get()==lv7[i]:
			Aadd=Aadd+(3*i)                                      #攻擊LV
		if cb3.get()==lv7[i]:
			Aadd=Aadd+(4*i)                                      #挑戰LV
		if cb4.get()==lv7[i]:
			if i==7:
				Apower=Apower*1.4                            #人火7
			elif var100.get():
				Apower=Apower*1.35                           #有開貓火
			else:
				Apower=Apower*fire[i]                        #火場<7
				

#**************輸出************************************************

	k7=1
	ATotal=(ATotal+Aadd)*Apower
	ETotal=(ETotal+Eadd)*Epower
	if (FOFI(ATotal)<FOFI(k1)*2):
		var8.set(FOFI(ATotal))                                  #基礎物理面板未超過上限
	else:
		var8.set(FOFI(k1)*2)
		var8.set(var8.get()+'(至頂)')
		ATotal=FOFI(k1)*2                                       #基礎物理面板超過上限
	if k2<=0:
		ETotal=0
		var13.set(0)                                            #無屬性
	elif FOFI(ETotal)<ET:
		var13.set(FOFI(ETotal))
		ETotal=FOFI(ETotal)                                     #基礎屬性面板未超過上限
	else:
		var13.set(ET)
		var13.set(var13.get()+'(至頂)')
		ETotal=ET                                               #基礎屬性面板超過上限
	for i in range(0,7):
		if cb8.get()==shp[i]:
			AD=FOFI(float(ATotal)*shpD[i]*critical*k3*k5*k7)
			ED=FOFI(float(ETotal)*shpD[i+7]*k4*k6*EC[0]*k7)
			var50.set(AD)                                   #物理傷害
			var14.set(ED)                                   #屬性傷害
			var60.set(AD+ED)                                #總傷害

#*******************************************************************************************

def Gun():
	return

#*********************************下拉式選單************************************************

cb1=ttk.Combobox(width=5,values=wapen,state="readonly")                          #選擇武器
cb2=ttk.Combobox(width=5,values=lv7,state="readonly")                            #攻擊等級
cb3=ttk.Combobox(width=5,values=lv7,state="readonly")                            #挑戰等級
cb4=ttk.Combobox(width=5,values=lv7,state="readonly")                            #ＩＣＥ等級
cb5=ttk.Combobox(width=5,values=lv5,state="readonly")                            #怨恨等級
cb6=ttk.Combobox(width=5,values=lv3,state="readonly")                            #無傷等級
cb7=ttk.Combobox(width=5,values=lv3,state="readonly")                            #轉福等級
cb8=ttk.Combobox(width=5,values=shp,state="readonly")                            #斬位
cb9=ttk.Combobox(width=5,values=lv3,state="readonly")                            #超心
cb10=ttk.Combobox(width=5,values=lv6,state="readonly")                           #屬性強化
cb11=ttk.Combobox(width=5,values=lv3,state="disabled")                           #攻擊守勢
cb12=ttk.Combobox(width=10,values=skill1,state="readonly")                       #冥赤
cb13=ttk.Combobox(width=10,values=skill2,state="disabled")                       #冰咒
cb14=ttk.Combobox(width=10,values=skill3,state="disabled")                       #溟波
cb15=ttk.Combobox(width=10,values=skill4,state="disabled")                       #煌黑
cb120=ttk.Combobox(width=8,values=CatFood,state="readonly")                      #貓飯等級

#***********************點選型Button********************************************************

Item=Checkbutton(text='鬼人粉塵',variable=var1).grid(row=1,column=4)
Item=Radiobutton(text='無鬼人藥',variable=var2,value=0).grid(row=1,column=5)
Item=Radiobutton(text='鬼人藥',variable=var2,value=1).grid(row=2,column=5)
Item=Radiobutton(text='鬼人藥 大',variable=var2,value=2).grid(row=3,column=5)
Item=Radiobutton(text='無怪力',variable=var3,value=0).grid(row=1,column=6)
Item=Radiobutton(text='怪力種子',variable=var3,value=1).grid(row=2,column=6)
Item=Radiobutton(text='怪力藥丸',variable=var3,value=2).grid(row=3,column=6)
Item=Checkbutton(text='力之護符',variable=var9).grid(row=2,column=4)
Item=Checkbutton(text='力之爪',variable=var10).grid(row=3,column=4)
buff1=Checkbutton(text='短催',variable=var11).grid(row=1,column=12)
skill=Checkbutton(text='無屬性強化',variable=var111).grid(row=3,column=10)
skill=Checkbutton(text='不屈',variable=False,state="disabled").grid(row=4,column=10)
skill=Checkbutton(text='屬性擊[會心]',variable=var17).grid(row=5,column=9,columnspan=2)
skill=Checkbutton(text='真·屬性擊[會心]',variable=var18).grid(row=6,column=9,columnspan=2)
buff2=Checkbutton(text='貓火',variable=var100).grid(row=1,column=11)

cb1.current(0)
cb2.current(0)
cb3.current(0)
cb4.current(0)
cb5.current(0)
cb6.current(0)
cb7.current(0)
cb8.current(5)
cb9.current(3)
cb10.current(0)
cb11.current(0)
cb12.current(0)
cb13.current(0)
cb14.current(0)
cb15.current(0)
cb120.current(0)
cb1.grid(row=1,column=1)
cb2.grid(row=2,column=7)
cb3.grid(row=2,column=8)
cb4.grid(row=2,column=9)
cb5.grid(row=2,column=10)
cb6.grid(row=4,column=7)
cb7.grid(row=4,column=8)
cb8.grid(row=3,column=1)
cb9.grid(row=4,column=9)
cb10.grid(row=6,column=7)
cb11.grid(row=6,column=8)
cb12.grid(row=4,column=11,columnspan=2)
cb13.grid(row=4,column=13,columnspan=2)
cb14.grid(row=6,column=11,columnspan=2)
cb15.grid(row=6,column=13,columnspan=2)
cb120.grid(row=1,column=13)

bt1=tk.Button(text='計算',fg='skyblue',command=Magnification).grid(row=5,column=5)
win.mainloop()
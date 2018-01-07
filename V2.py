
# coding: utf-8

# ###-----------------------

# In[113]:

import numpy as np


# In[114]:

durum = np.zeros((10),dtype='int')


# In[115]:

durum


# In[116]:

hücrem = 0


# In[117]:

import turtle
from turtle import *
vn = turtle.Screen()
robo = turtle.Turtle()
engel = turtle.Turtle()

mode('world')
setworldcoordinates(0,91,91,0)

reset()


# In[118]:

#direction standard mode	logo mode
#0 - east     	0 - north
#90 - north	90 - east
#180 - west	180 - south
#270 - south	270 - west r row,c colon

def dön(yön):
    turtle.setheading(yön)
    robo.setheading(yön)
    return

def harflidön(harf):
    return {
        "u": 0,
        "d": 270,
        "l": 180,
        "r": 90
    } [harf]


# In[119]:

#Alanı çiz
robo.reset()
def çiz(x,y,boy):
    robo.penup()
    robo.setpos(x,y)
    robo.pendown()
    robo.forward(boy)

    return

çiz(0,0,30)
çiz(0,10,30)
çiz(0,20,30)
çiz(0,30,30)

dön(270)

çiz(30,30,30)
çiz(20,30,30)
çiz(10,30,30)
çiz(0,30,30)


# In[120]:

#cell numpad kurallarıyla
def cell(number):
    return {
        1: (5,25),
        2: (15,25),
        3: (25,25),
        4: (5,15),
        5: (15,15),
        6: (25,15),
        7: (5,5),
        8: (15,5),
        9: (25,5)
    } [number]


def Git(sayı):
    global hücrem
    global yeniyön
    
    if hücrem == sayı:
        return
    durum[sayı]=1
    yeniyön = yönbul(sayı)
    komşu = komşubul(hücrem)
    #dummyi = komşu.index(sayı)
    #harf = yeniyön.index(komşu(sayı))
    turtle.setpos(cell(sayı))
    hücrem = sayı

#durduğu hücreye göre yönünü gideceği hücreye çeviriyor    
def yönbul(hücre):
    return {
        1: ["u","r"],
        2: ["l","r","u"],
        3: ["l","u"],
        4: ["d","r","u"],
        5: ["d","l","r","u"],
        6: ["d","l","u"],
        7: ["d","r"],
        8: ["d","l","r"],
        9: ["d","l"]
    } [hücre]


def komşubul(current):
    return {
        1: [2,4],
        2: [1,3,5],
        3: [2,6],
        4: [1,5,7],
        5: [2,4,6,8],
        6: [3,5,9],
        7: [4,8],
        8: [5,7,9],
        9: [6,8]
    } [current]
    
    return



# In[121]:

def tara():
    global komşular,i
    turtle.speed(1)
    turtle.left(90)
    i = 0
    numlist = [1,2,3,6,5,4,7,8,9]
    while i < 9:
        if i < 8:
            if durum[numlist[i+1]] == 2:
                Git(numlist[i])
                komşular = komşubul(numlist[i])
                current=i
                for j in komşular:
                    if durum[j] == 0:
                        Git(j)
                        a=j
                        i = numlist.index(a)
                        i += 1
                if i==current:
                    for k in komşular:
                        if durum[k] == 1:
                            durum[k] = 3
                            Git(k)
                            a=k
                            i = numlist.index(a)
                            i += 1
            else:
                Git(numlist[i])
                if durum[numlist[i]]==0:
                    durum[numlist[i]]=1
                i += 1 
        else:
            Git(numlist[i])
            if durum[numlist[i]]==0:
                durum[numlist[i]]=1
            i += 1  
    return


# In[122]:

#bittikten sonra  sıfırları kontrol (durum haritasız)
def komşularıtara():
    for komşu in komşubul(hücrem):
        başlangıçhücrem = hücrem
        if durum[komşu]==0:
            Git(komşu)
            Git(başlangıçhücrem)


# In[123]:

#durumları sıfır olanlara ziyaret
def hedefeGit():
    return


# In[124]:

def engelkoy(sayı):
    global durum
    engel.setpos(cell(sayı))
    durum[sayı]=2


# In[125]:

#engel oluşturuyor
engel.penup()

engel.color("yellow")
engel.shape("circle")
engel.shapesize(3,3)



# In[126]:

#engel konuyor
engelkoy(3)


# In[127]:

turtle.reset()
turtle.penup()

turtle.color("pink")
turtle.shape("turtle")

turtle.shapesize(3,2)
turtle.setpos(5,5)



# In[128]:

#başlangıç
dön(270)
hücrem = 1
turtle.setpos(cell(1))

turtle.speed(1)


# In[129]:

#main
tara()
komşularıtara()


# In[130]:

durum


# # dönüş yönlerini ayarla

# # numlist olmadan gitmenin yoluna bak

# # hedefe gitmenin yoluna bak

# In[ ]:




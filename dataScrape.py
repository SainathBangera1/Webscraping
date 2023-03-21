# Importing BeautifulSoup and
# it is in the bs4 module
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import numpy as np

dataSetArray = []
ball_Array = []
jolly_Array = []
superStar_Array = []
date_ArrayString = []
############################################ DATE AND YEAR ############################################
date_Array = []
date_Test = []

for i in range(2009, 2024):
    year = i
    # Opening the html file. If the file
    # is present in different location,
    # exact location need to be mentioned
    #HTMLFileToBeOpened = open("htmlData/2006.html", "r")
    HTMLFileToBeOpened = open('htmlData/'+str(i)+".html", "r")

    # Reading the file and storing in a variable
    contents = HTMLFileToBeOpened.read()
    beautifulSoupText = BeautifulSoup(str(contents), 'html.parser')
    drawDate = beautifulSoupText.find_all('td', class_='date')

    for d in drawDate:
        date_Test.append(str(d.decode_contents()))

    # Eliminate the Superscript of Dates
    date = ['th', 'rd', 'st', 'nd']
    for x in range(len(date_Test)):
        for d in date:
            date_Test[x] = re.sub('<sup>'+d+'</sup>', ',', str(date_Test[x]))
    # Eliminate days from the Date_array
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        for x in range(len(date_Test)):
            date_Test[x] = re.sub('<span>'+day+'</span>',
                                  '', str(date_Test[x]))
    # Eliminate Month with their Numeric Value
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    for mn in months:
        for x in range(len(date_Test)):
            date_Test[x] = re.sub(mn, str(months[mn])+","+str(i),
                                  str(date_Test[x]))

    # clearing the extra space between the DD MM and YY
    for x in range(len(date_Test)):
        date_Test[x] = date_Test[x].replace(' ', '')

    date_Array.append(date_Test)
# need to take the zeroth element of this array as it repeats 26 times if not done so
date_Array = date_Array[0]

# Converting the String value of DD-MM-YY to numeric value of list [DD,MM, YY]
for x in range(len(date_Array)):
    date_Array[x] = date_Array[x].split(',')

# dateArrayString Carries all the list of Dates in String format
for z in range(len(date_Array)):
    date_ArrayString.append(date_Array[z][0]+' / ' +
                            date_Array[z][1]+' / '+date_Array[z][2])

# date_Array Carries all the list of Dates in list of integer format
for y in range(len(date_Array)):
    date_Array[y] = [int(date_Array[y][0]), int(
        date_Array[y][1]), int(date_Array[y][2])]


######################################## 1997 to 2005 #######################################################

# for i in range(1997, 2006):
#     year = i
#     # Opening the html file. If the file
#     # is present in different location,
#     # exact location need to be mentioned
#     #HTMLFileToBeOpened = open("htmlData/2006.html", "r")
#     HTMLFileToBeOpened = open('htmlData/'+str(i)+".html", "r")

#     # Reading the file and storing in a variable
#     contents = HTMLFileToBeOpened.read()

#     # Creating a BeautifulSoup object and
#     # specifying the parser
#     beautifulSoupText = BeautifulSoup(str(contents), 'html.parser')
#     balls = beautifulSoupText.find_all('ul', class_='balls')
#     # ball_Array = []
#     jolly = beautifulSoupText.find_all('li', class_='jolly')
#     # jolly_Array = []

#     for i in range(len(jolly)):
#         # jollyArray.append(jolly[i].decode_contents())
#         jolly_Array.append(int(jolly[i].decode_contents()))

#     # fillterdBallArray carries the 6 numbers filltered from the jolly and superstar numbers
#     fillterdBallArray = []
#     for i in range(len(balls)):
#         strING = str(balls[i])
#         bool = '<li class="jolly">' in strING
#         # bool2 = '<li class="superstar">' in strING
#         if (bool == False):
#             fillterdBallArray.append(balls[i])

#     for i in range(len(fillterdBallArray)):
#         daySetNum = []
#         daySetNum2 = []
#         for j in fillterdBallArray[i]:
#             daySetNum.append(j)
#         for k in range(len(daySetNum)):
#             if (not daySetNum[k] == ' '):
#                 daySetNum2.append(daySetNum[k])
#         setNum = []
#         for l in range(len(daySetNum2)):
#             for num in daySetNum2[l]:
#                 setNum.append(int(num))
#         ball_Array.append(setNum)

# for x in range(len(ball_Array)):
#     ball_Array[x].append(jolly_Array[x])
# dataSetArray = ball_Array
# print("Done with writing 1997 to 2005 Data")
################################################### ONLY 2006 ########################################################
# superstart numbers where introduced in this year after March 2006 hence the data is till jolly number only

# ball_Array = []
# jolly_Array = []
# HTMLFileToBeOpened = open('htmlData/2006.html', "r")

# # Reading the file and storing in a variable
# contents = HTMLFileToBeOpened.read()

# # Creating a BeautifulSoup object and
# # specifying the parser
# beautifulSoupText = BeautifulSoup(str(contents), 'html.parser')
# balls = beautifulSoupText.find_all('ul', class_='balls')
# # ball_Array = []
# jolly = beautifulSoupText.find_all('li', class_='jolly')

# # drawDate = beautifulSoupText.find_all('td', class_='date')
# # print(drawDate)


# for i in range(len(jolly)):
#     # jollyArray.append(jolly[i].decode_contents())
#     jolly_Array.append(int(jolly[i].decode_contents()))

# # fillterdBallArray carries the 6 numbers filltered from the jolly and superstar numbers
# fillterdBallArray = []
# for i in range(len(balls)):
#     strING = str(balls[i])
#     bool = '<li class="jolly">' in strING
#     bool2 = '<li class="superstar">' in strING
#     if (bool == False):
#         fillterdBallArray.append(balls[i])

# for i in range(len(fillterdBallArray)):
#     daySetNum = []
#     daySetNum2 = []
#     for j in fillterdBallArray[i]:
#         daySetNum.append(j)
#     for k in range(len(daySetNum)):
#         if (not daySetNum[k] == ' '):
#             daySetNum2.append(daySetNum[k])
#     setNum = []
#     for l in range(len(daySetNum2)):
#         for num in daySetNum2[l]:
#             setNum.append(int(num))
#     ball_Array.append(setNum)

# newBallArray = []
# for x in range(len(ball_Array)):
#     if (len(ball_Array[x]) == 6):
#         newBallArray.append(ball_Array[x])

# for x in range(len(jolly_Array)):
#     newBallArray[x].append(jolly_Array[x])

# for y in newBallArray:
#     dataSetArray.append(y)
# print("Done with writing 2006 Data")
################################################### 2007 to 2023 ####################################################
ball_Array = []
jolly_Array = []
superStar_Array = []
for i in range(2009, 2024):
    year = i
    # Opening the html file. If the file
    # is present in different location,
    # exact location need to be mentioned
    #HTMLFileToBeOpened = open("htmlData/2006.html", "r")
    HTMLFileToBeOpened = open('htmlData/'+str(i)+".html", "r")

    # Reading the file and storing in a variable
    contents = HTMLFileToBeOpened.read()

    # Creating a BeautifulSoup object and
    # specifying the parser
    beautifulSoupText = BeautifulSoup(str(contents), 'html.parser')
    balls = beautifulSoupText.find_all('ul', class_='balls')
    # ball_Array = []
    jolly = beautifulSoupText.find_all('li', class_='jolly')
    # jolly_Array = []
    superstar = beautifulSoupText.find_all('li', class_='superstar')
    # superStar_Array = []

    for i in range(len(jolly)):
        # jollyArray.append(jolly[i].decode_contents())
        jolly_Array.append(int(jolly[i].decode_contents()))

    # Supersstar number was introduced after 2006

    for i in range(len(superstar)):
        # jollyArray.append(jolly[i].decode_contents())
        superStar_Array.append(int(superstar[i].decode_contents()))

    # fillterdBallArray carries the 6 numbers filltered from the jolly and superstar numbers
    fillterdBallArray = []
    for i in range(len(balls)):
        strING = str(balls[i])
        bool = '<li class="jolly">' in strING
        bool2 = '<li class="superstar">' in strING
        if (bool == False and bool2 == False):
            fillterdBallArray.append(balls[i])

    for i in range(len(fillterdBallArray)):
        daySetNum = []
        daySetNum2 = []
        for j in fillterdBallArray[i]:
            daySetNum.append(j)
        for k in range(len(daySetNum)):
            if (not daySetNum[k] == ' '):
                daySetNum2.append(daySetNum[k])
        setNum = []
        for l in range(len(daySetNum2)):
            for num in daySetNum2[l]:
                setNum.append(int(num))
        ball_Array.append(setNum)

for x in range(len(ball_Array)):
    ball_Array[x].append(jolly_Array[x])
    ball_Array[x].append(superStar_Array[x])


for y in range(len(ball_Array)):
    dataSetArray.append(ball_Array[y])

# newDataSet Array keep sthe copy of Integer format list-date and ball numbers
newDataSetArray = dataSetArray

for l in range(len(dataSetArray)):
    dataSetArray[l].insert(0, date_ArrayString[l])

for m in range(len(dataSetArray)):
    newDataSetArray[m].insert(0, date_Array[m])

# newDataSetArray = [ [ [DD, MM, YY] , 'DD / MM / YY' , 1st,2nd.3rd,4th,5th,6th,jolly,superstar ]]
# for yr in range(1997, 2023):

ascendingOrder = []

# helps to arrange the data in ascending sequence of month with dates
for x in range(2009, 2024):
    setArray = []
    for y in range(len(newDataSetArray)):
        if (newDataSetArray[y][0][2] == x):
            setArray.append(newDataSetArray[y])
    setArray.reverse()
    for data in setArray:
        ascendingOrder.append(data)
    # print(setArray)
    setArray = []

description = ['List_Date', 'Date', '1st Digit', '2nd Digit', '3rd Digit',
               '4th Digit', '5th Digit', '6th Digit', '7th Digit', '8th Digit']
# creates and makes the CSV file for storing data in sequence of year
with open('dataset.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(description)
    for i in range(len(ascendingOrder)):
        myFile.writerow(ascendingOrder[i])



dataOg = pd.read_csv('dataset.csv')

data2 = np.array(dataOg[['List_Date', 'Date', '1st Digit', '2nd Digit', '3rd Digit',
               '4th Digit', '5th Digit', '6th Digit']])

testData = []

for i in data2:
    tmpData=eval(i[0])
    actualData = [tmpData[0],tmpData[1],tmpData[2],i[2],i[3],i[4],i[5],i[6],i[7]]
    testData.append(actualData)


description2 = ['Day', 'Month','Year', 'Digit1', 'Digit2', 'Digit3',
               'Digit4', 'Digit5', 'Digit6']

# creates and makes the CSV file for storing data in sequence of year
with open('Superena.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(description2)
    for i in range(len(testData)):
        myFile.writerow(testData[i])

print("Done Writing Superena.csv file  . . . . ")
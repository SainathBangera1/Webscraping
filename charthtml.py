from dataScrape import newDataSetArray
import sys
import time
import csv
print("Loading....")
syms = ['\\', '|', '/', '-']
bs = '\b'
data = []
va = True
for _ in range(10):
    if (va == True):
        data = newDataSetArray
        va = False
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(0.3)

# main index page having links of all the years
main_top = '''<!DOCTYPE html>
\n<html lang="en">
\n<head>\n
    <meta charset="UTF-8">\n
    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n
    <title>Charts</title>\n
</head>\n
<body>\n
    <h1 style="width:100%;text-align:center">Year wise Charts</h1>\n
 '''
main_content = ''
for i in range(1997, 2023):
    main_content += "<h2><a href="+"./src/" + \
        str(i)+".html>"+str(i)+"</a></h2>\n"


main_bottom = '''\n</body>
\n</html>'''

outputFile = open("./index.html", "w+")
outputFile.writelines(main_top+main_content+main_bottom)
outputFile.close()

print("Index file created...")


for i in range(1997, 2023):
    top = '''<!DOCTYPE html>\n

        <html>\n
        <style>\n
        div {
        display: grid;
        grid-template-columns: auto auto auto;
        grid-gap: 10px;
        padding: 10px;
        }\n

        table, th, td {
        border:1px solid black;
        }\n

        #select {
        bgcolor:"red";
        }\n
        </style>\n
        <body>\n'''
    content = ''

    file = open("./src/"+str(i)+".html", "w+")
    content += "\n <h1 style='color:red'>"+str(i)+"</h1>"
    content += '''\n <div>'''
    for j in range(len(data)):
        if (data[j][0][2] == i):
            content += '''\n <table> '''
            content += '''\n <tr><th colspan="10">''' + \
                str(data[j][1])+'''</th></tr>\n'''
            count = 0
            start = 1
            end = 11
            while (count == 0):
                content += "<tr>\n"
                for k in range(start, end):
                    if k in [data[j][2], data[j][3], data[j][4], data[j][5], data[j][6], data[j][7]]:
                        content += "\n <td bgcolor='red' style='color:white'" + \
                            ">"+str(k)+"</td>\n"
                    else:
                        content += "\n <td>"+str(k)+"</td>\n"
                content += "</tr>\n"
                start = end
                end = end+10
                if (end > 91):
                    count = 1
        content += '''\n </table> \n'''
    content += '</div>'
    bottom = '\n </body> \n </html>'

    file.writelines(top+content+bottom)
    file.close()
    content = ''
print("Source File Created...")
print("program Terminated...")

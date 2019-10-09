from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter
class Seotools:
    def __init__(self,url):
        self.url=url

    def numberofscript(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        script=soup.find_all("script")
        print(script)
        print("Total no of scripts:",len(script))

    def listofscript(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        script=soup.find_all("script")
        text=soup.script.get_text()
        split=text.split()
        for i in split:
                print("List of the script text:", i)

    def wordsexcluding(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        for i in soup(["script","style"]):
                i.extract()
        text=soup.get_text()
        print("total no of word:",len(text))

    def metakeywords(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        metas=soup.find_all("meta")
        for meta in metas:
            if "name" in meta.attrs and meta.attrs["name"].upper()=="KEYWORDS":
                keywordlist=meta.attrs["content"].upper().split(",")
        for i in keywordlist:
                print("the meta tags keywords:",i)


    def keywordsocurrence(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        wordlist=soup.get_text().upper().split()
        metas=soup.find_all("meta")
        for meta in metas:
                if "name" in meta.attrs and meta.attrs["name"].upper()=="KEYWORDS":
                       keywordlist=meta.attrs["content"].upper().split(",")
        
        keyworddict={k:wordlist.count(k) for k in keywordlist}
        for k,v in keyworddict.items():
                print(f"the keyword {k} is occurre {v} time")


    def excelsheet(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        metas=soup.find_all("meta")
        for meta in metas:
            if "name" in meta.attrs and meta.attrs["name"].upper()=="KEYWORDS":
                keywordlist=meta.attrs["content"].upper().split(",")
        word=soup.get_text().upper().split()
        keyworddict={k:word.count(k) for k in keywordlist}
        wb=xlsxwriter.Workbook("qqqq.xlsx")
        ws=wb.add_worksheet()
        ws.write(0,0,"keyword")
        ws.write(0,1,"Occurrences")
        row=1
        for k,v in keyworddict.items():
              ws.write(row,0,k)
              ws.write(row,1,v)
        row+=1
        print("xlsx file is created")
        wb.close()
    

    def chartexcelsheet(self):
        file=urlopen(self.url)
        html=file.read()
        file.close()
        soup=BeautifulSoup(html,"html.parser")
        metas=soup.find_all("meta")
        for meta in metas:
             if "name" in meta.attrs and meta.attrs["name"].upper()=="KEYWORDS":
                 keywordlist=meta.attrs["content"].upper().split(",")
        word=soup.get_text().upper().split()
        keyworddict={k:word.count(k) for k in keywordlist}
        wb=xlsxwriter.Workbook("d:\\qqqq.xlsx")
        ws=wb.add_worksheet()
        bold=wb.add_format({"bold":True})
        ws.write(0,0,"keyword",bold)
        ws.write(0,1,"Occurrences",bold)
        row=1
        for k,v in keyworddict.items():
            ws.write(row,0,k)
            ws.write(row,1,v)
        row+=1
        chart=wb.add_chart({"type":"column"})
        chart.add_series({"name":"Occurrences","values":"=Sheet1!$B$3:$B$"+str(row+1),"categories":"=Sheet1!$A$3:$A$"+str(row+1)})
        ws.insert_chart(6,6,chart)
        wb.close()
        print("Created Excel sheet with chart")
        wb.close()


  
    
url=input("please enter the url")
cond="y"
while cond=="y" or cond=="Y":
    if cond=="y" or "Y":
        print("please 1 to Find total number of scripts")
        print("please enter 2 for  Display a list of the script text. ")
        print("please enter 3 to Find total number of words excluding scripts and styles")
        print("please enter 4 for Displaing all keywords from meta tag")
        print("please enter 5 for Displaing all keywords along with their number of occurrences in the page(using dictionary)")
        print("please enter 6 for Creating an excel sheet data")
        print("please enter 7 for Creating column chart")
        print("please enter 8 for exit()")
        option=int(input("enter the option"))
        c=Seotools(url)
        if option==1:
                c.numberofscript()
        elif option==2:
                c.listofscript()
        elif option==3:
                c.wordsexcluding()
        elif option==4:
                c.metakeywords()
        elif option==5:
                c.keywordsocurrence()
        elif option==6:
                c.excelsheet()
        elif option==7:
                c.chartexcelsheet()
        elif option==8:
                 exit()
        else:
                print("your entering option is invalid")
            
        cond=input("do you want to continue y/n")
print("HOPE YOU GET ALL SEO TOOL TO ANALYZE THE WEB PAGES....THANK YOU")

        
            

        

            
             

            






    
    

import requests #lib for get request
import xlwt #lib for creating the excel file
from xlwt import Workbook 
from os.path import basename

REQUEST_URL='https://remoteok.com/api/' #target URL of the website
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0' #user-agent that deals with the api and request as the web browser
header={
    'User-Agent':USER_AGENT,
    'Accept-language':'en-US, en; q=0.5',
}
def get_job_data(): #function for the requesting the url
    response=requests.get(url=REQUEST_URL,headers=header)
    return response.json() #getting response in json format

def get_data_in_excel(data): #function for saving the response in excel file 'job.xls'
    wb=Workbook()
    job_sheet=wb.add_sheet('job')
    head=list(data[1].keys()) #fetching the heads from the json file as keys
    for i in range(0,len(head)):
        job_sheet.write(0,i,head[i])
    for i in range(len(data)): #fetching the data from the json in values as json store data in key value pair
        values=list(data[i].values())
        for x in range(0,len(values)):
            job_sheet.write(i+1,x,values[x])
    wb.save('job.xls') #save excel sheet as named job.xls

if __name__=='__main__':  #statement for the testing the libraries
    data=get_job_data()[1:]
    print(get_data_in_excel(data))
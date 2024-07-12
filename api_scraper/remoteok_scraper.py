import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


BASE_URL = "https://remoteok.com/api/"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"
REQUEST_HEADER = {
    'USer-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}

def get_job_postings():
    res = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
    return res.json()

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    # print(headers)
    for i in range(0,len(headers)):
        job_sheet.write(0, i, headers[i])
    for i in range(0, len(data)):
        job = data[i]
        values = list(job.values())
        # print(values)
        for x in range(0,len(values)):
            value = str(values[x])
            if len(value) > 32767:
                value = value[:32767]
            job_sheet.write(i+1,x, value)
        
    wb.save('remote_job.xls')
    
def send_email(send_from, send_to, subject,text, files=None):
    assert isinstance(send_to,list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
    for f in files or []:
        with open(f,'rb') as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
        msg.attach(part)
        
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(send_from,'pqut rjcg atxf yfpy')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    

if __name__ == "__main__":
    json = get_job_postings()[1:]
    output_jobs_to_xls(json)
    send_email('thur.thunder.3@gmail.com',['sagarchhetry333@gmail.com'],'Jobs Posting','Please find the attached file in this email',files = ['remote_job.xls'])
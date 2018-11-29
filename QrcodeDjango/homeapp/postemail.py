import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
class SendEmailQrCode():

    serviceemail='servicegtrosemontcollege@gmail.com'
    multipartmsg=MIMEMultipart()
    def __init__(self, emailsend,subject,body,pathfilename):
        self.__subject=subject
        self.__emailsend=emailsend
        self.__body=body
        self.__pathfile="homeapp/qrcodes/"+pathfilename

    def sendQrcodetoEmail(self):
        self.multipartmsg['From']=self.serviceemail
        self.multipartmsg['To']=self.__emailsend
        self.multipartmsg['Subject']=self.__subject
        self.multipartmsg.attach(MIMEText(self.__body,'plain'))

        #attach file
        attachement=open(self.__pathfile,'rb')

        part=MIMEBase('application','octet-stream')
        part.set_payload((attachement).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachement; filename="+self.__pathfile)
        
        self.multipartmsg.attach(part)
        txt=self.multipartmsg.as_string()
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.serviceemail,'xbox2018')
        print("+++++hello CLASS QURCODE   ++++++++++")
        server.sendmail(self.serviceemail,self.__emailsend,txt)
        server.quit()





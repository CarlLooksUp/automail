from datetime import datetime
import automailer

today_date = str(datetime.now().date())
subject = "Meals for week of %s" % today_date 
automailer.send_email(automailer.parse_settings("mail_settings.txt"), 
                      subject, "Don't forget garbage on Monday night")

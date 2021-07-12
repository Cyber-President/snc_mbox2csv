import mailbox
import csv

writer = csv.writer(open("mbox-output.csv", "w"))

for message in mailbox.mbox('mail.mbox'):
	writer.writerow([message['message-id'], message['subject'], message['from']])
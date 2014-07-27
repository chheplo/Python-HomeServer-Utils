#! /usr/bin/env python

# Copyright Pratik Desai, Ph.D (chheplo).
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import urllib
import smtplib
from time import sleep

url = urllib.URLopener()

ip = "127.0.0.1"
while True:

    # This website returns your home ip in plain-text
    resp = url.open('http://icanhazip.com/')
    # This is your IP address
    html = resp.readline()

    # We want to only send the IP address when it changes
    if (html != ip):

        #  Format email to be send
        fromaddr = 'XYZ@gmail.com'
        toaddrs  = ['XXX@gmail.com','YYY@hotmail.com']
        SUBJECT = "Notification for IP address change"
        TEXT = ''+html+''
        message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)

        # Credentials (if needed)
        username = 'XYZ@gmail.com'
        password = '***********'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        for toad in toaddrs:
            server.sendmail(fromaddr, toad, message)
        server.quit()
        ip = html
    # Wait for an hour before checking back your IP address
    sleep(3600)

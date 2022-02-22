### CS432 Web Science Spring 2020                                     
### Assignment 1 January 28, 2020
### Hannah Holloway
---

###  Introduction

This report mainly discusses my approach and how I implemented and solved each of the three problems assigned to me. I will be discussing every problem in a different section. 

### Q1:

***The curl POST command:***

curl -X POST -F 'fname=hannah' -F 'lname=holloway' https://cs.mweigle/courses/cs525/namesEcho.php >> /home/hannah/test.txt

***The resulting response:***


    <!DOCTYPE html>
    <html>
    <body>
    <br/>
    <br/>
    <b>fname Posted:</b> hannah<br/>
    <b>lname Posted:</b> holloway<br/>
    </body>
    </html>

***Screenshots:***

The curl POST command:
![alt text](https://www.cs.odu.edu/~hhollowa/img/test2.png "Code Snip")

The resulting response:

![alt text](https://www.cs.odu.edu/~hhollowa/img/test.png "Code Snip")

### Q2.

***Code explaination:***
The code retrieves the website url and then goes through the list of links on the page and checks the status code to make sure the page is successful. If the status code is 200, then the extension is checked to see if it ends in .pdf. If the file/url ends in .pdf, the url and the amount of bytes it contains will be printed out.

***Code:***

    from bs4 import BeautifulSoup
    import urllib2
    import requests
    import ssl
    url = raw_input("Enter URL: ")

    File = urllib2.urlopen(url)
    Html = File.read()
    File.close()
    soup = BeautifulSoup(Html, "html.parser")

    for links in soup.find_all('a'):
    a = links.get('href')
    c = 'http'
    d = a[0:3]
    if c == d:
        pass
    b = requests.head(a)
    c = 'http'
    d = a[0:3]
    if c == d:
        pass
        
    elif  b.status_code >= 300 and b.status_code < 400:
        while b.status_code != 200:
            redi = urllib2.build_opener(urllib2.HTTPRedirectHandler)
            request = redi.open(a)
            a = request.url
            b = requests.head(a)
            
        a1 = '.pdf'
        b1 = a[-4:]
        if a1 == b1:
            print (a)
            pdf = urllib2.urlopen(a)
            bytez = pdf.headers["Content-Length"]
            print bytez + ' bytes'

    elif b.status_code == 200:
        a1 = '.pdf'
        b1 = a[-4:]
        if a1 == b1:
            print (a)
            pdf = urllib2.urlopen(a)
            bytez = pdf.headers["Content-Length"]
            print bytez + ' bytes'

    else:
        pass

  
 ***Screenshots:***
 
### Q3.


IN: I, M

SCC: G, C, A, B

OUT: D, H

Tendrils: K, P, O, L

Tubes: N, J

Disconnected: E, F
 
 
![alt text](https://github.com/cs432-websci-spr20/hw1-websci-hannahmholloway/blob/master/nodes.png?raw=true "Code Snip")

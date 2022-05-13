from __future__ import division
import glob
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk import *
import re
import nltk
import os
nltk.download('words')
import csv


words = words.words()
# Bring in the default English NLTK stop words
stoplist = stopwords.words('english')

# Define additional stopwords in a string
additional_stopwords = "com https http img osx a's accordingly again allows also amongst anybody anyways appropriate aside available because before below between by can't certain com consider corresponding definitely different don't each else et everybody exactly fifth follows four gets goes greetings has he her herein him how i'm immediate indicate instead it itself know later lest likely ltd me more must nd needs next none nothing of okay ones others ourselves own placed probably rather regarding right saying seeing seen serious she so something soon still t's th that theirs there therein they'd third though thus toward try under unto used value vs way we've weren't whence whereas whether who's why within wouldn't you'll yourself according afterwards allow already among any anyway appreciate as at became been believe better but can causes co consequently contains currently didn't doing during either especially every ex few following forth get go gotten hardly having hence hereby hi hopefully i'll ignored indeed insofar isn't its kept lately less liked looks maybe might much namely need new non not obviously ok one other ours overall perhaps presumably qv reasonably respectively say see seems sent shall six someone somewhere specifying sure tends thanx their thence therefore they think those thru took truly un until use usually viz wasn't we're were when whereafter wherever who whose with would you'd yours able across against almost although an anyhow anywhere are ask away become beforehand beside beyond c'mon cannot certainly come considering could described do done edu elsewhere etc everyone example first for from getting going had hasn't he's here hereupon himself howbeit i've in indicated into it'd just known latter let little mainly mean moreover my near neither nine noone novel off old only otherwise out particular please provides rd regardless said says seem self seriously should some sometime sorry sub take than that's them there's theres they'll this three to towards trying unfortunately up useful various want we welcome what whenever whereby which whoever will without yes you're yourselves about actually ain't alone always and anyone apart aren't asking awfully becomes behind besides both c's cant changes comes contain couldn't despite does down eg enough even everything except five former further given gone hadn't have hello here's hers his however ie inasmuch indicates inward it'll keep knows latterly let's look many meanwhile most myself nearly never no nor now often on onto ought outside particularly plus que re regards same second seemed selves seven shouldn't somebody sometimes specified such taken thank thats themselves thereafter thereupon they're thorough through together tried twice unless upon uses very wants we'd well what's where wherein while whole willing won't yet you've zero above after all along am another anything appear around associated be becoming being best brief came cause clearly concerning containing course did doesn't downwards eight entirely ever everywhere far followed formerly furthermore gives got happens haven't help hereafter herself hither i'd if inc inner is it's keeps last least like looking may merely mostly name necessary nevertheless nobody normally nowhere oh once or our over per possible quite really relatively saw secondly seeming sensible several since somehow somewhat specify sup tell thanks the then thereby these they've thoroughly throughout too tries two unlikely us using via was we'll went whatever where's whereupon whither whom wish wonder you your a b c d e f g h i j k l m n o p q r s t u v w x y z lo en png jps jpg eh ext tq lj pbs rt"

stoplist += additional_stopwords.split()

total=[]
def individual_count(filename,tokens,counter):
    file_location="./texts/"+filename
    counter[0]=filename
    word=""
    with open(file_location,"r") as obj:
        for i in obj.read():
                content = obj.read()
                only_words = re.sub("[^a-zA-Z]", " ", content) # Remove anything that isn't a 'word'
                no_single = re.sub(r'(?:^| )\w(?:$| )', ' ', only_words).strip()
                no_double = re.sub(r'(\b\w{1,3}\b)', ' ', only_words).strip()
                text = re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)', ' ', only_words).strip()
                total.append(text)                                                                              
                total.append(no_single)
                total.append(no_double)
                if i is ",":
                        i=tokens.index(word)
                        counter[i]+=1
                        total[i]+=1
                        word=""
                else:
                        word+=i
                writer(counter)

def get_overall_tokens():
    tokens=["filename"]
    for i in files:
        file_location="./texts/"+i 
        column=[]
        word=""
        with open(file_location,"r") as obj:
            for i in obj.read():
                if i is ",":
                    if word not in tokens:
                        tokens.append(word)
                    word=""
                else:
                    word+=i
    writer(tokens)
    return tokens

def writer(list):
    with open('./matrices/userdata.csv', mode='a') as obj:
        obj_w = csv.writer(obj, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        obj_w.writerow(list)



if __name__=="__main__":
    files=os.listdir("./texts/")
    tokens=get_overall_tokens()
    counter=[]
    for i in tokens:
        counter.append(0)
    counter[0]="total"
    total.extend(counter)
    for i in range(len(files)):
        individual_count(files[i],tokens,counter[:])
    print(total)
    writer(total)

import os
import sys

helptext="""
---Prntscrn-Scraper---search_text.py---

Author: Codex-Major

Info:
    Searches through each file in ./image_text for a given --string.
    If a match is found, the file will be placed into a directory in ./searches/<string>,
        along with other matches of the same word.

Usage:
        python3 search_text.py
        python3 search_text.py -s password

Arguments:
    -h          Shows this message.
    -s  <str>   String to search for.
    
"""

def chktxt(filepath,tries,filecount,srcword):
    sys.stdout.write("[{}/{}] Searching file for '{}'...\n".format(tries,filecount,srcword))
    if not os.path.exists('searches'):
        os.mkdir('searches')
    if not os.path.exists('searches/{}'.format(srcword)):
        os.mkdir('searches/{}'.format(srcword))
        return None
    if os.path.exists(os.path.join('searches/{}'.format(srcword), '{}'.format(filepath[11:]))):
        sys.stdout.write("[-] Already found '{}' in {}\n".format(srcword,filepath))
        return
    infile=open(filepath,'r')
    intxt=infile.read()
    words=intxt.split(" ")
    for word in words:
        word.replace(" ","")
        word.replace("\n","")
        if srcword in word:
            word=word.lower()
            sys.stdout.write("[+] Found a match on try {}! Singled the file out in ./searches/{}/{}\n".format(tries,srcword,filepath[11:]))
            open(os.path.join('searches/{}'.format(srcword), '{}'.format(filepath[11:])), 'wb').write(bytes(intxt, 'UTF-8'))
            break
    sys.stdout.write("[*] Matches were stored in ./searches/{}\n".format(srcword))

tries=0
if __name__ == "__main__":
    try:
        if (len(sys.argv) > 1):
            cmdargs=sys.argv[1:]
            if "-h" in cmdargs[0:] or "--help" in cmdargs[0:]:
                sys.stdout.write(helptext)
                exit(0)
            if "-s" in cmdargs[0:]:
                swidx=cmdargs.index("-s")
                srcword=cmdargs[swidx+1]
                srcword=srcword.lower()
            else:
                sys.stdout.write(helptext)
                sys.stdout.write("[!] Improper usage!\n")
                exit(0)
        else:
            srcword=input("[->] Search for what string? -> ")
        filecount=len(os.listdir('image_text'))
        emptyfs=[]
        sys.stdout.write("[+] Checking all files within ./image_text for '{}'.\n".format(srcword))
        for f in os.listdir('image_text'):
            try:
                tries+=1
                chktxt(os.path.join('image_text/', f), tries, filecount, srcword)
            except Exception as e:
                print(e)
    except FileNotFoundError:
        sys.stderr.write("[-] The ./image_text directory is empty or does not exist... create/populate it using find_text.py ...\n")
        exit(0)
    except KeyboardInterrupt:
        if (srcword):
            sys.stdout.write("[*] Matches were stored in ./searches/{}\n".format(srcword))
        sys.stderr.write("[-] Exiting search_text.py, goodbye!\n")
        exit(0)

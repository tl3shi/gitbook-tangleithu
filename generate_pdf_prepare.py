# coding=utf-8
import re
import os

kuohao = re.compile(r'][(](.*?)[)]')
def process_blog(link):
    newlink = link
    filename = re.findall(kuohao, newlink)[0]
    #copy file
    newfilename = "files/" + filename[filename.find("/")+1:] #+ "_new.md"
    os.system('cp %s %s' % (filename, newfilename))
    with open(filename, 'r', encoding='UTF-8') as f:
        content = f.readlines()

    begin = None
    end = None
    for i in range(0, len(content)):
        line = content[i]
        if ("---" in line) and end is None:
            if (begin is None):
                begin = i
            elif (end is None):
                end = i
                break
        if ("title: " in line):
            title = "#" + line[line.find(":")+1:]
    newcontent = [title] + content[end+1:]
    with open(newfilename, "w", encoding='UTF-8') as f:
        f.writelines(newcontent)
    return newlink.replace(filename, newfilename)


mdcontent = []
with open('SUMMARY.md.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()

for i in range(0, len(content)):
    line = content[i]
    if ("](blog-posts" in line):
        line = process_blog(line)
    mdcontent += line

with open("SUMMARY.md", "w", encoding='UTF-8') as f:
    f.writelines(mdcontent)

import re
import os

kuohao = re.compile(r'[(](.*?)[)]')
def process_blog(link):
    newlink = link
    filename = re.findall(kuohao, newlink)[0]
    #copy file
    newfilename = "new/" + filename + "_new.md"
    os.system('copy %s %s' % (filename, newfilename))
    with open(filename, 'r') as f:
        content = f.readlines()

    for i in range(0, len(content)):
        line = content[i]
        if ("title: " in line):
            title = title[title.find(":")+1:]
            break
    newcontent = [title] + content
    with open(newfilename, "w", encoding = "utf-8") as f:
        f.writelines(newcontent)
    newlink.replace(filename, newfilename)
    return newlink;


mdcontent = []
with open('SUMMARY.md', 'r') as f:
    content = f.readlines()

for i in range(0, len(content)):
    line = content[i]
    if ("](blog-posts" in line):
        line = process_blog(line)
    mdcontent += line

with open("SUMMARY2.md", "w", encoding = "utf-8") as f:
    f.writelines(newcontent)

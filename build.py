import shutil
import os

try:
    shutil.rmtree("dist")
except:
    pass

os.mkdir("dist")
template = open('template.html').read()


def build(dir):
    dirFullMain = "main/"+dir
    dirFullDist = "dist/"+dir
    for path in os.listdir(dirFullMain):
        pathFullMain = dirFullMain+"/"+path
        pathFullDist = dirFullDist+"/"+path
        if os.path.isdir(pathFullMain):
            os.mkdir(pathFullDist)
            build(dir+"/"+path)
        else:
            _, ext = os.path.splitext(pathFullMain)
            if ext == "html":
                [title, main] = open(pathFullMain).read().split("\n", 1)
                html = template.replace(
                    "{{title}}", title).replace('{{main}}', main)
                open(pathFullDist, 'a').write(html)
            else:
                shutil.copy(pathFullMain, pathFullDist)


build("")

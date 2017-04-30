#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os, re, json

def myUnescape(s):
    return s.replace("\\'", "'").replace('\\"', '"')

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def findRecursiveByExt(topdir, ext):
    pathList = []
    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(ext):
                pathList.append(os.path.join(dirpath, name))
    return pathList

def phpWhereIs(s, p):
    ln = 1
    f = open(p, 'r')
    for line in f:
        if re.search('>t\s*\(\s*[\'"](%s)[\'"]\s*\)' % re.escape(s), line):
            f.close()
            return ln
        ln += 1
    f.close()

def jsWhereIs(s, p, appname):
    ln = 1
    f = open(p, 'r')
    for line in f:
        if re.search('t\s*\(\s*[\'"]%s[\'"]\s*,\s*[\'"](%s)[\'"]\s*[,)]' % (appname, re.escape(s)), line):
            f.close()
            return ln
        ln += 1
    f.close()

def jsonWhereIs(s, p):
    ln = 1
    f = open(p, 'r')
    for line in f:
        if re.search('"%s"' % re.escape(s), line):
            f.close()
            return ln
        ln += 1
    f.close()

if __name__ == '__main__':
    lang = sys.argv[1]
    apppath = sys.argv[2]
    appname = sys.argv[3]

    ########## parse PHP files #################

    phpPathList = findRecursiveByExt(apppath, '.php')
    phpContents = {}
    phpCodeTranslations = []
    phpCodeTranslationsByFile = {}
    phpCodeTranslationsLineNumbersByFile = {}
    for path in phpPathList:
        f = open(path, 'r')
        tlist = list(set(re.findall('>t\s*\(\s*[\'"](.*)[\'"]\s*\)', f.read())))
        f.close()
        tlistUnesc = list(map(myUnescape, tlist))
        phpCodeTranslations.extend(tlistUnesc)
        phpCodeTranslationsByFile[path] = tlistUnesc
        # find line numbers
        phpCodeTranslationsLineNumbersByFile[path] = {}
        for i in range(len(tlist)):
            ln = phpWhereIs(tlist[i], path)
            transText = tlistUnesc[i]
            phpCodeTranslationsLineNumbersByFile[path][transText] = ln

    phpCodeTranslations.sort()

    jsonf = open('%s/l10n/%s.json'%(apppath, lang), 'r')
    jsonc = json.load(jsonf)

    keys = list(jsonc['translations'].keys())
    keys.sort()
    phpTranslations = list(map(myUnescape, keys))
    phpTranslationsLineNumbers = {}
    for i in range(len(phpTranslations)):
        ln = jsonWhereIs(keys[i], '%s/l10n/%s.json'%(apppath, lang))
        transText = phpTranslations[i]
        phpTranslationsLineNumbers[transText] = ln

    ########## parse JS files #################

    jsPathList = findRecursiveByExt(apppath, '.js')
    jsContents = {}
    jsCodeTranslations = []
    jsCodeTranslationsByFile = {}
    jsCodeTranslationsLineNumbersByFile = {}
    for path in jsPathList:
        f = open(path, 'r')
        tlist = list(set(re.findall('t\s*\(\s*[\'"]%s[\'"]\s*,\s*[\'"](.*)[\'"]\s*[,)]'%appname, f.read())))
        f.close()
        tlistUnesc = list(map(myUnescape, tlist))
        jsCodeTranslations.extend(tlistUnesc)
        jsCodeTranslationsByFile[path] = tlistUnesc
        # find line numbers
        jsCodeTranslationsLineNumbersByFile[path] = {}
        for i in range(len(tlist)):
            ln = jsWhereIs(tlist[i], path, appname)
            transText = tlistUnesc[i]
            jsCodeTranslationsLineNumbersByFile[path][transText] = ln

    jsCodeTranslations.sort()

    jsjsonf = open('%s/l10n/%s.js'%(apppath, lang), 'r')
    jsjsons = jsjsonf.read()
    jsjsons = jsjsons.replace('\n', '')
    jsjsons = re.sub('[^{]*({.*})[^}]*', '\\1', jsjsons)
    jsjsonc = json.loads(jsjsons)

    keys = list(jsjsonc.keys())
    keys.sort()
    jsTranslations = list(map(myUnescape, keys))
    jsTranslationsLineNumbers = {}
    for i in range(len(jsTranslations)):
        ln = jsonWhereIs(keys[i], '%s/l10n/%s.js'%(apppath, lang))
        transText = jsTranslations[i]
        jsTranslationsLineNumbers[transText] = ln

    print('########### useless PHP translations ###############\n')

    for s in phpTranslations:
        if s not in phpCodeTranslations:
            print('%s%s.json%s:%s%s%s: %s%s"%s"%s is useless, it was not found in any php file' %
                    (color.PURPLE, lang, color.END,
                    color.GREEN, phpTranslationsLineNumbers[s], color.END,
                    color.BOLD, color.RED, s, color.END))

    print('\n########### useless js translations ###############\n')

    for s in jsTranslations:
        if s not in jsCodeTranslations:
            print('%s%s.js%s:%s%s%s: %s%s"%s"%s is useless, it was not found in any js file' %
                    (color.PURPLE, lang, color.END,
                    color.GREEN, jsTranslationsLineNumbers[s], color.END,
                    color.BOLD, color.RED, s, color.END))

    print('\n########### missing php translations ###############\n')

    for fpath in phpCodeTranslationsByFile:
        for s in phpCodeTranslationsByFile[fpath]:
            if s not in phpTranslations:
                print('%s%s%s:%s%s%s: %s%s"%s"%s is not translated in %s%s%s.json%s' %
                        (color.PURPLE, fpath, color.END,
                        color.GREEN, phpCodeTranslationsLineNumbersByFile[fpath][s], color.END,
                        color.BOLD, color.RED, s, color.END,
                        color.GREEN, color.BOLD, lang, color.END))

    print('\n########### missing js translations ###############\n')

    for fpath in jsCodeTranslationsByFile:
        for s in jsCodeTranslationsByFile[fpath]:
            if s not in jsTranslations:
                print('%s%s%s:%s%s%s: %s%s"%s"%s is not translated in %s%s%s.js%s' %
                        (color.PURPLE, fpath, color.END,
                        color.GREEN, jsCodeTranslationsLineNumbersByFile[fpath][s], color.END,
                        color.BOLD, color.RED, s, color.END,
                        color.GREEN, color.BOLD, lang, color.END))


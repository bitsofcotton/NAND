#! /usr/bin/env python

import sys
import re

def parse_header(s):
  s += "\n"
  gheader_syntaxes  = {}
  gheader_syntaxes["require"]   = "require"
  gheader_syntaxes["include"]   = "include"
  gheader_syntaxes["class"]     = "class"
  gheader_syntaxes["extend"]    = "extend"
  lheader_syntaxes  = {}
  lheader_syntaxes["def"]       = "def"
  lheader_syntaxes["var"]       = "var"
  lheader_syntaxes["auto"]      = "auto"
  lheader_syntaxes["include"]   = "include"
  llheader_syntaxes = {}
  llheader_syntaxes["operator"] = "operator"
  work   = [{}]
  work[0]["type"]  = "none"
  indent = 0
  pidt   = False
  ppidt  = False
  mode   = ""
  temp   = [0]
  for ss in range(0, len(s)):
    pp = re.split(r"([\ \t\n\r\"\'\(\)\{\}\<\>\:\,])", s[ss])
    for p in pp:
      if(p == ' ' or p == '\t'):
        indent += 1
        continue
      else:
        if((not ppidt) and temp[0] != indent):
          print "NG: "
        pidt  = True
        ppidt = True
      if(p == '\\' or p == '\"' or p == '\''):
        if(not (0 < len(mode) and (mode[- 1] == '\\' or mode[- 1] == '\"' or mode[- 1] == '\''))):
          mode += p
        elif(0 < len(mode) and mode[- 1] == p):
          mode  = mode[:-1]
        else:
          temp[- 1] += p
      elif(p == '\r' or p == '\n'):
        if(0 < len(mode) and mode[- 1] == '\\'):
          indent = 0
          ppidt  = False
          mode   = mode[:-1]
        elif(len(mode) <= 0):
          if(1 < len(temp)):
            print temp
          mode  = ''
          temp  = [0]
          indent = 0
          pidt  = False
          ppidt = False
        else:
          print "NG***:"
      elif(p == ' '):
        pass
      else:
        if(len(temp) <= 1):
          temp[0] = indent
        if(0 < len(p)):
          temp.append(p)
  return work

def parse_source(s):
  return

parse_header(sys.stdin.readlines())


#! /usr/bin/env python

import sys
import re

# thanks to: https://qiita.com/hoto17296/items/e1f80fef8536a0e5e7db
flatten = lambda x: "_".join([z for y in x for z in (flatten(y) if (hasattr(y, '__iter__') and not isinstance(y, str)) else y,)])

def parse_typedef():
  return []

def parse_sentence():
  return []

def parse_block(buf, start):
  indent = 0
  ss = start
  for b in buf[ss]:
    if(b == ' ' or b == '\t' or b == ''): indent += 1
    else: break
  while(ss < len(buf)):
    idt = 0
    for b in buf[ss]:
      if(b == ' ' or b == '\t' or b == ''): idt += 1
      else: break
    if(idt < indent):
      break
    ss += 1
  return [ss, indent]

# input:  text lines.
# output: hash list
# type == type (root of the list)
#   ...[typename] || ...["root"] # root type
#     ...[name][0...]["type"] # (fn|inline|var|def)
#     ...[name][0...]["comment"] # comment
#     ...[name][0...]["license"] # license
# type == var
#     ...["text"] # var
#     ...["name"] # name of var
#     ...["type"] # type array
#     ...["init"] # initialize variables sentence array.
# type == def
#     ...["text"] # def
#     ...["name"] # name of def
#     ...["def"]  # block array
# type == fn|inline
#     ...["text"]   # fn | inline
#     ...["type"][0...] # type array
#     ...["ret"]    # type array
#     ...["entity"] # block array
# type array:
#   ...[0...]["type"] # typename
#   ...[0...]["arg"][0...]["type"] # type arg type, be able to recursive.
#   ...[0...]["arg"][0...]["init"] # type arg init array, be able to recursive.
# block array:
#   ...[0...]["text"] # (fn|inline|var|def|sentence)
def nameref(s):
  bra = {}
  braket = {}
  braquot = {}
  reserved_root = {}
  reserved_type = {}
  type_addfn    = {}
  typefn_special= {}
  typeop        = {}
  reserved_var  = {}
  reserved_flow = {}
  bra[")"] = "("
  bra["}"] = "{"
  bra["]"] = "["
  braquot["\""] = "\""
  braquot["\'"] = "\'"
  braket["("] = "("
  braket[")"] = ")"
  braket["{"] = "{"
  braket["}"] = "}"
  braket["["] = "["
  braket["]"] = "]"
  braket["\""] = "\""
  braket["\'"] = "\'"
  reserved_root["load"] = "load"
  reserved_root["def"]  = "def"
  reserved_root["fn"]   = "fn"
  reserved_root["inline"] = "inline"
  reserved_root["type"] = "type"
  reserved_type["def"] = "def"
  reserved_type["friend"] = "friend"
  reserved_type["ctor"] = "ctor"
  reserved_type["dtor"] = "dtor"
  reserved_type["op"]   = "op"
  reserved_type["enter"] = "enter"
  reserved_type["leave"] = "leave"
  reserved_type["inline"] = "inline"
  type_addfn["friend"] = "friend"
  type_addfn["ctor"]   = "ctor"
  type_addfn["dtor"]   = "dtor"
  type_addfn["op"]     = "op"
  type_addfn["enter"]  = "enter"
  type_addfn["leave"]  = "leave"
  typefn_special["this"] = "this"
  typefn_special["leaf"] = "leaf"
  typefn_special["super"] = "super"
  reserved_var["__pointer_bits__"] = "__pointer_bits__"
  reserved_var["__here__"] = "__here__"
  reserved_var["__callgraph__"] = "__callgraph__"
  reserved_var["res"] = "res"
  reserved_flow["for"] = "for"
  reserved_flow["from"] = "for"
  reserved_flow["to"] = "for"
  reserved_flow["?"] = "?"
  reserved_flow[":"] = ":"
  reserved_flow["break"] = "break"
  reserved_flow["assert"] = "assert"
  res = {}
  typen = "root"
  res[typen] = {}
  ptr   = []
  mode  = ''
  first = True
  tindent = 1
  bindent = 0
  tset  = False
  buf   = []
  for ss in range(0, len(s)):
    pp = re.split(r"([\ \t\n\#\(\)\{\}\[\]\:\,\?\"\'])", s[ss])
    buf.append([])
    for p in pp:
      buf[- 1].append(p)
  ss = 0
  while(ss < len(buf)):
    indent = 0
    sss = 0
    while(ss < len(buf) and sss < len(buf[ss])):
      p = buf[ss][sss]
      if(p == ' ' or p == '\t' or p == ''):
        if(indent >= 0 and p != ''):
          indent += 1
        sss += 1
        continue
      elif(indent >= 0):
        if(tset):
          tindent = indent
          tset = False
        if(0 < len(ptr)):
          if(ptr[0] == "load"):
            ptr = []
          elif(ptr[0] == "type"):
            typen = ptr[1]
            if(not (typen in res)):
              res[typen] = {}
            res[typen]["attribute"] = [ptr[2:]]
            ptr  = []
            tset = True
          elif((ptr[0] == 'fn' or ptr[0] == 'inline' or ptr[0] == 'def' or ptr[0] == 'var') and 2 <= len(ptr) and indent <= tindent and bindent <= indent):
            if(ptr[0] == 'fn' or ptr[0] == 'inline'):
              if(not (ptr[1] in res[typen])):
                res[typen][ptr[1]] = [{}]
              elif(ptr[0] == 'fn' or ptr[0] == 'inline'):
                res[typen][ptr[1]].append({})
              res[typen][ptr[1]][- 1]["text"] = ptr[0]
              if(ptr[1] == 'op'):
                res[typen][ptr[1]][- 1]["name"] = ptr[1] + ptr[2]
              else:
                res[typen][ptr[1]][- 1]["name"] = ptr[1]
            else:
              if(not (ptr[1] in res[typen])):
                res[typen][ptr[1]] = {}
              else:
                print("Duplicate name : ", ptr[1])
              res[typen][ptr[1]]["text"] = ptr[0]
              res[typen][ptr[1]]["name"] = ptr[1]
            if(ptr[0] == 'var'):
              if(ptr[2] != ':'): print("ERR ptr[2] != :")
              # loop:
              res[typen][ptr[1]]["type"] = parse_typedef()
              res[typen][ptr[1]]["init"] = parse_sentence()
              # block:
            elif(ptr[0] == 'def'):
              if(ptr[2] != ':'): print("ERR ptr[2] != :")
              pb = parse_block(buf, ss + 1)
              res[typen][ptr[1]]["def"] = pb
              if(indent < pb[1]):
                ptr = []
                ss = pb[0]
                break
            else:
              # loop
              res[typen][ptr[1]][- 1]["type"] = parse_typedef()
              res[typen][ptr[1]][- 1]["init"] = parse_sentence()
              res[typen][ptr[1]][- 1]["ret"]  = parse_typedef()
              pb = parse_block(buf, ss + 1)
              res[typen][ptr[1]][- 1]["entity"] = pb
              if(indent < pb[1]):
                ptr = []
                ss = pb[0]
                break
            ptr = []
            if(indent < tindent):
              if(0 < len(mode)):
                print("NG no closed : ", ss, " mode: ", mode)
              mode = ''
          else:
            print("ERR", ptr, s[ss][:- 1], typen)
            ptr = []
        if(len(ptr) <= 0):
          first   = True
          tindent = indent
        if(indent <= 0): typen = "root"
        bindent = indent
        indent  = - 1
      if(0 < len(mode) and mode[- 1] in braquot):
        if(p == mode[- 1]):
          mode = mode[:- 1]
          ptr[- 1] += p
        else:
          ptr[- 1] += " " + p
      elif(p == '#' or p == '\n'):
        indent = 0
        break
      elif(p in braket):
        if(p in bra):
          if(len(mode) <= 0 or mode[- 1] != bra[p]):
            print("no bra on ket : line", ss)
          else:
            mode = mode[:- 1]
        else:
          mode += p[:1]
        ptr.append(p)
      elif(first):
        if(typen == "root" and p in reserved_root):
          ptr.append(p)
        elif(typen != "root" and p in reserved_type):
          if(p in type_addfn):
            ptr.append("fn")
          ptr.append(p)
        elif(typen != "root"):
          ptr.append("var")
          ptr.append(p)
        else:
          print("parse error : ", ss)
        first = False
      else:
        # XXX: check
        ptr.append(p)
      sss += 1
    ss += 1
  return res

lines = sys.stdin.readlines()
lines.extend(['\n'])
work = nameref(lines)
wp = str(work).split("}")
for w in wp:
  print(w)
print("OK")


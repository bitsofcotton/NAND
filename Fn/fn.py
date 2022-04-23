#! /usr/bin/env python

import sys
import re

# thanks to: https://qiita.com/hoto17296/items/e1f80fef8536a0e5e7db
flatten = lambda x: "_".join([z for y in x for z in (flatten(y) if (hasattr(y, '__iter__') and not isinstance(y, str)) else y,)])

# input:  text lines.
# output: hash list
#   ...[typename] || ...["root"] # root type
#     ...[name]["type"] # (fn|friend|var|def)
#     ...[name]["pickle"] # entity of them.
def nameref(s):
  bra = {}
  braket = {}
  reserved_root = {}
  reserved_type = {}
  type_addfn    = {}
  reserved_var  = {}
  reserved_flow = {}
  res = {}
  bra[")"] = "("
  bra["}"] = "{"
  bra["]"] = "["
  braket["("] = "("
  braket[")"] = ")"
  braket["{"] = "{"
  braket["}"] = "}"
  braket["["] = "["
  braket["]"] = "]"
  reserved_root["load"] = "load"
  reserved_root["def"]  = "def"
  reserved_root["fn"]   = "fn"
  reserved_root["type"] = "type"
  reserved_type["def"] = "def"
  reserved_type["friend"] = "friend"
  reserved_type["ctor"] = "ctor"
  reserved_type["dtor"] = "dtor"
  reserved_type["op"]   = "op"
  reserved_type["enter"] = "enter"
  reserved_type["leave"] = "leave"
  type_addfn["ctor"]   = "ctor"
  type_addfn["dtor"]   = "dtor"
  type_addfn["op"]     = "op"
  type_addfn["enter"]  = "enter"
  type_addfn["leave"]  = "leave"
  type_addfn["friend"] = "friend"
  reserved_var["__pointer_bits__"] = "__pointer_bits__"
  reserved_var["__here__"] = "__here__"
  reserved_var["__callgraph__"] = "__callgraph__"
  reserved_flow["return"] = "return"
  reserved_flow["for"] = "for"
  reserved_flow["?"] = "?"
  res = {}
  typen = "root"
  ptr   = []
  ptrf  = []
  mode  = ''
  first = True
  bindent = 0
  tindent = 1
  for ss in range(0, len(s)):
    pp = re.split(r"([\ \t\n\(\#\)\{\}\[\]\:\,\?])", s[ss])
    indent = 0
    for p in pp:
      if(p == ' ' or p == '\t' or p == ''):
        if(indent >= 0 and p != ''):
          indent += 1
        continue
      elif(indent >= 0):
        if(0 < len(ptr) and indent < bindent and 0 < len(mode)):
          print("NG no closed : ", ss, " mode: ", mode)
          mode = ''
        elif(len(ptr) <= 0): pass
        elif(indent <= bindent or ptr[0] == "type"):
          if(not (typen in res)):
            res[typen] = {}
          idx = 1
          if(ptr[0] == 'fn' and typen != "root" and ptr[1] == "op"):
            idx = 2
          if(len(ptr) <= idx):
            print("No much information on line:", ss)
          else:
            if(not (ptr[idx] in res[typen])):
              res[typen][ptr[idx]] = {}
            if(res[typen][ptr[idx]] != {}):
              print("Duplicate name, without type operation, broken result.")
            if(len(ptrf) <= 0):
              res[typen][ptr[idx]]["type"] = ptr[0]
              res[typen][ptr[idx]]["pickle"] = ptr[idx + 1:]
            else:
              res[typen][ptr[idx]]["type"] = ptr[0]
              res[typen][ptr[idx]]["pickle"] = ptr[idx + 1:]
              if(not ("blocks" in res[typen][ptr[idx]])):
                res[typen][ptr[idx]]["blocks"] = []
              res[typen][ptr[idx]]["blocks"].append(ptrf)
              ptrf = []
          ptr = []
        elif((bindent < indent or tindent < indent) and len(ptrf) <= 0):
          ptrf.append("")
        if(indent <= 0): typen = "root"
        if(len(ptrf) <= 0):
          first   = True
          tindent = indent
        bindent = indent
        indent  = - 1
      if(p == '#' or p == '\n'): break
      elif(p in braket):
        if(p in bra):
          if(len(mode) <= 0 or mode[- 1] != bra[p]):
            print("no bra on ket : ", ss)
          else:
            mode = mode[:- 1]
        else:
          mode += p[:1]
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
        if(len(ptrf) <= 0):
          ptr.append(p)
          if(ptr[0] == 'type'): typen = ptr[1]
        else: ptrf.append(p)
  return res

work = nameref(sys.stdin.readlines())
print(work)
print("OK")


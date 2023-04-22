/* N.B. we choose start language as C.
     this is because the most of the unix like systems have C compiler
     as a default.
     So even we choose any of the language, they depends on the compiler
     what the base system firstly have. In principle, we cannot avoid
     infection on the language if the default compiler is infected
     condition. So after of them, we should rewrite them into gas or so,
     however, there's some rumor ld or gas somewhat has glitches
     (infection?). Even on windows, also masm.exe compiled executable binary
     detected as a malware by some of the virus detector, the rumor exists.
   N.B. However, our machine is infected including clang compile nor
     mem/integer some glitch operation on some of the source, 
     We should start with some of the starting compiler as hex-coded
     lisp intepreter, then, C to lisp, then, to run with or to compile
     some of the compilers on *TRUSTED* hardwares.
*/
/*
 * This is a transpiler, so we only need to task symbolic ones.
 * This is hinted by some of the C++ to C transpilers around someone on github.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N_DEF 2048

typedef struct {
  char* type;
  char* def;
  char* body;
  int prev;
  int next;
} defstr_t;

defstr_t dstr[N_DEF];
int dstr_head = - 1;
int dstr_tail = - 1;
int dstr_size = 0;

char** append_deftable(char* type, char* def) {
  if(dstr_head < 0 || dstr_tail < 0 || dstr_size == 0) {
    dstr_head = dstr_tail = 0;
    dstr[dstr_head].type = type;
    dstr[dstr_head].def  = def;
    dstr[dstr_head].prev = dstr[dstr_tail].next = - 1;
    dstr_size ++;
    return &dstr[dstr_head].body;
  }
/*
  // int idx = dstr_head;
  // seek to insert [idx, idx + 1];
  dstr[idx].type = type;
  dstr[idx].def  = def;
  dstr[idx].prev = head;
  dstr[idx].next = tail;
  dstr[head].next = idx;
  dstr[tail].prev = idx;
  dstr_size ++;
  return &dstr[idx].body;
*/
  return NULL;
}

int seek_deftable(const char* type, const char* def) {
  if(dstr_head < 0 || dstr_tail < 0 || dstr_size == 0) return - 1;
  int head = dstr_head;
  int tail = dstr_tail;
  int size = dstr_size;
  while(head != tail) {
    if(strncmp(dstr[head].type, type, strlen(type)) == 0 &&
       strncmp(dstr[head].def,  def , strlen(def )) == 0)
      tail = head;
    else if(strncmp(dstr[tail].type, type, strlen(type)) == 0 &&
            strncmp(dstr[tail].def,  def , strlen(def ))  == 0)
      head = tail;
    else {
      int mid = head;
      for(int i = 0; i < (size + 1) / 2; i ++)
        mid = dstr[mid].next;
      if( strncmp(dstr[mid].type, type, strlen(type)) < 0 ||
         (strncmp(dstr[mid].type, type, strlen(type)) == 0 &&
          strncmp(dstr[mid].def , def , strlen(def )) < 0) )
        tail = mid;
      else
        head = mid;
    }
  }
  if(strncmp(dstr[head].type, type, strlen(type)) == 0 &&
     strncmp(dstr[head].def , def , strlen(def )) == 0)
    return head;
  return - 1;
}

void read_deftable(char** lines, const int s_line) {
  char context = 'R';
  char context_before = 'R';
  char** defstr;
  for(int i = 0, jj = 0; i < s_line; i ++) {
    printf("%c", context);
    if(context == 'R' && strncmp(lines[i], "type", strlen("type")) == 0)
      context_before = context = 'T';
    if(context == 'T' && lines[i][0] != ' ' && lines[i][0] != '\n' && lines[i][0] != '\t') {
      context_before = context = 'R';
      jj = 0;
    }
    int j = 0;
    const int len = strlen(lines[i]);
    for( ; j < len && (lines[i][j] == ' ' || lines[i][j] == '\t'); j ++) ;
    if(jj < j && context == 'D') {
      // follow.
      // if follow is end, if() context = context_before;
    } else if(context == 'D') {
      printf("Something wrong @ (%d, %d)\n", i, j);
      jj = j;
    } else if(strncmp(&lines[i][j], "def", strlen("def")) == 0) {
      context = 'D';
      // scan
      puts(&lines[i][j]);
      char* type;
      char* def;
      type = "type";
      def  = "type";
      if(seek_deftable(type, def) < 0) {
        // free.
        printf("Double definition of same string @ (%d, %d)\n", i, j);
        continue;
      }
      defstr = append_deftable(type, def);
      lines[i][0] = '\0';
    }
    jj = j;
  }
}

int main(int argc, char* argv[]) {
  FILE* file;
  int c = 0;
  int lines = 1;
  char** data;
  file = fopen(argv[1], "r");
  if(file == NULL) return - 1;
  while((c = fgetc(file)) != EOF)
    if(c == '\n') lines ++;
  rewind(file);
  data = (char**)calloc(lines, sizeof(char*));
  for(int i = 0; i < lines; i ++) {
    int cnt = 0;
    int ws  = 1;
    int backup;
    backup = ftell(file);
    for( ; ; cnt ++) {
      int cc;
      cc = fgetc(file);
      if(cc == EOF || cc == '\n') break;
      if(cc == '#' && ws) break;
      if(cc != ' ' || cc != '\t') ws = 0;
    }
    data[i] = (char*)calloc(cnt + 1, sizeof(char));
    fseek(file, backup, SEEK_SET);
    for(int j = 0; j < cnt; j ++)
      data[i][j] = fgetc(file);
    data[i][cnt] = '\0';
  }
  fclose(file);
  read_deftable(data, lines);
  return 0;
}

/*
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
def nameref(res, uri, load):
  load.append(uri)
  f = open(uri)
  s = f.readlines()
  s.extend(['\n'])
  f.close()
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
  backtree = []
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
              if(ptr[2] != ':'): print("syntax error ptr[2] != :, ", ss)
              work = parse_typedef(buf[ss], sss, backtree, res)
              if(work["status"] == "done"):
                res[typen][ptr[1]]["type"] = work["tree"]
                res[typen][ptr[1]]["init"] = parse_sentence()
                backtree = []
              elif(work["status"] == "not defined"):
                print("type verification: type not defined: ", ss)
              elif(work["status"] == "short"):
                # XXX: next indent check:
                sss += 1
                continue
              else:
                print("fatal error.")
                exit(0)
              pb = parse_block(buf, ss + 1)
              if(indent < pb[1]):
                ptr = []
                ss = pb[0]
                break
            elif(ptr[0] == 'def'):
              if(ptr[2] != ':'): print("syntax error ptr[2] != :, ", ss)
              pb = parse_block(buf, ss + 1)
              res[typen][ptr[1]]["def"] = pb
              if(indent < pb[1]):
                ptr = []
                ss = pb[0]
                break
            else:
              work = parse_typedef(buf[ss], sss, backtree, res)
              if(work["status"] == "done"):
                res[typen][ptr[1]]["type"] = work["tree"]
                res[typen][ptr[1]]["init"] = parse_sentence()
                backtree = []
              elif(work["status"] == "not defined"):
                print("type verification: type not defined: ", ss)
              elif(work["status"] == "short"):
                # XXX: next indent check:
                sss += 1
                continue
              else:
                print("fatal error.")
                exit(0)
              #res[typen][ptr[1]][- 1]["init"] = parse_sentence()
              #res[typen][ptr[1]][- 1]["ret"]  = parse_typedef()
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
          print("syntax error : ", ss)
        first = False
      else:
        # XXX: check
        ptr.append(p)
      sss += 1
    ss += 1
  return res

*/

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
#define N_DEF   2048
#define N_CHAIN 2048
#define N_FUN   2048

typedef struct {
  char* type;
  char* def;
  char* body;
  int prev;
  int next;
} defstr_t;

typedef struct {
  /* */
  ;
} defchain_t;

typedef struct {
  char* ret;
  int*  rtype;
  char* fun;
  char** variables;
  int*** vtype;
  defchain_t chain[N_CHAIN];
} deffun_t;

defstr_t   dstr[N_DEF];
deffun_t   dfun[N_FUN];
int dchain_head[N_FUN];
int dchain_tail[N_FUN];
int dchain_size[N_FUN];
int dstr_head = - 1;
int dstr_tail = - 1;
int dstr_size = 0;
int dfun_head = - 1;
int dfun_tail = - 1;
int dfun_size = 0;

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


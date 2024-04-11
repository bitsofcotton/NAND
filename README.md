# NAND(Never finish)
Natural tinier compiler which code with natural tinier comments and licenses on a file.

This aims to compile nand source into C source and check the output by hand or eyes.
Otherwise, they can even infect if whole system is infected condition.
(All we can do is to transcode and check the transformed or compiled source by hands or eyes even any of the code patches, or, we can do only to crypt them with the cryption algorithm hidden from the attacker.)

# Syntax concrete (7: renew).
* ':' directive
* * name : "(uri|path)"(.type|.function|.op)? (file root context only)
* * * import once, no need include guard.
* * * to define some of the name, we should use separated file.
* * name(\[templates...\]) : op(\[templates...\])? operator-name : (inherit op-name) : type? (file root context only)
* * * multiple lines.
* * * operator collections to types.
* * * if caller specified name doesn't match this op, call inherit.
* * * enter, leave, call, return
* * * * for each operator call, non const or const first/last operation.
* * * (operators)
* * * * could call another operator classes.
* * name(\[templates...\]) : type(\[templates...\])?
* * * multiple lines.
* * * use some integer or type sets as a type.
* * * like typedef struct ... in C but with ctor(...), dtor().
* * * ctor(name! ...) '\!' specifies moved argument.
* * * val \. element : in type element lookup out of the scope.
* * variables
* * * a : b
* * * a : const(b)
* * * * a is (non const) reference of b or const reference of b.
* * * * the original variable will not be used like some awesome languages.
* * * a : static(b)
* * * * a is initialized by b once in first of execution.
* * * a : func(b)
* * * * a is instanced variable of function.
* * * a : func!(b)
* * * * a is function returned reference.
* * * * we should use function definition as entity ones in header files.
* * name(\[templates...\])?(name : type (: "comment")?, ...) const? export? : type
* * * function, name! returns reference.
* * * with calling function, we must specify the variable name as:
* * * * name(name = val, ...)
* * * no return mnemonic, instead of them, reserved "res" variable.
* * * * from awesome embedded C language.
* * * on function call, pass const type to type causes auto makeing instance.
* * * export exports the function, also prevent to be inlined.
* Special characters
* * Int
* * * one of two type we have on this, pointer wide, full set of arithmetic/bit ops.
* * Vec\[type\]
* * * one of two type we have on this, vector we call ctor(...), dtor() on around instances, first operand with size.
* * * We have : reserve, resize, push, pop, delete, op \[\] type function on this,
* * move(...)
* * * like in C++.
* * op-noop
* * * noop root operator.
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * () ? () : ()
* * * 3-term operator like in C.
* * '(for|para)\[operator\] ... from ... to ... : label', operator ++, operator \< function definition is used,
* * * break label
* * * when parallel, out of the scope treated as global, in the scope treated as thread variable (except for the reference).
* * assert(x)
* * * stop execution or compilation if x is false.
* * * we can override this with assert function redefinition in execution time.
* * \# will treat line after them as a comment.
* * * \# license? comment...
* * type or op can specify (type \| ... \| type) or (op \| ... \| op), also be able to specify template omitted.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).

# Tips
One of the method reducing source code is to exclude same or similar structures from reading binary perspective.
So with this, this repository aims and follows class capsule with arithmetic method in mathematics. One of a perspective of mathematics is to treat quantities and their structures as calculatible possible simple way, and is often has a structure repeat, invert, and they sometimes treated as arithmetic operations.
Some conditions needs variables along with initialize / ensure method.
Except some of the special flows especially initialize/error flow, I don't know whether or not special flows other than if then else, for, while is needed. And if we implement such flows with class capsule, it usually vanishes the condition.
But, it would be greately appreciated if you know the methods reducing source code other than along with preparing data nor how to treat data in the codes.

# Tips
Second of the method to reduce function code is to match same-result algorithms as only one code.
This is especially in sort algorithms, however, to reduce such codes, we need to check by hands now.
So we need to do them only library code as maximum compressed and functional enough ones.
So there's many libraries exists doing this.

# Tips
To exclude same... from perspective on algorithm, we only get in/output similarity or algorithm similarity itself.
So we need same from perspective on data to exclude multiple description writing on the code. However, this is already done by some of the known ongoing libraries s.t. bison/json for best practice. So there isn't exist new field for us (however, there could be another way for another peroson... eg. programs for the web).

# General Tips
Some of the algorithm description causes tan\<a,x\> type descriptions, however, if the intension of the first we observed isn't effective to such a vector in data amount meaning, the calculation can slips on the intension.
So first intension amount : information amount on data/algorithm on binary tree description we have is the matter if the result breaks.
We can exclude the information amount into accuracy or dimensions or multiple on layers, however, in any which case we have the amounts, the whole system description integrity is also matters.

Since we have non tangle dimension upper limits, we should exclude them into accuracy or multiple on layers, however, accuracy on in/output has upper bounds to describe the function enough or not, so the only the secure way to exclude the information amount is multiple on layers, this don't touch any extensions of the calculation however this also has the limits.

So heavy tuned functions, we have upper function data amount limit around 2peta or so because 16 depth 3 color tree has so. This is the case we make the hypothesis in/out/internal status is completely separable and tanglement can be calculated in the tangled form. However, the hypothesis we make includes each in/out/internal status tanglement causes information amount of them can be broken. So the hypothesis of such of them also makes the hypothesis uniqueness of the each in/out/internal status pillars and only refers unique 3 of the pillar they stands on. In general, such hypothesis can fails if the subject on them is not unique existance.

# General Tips on pure functions
So with above, heavy tuned function only with in/output without any internal status with start, the upper bound of them are 19683 (around 20k) functions with uniqueness of the whole on input with input tangling. (output only depends on f and input, so it's unique on raw meaning). So with such amount of the input information, we need to code amount up to 20k or so. This is around 2500 of 8 bit numerators we need on the model. If we apply this on the image, we need around 29px x 29px on each pixel with 3 term on image prediction nor 833px height on image extend prediction. Either, only one image, 50px x 50px upper limit.

# General Tips on any functions
Any functions with heavy tuned has up to 12 variables.
This is because 4 variables for each variable on in/out/states they should be separated.
Because we only need 3+1 variables on non uniqueness of the one function, however, we also need the some large dimension parameters on compress/decompress function theirselves.
However, this description also have a domain they have some of the sets of multiple viewpoints on each of in/out/states.

In addition to this, this is we cannot describe as a function of f, however, some of the probability based functions have up to 16 variables because of hidden state part. However, 16 variables is too large not to tangle in raw.

# Things undone.
This repository has NO materialized implementation.
There exists huge fields they have important materials.

# Control directory
We cram the scrapped delusion which all the things we want supported by computer for now into Control directory (can be different from yours). Some of the future, this categorize can be changed.

# close readme.md and their fixes
2023/08/10.
2023/08/10 fix some.
2024/04/09 fix some. add general tips.
2024/04/11 syntax is concrete in first try. might be changed from some implementation simplify constarints.


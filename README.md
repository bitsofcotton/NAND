# NAND(Never finish)
Natural tinier compiler which code with natural tinier comments and licenses on a file aims to easy to audit.

This aims to compile nand source into C or lisp source and check the output by hand or eyes.
Otherwise, they can even infect if whole system is infected condition.
Searching assertion intention amplifier methods. (basically, they're only a saturation of the structure attributes balanced to cognitive load.).

# Syntax concrete (c).
* ':' directive on root context
* * namespace-name : "(uri|path)"(.type|.ctor|.op)?
* * * import once, no need include guard.
* * * to define some of the name, we should use separated file.
* * type-name(\[templates...\])? : "type"
* * * multiple lines.
* * * use integer or vector or type sets as a type.
* * * like typedef struct ... in C but with dtor().
* * * enter/leave is replaced into the internal of operators.
* * * val \. element : in type element lookup out of the scope.
* * type-name(\[templates...\])? : "ctor"
* * * type ctors.
* * * type-name! returns reference.
* * "op(symbol)"operator-name(\[templates...\])?(variables ...) : type?
* * * per operator on type, like in the class internal definition of C++.
* * * call internally templated another operators or enter/leave for another operators.
* * * type! means they returns reference.
* ':' directives
* * variables
* * * a : b
* * * a : const(b)
* * * * a is (non const) reference of b or const reference of b.
* * * * the original variable will not be used like some awesome languages.
* * * a : static(b)
* * * * a is initialized by b once in first of execution.
* * * a : type-name(b)
* * * * a is instanced variable of ctor.
* * * a : type-name!(b)
* * * * a is ctor returned reference.
* * * * we should use function definition as entity ones in header files.
* * * a : (equation)
* * * * substitute and initiate calculation result into variable.
* Special characters
* * Int
* * * one of two type we have on this, pointer wide, full set of arithmetic/bit ops.
* * Vec\[type\]
* * * one of two type we have on this, vector we call ctor(...), dtor() on around instances, first operand with size.
* * * We have : op+reserve, op+resize, op+push, op-pop, op-delete, op\[\] type function on this,
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * () ? () : ()
* * * 3-term operator like in C.
* * 'label : (for|para)\[operator-name\] ... from ... to ...', operator ++, operator \< function definition is used,
* * * break label
* * * when parallel, out of the scope treated as global, in the scope treated as thread variable (except for the reference).
* * assert(x)
* * * stop execution or compilation if x is false.
* * * we can override this with compiler option on execution time.
* * \# will treat line after them as a comment.
* * * \# license? comment...
* * generic programming like specifying multiple types is abandoned
* * * instead of them, we can define each operator as a simple one.
* * class capsule private can be specified global policy on compile time as single file access.

# Tips on reduction
To make things simple enough easy to audit, we need to reduce the code amount also amplify assertion intensions by simple syntax.

One of the method reducing source code is to exclude same or similar structures from reading binary perspective.

So with this, this repository aims and follows class capsule with arithmetic method in mathematics. One of a perspective of mathematics is to treat quantities and their structures as calculatible possible simple way, and is often has a structure repeat, invert, and they sometimes treated as arithmetic operations.
Some conditions needs variables along with initialize / ensure method.

We only need if-then-else and for loop with break labels, there's some of the exceptions however, we don't need them because fuction separation exists.


Second of the method to reduce function code is to match same-result algorithms as only one code.
This is especially in sort algorithms, however, to reduce such codes, we need to check by hands now.
So we need to do them only library code as maximum compressed and functional enough ones.
So there's many libraries exists doing this.

To exclude same... from perspective on algorithm, we only get in/output similarity or algorithm similarity itself.
So we need same from perspective on data to exclude multiple description writing on the code. However, this is already done by some of the known ongoing libraries s.t. bison/json for best practice. So there isn't exist new field for us (however, there could be another way for another peroson... eg. programs for the web).

However, it would be greately appreciated if you know the methods reducing source code other than along with preparing data nor how to treat data in the codes.

# Tips on hard tune to break output
The -Ohard loop hard optimization causes our phenomenon - structure also algorithm one to one map slips as a result of N-calculation on QP shortest path around hypothesis and their combination phenomenon.

So to avoid them, we need to add some extra constant variables on loop even we only need only one dimension for them in surface.

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
2024/04/15 update readme.
2024/04/20 add tips on layers.
2024/05/16 try to include auditing perspective, however, we don't know how to do them now (might be only the way is to compress some well written libraries as the descriptions only).
2024/09/06 fix and simplify, punch some non needed readme.
2025/02/02 update readme, update control directory, should go this but we don't have much reason.
2025/05/31 update readme, for readability reason, we can go with this, but also in maze is it have some meaning in this decade?
2025/10/27 update readme. -Ohard exceptions.


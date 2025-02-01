# NAND(Never finish)
Natural tinier compiler which code with natural tinier comments and licenses on a file aims to easy to audit.

This aims to compile nand source into C or lisp source and check the output by hand or eyes.
Otherwise, they can even infect if whole system is infected condition.
(All we can do is to transcode and check the transformed or compiled source by hands or eyes even any of the code patches, or, we can do only to crypt them with the cryption algorithm hidden from the attacker.)

# Syntax concrete (b).
* ':' directive on root context
* * namespace-name : "(uri|path)"(.type|.function|.op)?
* * * import once, no need include guard.
* * * to define some of the name, we should use separated file.
* * operator-name(\[templates...\]) : inherit-op(\[templates...\])? : type?
* * * multiple lines.
* * * operator collections to types.
* * * if caller specified name doesn't match this op, call inherit.
* * * enter, leave, call, return
* * * * for each operator call, non const or const first/last operation.
* * * (operators)
* * * * could call another operator classes.
* * type-name(\[templates...\]) : inherit-type(\[templates...\])?
* * * multiple lines.
* * * use some integer or type sets as a type.
* * * like typedef struct ... in C but with ctor(...), dtor().
* * * ctor(name! ...) '\!' specifies moved argument.
* * * val \. element : in type element lookup out of the scope.
* * * enter, leave
* * * * for each variable change
* ':' directives
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
* * * on function call, pass const type to type causes auto making instance.
* * * export exports the function, also prevent to be inlined.
* Special characters
* * Int
* * * one of two type we have on this, pointer wide, full set of arithmetic/bit ops.
* * Vec\[type\]
* * * one of two type we have on this, vector we call ctor(...), dtor() on around instances, first operand with size.
* * * We have : reserve, resize, push, pop, delete, op \[\] type function on this,
* * move(...)
* * * like in C++, we use pointers to compile so instance move.
* * op-noop
* * * noop root operator.
* * type-root
* * * root of the type, void, no internal states.
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * () ? () : ()
* * * 3-term operator like in C.
* * 'label : (for|para)\[operator\] ... from ... to ...', operator ++, operator \< function definition is used,
* * * break label
* * * when parallel, out of the scope treated as global, in the scope treated as thread variable (except for the reference).
* * assert(x)
* * * stop execution or compilation if x is false.
* * * we can override this with assert function redefinition in execution time.
* * \# will treat line after them as a comment.
* * * \# license? comment...
* * type or op can specify (type \| ... \| type) or (op \| ... \| op), also be able to specify template omitted.
* * It's no concrete 'private' definition.

# Tips on layers
There exists universal approximation theorem around 1980s-1990s but ongoing machie learnings uses many of layers often have 6 or so.
This is valid because non commutative algebra between the layers has the limit 6 dimension without some habit vectors from the perspective we have.
Also, the 6 of layers can be reduced into 4 of layers if we only to apply such learned results into some of the input stream.
So same method, we can reduce 2/3 per each on only to apply some functions, however, there's some entropy vs. last observation limit we don't get better result lower bound.

Also, the internal states entropy the function and the learned vector have has the upper bound up to around 2Pbits or so, without some habit vectors, from 3-function 16-depth tri-colored tree perspective.
So we need up to around 250TB on the memory, however, we cannot have them from our currency reason, so we can only get some projection of them by some larger communities.

Also, to learn something from the vector set, we need the vector dimension up to d := 2/sqrt(log(2)) \* sqrt(n \* log(n)) for n : input number of the vectors.
This is the rough our limit on learning.

Whole of this tip, so we need the internal states bits, in another words, the vector dimension on some machine learning, has the upper bound from 2 of them:
(i) vector input number, (ii) the dimension the function input/output have.
(i) is described below d \* 4 + 19683, (ii) is around dimension \* 4 + 19683.

So en/decode the input is the matter but this is well done by some places and someones we can find on the Internet.
So there's no new field on us.

# Tips on reduction
To make things simple enough easy to audit, we need to reduce the code amount.

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
Either, in the form p1 and randtools treats the input as finite accuracy fixed point number but aligns on last of the function, so around middle part of the function could be broken as some of discontinuity.
So the concrete method to have correct result cannot reduce or omit some of the loop number or algorithm topology as to be a Lie algebraic continuity.

So if this condition is true for our observations, some of the continuity concerns some of the observation.

However, there's also the probability they depends on data amount function have itself only.

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



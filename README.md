# NAND(Never finish)
Natural tinier compiler which code with natural tinier comments and licenses on a file.

A randtools optimizer is valid in making invariant meaning, however is not valid in output complexity meaning. So if we decide to use safe method, no hard optimization can be accepted, if we decide to believe invariant meaning strong, whole program optimization is accepted.

This aims to compile nand source into C source and check the output by hand or eyes. Otherwise, they can even infect if whole system is infected condition. (All we can do is to transcode and check the transformed or compiled source by hands or eyes even any of the code patches, or, we can do only to crypt them.)

# Read some modern language descriptions
Some of the syntax changes, however, isn't concrete enough.

We should have operators to types as possible as enough transparent ones.

Because some of the state-of-the-art languages says the class capsule as
problematic ones.

# Syntax concrete (6).
* load is omitted in root context. (root context only)
* * name : "(uri|path)"(.type|.function)?
* * import once, no need include guard.
* * also, we should use this as define directives.
* let is omitted
* * a : b
* * a : const(b)
* * * a is (non const) reference of b or const reference of b.
* * * the original variable will not be used like some awesome languages.
* * a : static(b)
* * * a is initialized by b once in first of execution.
* * a : func(b)
* * * a is instanced variable of function.
* * a : func!(b)
* * * a is function returned reference.
* * * we should use function definition as entity ones in header files.
* * a : operator-name(\[...\])\[b\]
* * * bind operator to type as a variables.
* name(name : type (: "comment")?, ...) const? : (inline)? type
* * function, name! returns reference.
* * with calling function, we must specify the variable name as: name(name = val, ...)
* * no return mnemonic, instead of them, reserved "res" variable.
* * from awesome embedded C language.
* op(\[templates...\])? operator-name : type-name (root context only)
* * operator collections transparent to types.
* * enter, leave, call, return
* * * for each operator call, non const or const first/last operation.
* * (operators)
* * * could call another operator classes.
* Special variables
* * Int
* * * only type we have on this, pointer wide, full set of arithmetic/bit ops.
* * type typename
* * * use some integer sets as a type.
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * \_\_callgraph\_\_
* * * information for debugging.
* Special flows
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
* * type can specify (type \| ... \| type), also be able to specify template omitted.
* * val \. element
* * * in type element lookup.
* * defined?(...)
* * * refers name table, returns true or false in first Int type.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
For this, please refer randtools (with F_p integer, using (F_p)^k register on each).
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

# Things undone.
This repository has NO materialized implementation.
There exists huge fields they have important materials.

# Control directory
We cram the scrapped delusion which all the things we want supported by computer for now into Control directory (can be different from yours). Some of the future, this categorize can be changed.

# close readme.md and their fixes
2023/08/10.
2023/08/10 fix some.

#


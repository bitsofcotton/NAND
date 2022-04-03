# NAND(Never finish)
Natural simpler compiler which code with natural simpler comments and licenses on a file.

Aims to add one of a code stack s.t. small code amount on both compiler/library with comment connected (ideally one can read whole easily) bases on not the latest but a modern C compiler. But to make this practical, we need const. operation hard optimization.

Library target : working memory size as O((input size)^2) to make tables, calculation step on each function upto O(((mem size) * lg(mem size))^1.5), ideally O(lg((mem size) * lg(mem size))), O(lg(mem size)) with caching for outlet.

# Syntax freeze.
* load (name :)? (uri|path.path...)(.type|.function)
* type classname : inherit : "comment" : "license"
* * Only one class inheritation is accepted.
* def name : definition : "comment" : "license"
* * block-wise.
* let is omitted, like swift's let:
* * a : b
* * a : const(b)
* * * a is (non const) reference of b or const reference of b.
* * * the original variable will not be used like some awesome languages.
* * a : static(b)
* * * a is initialized by b once in first of execution.
* * a : auto(b)
* * a : type(b)
* * a : func(b)
* * * a is instanced object of b
* * a : func!(b)
* * * a is function returned reference.
* * a : (fn ...)(...) \\ ...
* * * initialize with lambda function.
* * a : b : "comment" : "license"
* * * comment and license.
* fn name(name : type : "comment", ...) : type : "comment" : "license"
* * function, also lambda be. from awesome scala.
* * function name! returns reference.
* a +=item val
* * operator with some extension to C.
* * super class operator is also operator +=item .
* * if there's no such operator, search super, then, replace with
* * root class definition on op += or some with refactored one.
* start with _ as private in type
* friend
* * in-type friend functions to write down inter-type initializer operator.
* ctor, dtor
* * from some awesome programming languages.
* enter, leave
* * every variable change, we call this first / last.
* * only described in the same class are affected.
* only variable/ctor/dtor/enter/leave/friend/operator can be defined in type block.
* this and leaf (end of leaf of the object) and super object references.
* typeof, typeid
* 'for ... in ... : label', type.foreach class function definition is used,
* * break label
* inverse(function, result) : worst case brute force inverse function.
* special types can be overrided.
* * Int\[0\] : void, Object root, no inheritation.
* * Int\[__pointer_bits_\] inherites Int\[0\]. : only one integer class, bool for nonzero, on register integer.
* * Duck[type, type, ...] : Duck type programming
* special functions
* * assert(x)
* * * stop execution or compilation if x is false.
* * Duck function("function name")
* * * returns function that have function name.
* special variables
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * \_\_callgraph\_\_
* * * information for debugging.
* flows
* * if ... elif ... else
* * switch-case for constant. case variable optimization.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
For this, please refer randtools (with F_p integer, using (F_p)^k register on each).

So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).

# General Tips
If we have described end of condition as condition itself, the algorithm is defined and it is usually be optimization problem.
So we need the code set faster than them ideally described in above, s.t. for m constraint n variables, ideally memory is smaller than O(mn), arithmetic operation number is smaller than O(mn^2), for mn core CPUs, the time is faster than O(lg(m) + lg(n) + L) for L bit operation.



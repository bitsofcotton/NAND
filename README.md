# NAND(Never finish)
Natural simpler compiler which code with natural simpler comments and licenses on a file.
Aims to add one of a code stack s.t. small code amount on both compiler/library with comment connected (ideally one can read whole easily) bases on not the latest but a modern C compiler. This repository pefer explicit description.

# Syntax freeze.
* load (name :)? (uri|path.path...)(.type|.function)
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
* * type can specify (type \| ... \| type), also be able to specify template omitted.
* * with calling function, we must specify the variable name as: name(name = val, ...)
* inverse(function, result) : worst case brute force inverse function.
* typeof, typeid
* type classname : inherit : "comment" : "license"
* * Only one class inheritation is accepted. Treat as arithmetic ones.
* * a +=item val
* * * operator with some extension to C.
* * * super class operator is also operator +=item .
* * * if there's no such operator, search super, then, replace with
* * * root class definition on op += or some with refactored one.
* * start with _ as private in type
* * friend
* * * in-type friend functions to write down inter-type initializer operator.
* * ctor, dtor
* * * from some awesome programming languages.
* * enter, leave
* * * every variable change, we call this first / last on all of the functions in type.
* * only variable/ctor/dtor/friend/enter/leave/operator can be defined in type block. only operator we can specify return type others auto generated with this or void.
* * needs super function explicit to call super functions, not to be auto called.
* * this and leaf (end of leaf of the object) and super object references.
* special types and variables and flows.
* * Int\[0\] : void, Object root, no inheritation.
* * Int\[\_\_pointer_bits\_\_\] inherites Int\[0\]. : only integer class, bool for nonzero.
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * \_\_callgraph\_\_
* * * information for debugging.
* * () ? () : ()
* * * 3-term operator like in C.
* * return result
* * 'for ... from ... to ... : label', type.op ++for, type.op \<for function definition is used,
* * * break label
* * assert(x)
* * * stop execution or compilation if x is false.
* \# will treat line after them as a comment:

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
For this, please refer randtools (with F_p integer, using (F_p)^k register on each).
So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).

# General Tips
If we have described end of condition as condition itself, the algorithm is defined and it usually be optimization problem.
So we need the code set better efficient than them s.t. for m constraint n variables, ideally memory is smaller than O(mn), arithmetic operation number is smaller than O(mn^2), for mn core CPUs, the time is faster than O((lg(m) + lg(n)) \* L) for L bit operation.



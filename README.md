# NAND(Stub)
Natural simpler compiler which code with natural simpler comments and licenses on a file.

We support: type safe, class capsule, assertion, data integrity check gate (mutex for them), and don't support special flows.

Aims to small code amount with comment connected, moderate worst-case speed, no matter better-case speed with medium functionality.
So we target to implement working memory size as O((input size)^2) to make tables, calculation on each function upto O(((mem size) * lg(mem size))^1.5), ideally O(lg((mem size) * lg(mem size))), especially no block condition, O(1) with caching for outlet.

Also aims to revert operation via randtools solver but to be brute force in some cases, both compiler and entire library source code be in the size one can read easily, which compiler itself is in specific mnemonic code.

So the source codes we reference is huge, it should import prior sources with license notifications.

# Draft syntax.
* header
* * using name : (path.path(.type)|type)
* * type classname (: inherit) : "comment" : "license"
* * * Only one class inherit is accepted.
* * def name : definition : "comment" : "license"
* * * block-wise.
* * let : like swift:
* * * let a : b
* * * let a : const(b)
* * * * a is (non const) reference of b or const reference of b.
* * * * the original variable will not be used like some awesome languages.
* * * let a : auto(b)
* * * let a : type(b)
* * * let a : func(b)
* * * let a : const auto(b)
* * * let a : const type(b)
* * * let a : const func(b)
* * * * a is instanced object of b
* * * let a : func!(b)
* * * let a : const func!(b)
* * * * a is function returned reference.
* * * let a : b : "comment" : "license"
* * * op +=item val
* * * * operator with some extension to C.
* * * * super class operator is also operator +=item .
* * * * if there's no such operator, search super, then, replace with
* * * * root class definition on op += or some with refactored one.
* * fn name(name : type : "comment", ...) : type : "comment" : "license"
* * * function, also lambda be. from awesome scala.
* * * name! returns reference.
* * friend
* * * in-class friend functions to write down inter-class initializer operator.
* * start with _ as private
* * ctor, dtor
* * * from some awesome programming languages.
* * enter
* * ensure
* * * every variable change, we call this first / last.
* * * only described in same class are affected.
* * this and leaf (end of leaf of the object) and super object references.
* * typeof, typeid
* source
* * 'for ... in ... : label', no 'for ... ; ... ; ...'.
* * inverse(function) : worst case brute force inverse function.
* special types can be overrided.
* * Int\[0\] : void, Object root.
* * Int\[platform_depends\] inherites Int\[0\]. : only one integer class, bool for nonzero, on register integer.
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

* pending libraries
* * Range\[def type, type lower, type upper, type default\]
* * * restrict inputs.
* * State\[Int states\]
* * * Status class, initialize with json,
* * * returns next status function pointer on each.
* * Struct\[Array\[Int\] size\]
* * * Copy reference structure from file, and write to file.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
For this, please refer randtools (with F_p integer, using (F_p)^k register on each).

So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).


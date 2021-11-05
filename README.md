# NAND(Stub)
Natural simpler compiler with natural simpler comments on file.
Aims to small code amount with comment connected, moderate worst-case speed, no matter better-case speed with medium functionality, zero copy without relocation nor i/o.  

(We target to implement working memory size as O((input size)^2) to make tables, calculation on each function upto O(((mem size) * lg(mem size))^1.5), ideally O(lg((mem size) * lg(mem size))), especially no block condition, O(1) with caching for outlet.
So overall we estimate to target the functions O(((input size)^2 * lg(input size) * lg((input size) * 2 * lg(input size)))^1.5 + (cache calculation time) * (depth in functions) * (cache size)). Overall we claculate with cache, O((input size)^4 lg^3((input size) * lg(input size)) * #(calculation function)) in worst case, this is equivalent to O((mem size)^2 lg^3((mem size) * lg(mem size)) * #(calculation function)) in worst case. So we target with many core architectures to have the core# such of them.)

Aims to revert operation via randtools solver but to be brute force in some cases. Library oriented. Convert to C language.

So it's huge, it should import prior sources with license notifications, so multiple file link is needed.

Const operation should be hardly calculated to optimize.  

Aims to both compiler and entire library source code are size that is readable by one person, compiler itself in specific mnemonic code.

Searching the ways to prevent mistakes in the code other than type-safe, class-capsule, assertion. (to guarantee intend|expect to do.)

# Draft syntax.
* header
* * using name : (path.path(.class)|class)
* * * use library (class) as the name.
* * class classname (: inherit) : "comment" : "license"
* * * pure class, only one class inherit is accepted.
* * def name : definition : "comment" : "license"
* * * type and some definitions, block-wise.
* * let : like swift:
* * * let a : b
* * * let a : const(b)
* * * * a is (non const) reference of b or const reference of b.
* * * let a : auto(b)
* * * let a : type(b)
* * * let a : func(b)
* * * let a : func!(b)
* * * let a : const auto(b)
* * * let a : const type(b)
* * * let a : const func(b)
* * * let a : const func!(b)
* * * * a is instanced object of b
* * * * or operator type operator on object of b
* * * * func! returns reference.
* * * let a : b : "comment" : "license"
* * * * with comment.
* * * op +=item val
* * * * operator with some extension to C.
* * * * super class operator is also operator +=item .
* * * * if there's no such operator, search super, then, replace with
* * * * root class definition on op += or some with refactored one.
* * fn name(name : type : "comment", ...) : type : "comment" : "license"
* * * function, also lambda be. from awesome scala.
* * * const return type makes reference to the variable.
* * friend
* * * in-class friend functions to write down inter-class operator.
* * start with _ as private
* * ctor, dtor
* * * from some awesome programming languages.
* * enter
* * ensure
* * * every variable change, we call this first / last.
* * this and leaf (end of leaf of the object) and super object references.
* * typeof, typeid
* * * typeof(this), typid(class name) and so on.
* source
* * no exception methods, instead of it, template class result.
* * no thread directives, instead of it, template class.
* * with parallel 'for ... in ... : label', no 'for ... ; ... ; ...'.
* * inverse(function) : worst case brute force inverse function if function
* * is a deterministic one.
* special classes can be overrided.
* * Int\[0\]
* * * void, Object root.
* * Int\[1\] inherites Int\[0\]. : bool class.
* * Int\[platform_depends\] inherites Int\[0\]. : only one integer class.
* * * on register integer.
* * Duck[type, type, ...]
* * * Duck type programming.
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

# General Tips
If the data is enough, machine learning methods can implement any of the implementation.
For this, please refer randtools (with F_p integer, using (F_p)^k register on each).

So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).

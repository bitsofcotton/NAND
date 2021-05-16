# NAND
Natural simpler compiler with natural simpler documentation on pairs of file.
Aims to small code amount with documentation, moderate worst-case speed, no matter better-case speed with medium functionality.
And aims to revert operation via randtools solver. Library oriented. Convert to C language.
So it's huge, it should import prior sources with license notifications, so multiple file link is needed.
And, const operation should be hardly calculated to optimize.  

Stub of planning project.

If you know other techniques to have an language structure that source code
structure to be write once and small amount of lines with low complexity
on both compiler and program, please teach me, or, simply please send me
on issue on this bitsofcotton/NAND .

# Syntax Before draft.
* header
* * using name : path.path(.class)
* * * use library (class) as the name.
* * class classname (: inherit) : "comment"
* * * pure class, only one class inherit is accepted.
* * def name : definition : "comment"
* * * type and some definitions, block-wise.
* * let : like swift:
* * * let a : b
* * * let a : const(b)
* * * * a is (non const) reference of b or const reference of b.
* * * let a : auto(b)
* * * let a : type(b)
* * * let a : func(b)
* * * let a : const auto(b)
* * * let a : const type(b)
* * * let a : const func(b)
* * * * a is instanced object of b
* * * * or operator type operator on object of b
* * * * or function return makes some object.
* * * * (const ... defined function returns reference).
* * * let a : b : "comment"
* * * * with comment.
* * * operator +=item val
* * * * operator with some extension to C.
* * * * super class operator is also operator +=item .
* * * * if there's no such operator, search super, then, replace with
* * * * root class definition on operator += or some with refactored one.
* * fn name(name : type : "comment", ...) : type : "comment" (definition)
* * fn name(name : type, ...) : type (function)
* * * function definition. also lambda be. from awesome scala.
* * * const return type makes reference to the variable.
* * friend
* * * in-class friend functions to write down inter-class operator.
* * start with _ as private
* * ctor, dtor
* * * from some awesome programming languages.
* * ensure
* * * every variable change, we call this last.
* * this and leaf (end of leaf on the object) and super object references.
* * typeof, typeid
* * * typeof(this), typid(class name) and so on.
* source
* * no exception methods, instead of it, template class result.
* * no thread directives, instead of it, template class.
* * with parallel 'for ... in ...', no 'for ... ; ... ; ...'.
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
* special variables
* * \_\_pointer_bits\_\_
* * * number of pointer bit size.
* * \_\_here\_\_
* * * information for debugging.
* * \_\_callgraph\_\_
* * * information for debugging.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation. For this, please refer randtools (with F_p integer, using F_p^k register).
<!--
In another words, topology of the machine learning block diagrams is needed in only the case when we met the condition the problem is huge nor the problem is something sparse.
-->

So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system).
<!--
In another words, if we don't need such readability and we have much of datas and their relations, machine learning is better.
We call when the constraints size is able to count-up by human, it's readable one. If the data we collected is not so concrete, the results also be not so concrete when machine learning. -->


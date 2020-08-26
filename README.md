# NAND
Natural simpler compiler with natural simpler documentation on pairs of file.
Aims to readability (for me), compact and low-complexity implementation, moderate worst-case speed, no matter better-case speed.
And aims to revert operation via QP solver. Library oriented. Convert to C language. So it's huge, it should import prior sources with license notifications, so multiple file link is needed. And, const operation should be hardly calculated to optimize.  

Stub of planning project.

# Syntax Before draft.
* header
* * using name : path.path(.class)
* * * use library (class) as the name.
* * class classname (: inherit)
* * * pure class, only one class inherit is accepted.
* * def name : definition
* * * type and some definitions, block-wise.
* * let : like swift:
* * * let a : b
* * * * a is reference of b.
* * * let a : auto(b)
* * * let a : type(b)
* * * * a is instanced object of b or operator type object of b.
* * * let a : const(b)
* * * let a : var(b)
* * * * const cast
* * * operator +=item val
* * * * operator with some extension of C.
* * fn name(type, ...) : void
* * * function definition. also lambda be.
* * friend
* * * in-class friend functions.
* * start with _ as private
* * ctor, dtor
* * * from some awesome programming languages.
* * this and leaf (if it's end leaf, this ref) and super object references
* source
* * no exception methods, instead of it, template class result.
* * no thread directives, instead of it, template class.
* * with parallel 'for ... in ...', no 'for ... ; ... ; ...'.
* special classes can be overrided.
* * Int\[0\]
* * * void, Object root.
* * Int\[platform_depends\] inherites Int\[0\].
* * * on register integer.
* * Duck[type, type, ...]
* * * Duck type programming.
* special functions
* * assert(x)
* * * stop execution or compilation if x is false.
* special variables
* * __pointer_bits__
* * * number of pointer bit size.
* * __here__
* * * information for debugging.

# General Tips
If the data is enough, machine learning methods can implement any of the implementation because A in N^{n\*n}, A\*2^x in randtools meaning.
If we're working on R, with logarithm and exponent matrix (can be defined with differential matrix, not the logarithm of matrix nor exponent of matrix), we can handle transcendental numbers on them (if the data series is enough). If data is not seriarized, exp(A\*log(x)) can be used for them. So general form is as Sum exp(A_k\*log(x)) + A_0\*x, this can be trained with existing machine learning things. So almost any of the algorithms we met (on converged series) can be described as machine learning.

On the other hands, Quadratic Programming also in them, any of inverse function on the computer that all part converges can be described as quadratic programming form.

So around this, we aims and we need the implementation of compact and low complexity and whole readable library, (and system). (In another words, if we don't needs such things and we have much of datas, machine learning is better.)

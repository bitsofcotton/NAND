# NAND
Natural simpler compiler with natural simpler documentation on pairs of file.
Aims to readability (for me), compact and low-complexity implementation, moderate worst-case speed, not slow better-case speed.
And aims to revert operation via QP solver. Library oriented. Convert to C language. So it's huge, it should import prior sources with license notifications, so multiple file link is needed. And, const operation should be hardly calculated to optimize.  

Stub of planning project.

# Syntax Before draft.
* header
* * using   : use library (as the name).
* * class   : pure class, only one class inherit is accepted.
* * extend  : pure extends class.
* * def     : type and some definitions, block-wise.
* * var     : like swift:
* * * var a : b
* * * * a is reference of b.
* * * var a : auto(b)
* * * var a : type(b)
* * * * a is instanced object of b.
* * * var a : const(a)
* * * var a : var(a)
* * * * const cast
* * * operator +=item val
* * * * operator with some extension of C.
* * * fn name(type, ...) : void
* * * start with _ as private
* * * ctor, dtor
* * * * from some programming languages.
* * * this and leaf and super object references
* source
* * no exception methods, instead of it, template class result.
* * no thread directives, instead of it, template class.
* * with parallel 'for ... in ...', no 'for ... ; ... ; ...'.
* special classes can be overrided.
* * Object
* * Int<8>
* * Int<16>
* * Int<32>
* * Int<64>
* * Float is for speed, it's not invertible in general.
* * Duck

# NAND
Natural simpler compiler with natural simpler documentation on pairs of file.
Aims to readability (for me), compact and low-complexity implementation, moderate worst-case speed, not slow better-case speed.
And aims to revert operation via QP solver. Library oriented. Convert to C language. So it's huge, it should import prior sources with license notifications, so multiple file link is needed. And, const operation should be hardly calculated to optimize.

Stub of planning project.

# Status
Being determined syntaxes.

# Syntax Before draft.
* header
* * require : require once.
* * include : include multiple with this indent.
* * class   : pure class.
* * extend  : pure extends class.
* * def     : type and some definitions, block-wise.
* * var     : like swift:
* * * var a : b
* * * * a is reference of b.
* * * var a : auto(b)
* * * var a : type(b)
* * * * a is instanced object of b.
* * * var a : const(a)
* * * * const cast
* * * operator +=item val
* * * * operator with some extension of C.
* * * void func(type, ...)
* source
* * require 'a/b/c.hg' : python style.
* * using a.b.c.classd : C++ style.
* * void func(var a : type, ...)
* * no exception methods, instead of it, template class result.
* * no thread directives, instead of it, template class.
* * with parallel 'for ... in ...', no 'for ... ; ... ; ...'.
* special classes can be overrided.
* * Int<8>
* * Int<16>
* * Int<32>
* * Int<64>
* * Float is for speed, it's not invertible in general.
* * Duck

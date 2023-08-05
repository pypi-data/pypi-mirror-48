# Ganit (गणित)
Ganit(गणित) means calculation in Sanskrit. As the name suggests, this is a calculation utility. This is a parser library implemented in python. The library takes as argument an expression, either infix or postfix and evaluates the expression and returns the result. It supports all major mathematical functions. This uses a slightly extended version of Shunting Yard algorithm. You can read more about this algorithm [here](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).

The evaluator can take variables as arguments. So, evaluation of expression like `x^2 + y^3` is possible with this library. It can also take an expression as a variable.So, function composition is also supported. Or in other words, nested expression like `cos(x^2+y^2)^2 + sin(x^2+y^2)^2` is also possible. Or even evaluation of nested expression like `cos(y); y = sin(theta); theta=acos(sin(x)); x = 45` is possible, it actually evaluates `cos(sin(acos(sin(45))))` in this case. It starts from the innermost expression and gradually evaluates the outermost.

Apart from evaluating the expression, parser can return prescanned expression. A prescanned expression is the one which converts an expression by changing multiple occurences of +/-. e.g. `-2` will be converted to `0-2` and `--2` to `0+2` or `---2` to `-2` and so on. Similar changes occur for multiple occurences of `+` as well.

The parser can also return the postfix expression of a given infix expression. e.g. `2 * 4` will be returned as `2 4 *`.

Please note that, the logical, trigonometric, algebraic etc. expression group evaluation is not part of original Shunting Yard algorithm. To extend the functionality I had to extend the Shunting Yard Algorithm. So, if the original expression comes with any Logical Expression, the resultant postfix is not a pure result of Shunting Yard algorithm and if you are planning to use the Coverted Postfix Expression to some other Postfix evaluator, please make sure that the evaluator also supports the conversion. Please check Logical Operations subsection for more details on what are all the conversions happen for Infix to Postfix evaluation. On the other hand, if you have any other postfix expression which has characters other than Basic Arithmetic Operators, the expression may fail evaluation. A list of all the supported functions and operators are available in 'Supported functions' section.

## Usage
### pip install
The module can be installed using pip with the following command-
```bash
$ sudo pip install ganit
```
### Download Source Code
The source code can be downloaded and the parser can be called directly in program.

Once the package is downloaded, you can use the main `Parser` module from the package and use it in your application.

```python
# import the library and the main parser module
from ganit import Parser
# Create an object of the parser
p = Parser()
print(p.prescan("2 * 4")) # It will print '2*4'
print(p.convert("2 * 4")) # It will print '2 4 *'
# Evaluate the expression
print(p.evaluate("2*4")) # It will print '8'
```
The other way to use Ganit is in console itself. This may be useful while writing some application with Ganit Library to know the result of it beforehand. Following is an example Ganit console session -

```python
$ python
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ganit import ganit
>>> ganit()
Type quit to exit
Ganit>>> 2*4
Prescanned Expression 2*4
Postfix Notation 2 4 * 
Evaluation Result 8
Ganit>>> 5*7==35?30:25
Prescanned Expression 5*7=35?30:25
Postfix Notation 5 7 * 35 = 30 ? 25 : 
Evaluation Result 30
Ganit>>> 6 & 6
Prescanned Expression 6&6
Postfix Notation 6 6 & 
'"\'&\' only works for boolean conditions"'
Ganit>>> True & False
Prescanned Expression True&False
Postfix Notation True False & 
Evaluation Result False
Ganit>>> 
```

## Evaluation
The library can be used for 3 different tasks -
* Prescanning of an expression
* Conversion of infix notation to postfix notation
* Evaluation of Infix/Postfix expression

The library gives 5 predefined variables -
1. **e** - Euler's Number
1. **pi** - π
1. **tau** - τ, the circle constant equal to 2*π, the ratio of a circle’s circumference to its radius.
1. **True** - boolean True value to work with logic expressions. If any expression tries to do any mathematical operation on `True`, it is treated as 1. So, `1+True` results in `2`.
1. **False** - boolean False value to work with logic expressions. If any expression tries to do any mathematical operation on `False`, it is treated as 0. So, `1+False` results in `1`.
1. **now** - gives datetime object which has value of now, returns the current timestamp
1. **today** - gives date object which has value of today, returns the current date

### Prescanning of Expression
If an infix expression is not properly embraced, finding the difference between negation and subtraction is difficult during infix to postfix conversion. So, before processing an infix notation, the library checks for occurences of minus/plus signs and tries to find what purpose the sign is serving.
Below are some conversions happened during prescan-
 * '-2' is changed to '0-2'
 * '--2' is changed to '0+2'
 * '---2' is changed to '0-2'
 * '(-2)' is changed to '(0-2)'
 * '4*-7' is changed to '4*(0-7)'

Similar logic is also applied for multiple occurences of '+' sign as well. This method also converts all the two character operators to single character operator for shunting yard algorithm to work properly, e.g. '==' converts to '='. Please check the 'Test' section for more details.

The argument of prescan is the expression to be evaluated. A 'dict' object can also be passed as argument, which has a key "exp". The "exp" key of the 'dict' object holds the expression.

This method does not check for validity of the expression. e.g. If you pass an expression with a variable and the variable is not passed, the method still succeeds and returns a changed expression.

Following are some examples of  prescan

```python
from ganit import Parser
p = Parser()
# prescan the infix expression
print(p.prescan("2 * 4")) # It will print '2*4'
# passing dict as expression
d = {"exp": "2 * x"}
print(p.prescan(d)) # It will print "2*x"
print(p.prescan(2)) # It will print "2"
print(p.prescan(3.14)) # It will print "3.14"
```

### Conversion of Infix to Postfix
Before evaluating any expression, parser converts any infix notation to postfix notation, thus making the processing easier.

This uses a slightly extended version of Shunting Yard algorithm. You can read more about this algorithm [here](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

The convert method takes 2 arguments -
1. The required exp argument, which can be either an 'int' or 'float' or 'str' object (where you do not need to pass any variables) or a 'dict' object containing keys "exp" and "variables".
1. In case the first argument is 'str', a 'dict' object with all the variables can be passed to it. If the first object is 'dict' object, the second argument is ignored.

This method checks the validity of the passed infix expression but does not evaluate it.

```python
from ganit import Parser
p = Parser()
# Convert only numeric or predefined variables like e, pi and tau
print(p.convert("2 * 4")) # It will print '2 4 *'
d = {"exp": "2*x", "variables": {"x":2}}
print(p.convert(d)) # It will print '2 x *'
print(p.convert(d, {"y": 2})) # It will print '2 x *'
d = {"exp": "2*x", "variables": {"y":2}}
print(p.convert(d)) # It will throw error as the variable 'x' is not passed as variable
print(p.convert(d, {"x": 2})) # It will also throw an error, as the first object is of type dict, so second argument is ignored.
print(p.convert("2*x", {"x": 2})) # It will print '2 x *'
print(p.convert(2)) # It will print '2'
print(p.convert(2, {"x": 2})) # It will print '2'. The second argument is ignored.
print(p.convert("2 * pi")) # It will print '2 pi *'
```

### Evaluation of Infix/Postfix expression
The actual evaluation happens here.

The evaluate method has 3 arguments -
1. The required exp argument, which can either be an 'int', a 'float' or a 'str' or a 'dict' object containing "exp", "variables", "convert" as keys. The expression passed to this method can also be a postfix notation.
1. The second argument is a 'bool' value. This determines if the expression needs to be first converted to a postfix nontation or not. If an postfix notation is passed, this variable should be passed as False. The default value is True. If the first argument is of type 'dict', this value is ignored, even if passed.
1. If the first argument is 'str', a 'dict' object with all the variables as keys can be passed to it. If the first object is 'dict' object, this argument is ignored.

This method checks the validity of the passed postfix expression first, then proceeds with evaluation. If postfix notation is wrong, it does not perform any calculation.

Evaluation can be done in nested fashion. So, an expression can contain a variable which in turn is another expression and the pattern go infinitely (or, till stack supports).

```python
from ganit import Parser
p = Parser()
print(p.evaluate("2 * 4")) # It will print '8'
print(p.evaluate("2 * x")) # It will throw error
print(p.evaluate("2 * x", {"x": 2})) # It will print 4
# A postfix notation is passed as argument
print(p.evaluate("2 x *", False, {"x": 2})) # It will print 4
# Nested Expression
d = {"exp": "2 * x", "variables": { "x": {"exp": "2*y", "variables": {"y": 3}} }}
p.evaluate(d) # it will print '12'
# Nested postfix expression
d = {"exp": "2 * x", "variables": { "x": {"exp": "2 y *", "convert": False, "variables": {"y": 3}} }}
p.evaluate(d) # it will also print '12'
```
## Variable naming restriction
This evaluator works on shunting yard algorithm. But the basic shunting yard algorithm does not have very extensible support for operators spanning more than 1 character and also do not support different mathematical functions (such as, log, sin, cos etc). So, to add these functionality, the algorithm has been extended a little bit to suit these needs. Most of the two character logical expressions are internally converted to use single variable. So, apart from the basic arithmetic operators and mathematical function names, we reserve some characters for this conversion and these characters can also be not used as variable names for the expression. Following is the complete list of characters and function names, that are being used internally in some or the other ways.

Variable names are case sensitive. So, `x` is not same as `X` or vice versa.

Sl. No. | Name | Type
------- | ---- |----
1 | `+` | Basic Operation
2 | `-` | Basic Operation
3 | `*` | Basic Operation
4 | `/` | Basic Operation
5 | `%` | Basic Operation
6 | `^` | Basic Operation
7 | `abs` | Algebraic Function
8 | `ceil` | Algebraic Function
9 | `floor` | Algebraic Function 
10 | `round` | Algebraic Function 
11 | `factorial` | Algebraic Function
12 | `gcd` | Algebraic Function
13 | `exp` | Algebraic Function
14 | `pow` | Algebraic Function
15 | `sqrt` | Algebraic Function
16 | `log` | Algebraic Function
17 | `ln` | Algebraic Function
18 | `log2` | Algebraic Function
19 | `Log` | Algebraic Function
20 | `sin` | Trigonometric Function
21 | `cos` | Trigonometric Function
22 | `tan` | Trigonometric Function
23 | `asin` | Trigonometric Function
24 | `acos` | Trigonometric Function
25 | `atan` | Trigonometric Function
26 | `sinh`  | Trigonometric Function
27 | `cosh` | Trigonometric Function
28 | `tanh` | Trigonometric Function
29 | `asinh` | Trigonometric Function
30 | `acosh` | Trigonometric Function
31 | `atanh` | Trigonometric Function
32 | `hypot` | Trigonometric Function
33 | `deg` | Angle Unit Conversion
34 | `rad` | Angle Unit Conversion
35 | `?` | Ternary Operator
36 | `:` | Ternary Operator
37 | `?:` | Ternary Operator
38 | `>` | Logical Operation
39 | `<` | Logical Operation
40 | `>=` | Logical Operation
41 | `<=` | Logical Operation
42 | `\|` | Logical Operation
43 | `&` | Logical Function
44 | `!` | Logical Operation
45 | `=` | Logical Function
46 | `==` | Logical Operation
47 | `!=` | Logical Operation
48 | `~` | Logical Operation
49 | `#` | Logical Operation
50 | `@` | Logical Operation
51 | `,` | Infix Expression Separator
52 | `(` | Infix Expression Separator
53 | `)` | Infix Expression Separator
54 | `pi` | Predefined Variable
55 | `e` | Predefined Variable
56 | `tau` | Predefined Variable
57 | `True` | Predefined Variable
58 | `False` | Predefined Variable

## Supported functions
### Basic Arithmatic Operations
1. `+` : Addition.
1. `-` : Subtraction.
1. `*` : Multiplication.
1. `/` : Division.
1. `%` : Modulus.
1. `^` : Power.

### Algebraic Operations
This section defines all the supported algebraic functions supported by the library. The functions are a thin wrapper over python Math library.

1. `abs` : this function takes only one parameter and returns the absolute value of the parameter passed. e.g. `abs(-2) = 2`, `abs(2) = 2`
1. `ceil`: this function takes only one parameter and returns the smallest integer value greater than or equal to the argument. e.g. `ceil(-2.8) = -2`, `ceil(2.8) = 3`
1. `floor`: this function takes only one parameter and returns the largest integer value less than or equal to the argument. e.g. `floor(-2.88654) = -2`, `floor(2.8) = 2` 	
1. `round`: this function takes two arguments and returns a floating point number that is a rounded version of the specified number, with the specified number of decimals. The first argument is the number to be rounded while the second argument specifies the number of decimals to be presented in the rounded number. If the second argument is 0, it returns the rounded integer.
1. `factorial`:	this function takes one integer argument and returns the factorial of the argument. If the specified number is not integral or negative, raises error.
1. `gcd`: this function takes two integers and returns the greatest common divisor of the integers a and b. If either a or b is nonzero, then the value of gcd(a, b) is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.
1. `exp`: this functions takes one arguments and returns `e` raised to the power of the argument, where `e = 2.718281…`; is the base of natural logarithms. This is usually more accurate than `e^x` or `pow(e, x)`, where is the argument.
1. `pow`: this function takes two arguments and returns the result of first argument raised to the second argument. e.g. pow(3,2) return 9
1. `sqrt`: this function takes positive number argument and returns the square root of the argument. e.g. sqrt(9) returns 3. If the specified number is negative, this function raises error.
1. `log`: this function takes one argument and returns the base-10 logarithm of the argument.
1. `ln`:  this function takes one argumetn and returns the natural logarithm of the argument (to base e).
1. `log2`: this function takes one argument and returns the base-2 logarithm of the argument
1. `Log`: this function takes two arguments and returns the logarithm of the first argument to the given base specified in second argument, calculated as log(x)/log(base).



### Trigonometric Operations

1. `sin`: takes an argument and returns the sine of the argument expressed in radians
1. `cos`: takes an argument and returns the cosine of the argument expressed in radians
1. `tan`: takes an argument and returns the tangent of the argument expressed in radians
1. `asin`: takes an argument and returns the arc sine of the argument, result is in radians
1. `acos`: takes an argument and returns the arc cosine of the argument, result is in radians
1. `atan`: takes an argument and returns the arc tangent of the argument, result is in radians
1. `sinh`: takes an argument and returns the hyperbolic sine of the argument
1. `cosh`: takes an argument and returns the hyperbolic cosine of the argument
1. `tanh`: takes an argument and returns the hyperbolic tangent of the argument
1. `asinh`: takes an argument and returns the inverse hyperbolic sine of the argument
1. `acosh`: takes an argument and returns the inverse hyperbolic cosine of the argument
1. `atanh`: takes an argument and returns the inverse hyperbolic tangent of the argument
1. `hypot`: takes two arguments and returns the Euclidean norm, `sqrt(x*x + y*y)`. This is the length of the vector from the origin to point `(x, y)`.

### Angle Unit Conversions

1. `deg`: takes an argument (in radians) and converts angle from radians to degrees.
1. `rad`: takes an argument (in degrees) and converts angle from degrees to radians.

### Logical Operations
1. `? :` : Ternary expression, this works pretty much like `if else` statement. If there is no need of an `else` statement, the `:` operation can be removed. But the `:` operation can only be used with `?`. So, any expression containing `:` but not containing `?` will throw an error. The use of this expression is as follows -
```
<Condition>?<Statement to be evaluated if condition is True>:<Statement to be evaluated if condition is False>
```
Or, you can remove the else part by removing `:`
```
<Condition>?<Statement to be evaluated if condition is True>
```
But the following will cause an error.
```
:<Statement>
```
1. `>`: Greater than.
1. `<`: Less than.
1. `>=`: Greater than Equal check. Checks if left hand side of the operator is greater than or equal to the right hand side of the operator. This operator is converted to `@` internally.
1. `<=`: Less than Equal check. Checks if left hand side of the operator is less than or equal to the right hand side of the operator. This operator is converted to `#` internally.
1. `|`: Or operation. This operator performs logical `or` operation of two operands. Please note that, this operator does not work as short circuit operator. So, both the operands will be evaluated regardless of whether the first operand evaluates to `True` or `False`. And this operator only works for boolean operands.
1. `&`: And operation. This operator performs logical `and` operation of two operands. Please note that, this operator does not work as short circuit operator. So, both the operands will be evaluated regardless of whether the first operand evaluates to `True` or `False`. And this operator only works for boolean operands.
1. `!`: Inversion operation. This operator inverses the given expression. e.g. `!True` evaluates to `False` and the vice versa. This operator is converted to `~` internally.
1. `=`: Equality check. This operator performs equality check on the operands. Operands can be float, int or boolean.
1. `==`: Equality check. This operator performs equality check on the operands. Operands can be float, int or boolean. The same operation is repeated in two different operators keeping mind the general programming language constructs. `==` is more used than `=` for equality check.
1. `!=`: Non-equality check. This operator performs non-equality check on the operands. Operands can be float, int or boolean.


## Changelog
#### Version 0.1.0
First published version. Supports all the Basic Arithmetic, Algeraic and Trigonometric functions.

#### Version 0.1.1
Added support for ternary operator, Greater Than and Less Than operator.

#### Version 0.1.2
Addition of other logical operators

#### Version 0.1.3
Added support for `!=`, `==`, `>=` and `<=` and added variable naming restriction section in the README.md.

#### Version 0.1.4
Released `$` character from Reserved Characters set and made available for variable naming. Added definitions of algebraic and trigonometric functions. Added mathematical round function.

#### Version 0.1.5
Refactored the code to use lambda expression and dictionary to make things simpler. also added two new variables, namely now and today. These two variables are planned to be used in future with date time manipulation.

#### Version 0.1.6
Released Ganit Console

#### Version 0.1.7
Ganit Console formattinf issue resolved.

## Todo
- [x] Need to create pip package
- [x] Need to complete the documentation of all the supported functions
- [x] Need to complete the logical expressions group
- [ ] Need to add support for Date/Time manipulation
- [ ] Need to add support for Matrix Manipulation
- [ ] Need to add support for vector mathematics
- [ ] Need to add support for calculus
- [ ] Need to add support for complex number
- [ ] Need to make an AST which can make it portable to any language.
- [ ] Need to write the AST and Ganit can be used on that platform (shell script, .net script (dll), Java, JavaScript etc.)
- [ ] May be port this library to npm, maven etc.

## Test
The following tests were performed on the parser. As and when new functions are added, this list gets bigger.

Sl. No. | Original Exprression | Variables| Prescanned exprression | Postfix exprression | Postfix Result
------- | -------------------- | -------- | -----------------------| ------------------- | --------------
1 | `-` | `No Variable` | `0-` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Expression ends with an operator, which is invalid. System will exit'`
2 | `-2` | `No Variable` | `-2` | `-2` | `-2`
3 | `-9*-4` | `No Variable` | `0-9*(0-4)` | `0 9 0 4 - * - ` | `36`
4 | `-2--7` | `No Variable` | `0-2+7` | `0 2 - 7 + ` | `5`
5 | `2+-7` | `No Variable` | `2+(0-7)` | `2 0 7 - + ` | `-5`
6 | `-(2*7*-7)-8` | `No Variable` | `0-(2*7*(0-7))-8` | `0 2 7 * 0 7 - * - 8 - ` | `90`
7 | `-(2*7*-7)*-8` | `No Variable` | `0-(2*7*(0-7))*(0-8)` | `0 2 7 * 0 7 - *  0 8 - * - ` | `-784`
8 | `-(2*7*-7)*(-8)` | `No Variable` | `0-(2*7*(0-7))*(0-8)` | `0 2 7 * 0 7 - *  0 8 - * - ` | `-784`
9 | `-(2*7*-7)*cos(-8)` | `No Variable` | `0-(2*7*(0-7))*cos(0-8)` | `0 2 7 * 0 7 - * 0 8 - cos * - ` | `-14.259003313244127`
10 | `-(2*7*(-7))*cos(-8)` | `No Variable` | `0-(2*7*(0-7))*cos(0-8)` | `0 2 7 * 0 7 - * 0 8 - cos * - ` | `-14.259003313244127`
11 | `-(2*7*(-7))*atan(-8)` | `No Variable` | `0-(2*7*(0-7))*atan(0-8)` | `0 2 7 * 0 7 - * 0 8 - atan * - ` | `-141.75125056031723`
12 | `-(2 + 7)` | `No Variable` | `0-(2+7)` | `0 2 7 + - ` | `-9`
13 | `4 * -8` | `No Variable` | `4*(0-8)` | `4 0 8 - * ` | `-32`
14 | ` 4*  - 8 ` | `No Variable` | `4*(0-8)` | `4 0 8 - * ` | `-32`
15 | ` 2 *(-4 +8)` | `No Variable` | `2*(0-4+8)` | `2 0 4 - 8 + * ` | `8`
16 | `1-4` | `No Variable` | `1-4` | `1 4 - ` | `-3`
17 | `1 - 4 ` | `No Variable` | `1-4` | `1 4 - ` | `-3`
18 | ` 4*8 - 2` | `No Variable` | `4*8-2` | `4 8 * 2 - ` | `30`
19 | ` 4 -  +2` | `No Variable` | `4-2` | `4 2 - ` | `2`
20 | ` 4 +  -2` | `No Variable` | `4+(0-2)` | `4 0 2 - + ` | `2`
21 | `+++++` | `No Variable` | `` | `'Invalid Expression: '` | `'Invalid Expression: '`
22 | `------` | `No Variable` | `0+` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Expression ends with an operator, which isinvalid. System will exit'`
23 | `+` | `No Variable` | `` | `'Invalid Expression: '` | `'Invalid Expression: '`
24 | `+2` | `No Variable` | `+2` | `+2` | `2`
25 | `+9*+4` | `No Variable` | `9*4` | `9 4 * ` | `36`
26 | `+2-+7` | `No Variable` | `2-7` | `2 7 - ` | `-5`
27 | `2++7` | `No Variable` | `2+7` | `2 7 + ` | `9`
28 | `+(2*7*+7)+8` | `No Variable` | `(2*7*7)+8` | ` 2 7 * 7 * 8 + ` | `106`
29 | `+(2*7*+7)*+8` | `No Variable` | `(2*7*7)*8` | ` 2 7 * 7 * 8 * ` | `784`
30 | `+(2*7*+7)*(+8)` | `No Variable` | `(2*7*7)*(8)` | ` 2 7 * 7 *  8 * ` | `784`
31 | `+(2*7*+7)*cos(+8)` | `No Variable` | `(2*7*7)*cos(8)` | ` 2 7 * 7 * 8 cos * ` | `-14.259003313244127`
32 | `+(2*7*(+7))*cos(+8)` | `No Variable` | `(2*7*(7))*cos(8)` | ` 2 7 * 7 * 8 cos * ` | `-14.259003313244127`
33 | `+(2*7*(+7))*atan(+8)` | `No Variable` | `(2*7*(7))*atan(8)` | ` 2 7 * 7 * 8 atan * ` | `141.75125056031723`
34 | `+(2 + 7)` | `No Variable` | `(2+7)` | ` 2 7 +  ` | `9`
35 | `4 * +8` | `No Variable` | `4*8` | `4 8 * ` | `32`
36 | ` 4*  + 8 ` | `No Variable` | `4*8` | `4 8 * ` | `32`
37 | ` 2 *(+4 +8)` | `No Variable` | `2*(4+8)` | `2 4 8 + * ` | `24`
38 | `1+4` | `No Variable` | `1+4` | `1 4 + ` | `5`
39 | `1 + 4 ` | `No Variable` | `1+4` | `1 4 + ` | `5`
40 | ` 4*8 + 2` | `No Variable` | `4*8+2` | `4 8 * 2 + ` | `34`
41 | ` 4 +  +2` | `No Variable` | `4+2` | `4 2 + ` | `6`
42 | `4+log(5)` | `No Variable` | `4+log(5)` | `4 5 log + ` | `4.698970004336019`
43 | `` | `No Variable` | `` | `'Invalid Expression: '` | `'Invalid Expression: '`
44 | `2+3-4/5*9` | `No Variable` | `2+3-4/5*9` | `2 3 + 4 5 / 9 * - ` | `-2.2`
45 | `2+3*log(9)-` | `No Variable` | `2+3*log(9)-` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Expression ends with an operator, which is invalid. System will exit'`
46 | `{'exp': '2*x-t*y', 'variables': {'x': 1, 't': 1}}` | `{'x': 1, 't': 1}` | `2*x-t*y` | `'Invalid input y'` | `'Invalid input y'`
47 | `{'exp': '2*x-t*y', 'variables': {'x': 1, 't': 1, 'y': 1}}` | `{'x': 1, 't': 1, 'y': 1}` | `2*x-t*y` | `2 x * t y * - ` | `1`
48 | `2*4-3` | `No Variable` | `2*4-3` | `2 4 * 3 - ` | `5`
49 | `cos(5)` | `No Variable` | `cos(5)` | `5 cos ` | `0.28366218546322625`
50 | `2.445*4-3.9*log(5, 10)` | `No Variable` | `2.445*4-3.9*log(5,10)` | `2.445 4 * 3.9 5 10  log * - ` | `'Invalid Postfix Notation: Stack not 1'`
51 | `2*4-3*log(5, 10)` | `No Variable` | `2*4-3*log(5,10)` | `2 4 * 3 5 10  log * - ` | `'Invalid Postfix Notation: Stack not 1'`
52 | `((((ln(1)+2)*3)-cos((sqrt(4)+5)))+(sqrt(ln((6*4)))+4))` | `No Variable` | `((((ln(1)+2)*3)-cos((sqrt(4)+5)))+(sqrt(ln((6*4)))+4))` | `  1 ln 2 + 3 *  4 sqrt 5 +  cos -  6 4 *  ln sqrt 4 + +  ` | `11.028807433280551`
53 | `2*3-2*8*5/2%3*abs(-4)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)` | `2 3 * 2 8 * 5 * 2 / 3 % 0 4 - abs * - ` | `2`
54 | `2*3-2*8*5/2%3*abs(-4)*ceil(2)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2)` | `2 3 * 2 8 * 5 * 2 / 3 % 0 4 - abs * 2 ceil * - ` | `-2`
55 | `2*3-2*8*5/2%3*abs(-4)*ceil(2)*factorial(2)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2)*factorial(2)` | `2 3 * 2 8 * 5 * 2 / 3 % 0 4 - abs * 2 ceil * 2 factorial * - ` | `-10`
56 | `factorial(2)*2*3-2*8*5/2%3*abs(-4)*ceil(2)` | `No Variable` | `factorial(2)*2*3-2*8*5/2%3*abs(0-4)*ceil(2)` | `2 factorial 2 * 3 * 2 8 * 5 * 2 / 3 % 0 4- abs * 2 ceil * - ` | `4`
57 | `2*3-2*8*5/2%3*abs(-4)*ceil(2.8)*factorial(2)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2.8)*factorial(2)` | `2 3 * 2 8 * 5 * 2 / 3 % 0 4 - abs * 2.8 ceil * 2 factorial * - ` | `-18`
58 | `2*3-2*8*5/2%3*abs(-4)*ceil(2.8)*factorial(2)*gcd(5,15)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2.8)*factorial(2)*gcd(5,15)` | `2 3 * 2 8 * 5 * 2/ 3 % 0 4 - abs * 2.8 ceil * 2 factorial * 5 15  gcd * - ` | `-114`
59 | `2*3-2*8*5/2%3*abs(-4)*ceil(2.8)*factorial(2)*gcd(5.2,15)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2.8)*factorial(2)*gcd(5.2,15)` | `2 3 * 2 8 * 5* 2 / 3 % 0 4 - abs * 2.8 ceil * 2 factorial * 5.2 15  gcd * - ` | `'Value Error: 15.0 , 5.2. GCD can only be determined for integers.'`
60 | `2*3-2*8*5/2%3*abs(-4)*ceil(2.8)*factorial(1.2)*gcd(5,15)` | `No Variable` | `2*3-2*8*5/2%3*abs(0-4)*ceil(2.8)*factorial(1.2)*gcd(5,15)` | `2 3 * 2 8 * 5* 2 / 3 % 0 4 - abs * 2.8 ceil * 1.2 factorial * 5 15  gcd * - ` | `'Value Error: 1.2. Factorial calculation can only be done for integers greater than 0.'`
61 | `2*3-2*8*5/2*exp(2)` | `No Variable` | `2*3-2*8*5/2*exp(2)` | `2 3 * 2 8 * 5 * 2 / 2 exp * - ` | `-289.56224395722603`
62 | `2*pow(2,3)` | `No Variable` | `2*pow(2,3)` | `2 2 3  pow * ` | `16`
63 | `2*pow(2,3)*sqrt(4)` | `No Variable` | `2*pow(2,3)*sqrt(4)` | `2 2 3  pow * 4 sqrt * ` | `32`
64 | `2*pow(2,3)*log(1000)` | `No Variable` | `2*pow(2,3)*log(1000)` | `2 2 3  pow * 1000 log * ` | `48`
65 | `2*pow(2,3)*log2(16)` | `No Variable` | `2*pow(2,3)*log2(16)` | `2 2 3  pow * 16 log2 * ` | `64`
66 | `2*pow(2,3)*Log(16, 2)` | `No Variable` | `2*pow(2,3)*Log(16,2)` | `2 2 3  pow * 16 2  Log * ` | `64`
67 | `2*pow(2,3)*ln(e^2)` | `No Variable` | `2*pow(2,3)*ln(e^2)` | `2 2 3  pow * e 2 ^ ln * ` | `32`
68 | `-(2*7*-7)*sin(-8)` | `No Variable` | `0-(2*7*(0-7))*sin(0-8)` | `0 2 7 * 0 7 - * 0 8 - sin * - ` | `-96.95710816909141`
69 | `-(2*7*-7)*tan(-8)` | `No Variable` | `0-(2*7*(0-7))*tan(0-8)` | `0 2 7 * 0 7 - * 0 8 - tan * - ` | `666.3717226115972`
70 | `-(2*7*-7)*sinh(-8)` | `No Variable` | `0-(2*7*(0-7))*sinh(0-8)` | `0 2 7 * 0 7 - * 0 8 - sinh * - ` | `-146066.92492737592`
71 | `-(2*7*-7)*cosh(-8)` | `No Variable` | `0-(2*7*(0-7))*cosh(0-8)` | `0 2 7 * 0 7 - * 0 8 - cosh * - ` | `146066.95780271344`
72 | `-(2*7*-7)*tanh(-8)` | `No Variable` | `0-(2*7*(0-7))*tanh(0-8)` | `0 2 7 * 0 7 - * 0 8 - tanh * - ` | `-97.99997794310823`
73 | `-(2*7*-7)*atan(-8)` | `No Variable` | `0-(2*7*(0-7))*atan(0-8)` | `0 2 7 * 0 7 - * 0 8 - atan * - ` | `-141.75125056031723`
74 | `-(2*7*-7)*asin(-8)` | `No Variable` | `0-(2*7*(0-7))*asin(0-8)` | `0 2 7 * 0 7 - * 0 8 - asin * - ` | `math domain error`
75 | `-(2*7*-7)*acos(-8)` | `No Variable` | `0-(2*7*(0-7))*acos(0-8)` | `0 2 7 * 0 7 - * 0 8 - acos * - ` | `math domain error`
76 | `-(2*7*-7)*asin(-.8)` | `No Variable` | `0-(2*7*(0-7))*asin(0-.8)` | `0 2 7 * 0 7 - * 0 .8 - asin * - ` | `-90.874931364158`
77 | `-(2*7*-7)*acos(-.8)` | `No Variable` | `0-(2*7*(0-7))*acos(0-.8)` | `0 2 7 * 0 7 - * 0 .8 - acos * - ` | `244.81297139005787`
78 | `-(2*7*-7)*atanh(-8)` | `No Variable` | `0-(2*7*(0-7))*atanh(0-8)` | `0 2 7 * 0 7 - * 0 8 - atanh * - ` | `math domain error`
79 | `-(2*7*-7)*asinh(-8)` | `No Variable` | `0-(2*7*(0-7))*asinh(0-8)` | `0 2 7 * 0 7 - * 0 8 - asinh * - ` | `-272.09428351092436`
80 | `-(2*7*-7)*acosh(-8)` | `No Variable` | `0-(2*7*(0-7))*acosh(0-8)` | `0 2 7 * 0 7 - * 0 8 - acosh * - ` | `math domain error`
81 | `hypot(4,3)` | `No Variable` | `hypot(4,3)` | `4 3  hypot ` | `5`
82 | `deg(pi/3)` | `No Variable` | `deg(pi/3)` | `pi 3 / deg ` | `59.99999999999999`
83 | `rad(60)` | `No Variable` | `rad(60)` | `60 rad ` | `1.0471975511965976`
84 | `{'exp': 't y *', 'variables': {'x': 1, 't': 1, 'y': 1}, 'convert': False}` | `{'x': 1, 't': 1, 'y': 1}` | `ty*` | `'Expression ends with an operator, which is invalid. System will exit'` | `1`
85 | `{'exp': 't y *', 'variables': {'x': 1, 'y': 1}, 'convert': False}` | `{'x': 1, 'y': 1}` | `ty*` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Unknown Symbol in expression: t'`
86 | `{'exp': '3 t y *', 'variables': {'t': 1, 'y': 1}, 'convert': False}` | `{'t': 1, 'y': 1}` | `3ty*` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Invalid Postfix Notation: Stack not 1'`
87 | `{'exp': ' y     *', 'variables': {'t': 1, 'y': 1}, 'convert': False}` | `{'t': 1, 'y': 1}` | `y*` | `'Expression ends with an operator, which is invalid. System will exit'` | `'Invalid Postfix Notation: Causes Stack Underflow -  y     *'`
88 | `-2` | `No Variable` | `-2` | `-2` | `-2`
89 | `--2` | `No Variable` | `0+2` | `0 2 + ` | `2`
90 | `---2` | `No Variable` | `0-2` | `0 2 - ` | `-2`
91 | `----2` | `No Variable` | `0+2` | `0 2 + ` | `2`
92 | `-----2` | `No Variable` | `0-2` | `0 2 - ` | `-2`
93 | `++2` | `No Variable` | `2` | `2` | `2`
94 | `+++2` | `No Variable` | `2` | `2` | `2`
95 | `++++2` | `No Variable` | `2` | `2` | `2`
96 | `--++2` | `No Variable` | `0+2` | `0 2 + ` | `2`
97 | `++-2` | `No Variable` | `(0-2)` | ` 0 2 -  ` | `-2`
98 | `++++----2` | `No Variable` | `(0+2)` | ` 0 2 +  ` | `2`
99 | `++++-----2` | `No Variable` | `(0-2)` | ` 0 2 -  ` | `-2`
100 | `-(2*7*-7)*cos(---8)` | `No Variable` | `0-(2*7*(0-7))*cos(0-8)` | `0 2 7 * 0 7 - * 0 8 - cos * - ` | `-14.259003313244127`
101 | `-(2*7*-7)*cos(----8)` | `No Variable` | `0-(2*7*(0-7))*cos(0+8)` | `0 2 7 * 0 7 - * 0 8 + cos * - ` | `-14.259003313244127`
102 | `-(2*7*--7)*cos(--8)` | `No Variable` | `0-(2*7*(0+7))*cos(0+8)` | `0 2 7 * 0 7 + * 0 8 + cos * - ` | `14.259003313244127`
103 | `-(2*7*---7)*cos(---8)` | `No Variable` | `0-(2*7*(0-7))*cos(0-8)` | `0 2 7 * 0 7 - * 0 8 - cos * - ` | `-14.259003313244127`
104 | `-(2*7*----7)*cos(----8)` | `No Variable` | `0-(2*7*(0+7))*cos(0+8)` | `0 2 7 * 0 7 + * 0 8 + cos * - ` | `14.259003313244127`
105 | `-(2*7*-----7)*cos(----8)` | `No Variable` | `0-(2*7*(0-7))*cos(0+8)` | `0 2 7 * 0 7 - * 0 8 + cos * - ` | `-14.259003313244127`
106 | `sin(cos(45))` | `No Variable` | `sin(cos(45))` | `45 cos sin ` | `0.5014916033198201`
107 | `deg(asin(cos(45)))` | `No Variable` | `deg(asin(cos(45)))` | `45 cos asin deg ` | `31.68992191129556`
108 | `deg(asin(cos(rad(45))))` | `No Variable` | `deg(asin(cos(rad(45))))` | `45 rad cos asin deg ` | `45.00000000000001`
109 | `deg(acos(cos(rad(hypot(4, 3)))))` | `No Variable` | `deg(acos(cos(rad(hypot(4,3)))))` | `4 3  hypot rad cos acos deg ` | `4.999999999999992`
110 | `{'exp': 'deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t', 'variables': {'t': 16, 'x': 4, 'y': 9}, 'convert': True}` | `{'t': 16, 'x': 4, 'y': 9}` | `deg(acos(cos(rad(hypot(4,3)))))+y*x^t` | `4 3  hypot rad cos acos deg y x t ^ * + ` | `38654705669`
111 | `{'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': 4, 'y': 9}, 'convert': True}` | `{'t': 16, 'x': 4, 'y': 9}` |`atan(deg(acos(cos(rad(hypot(4,3)))))+y*x^t)` | `4 3  hypot rad cos acos deg y x t ^ * + atan ` | `1.5707963267690266`
112 | `{'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': '2*4 - 3', 'y': 9}, 'convert': True}` | `{'t': 16, 'x': '2*4 - 3', 'y': 9}` | `atan(deg(acos(cos(rad(hypot(4,3)))))+y*x^t)` | `4 3  hypot rad cos acos deg y x t ^ * + atan ` | `1.5707963267941685`
113 | `{'exp': 'hypot(x^2*4, y*t)', 'variables': {'t': 6, 'x': '2*4 - 3', 'y': '5*0.6'}, 'convert': True}` | `{'t': 6, 'x': '2*4 - 3', 'y': '5*0.6'}` | `hypot(x^2*4,y*t)` | `x 2 ^ 4 * y t *  hypot ` | `101.6070863670443`
114 | `{'exp': 'hypot(x^2*4, y*t)', 'variables': {'t': 6, 'x': '2*m - 3', 'y': '5*0.6'}, 'convert': True}` | `{'t': 6, 'x': '2*m - 3', 'y': '5*0.6'}` | `hypot(x^2*4,y*t)` | `x 2 ^ 4 * y t *  hypot ` | `'Invalid input m'`
115 | `{'exp': 'hypot(x+y*t,x*y)', 'variables': {'t': 6, 'x': '6', 'y': '5*0.6'}, 'convert': True}` | `{'t': 6, 'x': '6', 'y': '5*0.6'}` | `hypot(x+y*t,x*y)` | `x y t * + x y *  hypot ` | `30`
116 | `{'exp': 'hypot(x+y*t,x*y)', 'variables': {'t': 6, 'x': '4', 'y': '5*0.6'}, 'convert': True}` | `{'t': 6, 'x': '4', 'y': '5*0.6'}` | `hypot(x+y*t,x*y)` | `x y t * + x y *  hypot ` | `25.059928172283335`
117 | `{'exp': 'hypot(x+y*t,x*y)', 'variables': {'t': 6, 'x': '5*5', 'y': {'exp': 'a + b', 'variables': {'a': 9, 'b': 10}}}, 'convert': True}` | `{'t': 6, 'x': '5*5', 'y': {'exp': 'a + b', 'variables': {'a': 9, 'b': 10}}}` | `hypot(x+y*t,x*y)` | `x y t * + x y *  hypot ` | `494.92019558712695`
118 | `{'exp': 'x', 'variables': {'x': {'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': '2*4 - 3', 'y': 9}, 'convert': True}}}` | `{'x': {'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': '2*4 - 3', 'y': 9}, 'convert': True}}` | `x` | `x` | `1.5707963267941685`
119 | `{'exp': 'x*y + z^2', 'variables': {'x': 2, 'z': '5*0.5', 'y': {'exp': 'x + y', 'variables': {'x': {'exp': '2*y', 'variables': {'y': 1}}, 'y': {'exp': '2*x', 'variables': {'x': {'exp': '(sin(theta))^2 + (cos(theta))^2', 'variables': {'theta': {'exp': 'log(9*y) - 2*cos(z)+ln(e^2)', 'variables': {'z': 'e', 'y': {'exp': 'x', 'variables': {'x': {'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': '2*4 - 3', 'y': 9}, 'convert': True}}}}}}}}}}}}}` | `{'x': 2, 'z': '5*0.5', 'y': {'exp': 'x + y', 'variables': {'x': {'exp': '2*y', 'variables': {'y': 1}}, 'y': {'exp': '2*x', 'variables': {'x': {'exp': '(sin(theta))^2 + (cos(theta))^2', 'variables': {'theta': {'exp': 'log(9*y) - 2*cos(z)+ln(e^2)', 'variables': {'z': 'e', 'y': {'exp': 'x', 'variables': {'x': {'exp': 'atan(deg(acos(cos(rad(hypot(4, 3)))))+ y     *x^t)', 'variables': {'t': 16, 'x': '2*4 - 3', 'y': 9}, 'convert': True}}}}}}}}}}}}` | `x*y+z^2` | `x y * z 2 ^ + ` | `14.25`
120 | `{'exp': 'x', 'variables': {'x': {'exp': 'y', 'variables': {'y': {'exp': 'z', 'variables': {'z': 3}}}}}}` | `{'x': {'exp': 'y', 'variables': {'y': {'exp': 'z', 'variables': {'z': 3}}}}}` | `x` | `x ` | `3`
121 | `{'exp': 14.25}` | `No Variable` | `14.25` | `14.25` | `14.25`
122 | `{'exp': 14}` | `No Variable` | `14` | `14` | `14`
123 | `{'exp': 'x + y', 'variables': {'x': {'exp': 'y', 'variables': {'y': {'exp': 23}}}, 'y': {'exp': 25}}}` | `{'x': {'exp': 'y', 'variables': {'y': {'exp':23}}}, 'y': {'exp': 25}}` | `x+y` | `x y + ` | `48`
124 | `{'exp': 'cos(x^2 + y^2)^2 + sin(x^2 + y^2)^2', 'variables': {'x': 30, 'y': 20}}` | `{'x': 30, 'y': 20}` | `cos(x^2+y^2)^2+sin(x^2+y^2)^2` | `x 2 ^ y 2 ^ + cos 2 ^ x 2 ^ y 2 ^ + sin 2 ^ + ` | `1`
125 | `{'exp': 'cos(y)', 'variables': {'y': {'exp': 'sin(theta)', 'variables': {'theta': {'exp': 'acos(sin(x))', 'variables': {'x': 45}}}}}}` | `{'y': {'exp':'sin(theta)', 'variables': {'theta': {'exp': 'acos(sin(x))', 'variables': {'x': 45}}}}}` | `cos(y)` | `y cos ` | `0.8651625117859165`
126 | `2*4-3<5*2+4?4:3` | `No Variable` | `2*4-3<5*2+4?4:3` | `2 4 * 3 - 5 2 * 4 + < 4 ? 3 : ` | `4`
127 | `True?4:5` | `No Variable` | `True?4:5` | `True 4 ? 5 : ` | `4`
128 | `False?4:5` | `No Variable` | `False?4:5` | `False 4 ? 5 : ` | `5`
129 | `2*4?4:5` | `No Variable` | `2*4?4:5` | `2 4 * 4 ? 5 : ` | `"'?:' only works for boolean condition"`
130 | `{'exp': 'sin(theta)^2+cos(theta)^2<0', 'variables': {'theta': 30}}` | `{'theta': 30}` | `sin(theta)^2+cos(theta)^2<0` | `theta sin 2 ^ theta cos 2 ^ + 0 < ` | `False`
131 | `2*4-3<5*2+4?4*4^2:2*4-5*3` | `No Variable` | `2*4-3<5*2+4?4*4^2:2*4-5*3` | `2 4 * 3 - 5 2 * 4 + < 4 4 2 ^ * ? 2 4 * 5 3 * - : ` | `64`
132 | `2*4-3<5*2+4?4*4^2` | `No Variable` | `2*4-3<5*2+4?4*4^2` | `2 4 * 3 - 5 2 * 4 + < 4 4 2 ^ * ? ` | `64`
133 | `:4*2+5` | `No Variable` | `:4*2+5` | ` 4 2 * 5 + : ` | `'Invalid Postfix Notation: Causes Stack Underflow -  4 2 * 5 + : '`
134 | `4*3:4*2+5` | `No Variable` | `4*3:4*2+5` | `4 3 * 4 2 * 5 + : ` | `"Invalid operation ':', no matching '?' found"`
135 | `{'exp': 'x^2 + y^2 < 1 ? cos(theta) >1?4:5:6', 'variables': {'x': {'exp': 'sin(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'y': {'exp': 'cos(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'theta': 60}}` | `{'x': {'exp': 'sin(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'y': {'exp': 'cos(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'theta': 60}` | `x^2+y^2<1?cos(theta)>1?4:5:6` | `x 2 ^ y 2 ^ + 1 < theta cos 1 > ? 4 ? 5 : 6 : ` | `5`
136 | `{'exp': 'x^2 + y^2 < 1 ? cos(theta) >1+4-5:6', 'variables': {'x': {'exp': 'sin(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'y': {'exp': 'cos(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'theta': 60}}` | `{'x': {'exp': 'sin(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'y': {'exp': 'cos(phi)', 'variables': {'phi': 'acos(0.5)'}}, 'theta': 60}` | `x^2+y^2<1?cos(theta)>1+4-5:6` | `x 2 ^ y 2 ^ + 1 < theta cos 1 4 + 5 - > ? 6 : ` | `6`
137 | `1+True` | `No Variable` | `1+True` | `1 True + ` | `2`
138 | `1-True` | `No Variable` | `1-True` | `1 True - ` | `0`
139 | `1*True` | `No Variable` | `1*True` | `1 True * ` | `1`
140 | `1/True` | `No Variable` | `1/True` | `1 True / ` | `1`
141 | `1%True` | `No Variable` | `1%True` | `1 True % ` | `0`
142 | `5^True` | `No Variable` | `5^True` | `5 True ^ ` | `5`
143 | `1+False` | `No Variable` | `1+False` | `1 False + ` | `1`
144 | `1-False` | `No Variable` | `1-False` | `1 False - ` | `1`
145 | `1*False` | `No Variable` | `1*False` | `1 False * ` | `0`
146 | `1/False` | `No Variable` | `1/False` | `1 False / ` | `float division by zero`
147 | `1 % False` | `No Variable` | `1%False` | `1 False % ` | `float modulo`
148 | `5^False` | `No Variable` | `5^False` | `5 False ^ ` | `1`
149 | `True + False` | `No Variable` | `True+False` | `True False + ` | `1`
150 | `True - False` | `No Variable` | `True-False` | `True False - ` | `1`
151 | `True * False` | `No Variable` | `True*False` | `True False * ` | `0`
152 | `True / False` | `No Variable` | `True/False` | `True False / ` | `division by zero`
153 | `True % False` | `No Variable` | `True%False` | `True False % ` | `integer division or modulo by zero`
154 | `+True` | `No Variable` | `True` | `True ` | `True`
155 | `-True` | `No Variable` | `0-True` | `0 True - ` | `-1`
156 | `True` | `No Variable` | `True` | `True ` | `True`
157 | `False` | `No Variable` | `False` | `False ` | `False`
158 | `True` | `No Variable` | `True` | `True` | `True`
159 | `False` | `No Variable` | `False` | `False` | `False`
160 | `True \| True` | `No Variable` | `True\|True` | `True True \| ` | `True`
161 | `True & True` | `No Variable` | `True&True` | `True True & ` | `True`
162 | `True = True` | `No Variable` | `True=True` | `True True = ` | `True`
163 | `True != True` | `No Variable` | `True!True` | `True True ! ` | `False`
164 | `False \| False` | `No Variable` | `False\|False` | `False False \| ` | `False`
165 | `False & False` | `No Variable` | `False&False` | `False False & ` | `False`
166 | `False = False` | `No Variable` | `False=False` | `False False = ` | `True`
167 | `False != False` | `No Variable` | `False!False` | `False False ! ` | `False`
168 | `False \| True` | `No Variable` | `False\|True` | `False True \| ` | `True`
169 | `False & True` | `No Variable` | `False&True` | `False True & ` | `False`
170 | `False = True` | `No Variable` | `False=True` | `False True = ` | `False`
171 | `False != True` | `No Variable` | `False!True` | `False True ! ` | `True`
172 | `2=2` | `No Variable` | `2=2` | `2 2 = ` | `True`
173 | `2=4` | `No Variable` | `2=4` | `2 4 = ` | `False`
174 | `2!=6` | `No Variable` | `2!6` | `2 6 ! ` | `True`
175 | `6!=6` | `No Variable` | `6!6` | `6 6 ! ` | `False`
176 | `6\|6` | `No Variable` | `6\|6` | `6 6 \| ` | `"'\|' only works for boolean conditions"`
177 | `6&6` | `No Variable` | `6&6` | `6 6 & ` | `"'&' only works for boolean conditions"`
178 | `True\|6` | `No Variable` | `True\|6` | `True 6 \| ` | `"'\|' only works for boolean conditions"`
179 | `True&6` | `No Variable` | `True&6` | `True 6 & ` | `"'&' only works for boolean conditions"`
180 | `6\|True` | `No Variable` | `6\|True` | `6 True \| ` | `"'\|' only works for boolean conditions"`
181 | `6&True` | `No Variable` | `6&True` | `6 True & ` | `"'&' only works for boolean conditions"`
182 | `{'exp': 'x^2 = 4', 'variables': {'x': {'exp': '3/y*2', 'variables': {'y': 3}}}}` | `{'x': {'exp': '3/y*2', 'variables': {'y': 3}}}` | `x^2=4` | `x 2 ^ 4 = ` | `True`
183 | `{'exp': 'x^2 != 4', 'variables': {'x': {'exp': '3/y*2', 'variables': {'y': 3}}}}` | `{'x': {'exp': '3/y*2', 'variables': {'y': 3}}}` | `x^2!4` | `x 2 ^4 ! ` | `False`
184 | `{'exp': 'x^2 != 4 \| y^2 == 9', 'variables': {'x': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}}` | `{'x': {'exp': '3/y*2', 'variables': {'y': 3}},'y': 3}` | `x^2!4\|y^2=9` | `x 2 ^ 4 ! y 2 ^ 9 = \| ` | `True`
185 | `{'exp': 'x^2 != 4 \| y^2 = 9 ?4:6', 'variables': {'x': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}}` | `{'x': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}` | `x^2!4\|y^2=9?4:6` | `x 2 ^ 4 ! y 2 ^ 9 = \| 4 ? 6 : ` | `4`
186 | `{'exp': 'x^2 != 4 & y^2 = 9 ?4:x^2=4? y^2 !=9 ? y:y=3 & y^2=9 \| x^2 = 4? 6 : y:y', 'variables': {'x': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}}` | `{'x': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}` | `x^2!4&y^2=9?4:x^2=4?y^2!9?y:y=3&y^2=9\|x^2=4?6:y:y` | `x 2 ^ 4 ! y 2 ^ 9 = & 4 ? x 2 ^ 4 = : y2 ^ 9 ! ? y ? y 3 = : y 2 ^ 9 = & x 2 ^ 4 = \| 6 ? y : y : ` | `6`
187 | `True!=True` | `No Variable` | `True!True` | `True True ! ` | `False`
188 | `True!=False` | `No Variable` | `True!False` | `True False ! ` | `True`
189 | `False!=True` | `No Variable` | `False!True` | `False True ! ` | `True`
190 | `False!=False` | `No Variable` | `False!False` | `False False ! ` | `False`
191 | `True==True` | `No Variable` | `True=True` | `True True = ` | `True`
192 | `True==False` | `No Variable` | `True=False` | `True False = ` | `False`
193 | `False==True` | `No Variable` | `False=True` | `False True = ` | `False`
194 | `False==False` | `No Variable` | `False=False` | `False False = ` | `True`
195 | `1>=2` | `No Variable` | `1@2` | `1 2 @ ` | `False`
196 | `2>=2` | `No Variable` | `2@2` | `2 2 @ ` | `True`
197 | `3>=2` | `No Variable` | `3@2` | `3 2 @ ` | `True`
198 | `3<=2` | `No Variable` | `3#2` | `3 2 # ` | `False`
199 | `2<=2` | `No Variable` | `2#2` | `2 2 # ` | `True`
200 | `1<=2` | `No Variable` | `1#2` | `1 2 # ` | `True`
201 | `Pi > pi` | `No Variable` | `Pi>pi` | `'Invalid input Pi'` | `'Invalid input Pi'`
202 | `pi>pi` | `No Variable` | `pi>pi` | `pi pi > ` | `False`
203 | `{'exp': 'x^2 != 4 & y^2 = 9 ?4:x^2=4? y^2 !=9 ? y:y=3 & y^2=9 \| x^2 = 4? 6 : y:y', 'variables': {'X': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}}` | `{'X': {'exp': '3/y*2', 'variables': {'y': 3}}, 'y': 3}` | `x^2!4&y^2=9?4:x^2=4?y^2!9?y:y=3&y^2=9\|x^2=4?6:y:y` | `'Invalid input x'` | `'Invalid input x'`
204 | `1*False` | `No Variable` | `1*False` | `1 False * ` | `0`
205 | `ceil(-2.8)` | `No Variable` | `ceil(0-2.8)` | `0 2.8 - ceil ` | `-2`
206 | `ceil(2.8)` | `No Variable` | `ceil(2.8)` | `2.8 ceil ` | `3`
207 | `ceil(2.2)` | `No Variable` | `ceil(2.2)` | `2.2 ceil ` | `3`
208 | `{'exp': '$^2', 'variables': {'$': 2}}` | `{'$': 2}` | `$^2` | `$ 2 ^ ` | `4`
209 | `round(2.2, 0)` | `No Variable` | `round(2.2,0)` | `2.2 0  round ` | `2`
210 | `round(2.8, 0)` | `No Variable` | `round(2.8,0)` | `2.8 0  round ` | `3`
211 | `round(-2.88654, 2)` | `No Variable` | `round(0-2.88654,2)` | `0 2.88654 - 2  round ` | `-2.89`
212 | `round(-2.88654, 2.6)` | `No Variable` | `round(0-2.88654,2.6)` | `0 2.88654 - 2.6  round ` | `"Rounding takes only 'int' as second argument"`
213 | `floor(2.8)` | `No Variable` | `floor(2.8)` | `2.8 floor ` | `2`
214 | `floor(-2.88654)` | `No Variable` | `floor(0-2.88654)` | `0 2.88654 - floor ` | `-3`
215 | `factorial(-1)` | `No Variable` | `factorial(0-1)` | `0 1 - factorial ` | `'Value Error: -1.0. Factorial calculation can only be done for integers greater than 0.'`
216 | `ln(pow(e,2))` | `No Variable` | `ln(pow(e,2))` | `e 2  pow ln ` | `2`
217 | `ln(exp(2))` | `No Variable` | `ln(exp(2))` | `2 exp ln ` | `2`
218 | `sqrt(-9)` | `No Variable` | `sqrt(0-9)` | `0 9 - sqrt ` | `'Square root only works for positive numbers'`
219 | `now` | `No Variable` | `now` | `now ` | `2019-06-11 23:15:17.821153`
220 | `today` | `No Variable` | `today` | `today ` | `2019-06-11`
# Operator Precedence

Operator precedence is a very important concept in programming. It is an extension of the mathematical idea of order of operations (multiplication being performed before addition, etc.), to include other operators, such as those in Boolean logic.

Consider the following expression: `2 + 3 * 4`
We know that multiplication takes precedence over addition, so the above expression is equivalent to:

`2 + (3 * 4) = 14`

In Python, the operator precedence is as follows:

| Precedence | Operator                    | Description                                                                    |
| ---------- | --------------------------- | ------------------------------------------------------------------------------ |
| 1          | \*\*                        | Exponentiation (raise to the power)                                            |
| 2          | ~ + -                       | Complement, unary plus and minus (method names for the last two are +@ and -@) |
| 3          | \* / % //                   | Multiply, divide, modulo and floor division                                    |
| 4          | + -                         | Addition and subtraction                                                       |
| 5          | >> <<                       | Right and left bitwise shift                                                   |
| 6          | &                           | Bitwise 'AND'                                                                  |
| 7          | ^ \|                        | Bitwise exclusive `OR` and regular `OR`                                        |
| 8          | <= < > >=                   | Comparison operators                                                           |
| 9          | <> == !=                    | Equality operators                                                             |
| 10         | = %= /= //= -= += \*= \*\*= | Assignment operators                                                           |
| 11         | is is not                   | Identity operators                                                             |
| 12         | in not in                   | Membership operators                                                           |
| 13         | not or and                  | Logical operators                                                              |

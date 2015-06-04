Date: 06-04-2015
Title: Const Liffy Pattern For C++
Slug: Const-Liffy-Pattern
Author: Barry Steyn
Tags: C++, Software Engineering

# Introduction
Immutable state has [many advantages](http://www.drdobbs.com/cpp/practical-advantages-of-immutable-values/240163690). Unfortunately, C++ is designed to easily mutate state. My colleague Vincent Lascaux shared a code snippet that tries to alleviate this problem by attempting to avoid normal variables in favor of using constants that are always initialized. I decided to name his pattern *const liffy*...

## Background Knowledge

[C++ standard 11](http://en.wikipedia.org/wiki/C%2B%2B11) introduced some amazing features to C++. Two such features are:

 1. The [auto](http://en.cppreference.com/w/cpp/language/auto) variable initializer.
 2. [Lambda functions](http://en.cppreference.com/w/cpp/language/lambda).

### Auto Variable initializer
The keyword *auto* can be used to declare a variable. During compilation, the compiler will replace the *auto* keyword using the rules for [template argument deduction](http://en.cppreference.com/w/cpp/language/template_argument_deduction) thereby ensuring type safety.

Standard modifiers for variables (like & and *const*) are valid to put before *auto*. For example, the following is perfectly legal:

    :::c++
    auto a = 1;
    const auto b = 1;
    const auto& c = result_of_some_function();

### Lambda Functions
A Lambda function is an unnamed function object capable of *capturing* variables in scope. The syntax is as follows

 > `[capture-list] (parameters) { body }` [ref]This is not the only syntax for lambdas in C++, there are other [syntaxes](http://en.cppreference.com/w/cpp/language/lambda#Syntax)[/ref]

The capture list is very important. It specifies the way that variables declared outside the lambda are available within the lambda. if a lambda function uses a capture list specified by `[&]`, then all variables declared in the block where the lambda is invoked is available to the lambda *as a reference*. The *parameters* are optional (in fact, no parameters are used in the *const liffy* pattern).

For example, the following code uses a lambda function to *filter* out all strings that do not contain the substring *"world"*:

    :::c++
    string word = "world";
    vector<string> strings = { string("hello"), string("world"), string("hello world")};
    vector<string> results;
    for_each(strings.begin(), strings.end(), [&] (string test) {
       if (test.find(word) != string::npos)
        results.push_back(test);
    });

# The Const Liffy Pattern
Using lambda functions, we can initialize const variables by immediately invoking the lambda:

    :::c++
    const auto var = [&] { code here...; return something; } ()

Note the invokation operator `()` operator in the above snippet. JavaScript calls this pattern an [immediately invoked function expression](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression) commonly just called `iffy`. I therefore named the pattern above *const liffy*, with *liffy* being short for *lambda iffy*.

The *const liffy* pattern elegantly lets one use immutable state. Some examples should set things straight.

## Reading A Variable Protected By A Mutex
Multithreaded programming requires the use of a [mutex](http://en.wikipedia.org/wiki/Mutual_exclusion) to guard against [race conditions](http://en.wikipedia.org/wiki/Race_condition).

Here is a generic example of reading a variable that is protected by a mutex:

    :::c++
    Object* instance;
    std::mutex obj_mutex;
    {
        std::lock_guard<std::mutex> lock(obj_mutex);
        instance = &protected_variable;
    }

The code sample above suffers from the following:

  * The variable `instance` starts off as being uninitialized (or in the above case, initialzed to what can be considered a bogus value: *nullptr*).
  * Type information is lost: If `instance` could be a reference instead of a pointer, *nullptr* errors would never happen.

Using the *const liffy* pattern ameliorates the situation:

    :::c++
    const auto& instance = [&] {
      std::lock_guard<std::mutex> lock(obj_mutex);
      return protected_variable;
    }()

In the above code sample, `instance` is a constant reference that is initialized to the required value. All the issues mentioned in the first example have been solved.

## Creating Short Helper Functions
Assume we have a *Shape* class that is sub-classed with different types of shapes (e.g. circle, square). Given **shapes**, a collection of *Shape* objects, a render function will only draw red square or blue circles. That render function could look like this:

    :::c++
    for (auto&& shape :Shapes)
      bool shouldDraw = false;
      switch (shape.type) {
        case ShapeType::Square: shouldDraw = shape.color() == Color::red; break;
        case ShapeType::Circle: shouldDraw = shape.color() == Color::blue; break;
      }
      if (shouldDraw) Draw(shape);
    }

In the above code snippet, the variable *shoulddraw* is initialized to `false` (which becomes the default of the switch statement). The `false` value is then overwritten with the correct logic in the switch statement. But why intialize *shoulddraw* to false?

  * At the time of intialization, it is not known what the state of *shoulddraw* should be. Setting it to `false` does not really make sense.
  * A programmer is then forces to read the proceeding four lines of the switch statement to make sense of what *shoulddraw* is. So in effect, one has to read these lines just to make sense of *shoulddraw*.

Seeing as a *lambda* function is really an anonymous helper function, the *const liffy* pattern can help here as well:

    :::c++
    for (auto&& shape :Shapes)
      const bool shouldDraw = [&] {
        switch (shape.type) {
          case ShapeType::Square: return shape.color() == Color::red;
          case ShapeType::Circle: return shape.color() == Color::blue;
          default: return false;
        }
      }();

      if (shouldDraw) Draw(shape);
    }

With the const liffy pattern, *shoulddraw* becomes a constant. The code is not only cleaner by using `false` in the default of the switch statement, but it is also easier to reason about and understand.

# Conclusion
The *const liffy* pattern is actually just the result of an anonymous block. It is done all the time in languages like [scala](http://en.wikipedia.org/wiki/Scala_%28programming_language%29) and is inspired by the discipline of functional languages. Using it allows for immutable state with all its [advantages](http://www.drdobbs.com/cpp/practical-advantages-of-immutable-values/240163690).

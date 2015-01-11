Date: 2012-10-12
Title: Javascript: Object Prototypes
Tags: development, JavaScript
Slug: Javascript-Objects-Prototypes
Category: Blog

This post discusses JavaScript objects with emphasis on its prototype linkings. After reading this post, you should understand the following:

* Object creation in JavaScript.
* Prototype linkings.
* What `Object.prototype` and `Function.prototype` are used for.

[Douglas Crockford's](http://en.wikipedia.org/wiki/Douglas_Crockford) wonderful book [JavaScript: The Good Parts](http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742/ref=sr_1_1?ie=UTF8&qid=1346978272&sr=8-1&keywords=javascript+the+good+parts) does a fanastic job of explaining this topic, and I urge the interested reader to buy his book.

#JavaScript Objects

In JavaScript the simple types are *numbers*, *strings*, *booleans* (*true* and *false*), *null* and *undefined*. All other values are objects. Even though there are multiple ways to create objects, there are really only two *atomic* mechanisms that are used:

1. Literals. 
2. Functions.

##Creating Objects From Literals <a id="cofl"></a>
Creating objects from literals is very simple. The following is an *object literal*:

    var person = {  
		"First_Name": "Barry",  
		"Last_Name": "Steyn",
        "do_Something": function() { alert('something'); }
    }  

Object Literals do not look like traditional objects. In fact, Object Literals look more like a structure that can hold things.  There is however one difference between a JavaScript object and a structure that can hold things: All JavaScript objects have a *prototype* linking.

##The Prototype Link
Every Object has a *hidden* link to another object called a *prototype link*. Objects by default are linked to the object `Object.prototype`. The prototype link is only used when retrieving property values from an object (it is not touched when updating an object). When retrieving a property value from an object, if it cannot be found, it will look for it in the prototype object that it is linked to. For example:

    person.age; // undefined - property age does not exist

JavaScript tried to find the property age on person, and it could not. So then it tried to find it on `Object.prototype` and it could not find it either. So it returned "*undefined*".

    Object.prototype.age = 56; // Every object is linked to Object.prototype by default
    person.age; // 56

JavaScript could not find age on person, but it did find it on `Object.prototype`, which is linked to person. Therefore the prototype linkage is used to *augment* an object with additional properties. In a classical object oriented language like Java or C++, augmentation is performed using inheritance. And so a prototype link can be considered as providing the property augmentation feature of object inheritance.

##Creating Function Objects <a id="cfo"></a>
Functions in JavaScript are objects and are [first class citizens](http://en.wikipedia.org/wiki/First-class_citizen). A variable can be assigned a function object like so:

    var addNum = function(num1, num2) {
            return num1 + num2;
    }

    typeof addNum; //function - which is an object in JavaScript

Since functions are objects, they too have a prototype link. But where object literals are by default linked to `Object.prototype`, function objects are linked to `Function.prototype`. There is one other difference that function objects have (and this is where it starts get confusing); function objects have in addition to a prototype link a *property* called *prototype*. This property (again, the *prototype* property **is not** the prototype link) can be manipulated (its use will be explained in the next section).

Just like `Object.prototype` is used to augment objects with properties, so `Function.prototype` is used to augment functions with properties.
    
    var result = addNum(3,4); // 7

    //Add a function to Function.prototype
    Function.prototype.substract = function(num1, num2) {
            return num1 - num2;
    }

    //We can now use subtract on any function object
    result = addNum.subtract(5,2); //3

`Function.prototype` is itself an object (big surprise there), and therefore it is linked to `Object.prototype`. If something cannot be found in `Function.prototype`, it will be searched for on `Function.prototype`'s linked prototype object, which is `Object.prototype`.

    Object.prototype.denominator = 10;
    Object.prototype.divide = function(num1) {
            return num1 / denominator;
    }

    var result = addNum.divide(50); // 5

In the above example, *addNum* was searched for *divide*. Then `Function.prototype` was searched, after which, `Object.prototype` was searched, where it was eventually found. Therefore prototype links are chained together, whereby if a property is not found in the current object, it then searches for it in its linked prototype object. And if that object does not have the property, it is then searched for in that object's linked prototype object, and so on, until the process ends with `Object.prototype`.

The process described above is the mainstay of [Prototype Based Programming](http://en.wikipedia.org/wiki/Prototype-based_programming), and it is called *prototype chaining*.

##Creating Objects From Functions <a id="coff"></a>
This section should not be confused with the previous section. Their titles share similar wording, but in this section, we are going to talk about how to create a new object using a function, and last section we talked about creating function objects.

To recap from the last section, this is how a *function object* is created:

    var Animal = function(name) {
            this.name = name;
    }

The variable `Animal`:

* Is a function and an object (remember, everything is an object in JavaScript).  
* It has a *prototype property*, and its prototype link is to set to `Function.prototype` by default.

But something special happens here if the function is invoked with the reserved word `new` (called the [constructor invocation pattern](http://doctrina.org/Javascript-Function-Invocation-Patterns.html#ci)):

    var cat = new Animal('fluffy'); //Using new to invoke the function

What happens here is that `new` creates an object from the function object `Animal`. Its power comes in because it will use `Animal`'s *prototype property* as the *prototype link* for the new object. And since `Animal` can set the value of its prototype property, objects constructed in this way do not have to be linked to `Object.prototype`. Got that? If not, here is an example which should explain things:

    var species = {
            "species":"human"
    }

    var Entity = function(name) {
        this.name = name;
    }

    var alien = new Entity("Yoda");

    Entity.prototype = species;
    var human = new Entity("Jason");

In the above, the `alien` and `human` objects are constructed from the function `Entity` via the *constructor invocation pattern* that is initiated by putting the `new` keyword in front of the function name. When `alien` is constructed, `Entity`'s prototype property has not been altered, and so `alien` is linked to `Object.prototype`. But when constructing `human`, `Entity`'s prototype property was altered to species, and so the prototype object linked to `human` is `species`, which in turn is itself linked to `Object.prototype`:

    alien.species; // undefined
    human.species; // human

###The problem with using the "constructor invocation pattern" <a id="pcip"></a>
Using `new` is one of four ways in which to invoke a function, the most popular way being to call the function. For example:

    var Vehicle = function(type) {
            this.type = type;
            return type;
    }

    var car = Vehicle("Toyota"); // Normal function call
    var plane = new Vehicle("Boeing");

In the example above, `car` was assigned the result of invoking `Vehicle` as a normal function, which in this case was *Toyota*. But `plane` on the other was assigned the result of using the *constructor invocation pattern* which is an object (the return is ignored). This is terrible, and it is very easy to make a mistake.

One recommended approach is to always start functions that are to be invoked with `new` with *capital letters*. This should help for readability, but when someone is spending days trying to hunt for a bug, this will be little compensation. <a id="remedy"></a>Instead, a much better way would be to augment `Object` with a create method if it does not exist:

    if (typeof Object.create !== 'function') { //If working with a version of JavaScript prior to 1.8.5
        Object.create = function(o) {
            var F = function() {};
            F.prototype = o;
            return new F();
        }
    }

Objects can now be created with a chosen prototype link by doing the following:

    var animal = {
        "type":"cat",
        "make_sound":function() {
            return "purrrr";
        }
    }

    var cat = Object.create(animal);
    cat.make_sound(); //purrrr
    cat.type; //cat

#Conclusion
Object orientation in JavaScript is a bit of a mess. This is because JavaScript is quite unsure about what it is, and ends up being a mix of a classical object oriented language and a prototype based language. Hence we get the `new` keyword, which makes JavaScript look like a classical object oriented language, even though it is not.

To summarise, here are the three objects this blog discusses:

    //Object Literal
    var objectLiteral = {
            "property1":"value1"
    };

    //Function Object
    var functionObject = function() {
    }

    //Object From Function
    var objectFromFunction = new functionObject();

And to summarise, the prototype linkings and properties available to each object:
<center>
    <table style="border-style: solid; border-width:1px; border-color: #000000;">
        <tr>
            <td><b>Object Literal</b></td>
            <td><b>Function Object</b></td>
            <td><b>Object From Function</b></td>
        </tr>
        <tr>
            <td>
                <ul>
                    <li> *Construction* - via curly braces `{}`</li>
                    <li> *Prototype Link* - Object.prototype</li>
                    <li> *Prototype Property* - does not exist</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li> *Construction* - via the `function` keyword </li>
                    <li> *Prototype Link* - Function.prototype</li>
                    <li> *Prototype Property* - exists</li>
                </ul>
            </td>
            <td>
                <ul>
                    <li> *Construction* - via `new` keyword with function object</li>
                    <li> *Prototype Link* - Whatever the function's (that was invoked by `new`) prototype property is set to (`Object.prototype` by default)</li>
                    <li> *Prototype Property* - does not exist</li>
                </ul>
            </td>
        </tr>
    </table>
</center>

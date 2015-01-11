Date: 2013-04-22
Title: Object Orientation: C++ And Java
Slug: Object-Orientation:C++_And_Java
Author: Barry Steyn
Category: Notes
Tags: Software, Computer Science, Algorithms
Latex:
Status: draft

#Core Concepts
 
 * Encapsulation - hiding infor

#Classes And Objects

 * Class is an abstract definition of something that has *attributes* and *actions*. 
 * An object is a specific instance of a class.

In C++:

    class Point {
        private:
            float x, y;
        public:
            Point(float X, float Y) : x(X), y(Y) {}
            const float getX() const;
            const float getY() const;
            void setX(const float &x);
            void setY(const float &x);
    };

    const float Point::getX() const {return x;}
    const float Point::getY() const {return y;}
    void Point::setX(const float &x) {this->x = x;}
    void Point::setY(const float &y) {this->y = y;}

In Java:

    public class Point {
        private float x=0, y=0;
        public Point(float X, float Y) {
            x = X;
            y = Y;
        }
        
        public float getX() { return x;}
        public float getY() { return y;}
        public void setX(float x) { this.x = X;}
        public void setY(float y) { this.y = Y;}
    }

**Some Key Differences**

 * In Java, the class and business logic is *'mixed'* together. In C++, they are separated.
 * In Java, an access modifier (normally public) is specified before a class.

# Inheritance
Assume Class B inherits from Class A. Class B has all *public* and *protected* attributes from Class A. Class B defines an *'is a'* relationship, whereby Class B *is a* Class A. This means that Class B can be used anywhere Class A is used. 

The following access modifiers apply to inheritance:

 * private - a base class will not inherit anything private from it's parent class.
 * protected - a base class will inherit and have access to all protected methods/attributes from it's parent. 
 * public - a base class will inherit and have access to all public methods/attributes from it's parent.

The difference between public and protected: Protected acts like *private* to everything except inherited classes.

A base class can also be abstract, meaning that it cannot be instantiated.

In C++
    
    class Shape {
        protected:
            Point center;
            Shape (Point & Center) : center(Center) {}
        public:
            const Point& getCenter();
            virtual void draw() = 0;
    };

    const Point& Shape::getCenter() {return center;}

    class Rectangle : Shape {
        private:
            int h, w;
        public:
            Shape(int H, int W, Point& Center) : h(H), w(W), center(Center) {}
            void draw();
    }

    public void Rectangle::draw() {...}

**Note:**

 * The pure virtual function makes this class abstract. Pure virtual signified by putting `=0` after the definition.
 * Inheritance accomplished by `:` operator.
 * Parent constructors can only be called in the intialization list.
 * Can have multiple inheritance.

In Java

    public abstract class Shape {
        protected Point center;
        protected Shape(Point center) {this.center = center;}

        public Point getCenter() {return center;}
        public void draw();
    }

    public class Rectangle extends Shape {
        private int h=0, w=0;
        
        public Shape(int h, int w, Point center) {
            this.h = h; this.w = w; this.center = center;
        }

        public void draw() {
            ...
        }
    }

**Note:**
    
    * Inheritance accomplished by `extends` key word.
    * Can only have a single inheritance.
    * Java uses the `super` keyword to call parent constructors explicitly. It must be the first statement in a child constructor.

#Multiple Inheritance
C++ allows it, Java (and C#) disallow it! This is because of the classic case known as the [diamond problem](http://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem):

    class A {
    }

    class B : A {
    }

    class C : A {
    }

    class D : B,C {
    }

In the above, class D has two copies of A. This leads to ambiguity (for instance, what destructor to call or what method to call). This is such a profound problem that Java (and C#) disallow multiple inheritance.

In C++, one can alleviate the problem by using [virtual base classes](http://www.learncpp.com/cpp-tutorial/118-virtual-base-classes/).

#Inheritance VS Interface
An interface is a contract whereby the class that implements the interface will implement the methods defined in the interface. Interfaces can be thought of a abstract class without any state (i.e. variables). In fact, this is how they are implemented in C++. An interface is vital for languages that do not allow multiple inheritance (e.g. Java or C#) as a class can implement multiple interfaces.

The difference between an interface and an inherited class: Use inheritance when the class is tightly coupled to the base class and forms an *is-a* relationship (e.g. square is-a shape), but use interfaces when the connection is loosely defined (e.g. square implements the svg-draw interface).

#Polymorphism

Polymorphism is the ability to provide *multiple implementations* for a particular method and *select the correct implementation* based on its surrounding context. This implies that polymorphic functions can be bound at run time (known as *late binding*). Polymorphism is accomplished using two mechanisms:

 * *Overloading* - multiple versions of the same function, but with different input parameters. 
 * *Overriding* - a multiple definitions of the same function in a parent class and in its child class.

Late binding applies to function *overriding*. A child class can be up-casted to its parent, yet when a parent invokes a method, the child's definition will be run. This is called a *virtual* function. In Java, all functions are virtual by default, and one must use the keyword `final` to make them non-virtual. In C++, all functions are by default non-virtual, and functions must be marked by the keyword `virtual` to make them virtual.

    

# Polymorphism

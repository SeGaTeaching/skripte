# Module 1 - Classless Objects

## Section 1 - What is an object?
1.1.1 Primitive data types
In the previous part of the course, you got to know some primitive data types.

In practice, only number, boolean and string types are actually used. Whether a type is a certain value can be checked with the typeof command.

With this command, we can also test not just a particular value, but a variable (or more precisely, what is placed inside it).

Try to execute the following commands in the console and observe the results. Furthermore, it would be good to try to test every piece of sample code that we discuss.


console.log(typeof 2.5); // -> number
console.log(typeof "one two three"); // -> string
console.log(typeof false); // -> boolean

Values can be placed in variables - we can store them there or perform actions on them (e.g., divide numbers or merge strings).


let nr = 2.5; 
nr = nr / 2;
console.log(typeof nr); // -> number

If we have not explicitly assigned any value to a declared variable, it contains an undefined value by default. The undefined value is also treated as one of the primitive types of data, equal to the string or number type.


let nr = 2.5; 
nr = nr / 2;
console.log(typeof nr); // -> number

Note that typeof returns the name of the data type as a string.

What do we actually mean by these types being primitive? Their "primitiveness" is that they are not complex. There is always one specific, simple value in a variable. A variable contains either a number, or a logical value, or a character string. Alternatively, there may be nothing there, which means that the undefined value is actually there. Primitive, isn't it?

Using only these types of data would greatly reduce the possibility of creating more advanced programs. Therefore, in addition to the primitive types, complex types are used. To simplify things a little, we can assume that we will be dealing with two such types – arrays and objects.

How is this a simplification? Well, arrays in JavaScript are also objects. In JavaScript, even functions are objects. In fact, everything in JavaScript, except a primitive, is an object. But for now, let’s pretend that we don't know this, and treat as objects only openly declared ... objects.


1.1.2 Array as a complex type
Complex types, such as arrays or objects, are data collections – an ordered set of different values can be placed in one variable. In the case of an array, individual values placed in a single variable are called elements, and are referred to by a number specifying their position in the collection (i.e. an index).

In JavaScript, indexes start at 0, so the first element will have an index of 0, the second an index of 1, and so on. As a reminder, arrays are most easily created using square brackets (although this is not the only way to create them).


let a = [10, 20, "en to tre", true, 50];
a[4] = a[4] * 2;
console.log(a[0]);    // -> 10
console.log(a[2]);    // -> en to tre
console.log(a[4]);    // -> 100

In the example, we created a five-element array, modified its last element, and referred to a few elements (displaying their values).

We’ll return to arrays and their more advanced applications in the following chapters.


1.1.3 An object as a different type of array
From a formal point of view, an object can be treated as a special kind of array.

In computer science, arrays of this type are called association arrays (or, in the theory of data structures, they are called maps).

How do they differ from ordinary arrays? We don’t refer to the individual elements of an object by means of indexes, which define their position in the collection, but by means of keys (i.e. we "associate" an element with a key).

A key is simply a label (a name), which is unique within an object and unambiguously defines the selected element.

In objects, we call their component elements properties. Each property will consist of a key (or label) and a value.

The idea of objects comes from observing the surrounding reality. Practically everything in our environment, whether material (e.g. a car) or abstract (e.g. a contact in an address book) is a collection of certain components.

We can name these elements, or properties, and assign them specific values. Properties define a given object.

As we’ll see later in the course, JavaScript allows you to create objects in many different ways. The easiest way is to use curly brackets.


let sampleObject = {
    id: 10, 
    delay: 20,
    name: "en to tre",
    isPresent: true,
    delay: 50
};
sampleObject.delay = sampleObject.delay * 2;
console.log(sampleObject.id);    // -> 10
console.log(sampleObject.name);    // -> en to tre
console.log(sampleObject.delay);    // -> 100

In the example, we have created a sampleObject containing five properties, modified the contents of the delay property and referred to the id, name, and delay properties (displaying their values).

In the further part of the course, we’ll alternatively use the equivalent terms key and property name, as well as property and object field.

---

## Section 2 - Literals

1.2.1 Basic way to create objects
As you’ve probably heard more than once, JavaScript is an extremely flexible language.

The syntax of the language allows us, in many cases, to achieve the same goal in different ways. It is no different with objects. There are several equivalent ways to create them, each with their own advantages and disadvantages. The simplest and most common is the use of literal notation – that is, the declaration presented earlier using curly brackets (another name for this is initializer notation).

In the example below, we create an empty object (without properties) and place it in the contact variable.


let contact = {};

We can modify an object created in this way by, among other things, adding new properties.

In our example, we add a property with the tel key. Note that the property is indicated by writing its name after the object name, where the names are separated by a dot. This is called dot notation.


contact.tel = "207-662-5412";
console.log(contact);
console.log(contact.tel);

Nothing stands in the way of declaring and initiating properties immediately when creating an object. This time the object will have two properties: phone and email. In the literal notation, the following properties are separated from each other by commas. A colon is used to separate a property name (a key) from a value.


let contact = {
    tel: "207-662-5412",
    email: "RonaldSMurphy@freepost.org"
};
console.log(contact);
console.log(contact.tel);

The key is a string. When creating an object, the key can be enclosed in quotation marks, although this is not necessary (JavaScript automatically interprets it as a string). However, this can be useful when you want to create a key consisting of several words. For example, the following construction will be wrong:

let contact = {
    first name: "Ronald"
};

and we need to change it to:


let contact = {
    "first name": "Ronald"
};

However, giving keys names consisting of many separate words is not the best idea.

If you need a multi-word name, it’s better to use, for example, the Camel case notation, and write firstName instead of "first name". The notation will be both more readable to the user and less burdensome on the computer. With multi-word keys, it will also be a problem to refer to the property of an existing object – dot notation does not allow it.

We’ll soon talk about solving this problem with the bracket notation.

By the way, have you noticed that the console.log used in this chapter is also an example of "dot notation"? It would appear that the console is an object and the log is its property. And so it is.


console.log(typeof console);    // -> object
console.log(typeof console.log);    // -> function

The result of the first command should not be surprising – we’ve already agreed that consoles are objects.

However, the log property type may come as a little bit of a surprise. On the one hand, it's obvious; after all, we use this construction as a function. This means, however, that the object property does not have to be of the number, Boolean, or string type. It could as easily be an array, an object, or a ... function.


1.2.2 Deleting objects
During the operation of our application, we’ll probably create many objects.

Each new object takes up memory, so there is a potential risk of overflow.

Luckily, there’s no need to overturn this problem (at least at the stage of learning where we are now).

The JavaScript engine uses a Garbage Collector, which decides for us whether the objects are still needed, and possibly removes them.


The JavaScript language doesn’t even provide for the possibility of explicitly deleting objects.

---

## Section 3 - Properties

Let's take a closer look at the properties of objects.

1.3.1 Types
As we mentioned earlier, we can assign primitive values to variables (e.g. number, Boolean, or string), complex values such as arrays or objects, and functions.


let nr = 10; 
let b = false; 
let str = "uno dos tres"; 
let arr = [10, 20, 30]; 
let obj = {
    x: 10, 
    y: 20
}; 
let fn = function(arg) {
    console.log(arg)
}; 
fn(123); //-> 123

Object properties can be treated in exactly the same way as variables – you can assign values of any type to them.

Let's create a test object with properties that are equivalent to the variables from the previous example.


let test = {
    nr: 10, 
    b: false, 
    str: "uno dos tres", 
    arr: [10, 20, 30], 
    obj: {
        x: 10, 
        y: 20
    }, 
fn: function(arg) {console.log(arg)} 
};
test.fn(123);


1.3.2 Nested properties
If the property of an object is another object that has properties itself, then we are dealing with nested properties.

The test object from the previous example contains the obj object, which in turn has the x and y fields.

Referring to such fields using dot notation is intuitive, and we simply add another dot and key (property name).




console.log(test.obj.x);
test.obj.y = 40;

Obviously, there may be more levels of nested properties.

1.3.3 A function as a property type – a method
The property of an object, as we have seen before, can also be a function.

A function that is the property of an object will be called a method.

Just as the properties of objects describe their characteristics, methods can be treated as their characteristic behavior, or ways of changing the state of an object.

As an example, let’s consider an object describing a point on the surface. We’ll only describe its two properties, which determine its position, that is, the position x and y. To this we’ll add two methods, moveVertically and moveHorizontally.

Look at the code below:


let point = {
    x: 0,
    y: 0,
    moveHorizontally: function(distance) {
        this.x = this.x + distance;
    },
    moveVertically: function(distance) {
        this.y = this.y + distance;
    }
}
console.log(point.x);    // -> 0
point.moveHorizontally(30);
console.log(point.x);    // -> 30

Obviously, there may be more levels of nested properties.

In the example, we have a new keyword, this.

In simple terms, it indicates the object we are in. However, we’ll leave a more detailed discussion of it for later. At this point, it’s enough to know that this.x simply indicates the x property of the object in which our method is located.

The method does not have to affect the state of the object, but this is essentially one of the main reasons for their use.

The test.fn method from the previous example not only doesn’t change the state of an object, it doesn’t even use any of its properties.

In real life applications, placing this function inside an object would be quite debatable, but for the moment we don’t care.

1.3.4 Adding a new property
Objects can change dynamically during their lifetime.

The changes concern not only the values stored in specific fields, but also all the properties that we can add or delete, and the type of data placed in them that we can change.

Let's go back to the example with a contact from the address book.


let contact = {
    tel: "207-662-5412",
    email: "RonaldSMurphy@freepost.org"
};

We’ll add the new fields firstName and lastName to the existing object, and display the values of the selected properties.


contact.firstName = "Ronald";
contact.lastName = "Murphy";
console.log(contact.tel);   // -> 207-662-5412
console.log(contact.firstName);     // -> Ronald

By the way, try to display a non-existent property, such as a notes. Note that a non-existent property of an object is treated as undefined and not, for example, as null.


console.log(contact.notes);

1.3.5 Modifying a property
By default, there are no restrictions on modifying the values placed in object properties (we’ll talk about non-writable properties in the chapter on configuring object properties).

Thus, we can assign a new value of any type to an existing object property at any time – we are not limited by the previous value type.

Let's use the contact example again.


let contact = {
    tel: "207-662-5412",
    email: "RonaldSMurphy@freepost.org"
};

After creating a contact, it turns out that the person placed in it has two email addresses.

At this point, it would be easiest to place an array of addresses in the email field, overwriting the old value.


contact.email = ["RonaldSMurphy@freepost.org", "rsmurphy@briazz.com" ];

However, if we know that one of these addresses is private and the other is business, it would be more logical to save them as an object – this will later allow us to easily distinguish the addresses by their "type".

Let’s overwrite the email field again.


contact.email = {
    private: "RonaldSMurphy@freepost.org",
    work: "rsmurphy@briazz.com" 
};
console.log(contact.email.work);

1.3.6 Deleting a property
The ability to manipulate objects would be incomplete if we were not able to remove a property.

We use the keyword delete for this.

We use it to indicate the property that is to disappear from the object.

For example, a person from our contact resigns from work and his / her email is no longer valid.

So, we modify the object by removing an unnecessary field from it.

Look at the code below:


delete contact.email.work;
console.log(contact.email.work);
console.log(contact.email.private);

---

## Section 4 - Dot notation vs. bracket notation

Until now, we have used dot notation as the basic way of referring to the properties and methods of an object.

Alternatively, we can also use bracket notation. This method is similar to referencing an array field, except that we don't give the index of an element, but instead we give its key. Remember, the key is a string!


contact.tel === contact["tel"];
contact.email.work === contact["email"]["work"]

1.4.1 Multi-word keys
This approach is slightly less intuitive than dot notation, but there are cases where it’s the only way out.

A typical example is the use of multi-word keys.

We can create an object containing a property whose key consists of several words.

However, we won’t be able to refer to this field later using a dot.

It is then that the bracket notation comes to our aid.

Look at the code below:


let contact = {
    "first name": "Ronald"
};
contact["first name"] = "Tim";
contact.first name = "Tim";    // SyntaxError: Unexpected identifier
contact."first name" = "Tim";    // SyntaxError: Unexpected string


1.4.2 Computed keys
However, bracket notation is more often used when operating on computed keys.

It may happen that the property key we want to refer to will be calculated during the operation of the program, on the fly.

In this case, dot notation will not allow us to combine the object name and calculated key (e.g. stored in a variable).

Again, we can use bracket notation to solve this problem.


let contact = {
    email_1: "RonaldSMurphy@freepost.org",
    email_2: "rsmurphy@briazz.com"
};
for(i=1; i<=2; i++) {
    let key = "email_" + i;
    console.log(key);
    console.log(contact[key]);
}

Pay attention to the line in which we calculate the key. We add a number from the variable i to the string "email_" – JavaScript automatically converts the number to a string here.

By the way, we can slightly improve the formatting of what our program displays on the console (the keys and values).

This may not apply directly to objects and their properties, but since we can display something in a more elegant way ...


for(i=1; i<=2; i++) {
    let key = "email_" + i;
    console.log(`${key}: ${contact[key]}`);
}

We’ll come back to this string formatting method in the following chapters.

---

## Section 5 - Property existence test and property enumeration

1.5.1 Property existence test and property enumeration
It may happen that we want to check if there is a property with a specific name in our facility (e.g. in contact with the notes field).

If you try to read a non-existent property, the undefined value will be returned.

JavaScript will behave the same if the field exists but has no value assigned to it.


if(contact.notes) { // if different then undefined
    console.log(contact.notes);
}

In most cases, it won’t matter to us whether a field does or does not exist, or simply has no value assigned to it.

Both cases are handled in the same way, with a new value being assigned to the property (if the field does not exist, it will automatically be created).


if(!contact.notes) { // if undefined (check !)
    contact.notes = "something really important";
}


  Note   It’s good practice to test if a given object field exists before trying to read it. The ease of use of dot notation often results in us taking shortcuts, assuming that an object should look a certain way. This can have fatal consequences, especially for nested objects.
Let's take a look at the contact object, which contains only the phone field. An attempt to display the value of the non-existent notes field will cause the console to appear undefined, and the program will continue to run.


console.log(contact.notes); // -> undefined

However, if we try to refer to a non-existent email field, which seems to contain the nested work and private fields, the consequences will be slightly more serious.


console.log(contact.email.private); // exception!

The JavaScript engine will try to find the private field in the object, which is ... undefined. This will end up throwing out an exception, which if not handled with the try ... catch, will terminate our program.

The easiest way to protect yourself is to either use the try ... catch block, or simply check before calling if the object and required field exist:


if(contact && contact.email) {
    console.log(contact.email.private);
}

or in a simpler form:


contact && contact.email && console.log(contact.email.private);


1.5.2 Existence test using "in"
JavaScript allows for a more unambiguous test of whether an object field exists – using the keyword in.

If the field exists, it’s returned true (even if the field has no set value).

Otherwise, the value false is returned.


if("notes" in contact) { // if true
    console.log(contact.notes);
}

Remember that the property name is a string, and this is how we must use it with the keyword in.


1.5.3 Enumeration "for ... in"
The keyword in also appears in a different construction, allowing us to enumerate all the fields of an object.

Frankly speaking, this is a much more practical use of it.

Using for ... in, we can go through the properties of an object (with some limitations, which we’ll talk about in the chapter on the configuration of properties).

More precisely – we go through the names of the properties, (i.e. the keys).

Let's display the property names of the contact object.


let contact = {
    tel: "207-662-5412",
    email: "RonaldSMurphy@freepost.org"
};
for(x in contact) {
    // print property name
    console.log(x);
}

The names of all the properties (keys) of the contact object are assigned to the variable x in turn.

To get to the value of a given field, we use bracket notation (the key is dynamically calculated and placed in the variable, so we cannot use dot notation).


for(x in contact) {
    // print property value 
    console.log(contact[x]);
}

Finally, if we would like to display the name, type, and value of all the properties, we could write it as follows:


for(x in contact) {
    // print property name, type and value
    console.log(`${x} : ${typeof contact[x]} : ${contact[x]}`);
}

1.5.4 The Object.keys method

Another way to retrieve the names of all the object properties is to use the Object.keys method.

This method returns an array of property names, which we can use in any way we want.

Continuing with the previous example, the following call should return an array ["tel", "email"] to the keys variable.

This array will contain all the keys (property names) of the contact object.


let keys = Object.keys(contact);

---

## Section 6 - References

1.6.1 References
Let's do a little experiment. Do you remember why we use the const keyword in declarations?

Before running the examples, reload the console page. This way, we make sure that the identifiers we use for the consts are no longer occupied (e.g. by running the previous examples).


const x = 10;
x = 20;    // TypeError: Assignment to constant variable.

The value placed in x is treated as a constant and protected against changes. This can be expected to work similarly for objects.

const contact = {};
contact = { email: "RonaldSMurphy@freepost.org"}; // TypeError: Assignment to constant variable.

As expected, the same exception as in the previous example is discarded – we cannot change the value we declared as const.

But we’ll try something else.


const contact = {};
contact.email = "RonaldSMurphy@freepost.org";
console.log(contact.email);

It turns out that not only is no exception generated, but the object is extended with a new field to which the value is assigned.

This value can later be easily modified or deleted.


contact.email = "rsmurphy@briazz.com";
console.log(contact.email);
delete contact.email;
console.log(contact.email);


1.6.2 The const object can be modified
Is this const behavior correct? It appears so, although it may require some additional explanation.

According to JavaScript documentation, "a constant cannot change through re-assignment" and "a constant cannot be re-declared".

This can be seen ideally in the case of simple types, such as the declaration and initialization of the constant x in our example. The value 10 that was placed there cannot be changed, period. You also cannot re-declare a variable or a constant with the same name x.

In the case of complex types (i.e. arrays and objects) variables and constants (the var, let, const keywords) do not contain the entire object. They only contain the object reference. For the sake of simplicity, we can imagine the reference as an address indicating where the object is really stored.

So, the const keyword protects only the reference, the address, from change. We cannot change the reference, e.g. by replacing the object (the new object has a different address). However, changes inside an object – adding a new property, changing a value, etc. do not affect the reference.

Let's try to understand it with an even simpler example.

Let's assume that we have a document with our residence written down in it. It’s only a reference – our house is not physically pushed into the document. If for some reason we cannot change this address (maybe we’ve messed something up?) then we have a situation with a const declaration.

References or addresses cannot be changed. However, it doesn’t affect what is happening inside the house – we can, for example, paint it, completely reorganize it, demolish all the walls and make one big space. The house is our object, whose properties we can modify freely.

We just can't change the references, that is, the const declaration, which is written in our mysterious document.

In the case of objects, const is designed to protect against a re-declaration or assignment of a new object.

There are, of course, methods to protect objects, or more precisely their properties, from changes.

These will be discussed in the chapter on property configuration.

1.6.3 Comparing objects
Since we already know that in the case of objects in variables and constants, only the references are stored, we should no longer be surprised by the results of object comparison.


var point1 = {x: 10, y: 20};
var point2 = {x: 10, y: 20};
console.log(point1 === point2);     // false

As you probably expect, the result of the comparison will be false. The comparison concerns the references of two independent objects.

Although they have identical properties of the same values, this doesn’t change the fact that they’re different objects. Coming back to the example of a house – we can have two identical houses on the street, next to each other. Same plan, same construction, same decoration. All in all, the owners themselves have trouble distinguishing them. But their addresses are different, and we are comparing the addresses.


let point3 = point1;
console.log(point1 === point3);     // true

This time the comparison will return true. We’ve written the content of point1 into the variable point3 (i.e. in both variables there is a reference to the same object).

We can easily check it by doing one more small experiment.


point3.z = 40;
console.log(point3.z);    // 40
console.log(point1.z);    // 40
console.log(point2.z);    // undefined

Using a reference stored in point3, we modify the object by adding a z field to it. The change is visible in the point3 and point1 variables, because they contain references to the same object. On the other hand, point2 points to a different object, and the action taken on point3 has no effect on it.

JavaScript does not have a ready-to-use mechanism to compare two objects by their properties (called deep comparison).

Writing your own recursive function, which will pass all fields (also nested) is not a big problem, however, and at the end of these courses you will certainly be able to do it yourself. As you rightly guess, we’ll use the construction for ... in.

There are also numerous libraries that provide such functionality.

1.6.4 Copying objects (copying references (), cloning, merging)
As we checked a moment ago, assigning an object from one variable to another only creates a copy of the reference. But what if we want to copy the contents of the object?

We would have to create a new target object, save the reference to a new variable, and copy the properties of the source object to the target one by one.

We can use the Object.assign method for this. The method takes the target object as the first argument, to which the fields from other objects will be copied. The second and subsequent arguments (there is no limit to the number of objects) will be used as the source of the properties to be copied. If a property with the same name as the source object already exists in the target object, it will be overwritten with a new value (the target is overwritten with the source).

In the example below, we create two empty objects and then, using Object.assign, extend their properties.


let point0 = {x:10, y: 20 };
let point1 = point0;    // copy reference
let point2 = {};
Object.assign(point2, point0);  //  copy properties into the new object
console.log(point2.x);
console.log(point2.y);
console.log(point1 === point0); // true
console.log(point1 === point2); // false

As a result of the execution of our code, the variable point1 will contain a reference to the same object as point0, while point2 will be a new object to which the contents of point0 have been copied (i.e. it will contain the two fields x and y, with the values 10 and 20).

The source objects, that is, the ones from which we’ll copy the properties, can be many.

All the properties of each source are copied to the target object, with the objects copied in the order in which they occur as arguments of the Object.assign method (from left to right).

The order is important for the same property names in several source objects.


let point3 = {};
Object.assign(point3, point0, {z: 100});
console.log(point3.z);

This time we create a point3 object with three fields: x, y, and z (with the values 10, 20, and 100 respectively). They’re copied from the point0 object and from the object placed directly as a call argument.

The list of source objects can, of course, be longer. As we indicated earlier, the properties with the same names are overwritten.

Continuing our example, let's check how overwriting properties works in practice.


var point4 = {};
Object.assign(point4, point3, {z: 200, color: "red"});
console.log(point4.z);    // 200

Note that the z field occurs both in the point3 object (and has a value of 100) and in the object inserted as the last argument (which has a value of 200). As we indicated earlier, in this case, the value from the last, most right-handed argument "wins".

The Object.assign function returns a reference to the target object that has been modified, so we can simplify our example by giving as the first argument (and without much thought) an empty object to which we assign the reference to a variable after completing the Object.assign method.


let point0 = {x:10, y: 20 };
let point2 = Object.assign({}, point0);
let point3 = Object.assign({}, point0, {z: 100});

A convenient alternative to Object.assign is to use the spread operator. There are some differences in the operation of both mechanisms, but they’re so subtle that we won’t bother with them at the moment.

The example rewritten once again, this time using the operator mentioned, will look like this:


let point0 = {x:10, y: 20 };
let point2 = { ...point0};
let point3 = { ...point0, z: 100};

The three dots preceding the object cause it to be spread out into individual fields, which are placed in the new object. The operation can be performed on many objects at the same time, additionally completing single fields according to normal syntax.

For example, the code:


let point4 = { ...point3, ...{z: 200, color: "red"});

will produce the same effect as:


let point4 = { ...point3, z: 200, color: "red");

You have probably already noticed that the mechanisms shown allow you to combine existing objects to create a new object.

Using them to copy, or to be more precise, clone a single object is just a special case of this.

However, the actions presented have a certain limitation – they all represent shallow cloning.

If there is shallow, then as you can guess, there should also be deep cloning.

What is the difference between them? Shallow cloning does not copy nested objects, operating only on their references.

This is unnoticeable in the examples we analyzed, so we’ll prepare another piece of test code:


let circle1 = {
    radius: 100,
    center: {
        x: 100,
        y: 100
    }};
let circle2 = {…circle1};
circle1.radius = 200;
circle1.center.x = 200;
console.log(circle2.radius);
console.log(circle2.center.x);
console.log(circle1 === circel2); // false
console.log(circle1.center === center); // true !

What’s happening this time?

The new circle2 object is copied "shallow".

This is a new object, independent of circle2. You can see it after trying to change the radius field – the change in point1 is not visible in point3.

However, the center field is an object – it is nested here.

Our Object.assign method (or in this case the spread operator) copies only the reference from the center field to the new circle2 object.

This can be seen both when trying to change one of the properties of the center field and when comparing these fields directly from both objects.

So we can already guess what deep cloning will be.

We’ll copy the values of all the fields, regardless of their nesting, if necessary creating new objects that are properties of the parent object.

JavaScript does not have a built-in mechanism for this type of cloning, but we can easily write this piece of code ourselves. The function that we write will check the types of all properties of the copied object. If a property turns out to be an object, the same function will be called for it again (so we use recursion). This code here may not be optimal, but it demonstrates the principle of deep cloning.

Analyze the function shown below:


let deepClone = function(obj) {
    let newObj = {...obj};
    for(property in newObj) {
        if(typeof newObj[property] === "object") {
            newObj[property] = deepClone(newObj[property]);
        }
    }
    return newObj;
}

Invent a sample object with at least three nesting levels, clone it using this function, and check that all properties, at any nesting level, are actually independent of the source object.

---

## Section 7 - Methods

1.7.1 Methods
We’ve previously discovered that the properties of an object can be of any type.

Then the name method appeared (i.e. a property) which is a function. In most cases, the reasonable use of objects begins when we equip them with methods.

Let's create a circle object in which we place the getType method.


let circle = {
    radius: 100,
    center: {
        x: 0,
        y:0
    },
    getType: function() {
        return "circle";
    }
};

There is a simplified way of declaring the method, which may be a bit more readable. Compare both examples by finding a difference in the way the method is defined. The effect of both declarations is identical.


let circle = {
    radius: 100,
    center: {
        x: 0,
        y:0
    },
    getType () {
        return "circle";
    }
};

In order to call up the method, we usually use dot notation.

We point to the object, name the method, and then add a parenthesis.

In parentheses, as in the case of regular functions, the arguments passed on may appear.


console.log(circle.getType());

The method can obviously also be called up using bracket notation.


console.log(circle["getType"]() );


1.7.2 The this keyword
The methods make real sense when they use object fields. Most often they’ll be used to influence their state (i.e. modify their properties) or to retrieve information about them.

However, in order to do so, we must have access to the object's fields from inside the method. How to do this?

The easiest way would be to refer to the object by its name, in other words, use the variable in which it was placed.

Let's modify the getType method from the previous example. We’ll test whether the object has a radius field, and whether a number is stored in it.

Depending on the test result, we’ll return either "circle" or "unknown". Note that we’ll use the conditional operator instead of the if construction. Look at the code below:


let circle = {
    radius: 100,
    center: {
        x: 0,
        y:0
    },
    getType () {
        return (typeof circle.radius === "number") ? 
        "circle" : "unknown" ;
    }
};
console.log(circle.getType());

The example works, right? But this way has a big flaw – so never, ever, ever use it! The problem will become apparent when we make a copy of our circle object.


let figure = {...circle};
delete circle.radius;
console.log(figure.radius);
console.log(figure.getType()); // "unknown"!

The figure object is a copy of the circle. Deleting the radius field in the circle object does not affect the field with the same name in the new figure object. So we would expect figure.getType to return "circle", but instead we get "unknown".

You've probably already figured out what actually happened. By calling the figure.getType method, we instinctively expect it to check the type of the radius field in this very object.

However, in the code of the method, we clearly indicate to check the radius field type of the circle object.

The method, which seems quite simple and logical, proves to be completely useless. So, what's the solution? A new keyword comes to the rescue – this.

To give a simplified explanation, we can say that this one will always contain a reference to the object we are in. We’ll use it inside the methods to refer to the property of the object in which the method is located.

Let's verify this by correcting the previous example - look at the code:


let circle = {
    radius: 100,
    center: {
        x: 0,
        y:0
    },
    getType () {
        return typeof this.radius === "number" ? "circle" : "unknown" ;
    }
};
console.log(circle.getType());
let figure = {...circle};
delete circle.radius;
console.log(figure.radius);
console.log(figure.getType()); // "circle"

This time the effect of the program is in line with our expectations.

The keyword this is not only applicable to objects.

We’ll take a closer look at this topic in the section dedicated to more advanced function constructions. However, one issue related to this, and to functions, should be addressed now. You probably remember the construction of the arrow function, which allows you to shorten the definition of a function.

For example:


let add = function (a,b) {
    return a + b;
}

can be written in a more compact form:


let add = (a,b) => a + b;

Arrow functions differ from ordinary functions not only in form. They contain inside themselves lexical scoping. Without going into detail, the method we would define in the form of an arrow will not have access to the properties of the object using this.

We should not use arrow functions to declare object methods.

1.7.3 this inside nested objects
The property of an object may be an object with its own property. We previously called it property nesting.

Let's place the method in such a nested object and check what this refers to in it - look at the code:


let circle = {
    radius: 100,
    center: {
        x:0,
        y:0,
        show(){console.log(`${this.x}, ${this.y}`)}
    }
}
circle.center.show();

As you can see, this refers to the object in which the method is directly placed.

Simple and logical, right? But what to do if, from our show method, we want to have access to the properties of the parent object, for example, to the radius field?

There is no such possibility, which is quite reasonable from the point of view of the concept of object-oriented programming.

For the method, its whole world should be the object in which it was defined. Of course, it may happen that the method will need some data from a higher level, but then we can pass them on as call arguments.

There is another simple justification for this limitation – the fact that we use object references.

Let’s add the following piece of code to the previous example:


let test = {
    point: circle.center
}

In the test.point field, there is a reference to the same object that’s in the circle.center. If we would like to find the parent object from this object, an ambiguity will appear – the parent object would be both test and circle.

Logically, this is not feasible.

1.7.4 Getters and setters
Two specific types of method are setters and getters, i.e. functions whose task is to change or check the properties of an object. In fact, these functions do not have to set properties or download them, but this is theoretically their purpose.

They have several specific features:

we declare them using the keywords set and get;
the setter method must take exactly one argument;
the getter method cannot accept any argument;
these methods are seen as ordinary properties with the name of the method;
setter and getter methods are not called as functions, they are used to assign a value to a property (setter) or to take a value from a property (getter)
there may be a pair of setter and getter of the same name, and it will be treated as a property with read and write capabilities.
From the point of view of using the object, the setter will behave like a normal property to which we assign a value. In fact, however, the method to which the value is passed on as an argument will be called. And what we do with this value inside a method depends entirely on our imagination.


Let's start with a simple example with a getter method. It will return the _tel property value.

let contact = {
    _tel: "207-662-5412",
    get tel() {return this._tel;}
};
console.log(contact.tel);
contact.tel = "100-100-1000";
console.log(contact.tel);
contact.email = "RonaldSMurphy@freepost.org";
console.log(contact.email);

In our object, we didn't define a tel setter, so an attempt to write into such a property will not succeed.

What's more, since there is already a getter with this name, JavaScript will not allow us to create a new property with this name.

For comparison, we see that an attempt to assign a value to a non-existent email field will create it and save the value.

Let's add a setter method to the example.

Using the contact object, we will now be able to both read from a fake tel field and write to it.


let contact = {
    _tel: "207-662-5412",
    get tel() {return this._tel;},
    set tel(t) { this._tel = t;}
};
console.log(contact.tel);
contact.tel = "100-100-1000";
console.log(contact.tel);

Setter and getter methods can perform much more complex actions than just operations on a single property. They are often used to create fake fields that are, for example, aggregated from the values of several real fields, modified on the fly, validated, etc.

For example:


let contact = {
    _age: 36,
   firstName : "David",
    lastName : "Taylor",
    get fullName() {return `${this.firstName} ${ this.lastName}`;},
    get age() { return this._age;},
    set age(a) { if( a > 0) this._age = a;}
};
console.log(contact.fullName);
contact.age = -20;
console.log(contact.age);

---

## Section 8 - Property and object configuration (flags and more)

1.8.1 Property configuration
In one of the previous examples, we tested how the enumeration of object properties works.

We used the Object.keys method and the for ... in construction. We assumed that in this way we would list all the object properties.

That is usually true, but we can change it by configuring individual properties as well as the whole object. Configuration also allows us to change some other features of object properties.

So, let's take a closer look at this topic, and let's go back to the previous example - look at the code:


let contact = {
    _age: 36,
    firstName : "David",
    lastName : "Taylor",
    get fullName() {return `${this.firstName} ${ this.lastName}`;},
    get age() { return this._age;},
    set age(a) { if( a > 0) this._age = a;}
};
let keys = Object.keys(contact);
console.log(keys);

An array "show", "_age", "firstName", "lastName", "lastName", "fullName", "age"] will be assigned to the keys variable, containing all the keys (property names) of the contact object.

Let's use another method now, Object.getOwnPropertyName.


let desc = Object.getOwnPropertyDescriptor(contact, "firstName");
console.log(desc);

This method allows us to retrieve information about the indicated property of the selected object.

In our example, we check the firstName property of the contact object. The desc variable should be filled in by an object describing the attributes of this property.


{
    value: "David", 
    writable: true, 
    enumerable: true, 
    configurable: true
}

As you can see, each property, apart from the name and value, has such attributes as writable, enumerable, and configurable. As you can guess, the configuration of properties will be set by manipulating these attributes.

The exceptions are the setter and getter methods, which do not have writable fields in the configuration, but instead the get and set fields appear.

Object properties, created in the way we did it in all the previous examples, have all their configuration attributes set to true by default (i.e. you can write to them, they are enumerable, and reconfigurable).

We can set our own configuration of properties using the Object.defineProperty method.

This method is used to create a new object property, but it can also be used to modify an existing property.

Let's take a look at another example:


let contact = {};
Object.defineProperty(contact, "_age", {
    value: 36,
    writable: true,
    enumerable: false,
    configurable: true
});
Object.keys(contact);
console.log(contact._age);

We have added the _age property to an empty contact object, marking it not to be enumerable. And it really isn't – calling Object.keys won't return it.

Similarly, when executing for ... in, it will not be taken into account. However, the property exists, which we can check by displaying its value.

To change the configuration of an existing property, we also use the Object.defineProperty method.

Continuing with the previous example, let’s try to convert the _age field to read only.


Object.defineProperty(contact, "_age", {
    value: contact._age,
    writable: false,
    enumerable: false,
    configurable: true
});
contact._age = 100;
console.log(contact._age);

As you can see, the change in the configuration of the writable attribute to false means that we cannot modify the value of our _age property.

Besides enumerable and writable, there is also an attribute called configurable in the configuration. Setting it to false will make it impossible to reconfigure the property or to delete it with the delete command.

Object.keys and the for ... in loop operate only on properties that are enumerable.

However, if we would like to retrieve all the fields without paying attention to their configuration, we can use the Object.getOwnPropertyNames method.

It works similarly to Object.key, but it returns an array of all the keys (property names), regardless of whether they are enumerable or not.


let enumKeys = Object.keys(contact);
let allKeys = Object.getOwnPropertyNames(contact);
console.log(enumKeys);
console.log(allKeys);


1.8.2 Object configuration
The configuration can also be changed at the level of the whole object (not only its individual properties).

The following methods are used for this purpose, among others:

Object.preventExtensions(obj) – after calling this method, we won't be able to add new properties to the object obj;
Object.seal(obj) – does not allow the adding, removing, or reconfiguring of the properties of the object obj;
Object.freeze(obj) – similar to Object.seal, but additionally makes it impossible to change the value of the property.

We also have methods to check if the object configuration has been changed.

And so, we can use these methods respectively: Object.isExtensible, Object.isSealed(obj) and Object.isFrozen(obj).

---

## Section 9 – Other ways to create objects

1.9.1 Other ways to create objects
In all the examples that have appeared so far in our play with objects, we used the literal notation to create them.

This method is primarily simple and legible, and generally enough for most applications.

It is ideal when we create a single object.

However, this is not the only method available in JavaScript to create objects, and so we will take some time to look at alternative techniques.



1.9.2 Factory
Let's start with a technique called factory in object-oriented programming. This is the name given to functions that create and return objects. In JavaScript, factory is a programming pattern rather than a mechanism of the language itself, but understanding it will allow us to move smoothly to a technique based on a constructor.

The idea itself is very simple. We create a function that will return a new object of our defined type every time it is called. We can pass arguments to a function that will be used to initiate the new object.

Let's say we need to create several points on a surface where each point is an object. The objects will have the same properties, and they will only differ in their values. Let's look at the first example:


let createPoint  = function(x, y) {
    let obj = {};
    obj.x = x;
    obj.y = y;
    return obj;
};
let point1 = createPoint(1,1);
let point2 = createPoint(2,2);
console.log(point1.x); // ->  1
console.log(point2.x); // -> 2

The createPoint function is our factory. Inside the factory, we create an empty object, then add the x and y properties to it, and initialize it with the values given as arguments of the function. The function returns the created and initiated object with a return. A function prepared in this way is used to create the two objects point1 and point2.

Let's improve the appearance of our function a little, without changing its operation.

Doesn't it look a bit simpler?


let createPoint  = function(x, y) {
    return {
        x:x,
        y:y
    }
};

We can go one step further. JavaScript makes our code even simpler.

If we have defined variables, in this case the x and y arguments passed to the function, we can insert them into the object without separating them into key and value.

Such a property will have both a variable name and its value.


let createPoint  = function(x, y) {
    return {
        x,
        y
    }
};

What's interesting is that we can present the same function in an even shorter form using arrow notation.


let createPoint  = (x, y) => ({x, y});

But let's get back to normal notation. Let's declare the local variables _color and _info in the function. Additionally, we’ll add a new property to our object – the getColor method. Its only task will be to return the value of our new local variable.

Let's try to write some information to the console.

Look at the code below:


let createColoredPoint  = function(x, y, color) {
    let _info = "... object under construction";
    let _color = color;
    console.log(_info);
    return {
        x,
        y,
        getColor() {return _color}
    }
};
let coloredPoint1 = createColoredPoint (1, 1, "red");// -> ... object under construction
let coloredPoint2 = createColoredPoint (2, 2, "green");// -> ... object under construction 
console.log(coloredPoint1.getColor());    // -> red
console.log(coloredPoint2.getColor());    // -> green
console.log(coloredPoint1._color);   // -> undefined !!!

Let's try to explain what actually happened after we ran our program. In JavaScript, each time a function is called, a new environment is created for it, containing among others its local variables. In our example, twice (because we call our function so many times) a new environment is created, together with the variables _color and _info.

The variable _info is only used inside the function while it is running. We display its contents on the console and do not return to it again. After leaving the function, it won’t be needed anymore, so we won’t have access to it (we can assume that it is removed).

Things are different for the _color variable. We refer to it in the getColor method of our newly created object. And since the object is returned by a function (after all, it is a factory), it will also exist after the function has finished working. And with it, the getColor method will exist, which we can run. How will the method get the value of the local variable _color from a function that is already finished? JavaScript is prepared for this scenario. It recognizes the situation and, together with our new object, stores the call environment of the function in which the object was created. So, in human terms, the local variables of the function, which are used by the methods of the returned object, are not deleted. And more importantly, each call to a function has its own independent environment, just as objects created by the factory are independent. This mechanism is called closure.

By the way, we’ve seen how to create private property. In object-oriented programming, these are properties to which only the methods of our object have access. This is the case in our example. The local variable _color is not accessible from the outside, but only with the getColor method. Therefore, we can treat it as private property.

1.9.3 The constructor and the new keyword
As we mentioned, the factory in JavaScript is not really a mechanism of the language itself, but a programming pattern. On the language level, however, a similar technique is provided, using the constructor functions (or simply the constructor).

A constructor, like a factory, is a function that creates and returns an object. However, it differs from the factory in several respects. First of all, it requires the use of the keyword new when creating a new object. Additionally, it implicitly performs some actions that we have taken in the factory explicitly (e.g. creating an empty object).

So let's turn our factory example into a code that uses the constructor function. The changes are small, and you can probably find them easily by comparing the two programs.

Look at the code below:


let ColoredPoint = function(x, y, color) {
    let _info = "... object under construction";
    let _color = color;
    console.log(_info);
    
    this.x = x;
    this.y = y;
    this.getColor = function() {return _color};
};
let coloredPoint1 = new ColoredPoint(1, 1, "red");
let coloredPoint2 = new ColoredPoint(2, 2, "green"); 
console.log(coloredPoint1.getColor());    // -> red
console.log(coloredPoint2.getColor());    // -> green
console.log(coloredPoint1._color);   // -> undefined !!!

Usually the names of constructors begin with capital letters, hence the name of the ColoredPoint function. The first change that is noticeable is the lack of the word return. In the constructor, this is not necessary, after running it with new, it will automatically return an implicitly created object. We have access to this implicitly created object in the constructor using the keyword this. With this, we define and initiate the properties of the new object. Because the constructor is a function, we can also use the closure here. This part of the code is practically no different from the factory.

Let's do one more little experiment:


console.log(coloredPoint.constructor.name);

The name of our constructor will appear on the console: "ColoredPoint". Everything matches up ... But wait, after all, we didn’t define the property of the constructor in our object anywhere.

So how did it get there? Let's check the type of this property (or more precisely the type of value placed in the property).


console.log(typeof coloredPoint.constructor);

It turns out it's a function.

Let's try the same thing with an empty object.


let a = {};
console.log(typeof a.constructor);

The effect is the same as before.

It's time to complicate our idea of objects a little. With {} or new we do not really create an empty object.

To create it, we use the implicitly generic Object constructor, on which most objects in JavaScript are built.

The Object constructor contains some generic properties and methods that can be useful in all objects (including in the constructor property). What exactly does it mean to create an object on the basis of another object? We’ll explain this more in the part of the course concerning prototypes.

At the moment, it’s enough to know that most of the objects we create inherit properties from the generic Object constructor object.

Note that the inherited properties are not enumerated with the "for ... in" loop, nor Object.kesys nor Object.getOwnPropertyNames. They are available, we can use them, but they are treated slightly differently from the object's own properties.

The name of the getOwnPropertyNames method does not appear by accident.

1.9.4 new Object()
Since Object is the constructor of a generic object, can we use it to create a new object?

Of course we can.

This way we will create an empty object (without our properties, but with properties supported by Object).


let emptyObject = new Object();
console.log(emptyObject.constructor.name); 

The effect of using new Object() will be the same as {}.


let anotherEmptyObject = {};
console.log(anotherEmptyObject.constructor.name);

In both cases, there is an inherited constructor property.

This means that the objects contain what has been added from the constructor Object.

1.9.5 Object.create
Another interesting technique for creating an object is by using the Object.create method.

It allows you to create a new object based on an existing object (which will be used as a prototype of our new object). The base object is given as an argument for calling the method.

Since we haven't dealt with prototypes yet, we’ll look at the method to create an object without a prototype (we’ll give null as an argument).


et reallyEmptyObject = Object.create(null);
console.log(typeof reallyEmptyObject.constructor);

Note that this time undefined appears on the console.

This means that there is no property called constructor in reallyEmptyObject.

This time we create a really empty object. However, treat this only as an exercise.

Unless you are 100% sure why you need an object that is not based on the generic Object constructor, create it in the normal way (factory, constructor, object literals, classes).

1.9.6 Class
There is another, very important method for creating objects.

It’s through the use of classes.

This is the basic way to manage objects in most programming languages.

In the case of JavaScript, it was added in one of the following language editions (ECMA6).

However, it is a subject that is so extensive that we will dedicate the whole next chapter of our course to it.

---

## Section 10 – Prototypes

1.10.1 Prototypes
Objects can be found in most popular programming languages. We use them in Python, Java, C# or C++.

The vast majority of languages use a class approach, which basically means that before we create an object, we have to define a class (with methods and properties).

A class is treated as a kind of template, on which we create objects (instances). When assigning values to properties or calling methods, we’re already working on objects and not on classes.

One of the most important things that classes allow for is inheritance. Based on an existing class, we can create a new one, which will contain the properties and methods of the base class.

Originally, JavaScript did not use classes. In our examples, we’ve done very well so far using the classless model. But how do we implement inheritance without classes? In a slightly different form than that known as classes, we did it using prototypes, i.e. existing objects connected in an appropriate way to newly created objects. Hence the name – a prototype object model.

The ECMA6 standard introduced classes into JavaScript as an alternative to prototypes and constructors. Both of these approaches can now be applied equivalently.

Admittedly, the class approach is much simpler for people who are starting to learn programming or switching to JavaScript from another object-oriented language.

There are many JavaScript programmers who have only used classes, often without knowing about the existence of prototypes. So, we won’t devote too much space to prototypes in this course, instead looking at classes much more closely. However, when programming in JavaScript, you must at least be aware of the existence of prototype technology.

  Note   Nowadays, most often literal notation and classes are used to create objects in JavaScript. The literal notation technique is suitable for creating objects that are not very complex, often created ad hoc, in which we are not interested in using inheritance. Classes are used wherever we will repeatedly create similar objects, often a little more complex, in which inheritance appears.

print("Hello world!")
Let's take a look at the objects created using literal notation. Let's create two objects, point and coloredPoint. The point object contains the coordinates of its position on the surface, while coloredPoint contains only color.


let point = {x:0, y:0};
let coloredPoint = {color: "red"};

We mentioned earlier that every new object in JavaScript is created by default from the generic Object constructor.

One of the properties that each object inherits is the __proto__ field. Let's see what happens when we use this field to connect our two objects.


coloredPoint.__proto__ = point;

Thus, the point object becomes a prototype of the coloredPoint object. By the way, point also has its prototype, which is an object created by default on the basis of the Object constructor. Hence we are talking about a chain of prototypes.

  Note   In normal programming, we absolutely do not use __proto__. Direct use of this field is considered obsolete, withdrawn from the standards, slow. Here, we use it only to learn the basics of prototyping step by step.

Let's try to refer to the property of the coloredPoint object.


console.log(Object.getOwnPropertyNames(coloredPoint));
console.log(coloredPoint.color);
console.log(coloredPoint.x);

As expected, Object.getOwnPropertyNames shows us that the object has only the color property.

The fact that we have access to it is therefore obvious. However, we try, successfully, to read the x field. What happens then? JavaScript does not find a field named x in the coloredPoint object and looks for it in the prototype.

If it doesn't find it there, it looks for it in the prototype, and so on (hence the chain of prototypes).

Now let's try to change the value of the property we inherited from the prototype.


coloredPoint.x = 100;   // new property
console.log(coloredPoint.x);
console.log(point.x);
console.log(Object.getOwnPropertyNames(coloredPoint));

It turns out that when trying to write to such a property, JavaScript does not follow the chain of prototypes.

If it doesn’t find a property directly in the object, it creates it, and assigns a new value to it. This way, among other things, the properties of the prototype are protected (and the same prototype can be used by many different objects).

Now let's change the value of one of the properties of the point object, which is our prototype, to a test.


point.y = 200;
console.log(coloredPoint.y);
console.log(point.y);

The change is visible both at the level of the point object and the coloredPoint object, for which point is a prototype. Using the __proto__ property for prototypes is, as we wrote earlier, not recommended. To present alternatives, let’s use a slightly more elaborate scenario.


1.10.2 __proto__
Let's start again with the unrecommended __proto__ way.

Let’s create a figure object that has one getType method. The method will check if we have a type field in the object, returning either its value or the string "unknown".

The second object, circle, contains the properties type, center, and radius. Both objects are created using the letter technique. Using __proto__, we assign a figure as the prototype circle.

Look at the code below:


figure = {
    getType: function() {
        return this.type ? this.type : "unknown";
    }
};
let circle = {
    type: "circle",
    center: {x:0, y:0},
    radius: 100
};
circle.__proto__ = figure;

Let's call the getType method for both objects:


console.log(figure.getType());
console.log(circle.getType());

If you call figure.getType, it will return "unknown"; after all, the object has no type field. Calling circle.getType will display "circle", a string stored in the type field of the circle object.

In this case, JavaScript doesn’t find the getType method directly in circle, so it starts searching the prototype chain.

After finding the method in the prototype, it calls it. Only one thing may need to be explained.

Look at the getType method declaration. Inside it, we refer to the type field using the word this.

We explained earlier that this refers to the object in which we define the method. That was a bit of a simplification, but usually true. In fact, this refers to the object in the context of which a given function is called. In our case, the method belongs to figure, but it is called in circle.

In such a situation, this inside it refers to circle and not to figure.


1.10.3 Object.setPrototypeOf
What alternatives do we have if using __proto__ is not recommended?

First, we can use the Object.setPrototypeOf and Object.getPrototypeOf methods.

The first one allows us to associate the target object with the prototype object.

The second one returns the prototype of the indicated object (in our example, the proto variable should refer to the figure object).


Object.setPrototypeOf(circle, figure);
let proto = Object.getPrototypeOf(circle);
console.log(circle.getType());

1.10.4 Object.create
We can also create an empty object on the basis of the selected prototype, completing it later with the necessary fields.

We use the Object.create method we already learned about.

Previously, we used it with a null argument, which meant that we created an empty object without a prototype.


let circle = Object.create(figure)
circle.type = "circle";
circle.center = {x:0, y:0},
circle.radius = 100;
console.log(circle.getType());

1.10.5 Constructor
The last approach is to use the constructors. First of all, we define the Figure constructor, with which we create a figure object.


let Figure = function(){
    this.getType = function() {
        return this.type ? this.type : "unknown";
    }
};
let figure = new Figure;

In the next step, we define the Circle constructor and, more importantly, we bind the figure object to it as a prototype. Note that until now the prototype has been connected directly to the object. This time it’s different – we bind it to a function that will create objects.

Each time we call the Circle constructor (using new, of course) it will create a new object with type, center, and radius fields. The prototype for each object will be a figure.


let Circle = function(center, radius){
    this.type = "circle";
    this.center = center;
    this.radius = radius;
};
Circle.prototype = figure;
let circle1 = new Circle({x:0, y:0}, 10);
let circle2 = new Circle({x:100, y:100}, 100);

For the sake of variety, let’s define another constructor, Triangle.

As you can guess, it will be used to create triangle objects. Its prototype will also be a figure.


let Triangle = function(v1, v2, v3) {
    this.type = "triangle";
    this.vertices = [ v1, v2, v3];
};
Triangle.prototype = figure;
let triangle1 = new Triangle({x:0, y:0}, {x:50, y:50}, {x:10, y:100});
console.log(circle1.getType());
console.log(triangle1.getType());

If you decide to use prototypes, it’s definitely best to use a method based on constructors or Object.create.


Let's do one more test, which will show us a very useful feature of prototypes. The prototype is an object, so we can modify it by adding new methods.

Let's say we want to modify an object that is a Circle prototype. We don't have to refer directly to the figure, but we can do it in the following way:


Circle.prototype.hi = function(){console.log("Hi!")};

We’ve added the hi method to the prototype, whose only task is to display greetings to the console.

We’ve modified the figure object, which is a prototype of the circle1, circle2, and triangle1 objects. What's important is that the hi method will be available not only for objects newly created with the Circle or Triangle constructors, but for all existing objects, whose prototype is just figure.

Let's check it out:


circle1.hi();
triangle1.hi();
figure.hi();

As expected, the greeting "Hi!" is displayed three times.

The feature of prototypes presented here allows for modifications to existing objects (e.g. predefined objects). Let's use the String constructor as an example. It is predefined and allows us to create string objects. Such objects have many methods and properties, e.g. length, which returns the length of the stored string.


let testString = new String("unu doi trei");
console.log(testString.length);

Like every designer, String also has the prototype property.

Let's try to use it:


String.prototype.hi = function(){console.log("Hi!")};
console(string.hi());

Adding the hi writing method to the String designer is not particularly useful, but it highlights some interesting possibilities. Note that after our changes, we can also make such a piece of code:


console.log("abcd".hi());

Why does "abcd", which is a primitive value, act as if it were an object containing a hi field? It's because of autoboxing.

JavaScript converts the simple type (in this case the string) to the corresponding object (in our case, an object based on the String constructor) as and when necessary.

And we indicated, this requires the use of a dot, suggesting that with dot notation we treat the text "abcd" as an object.


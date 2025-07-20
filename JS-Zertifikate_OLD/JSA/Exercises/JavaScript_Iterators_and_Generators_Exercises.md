
# Iterators and Generators - Übungsaufgaben

## Aufgabe 1
Schreiben Sie eine Generatorfunktion, die alle geraden Zahlen bis zu einem bestimmten Limit generiert. Implementieren Sie eine Schleife, um nur die ersten 10 generierten Werte zu sammeln und auf der Konsole auszugeben.

## Aufgabe 2
Erstellen Sie einen Iterator für ein Objekt, das die Fibonacci-Folge bis zu einer bestimmten Grenze generiert. Nutzen Sie den Iterator, um die ersten 7 Werte der Sequenz anzuzeigen.

## Aufgabe 3
Definieren Sie eine Generatorfunktion, die Zahlen ab 1 unbegrenzt hochzählt, aber bei einem bestimmten Limit stoppt. Verwenden Sie den Generator in einer Schleife und geben Sie nur die ungeraden Zahlen bis zu 15 aus.

## Aufgabe 4
Erstellen Sie einen benutzerdefinierten Iterator, der durch die Buchstaben eines Strings iteriert und nur die Großbuchstaben zurückgibt. Testen Sie den Iterator mit einem Beispielstring.

## Aufgabe 5
Schreiben Sie eine Generatorfunktion, die die Fakultäten von Zahlen ab 1 bis zu einer gegebenen Grenze berechnet. Verwenden Sie die Funktion, um die ersten 5 Fakultäten anzuzeigen.

## Aufgabe 6
Erstellen Sie einen Generator, der die Zeichen eines Wortes einzeln zurückgibt und dann das Wort rückwärts ausgibt. Verwenden Sie den Generator, um die Zeichen eines beliebigen Wortes zu iterieren.

## Aufgabe 7
Definieren Sie ein Objekt, das die Methode `[Symbol.iterator]` enthält und ein Array von Zufallszahlen (bis zu einem gegebenen Limit) zurückgibt. Verwenden Sie den Spread-Operator, um die Zufallszahlen in einer Konsole auszugeben.

## Aufgabe 8
Implementieren Sie eine Generatorfunktion, die die Werte aus zwei Arrays mischt und einen nach dem anderen zurückgibt, bis beide Arrays leer sind. Testen Sie die Funktion mit zwei Beispielarrays.

## Aufgabe 9
Erstellen Sie einen Generator, der die Potenzen von 2 bis zu einem bestimmten Limit generiert. Verwenden Sie den Generator, um alle Potenzen von 2 bis zu 1024 zu berechnen und auszugeben.

## Aufgabe 10
Schreiben Sie eine Generatorfunktion, die über ein Objekt iteriert und nur die Werte zurückgibt, deren Schlüssel aus einer ungeraden Anzahl von Buchstaben besteht. Testen Sie die Funktion mit einem Beispielobjekt.

## Aufgabe 11
Erstellen Sie eine Generatorfunktion, die abwechselnd einen Wert aus zwei Listen zurückgibt, bis eine der Listen leer ist. Verwenden Sie die Funktion mit zwei Beispiel-Listen unterschiedlicher Länge.

## Aufgabe 12
Definieren Sie einen Generator, der die Ziffern einer Zahl einzeln zurückgibt. Verwenden Sie den Generator, um die Ziffern der Zahl 123456 auszugeben.

## Aufgabe 13
Implementieren Sie eine Generatorfunktion, die alle Primzahlen bis zu einem gegebenen Limit generiert. Geben Sie die ersten 10 Primzahlen mit dieser Funktion aus.

## Aufgabe 14
Schreiben Sie eine Generatorfunktion, die abwechselnd ein Element aus einem Array und eine zufällige Zahl zwischen 1 und 10 zurückgibt, bis das Array durchlaufen ist.

## Aufgabe 15
Erstellen Sie einen Generator, der die Quadratzahlen bis zu einer bestimmten Grenze berechnet und zurückgibt. Verwenden Sie den Generator, um die Quadratzahlen von 1 bis 100 zu ermitteln.

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
function* evenNumbers(limit) {
    for (let i = 0; i <= limit; i += 2) {
        yield i;
    }
}
const evens = evenNumbers(20);
for (let i = 0; i < 10; i++) {
    console.log(evens.next().value);
}
```

### Lösung zu Aufgabe 2
```javascript
let fibonacciIterator = {
    [Symbol.iterator]() {
        let a = 0, b = 1;
        return {
            next() {
                let temp = a;
                a = b;
                b = temp + b;
                return { value: temp, done: temp > 20 };
            }
        };
    }
};
for (let num of fibonacciIterator) {
    console.log(num);
}
```

### Lösung zu Aufgabe 3
```javascript
function* oddCounter(limit) {
    let count = 1;
    while (count <= limit) {
        yield count;
        count += 2;
    }
}
for (let num of oddCounter(15)) {
    console.log(num);
}
```

### Lösung zu Aufgabe 4
```javascript
let uppercaseIterator = {
    string: "JavaScript Iterator",
    [Symbol.iterator]() {
        let index = 0;
        return {
            next: () => {
                while (index < this.string.length) {
                    let char = this.string[index++];
                    if (char === char.toUpperCase() && char !== " ") {
                        return { value: char, done: false };
                    }
                }
                return { done: true };
            }
        };
    }
};
for (let letter of uppercaseIterator) {
    console.log(letter);
}
```

## Aufgabe 5
```python
def factorial_generator(limit):
    result = 1
    for i in range(1, limit + 1):
        result *= i
        yield result

# Test: Displaying the first 5 factorials
for value in factorial_generator(5):
    print(value)  # Output: 1, 2, 6, 24, 120
```

## Aufgabe 6
```python
def word_reverse_generator(word):
    for char in word:
        yield char
    for char in reversed(word):
        yield char

# Test: Iterating over characters in the word "hello"
for char in word_reverse_generator("hello"):
    print(char)  # Output: h, e, l, l, o, o, l, l, e, h
```

## Aufgabe 7
```python
import random

class RandomNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit <= 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(1, 100)

# Test: Displaying random numbers using spread operator simulation
numbers = RandomNumbers(5)
print(*numbers)  # Output: Five random numbers
```

## Aufgabe 8
```python
def mix_arrays_generator(array1, array2):
    it1, it2 = iter(array1), iter(array2)
    while True:
        try:
            yield next(it1)
        except StopIteration:
            break
        try:
            yield next(it2)
        except StopIteration:
            break

# Test: Mixing elements of two arrays
for value in mix_arrays_generator([1, 2, 3], ['a', 'b', 'c']):
    print(value)  # Output: 1, a, 2, b, 3, c
```

## Aufgabe 9
```python
def power_of_two_generator(limit):
    value = 1
    while value <= limit:
        yield value
        value *= 2

# Test: Displaying powers of 2 up to 1024
for power in power_of_two_generator(1024):
    print(power)  # Output: 1, 2, 4, 8, 16, ..., 1024
```

## Aufgabe 10
```python
def odd_key_length_values(obj):
    for key, value in obj.items():
        if len(key) % 2 != 0:
            yield value

# Test: Displaying values of keys with odd length
obj = {"one": 1, "three": 3, "four": 4, "seven": 7}
for value in odd_key_length_values(obj):
    print(value)  # Output: 1, 3, 7
```

## Aufgabe 11
```python
def alternate_list_generator(list1, list2):
    it1, it2 = iter(list1), iter(list2)
    while True:
        try:
            yield next(it1)
        except StopIteration:
            return
        try:
            yield next(it2)
        except StopIteration:
            return

# Test: Alternating between two lists
for item in alternate_list_generator([1, 2, 3], ['a', 'b']):
    print(item)  # Output: 1, a, 2, b, 3
```

## Aufgabe 12
```python
def digit_generator(number):
    for digit in str(number):
        yield int(digit)

# Test: Displaying digits of the number 123456
for digit in digit_generator(123456):
    print(digit)  # Output: 1, 2, 3, 4, 5, 6
```

## Aufgabe 13
```python
def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Test: Displaying the first 10 primes
for prime in prime_generator(29):
    print(prime)  # Output: 2, 3, 5, 7, 11, ..., 29
```

## Aufgabe 14
```python
import random

def mixed_array_random_generator(array):
    for element in array:
        yield element
        yield random.randint(1, 10)

# Test: Displaying elements with random numbers
for item in mixed_array_random_generator([1, 2, 3]):
    print(item)  # Output: 1, random, 2, random, 3, random
```

## Aufgabe 15
```python
def square_generator(limit):
    for i in range(1, limit + 1):
        yield i * i

# Test: Displaying squares up to 100
for square in square_generator(10):
    print(square)  # Output: 1, 4, 9, 16, ..., 100
```



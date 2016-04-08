# **Zadanie 2 - liczebniki Churcha**#

**Rachunek Lambda** używany do badania zagadnień związanych z podstawami matematyki jak na przykład rekurencja. Jest to narzędzie przydatne w badaniu algorytmów. Rachunek lambda nie zawiera sam z siebie liczb, więc należy je skonstruować.

**Liczba naturalna Churcha** to funkcja wyższego rzędu pobierająca dwa argumenty - funkcję f i argument x, która n-krotnie aplikuje f do x. 
Przykładowo:

zero = f x =x
jeden = f x =f x
dwa = f x = f (f x)
trzy= f x= f (f (f x))
cztery f x= f(f(f(f x)))

Operacje arytmetyczne mogą być reprezntowane przez funkcje na liczbach Churchach, możemy zdefiniować m.in. takie operacje jak inkrementacja, dodawanie, mnożenie, eksponenta.


**Inkrementacja (succ):**
succ = n f x =  f ( n f x )  // wykonanie funkcji f n+1 razy

**Dodawanie (add):**
add=n m f x= n f( m f x)//wykonanie funkcji f m+n razy

**Mnożenie (mult):**
mult=n m f x= m(n f) x

**Eksponenta (exp):**
exp=n m f x= (n m) f x

W programie poza wyżej wymienionymi funkcjami zaimplementowano także funckję **church2int**, która pozwala na zamianę liczby Churcha na int, co ułatwia weryfikację wyników.

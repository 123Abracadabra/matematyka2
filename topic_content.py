# -*- coding: utf-8 -*-

TOPIC_CONTENT = {
    "Liczby i działania": {
        "theory_base": """**Kolejność działań (MNOŻENIE przed DODAWANIEM):**
Nawias → potęgi i pierwiastki → × i ÷ → + i −

**Liczby ujemne:** (−) × (−) = (+), (−) × (+) = (−)

**Porównywanie liczb:** zamieniaj wszystko na ułamki dziesiętne.
Przykład: 1/3 ≈ 0.333, więc 1/3 > 0.25""",

        "theory_ext": """**Działania z potęgami i pierwiastkami:**
• aᵐ × aⁿ = aᵐ⁺ⁿ
• aᵐ ÷ aⁿ = aᵐ⁻ⁿ
• (aᵐ)ⁿ = aᵐⁿ
• a⁰ = 1 (dla a ≠ 0)
• a⁻ⁿ = 1/aⁿ

**Pierwiastki:** √(a·b) = √a · √b, √(a/b) = √a/√b

**Błąd do unikania:** (−3)² = 9, ale −3² = −9 (brak nawiasu!)""",
    },

    "Zbiory liczbowe": {
        "theory_base": """**Rodziny liczb (od najmniejszej do największej):**
ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ

• ℕ (naturalne): 0, 1, 2, 3, ...
• ℤ (całkowite): ..., −2, −1, 0, 1, 2, ...
• ℚ (wymierne): wszystkie ułamki p/q
• ℝ (rzeczywiste): wszystkie liczby na osi liczbowej

**Test:** liczba należy do ℕ tylko gdy jest nieujemna i całkowita.""",

        "theory_ext": """**Operacje na zbiorach:**
• A ∪ B — suma (elementy w A LUB w B)
• A ∩ B — iloczyn (elementy w A I w B)
• A \\ B — różnica (w A, ale NIE w B)
• A' — dopełnienie (wszystko poza A)

**Diagram Venna** — rysuj dwa koła, zaznaczaj część wspólną.

**Przedziały na osi:** ⟨a,b⟩ = [a,b], (a,b), [a,b), (a,b]
Okrągły nawias = koniec nie należy do przedziału.""",
    },

    "Ułamki": {
        "theory_base": """**Wspólny mianownik:** znajdź NWW mianowników.
Przykład: 1/4 + 1/6 → NWW(4,6)=12 → 3/12 + 2/12 = 5/12

**Skracanie:** dziel licznik i mianownik przez NWD.

**Ułamek z liczby:** n% z X = (n/100)·X
3/8 z 64 → 64÷8 = 8 → 8×3 = 24""",

        "theory_ext": """**Działania złożone na ułamkach:**
Kolejność: nawias → mnożenie/dzielenie → dodawanie/odejmowanie

**Dzielenie ułamków:** a/b ÷ c/d = a/b × d/c (odwróć i mnóż)

**Ułamki algebraiczne:** skracaj wspólne czynniki z licznika i mianownika.
Przykład: (x²−4)/(x−2) = (x+2)(x−2)/(x−2) = x+2 (dla x≠2)""",
    },

    "Procenty": {
        "theory_base": """**Procent jako ułamek:** p% = p/100

**Obliczenia:**
• p% z X = X · p/100
• Podwyżka o p%: X · (1 + p/100)
• Obniżka o p%: X · (1 − p/100)

**Wyznaczanie całości:** jeśli 80% to 96 zł → całość = 96 ÷ 0.8 = 120 zł""",

        "theory_ext": """**Procent składany:** po n latach z kapitałem K i stopą r:
Kₙ = K · (1 + r/100)ⁿ

**Zmiana wielokrotna:** wzrost o 20%, potem spadek o 20%:
wynik to 1.2 × 0.8 = 0.96 → NET spadek o 4% (nie 0%!)

**Błąd klasyczny:** wzrost o 50% i spadek o 50% ≠ 0%
bo 100 → 150 → 75 (strata 25%)""",
    },

    "Potęgowanie i pierwiastkowanie": {
        "theory_base": """**Podstawy potęgowania:**
• 2³ = 2×2×2 = 8
• (−a)² = a² (wynik zawsze ≥ 0)
• −a² = −(a²) (minus przed, bez nawiasu!)

**Pierwiastek kwadratowy:** √a = b gdy b² = a i b ≥ 0
√25 = 5, √0 = 0, √(−4) nie istnieje w ℝ""",

        "theory_ext": """**Własności potęg:**
• aᵐ · aⁿ = aᵐ⁺ⁿ
• aᵐ / aⁿ = aᵐ⁻ⁿ
• (aᵐ)ⁿ = aᵐⁿ
• (a·b)ⁿ = aⁿ·bⁿ
• a⁻ⁿ = 1/aⁿ

**Potęgi wymierne:** a^(1/n) = ⁿ√a, a^(m/n) = ⁿ√(aᵐ)

**Upraszczanie:** zawsze sprowadzaj do tej samej podstawy.""",
    },

    "Wartość bezwzględna": {
        "theory_base": """**Definicja:**
|x| = x gdy x ≥ 0
|x| = −x gdy x < 0

**Geometrycznie:** |x| = odległość x od 0 na osi liczbowej.
|x − a| = odległość x od a.

**Przykłady:** |−7| = 7, |0| = 0, |3| = 3""",

        "theory_ext": """**Równania z wartością bezwzględną:**
|f(x)| = a → f(x) = a LUB f(x) = −a (dla a > 0)

**Nierówności:**
• |x| < a → −a < x < a
• |x| > a → x < −a LUB x > a

**Schemat:** zawsze rysuj oś liczbową i zaznaczaj rozwiązania graficznie!""",
    },

    "Logarytmy": {
        "theory_base": """**Definicja:** logₐ(b) = c ⟺ aᶜ = b

**Warunki:** a > 0, a ≠ 1, b > 0

**Ważne wartości:**
• log₂(8) = 3 (bo 2³=8)
• log₁₀(1000) = 3 (bo 10³=1000)
• logₐ(1) = 0, logₐ(a) = 1""",

        "theory_ext": """**Własności logarytmów:**
• logₐ(x·y) = logₐ(x) + logₐ(y)
• logₐ(x/y) = logₐ(x) − logₐ(y)
• logₐ(xⁿ) = n·logₐ(x)
• logₐ(b) = log(b)/log(a) (zmiana podstawy)

**Równania logarytmiczne:** sprowadź do tej samej podstawy.
log₃(x) + log₃(x−2) = 1 → log₃(x(x−2)) = 1 → x(x−2) = 3""",
    },

    "Wyrażenia algebraiczne": {
        "theory_base": """**Wyrazy podobne:** te same litery i wykładniki.
3x + 2y − x + 5y = (3x−x) + (2y+5y) = 2x + 7y

**Wzory skróconego mnożenia:**
• (a+b)² = a² + 2ab + b²
• (a−b)² = a² − 2ab + b²
• (a+b)(a−b) = a² − b²""",

        "theory_ext": """**Rozkład na czynniki:**
• Wyłącz wspólny czynnik: 6x² + 4x = 2x(3x+2)
• Użyj wzorów skróconego mnożenia
• Dla trinomialu x²+bx+c szukaj p,q: p+q=b, p·q=c

**Ułamki algebraiczne:** NWD licznika i mianownika.
(x²−4)/(x²+2x) = (x−2)(x+2) / x(x+2) = (x−2)/x

**Dziedzina:** wykluczaj mianownik = 0.""",
    },

    "Równania i nierówności": {
        "theory_base": """**Zasada:** to samo po obu stronach ⇒ równanie równoważne.

**Schemat:**
1. Usuń nawiasy
2. Przenieś x na lewą, liczby na prawą
3. Podziel przez współczynnik przy x
4. Sprawdź wynik!

**Uwaga w nierównościach:** mnożenie/dzielenie przez ujemną → odwróć znak!""",

        "theory_ext": """**Równania kwadratowe:** ax² + bx + c = 0
Δ = b² − 4ac
• Δ > 0 → dwa rozwiązania: x = (−b ± √Δ) / 2a
• Δ = 0 → jedno: x = −b/2a
• Δ < 0 → brak rozwiązań w ℝ

**Nierówności kwadratowe:** narysuj parabolę, zaznacz znak.
ax² + bx + c > 0: obszar powyżej osi x.

**Równania z parametrem:** traktuj parametr jak stałą.""",
    },

    "Układy równań": {
        "theory_base": """**Metoda podstawiania:**
1. Z jednego równania wyraź jedną zmienną
2. Podstaw do drugiego
3. Rozwiąż, wróć i oblicz drugą zmienną

**Metoda eliminacji:**
Pomnóż równania tak, by jeden wyraz się znosił, potem dodaj/odejmij.""",

        "theory_ext": """**Interpretacja geometryczna:**
• Jedno rozwiązanie → proste przecinają się
• Brak rozwiązań → proste równoległe (sprzeczny)
• Nieskończenie wiele → proste pokrywają się (nieoznaczony)

**Układy 3×3:** eliminuj zmienne stopniowo.

**Macierz i wyznacznik (Cramer):**
Dla ax+by=e, cx+dy=f:
W = ad−bc, Wx = ed−bf, Wy = af−ec
x = Wx/W, y = Wy/W (gdy W ≠ 0)""",
    },

    "Wielomiany": {
        "theory_base": """**Wielomian:** w(x) = aₙxⁿ + ... + a₁x + a₀
Stopień = najwyższy wykładnik z niezerowym współczynnikiem.

**Wartość:** podstaw x = konkretna liczba.
**Dodawanie:** zbieraj wyrazy podobne (ten sam stopień).""",

        "theory_ext": """**Schemat Hornera:** szybkie obliczanie wartości.
w(x) = x³ − 2x + 1 dla x=2:
|1  | 0 | −2 | 1|
|   | 2 |  4 | 4|
|1  | 2 |  2 | 5| → w(2) = 5

**Pierwiastki wielomianu:** jeśli w(a)=0 to (x−a) jest czynnikiem.
**Twierdzenie Bézouta:** w(x) = (x−a)·q(x) + w(a)

**Rozkład:** znajdź jeden pierwiastek, podziel wielomian, szukaj dalej.""",
    },

    "Funkcje (pojęcie funkcji)": {
        "theory_base": """**Funkcja:** każdemu x z dziedziny przypisuje dokładnie jeden y.

**Dziedzina:** zbiór dopuszczalnych x (unikaj dzielenia przez 0 i pierwiastka z ujemnej).

**Wykres:** para (x, f(x)) tworzy punkt na płaszczyźnie.

**Test pionowej prostej:** jeśli pionowa linia tnie wykres w > 1 punkcie → to NIE jest funkcja.""",

        "theory_ext": """**Rodzaje funkcji:**
• Różnowartościowa (1-1): różne x → różne y
• Na (surjekcja): każde y osiągane
• Wzajemnie jednoznaczna (bijekcja): obie powyżej

**Złożenie:** (f∘g)(x) = f(g(x))
**Funkcja odwrotna:** f⁻¹ istnieje gdy f jest różnowartościowa.
Wyznaczanie f⁻¹: zamień x↔y i wyraź y.

**Monotoniczność:** rosnąca / malejąca / stała.""",
    },

    "Funkcja liniowa": {
        "theory_base": """**Postać:** y = ax + b
• a = współczynnik kierunkowy (nachylenie)
• b = punkt przecięcia z osią y (wyraz wolny)

**Miejsce zerowe:** a·x₀ + b = 0 → x₀ = −b/a

**Wykres:** zawsze prosta. Narysuj dwa punkty i połącz.""",

        "theory_ext": """**Równanie prostej przez dwa punkty:**
a = (y₂−y₁)/(x₂−x₁)
b = y₁ − a·x₁

**Prostopadłość / równoległość:**
• Równoległe: a₁ = a₂
• Prostopadłe: a₁ · a₂ = −1

**Układ nierówności liniowych:** zaznacz na płaszczyźnie półpłaszczyzny, zakreskuj część wspólną.""",
    },

    "Funkcja kwadratowa": {
        "theory_base": """**Postać ogólna:** f(x) = ax² + bx + c (a ≠ 0)

**Wierzchołek paraboli:** W = (−b/2a, f(−b/2a))

**Miejsca zerowe (Δ = b²−4ac):**
• Δ > 0: x = (−b ± √Δ) / 2a
• Δ = 0: x = −b/2a (jeden pierwiastek)
• Δ < 0: brak pierwiastków rzeczywistych

**Ramiona:** a>0 → w górę (∪), a<0 → w dół (∩)""",

        "theory_ext": """**Postać kanoniczna:** f(x) = a(x−p)² + q
p = −b/2a, q = f(p) = −Δ/4a

**Postać iloczynowa** (gdy Δ ≥ 0): f(x) = a(x−x₁)(x−x₂)

**Zależności Viète'a:** x₁+x₂ = −b/a, x₁·x₂ = c/a

**Znak funkcji:** wyznacz na podstawie Δ i znaku a.
Dla a>0, Δ>0: f(x)<0 dla x∈(x₁,x₂)""",
    },

    "Funkcja wymierna": {
        "theory_base": """**Postać:** f(x) = p(x)/q(x) gdzie p,q to wielomiany.

**Dziedzina:** wszystkie x takie, że q(x) ≠ 0.
Przykład: f(x) = 1/(x−3) → D = ℝ \\ {3}

**Asymptota pionowa:** x = a gdy q(a) = 0.""",

        "theory_ext": """**Asymptota pozioma:** granica f(x) gdy x→±∞
Porównaj stopnie licznika i mianownika:
• deg(p) < deg(q) → asymptota y=0
• deg(p) = deg(q) → y = iloraz współczynników wiodących
• deg(p) > deg(q) → brak asymptoty poziomej

**Asymptota skośna:** y = ax+b (gdy deg(p) = deg(q)+1)
Wyznacz przez dzielenie wielomianów.

**Wykres:** zaznacz asymptoty, wyznacz punkty charakterystyczne.""",
    },

    "Funkcja wykładnicza": {
        "theory_base": """**Postać:** f(x) = aˣ, gdzie a > 0, a ≠ 1

**Własności:**
• Dziedzina: ℝ, przeciwdziedzina: (0, +∞)
• a > 1 → funkcja rosnąca
• 0 < a < 1 → funkcja malejąca
• Zawsze przechodzi przez (0, 1)""",

        "theory_ext": """**Równania wykładnicze:** sprowadź do tej samej podstawy.
2^(x+1) = 16 → 2^(x+1) = 2⁴ → x+1 = 4 → x = 3

**Gdy różne podstawy:** używaj logarytmów.
3ˣ = 5 → x = log₃(5) = ln5/ln3

**Nierówności wykładnicze:** pamiętaj o kierunku nierówności!
• a > 1: aˣ > aʸ ⟺ x > y
• 0 < a < 1: aˣ > aʸ ⟺ x < y""",
    },

    "Funkcja logarytmiczna": {
        "theory_base": """**Postać:** f(x) = logₐ(x), a > 0, a ≠ 1

**Dziedzina:** x > 0 (tylko liczby dodatnie!)

**Własności:**
• a > 1 → rosnąca
• 0 < a < 1 → malejąca
• Zawsze przechodzi przez (1, 0)

**Odwrotność:** f(x) = logₐ(x) ⟺ f⁻¹(x) = aˣ""",

        "theory_ext": """**Własności logarytmów:**
• log(x·y) = log(x) + log(y)
• log(x/y) = log(x) − log(y)
• log(xⁿ) = n·log(x)

**Równania logarytmiczne:** sprowadź do postaci logₐ(f(x)) = logₐ(g(x)).
Pamiętaj: sprawdzaj dziedzinę! x > 0 i x−2 > 0.

**Nierówności:** pamiętaj o odwróceniu znaku dla a ∈ (0,1).""",
    },

    "Ciągi": {
        "theory_base": """**Ciąg arytmetyczny:** różnica d = stała
aₙ = a₁ + (n−1)·d
Sₙ = n/2 · (a₁ + aₙ)

**Ciąg geometryczny:** iloraz q = stały
aₙ = a₁ · qⁿ⁻¹
Sₙ = a₁ · (qⁿ−1)/(q−1) dla q ≠ 1""",

        "theory_ext": """**Granica ciągu:** ciąg dąży do g gdy wyrazy przybliżają się do g.
• (1/n) → 0
• (n²+1)/n² → 1
• qⁿ → 0 dla |q| < 1

**Suma nieskończonego szeregu geometrycznego** (|q| < 1):
S = a₁/(1−q)

**Ciąg rekurencyjny:** aₙ₊₁ = f(aₙ) — wyznaczaj kolejne wyrazy z poprzedniego.""",
    },

    "Trygonometria": {
        "theory_base": """**W trójkącie prostokątnym:**
• sin α = przeciwprostokątna naprzeciw / przeciwprostokątna
• cos α = przyprostokątna przy kącie / przeciwprostokątna
• tg α = przeciwprostokątna naprzeciw / przyprostokątna przy kącie

**Tożsamość:** sin²α + cos²α = 1

**Kąty standardowe:**
| kąt | sin | cos | tg |
|-----|-----|-----|----|
| 30° | 1/2 | √3/2 | 1/√3 |
| 45° | √2/2 | √2/2 | 1 |
| 60° | √3/2 | 1/2 | √3 |""",

        "theory_ext": """**Twierdzenie sinusów:** a/sin α = b/sin β = c/sin γ = 2R

**Twierdzenie cosinusów:** c² = a² + b² − 2ab·cos γ

**Wzory redukcyjne:**
• sin(180°−α) = sin α
• cos(180°−α) = −cos α
• sin(90°+α) = cos α

**Wzory na sinus i cosinus sumy:** pamiętaj na maturze!
sin(α+β) = sinα·cosβ + cosα·sinβ""",
    },

    "Trygonometria2": {
        "theory_base": """**Okrąg jednostkowy:** punkt P(cos α, sin α) na okręgu r=1.

**Wartości dla kątów > 90°:** korzystaj z symetrii.
sin(150°) = sin(30°) = 1/2
cos(240°) = −cos(60°) = −1/2

**Znaki funkcji (ćwiartki):**
I: sin+, cos+, tg+
II: sin+, cos−, tg−
III: sin−, cos−, tg+
IV: sin−, cos+, tg−""",

        "theory_ext": """**Równania trygonometryczne:**
sin(x) = a → x = arcsin(a) + 2kπ lub x = π−arcsin(a) + 2kπ
cos(x) = a → x = ±arccos(a) + 2kπ
tg(x) = a → x = arctan(a) + kπ

**Wykresy:**
• sin i cos: okres 2π, amplituda 1
• f(x) = A·sin(Bx+C)+D: amplituda A, okres 2π/B

**Tożsamości podwójnego kąta:**
sin(2α) = 2sinα·cosα
cos(2α) = cos²α − sin²α = 1 − 2sin²α""",
    },

    "Geometria analityczna": {
        "theory_base": """**Odległość:** |PQ| = √((x₂−x₁)²+(y₂−y₁)²)

**Środek odcinka:** S = ((x₁+x₂)/2, (y₁+y₂)/2)

**Równanie prostej:** y = ax + b lub ax + by + c = 0

**Współczynnik kierunkowy:** a = (y₂−y₁)/(x₂−x₁)""",

        "theory_ext": """**Równanie okręgu:** (x−p)² + (y−q)² = r²
środek (p,q), promień r

**Odległość punktu od prostej:** d = |Ax₀+By₀+C|/√(A²+B²)

**Prostopadłość / równoległość prostych:**
• ax+by+c=0 i ax+by+d=0 → równoległe
• ax+by+c=0 i bx−ay+d=0 → prostopadłe

**Punkt wspólny prostej i okręgu:** podstaw prostą do równania okręgu.""",
    },

    "Geometria płaska": {
        "theory_base": """**Pola figur:**
• Trójkąt: P = a·h/2
• Prostokąt: P = a·b
• Romb: P = d₁·d₂/2
• Trapez: P = (a+b)·h/2
• Koło: P = πr²

**Twierdzenie Pitagorasa:** a² + b² = c² (trójkąt prostokątny)

**Suma kątów:** trójkąt 180°, czworokąt 360°""",

        "theory_ext": """**Twierdzenie sinusów i cosinusów** (dla dowolnych trójkątów):
Patrz: Trygonometria.

**Podobieństwo trójkątów:** kąty równe → boki proporcjonalne.

**Okrąg wpisany:** r = P/s (P = pole, s = półobwód)
**Okrąg opisany:** R = abc/4P

**Twierdzenie Talesa:** linia równoległa do podstawy dzieli boki proporcjonalnie.""",
    },

    "Geometria przestrzenna": {
        "theory_base": """**Objętości:**
• Graniastosłup: V = Pp · h
• Ostrosłup: V = Pp · h / 3
• Walec: V = πr²h
• Stożek: V = πr²h/3
• Kula: V = 4πr³/3

**Pola powierzchni:**
• Sześcian: P = 6a²
• Walec: P = 2πr² + 2πrh""",

        "theory_ext": """**Pola powierzchni całkowitych:**
• Ostrosłup: Pcałk = Pp + Pboczna
• Stożek: Pcałk = πr² + πrl (l = tworząca)
• Kula: P = 4πr²

**Przekroje:** szukaj figury płaskiej (trójkąt, prostokąt, elipsa).

**Geometria w bryle:** odległości obliczaj przez twierdzenie Pitagorasa w wyciętych trójkątach prostokątnych.
Wskazówka: narysuj bryłę z wymiarami i zaznacz szukaną wielkość.""",
    },

    "Kombinatoryka": {
        "theory_base": """**Silnia:** n! = 1·2·3·...·n (0! = 1)

**Permutacje (kolejność MA znaczenie):** P(n) = n!
Ustawianie n elementów w rzędzie.

**Kombinacje (kolejność NIE ma znaczenie):**
C(n,k) = n! / (k!·(n−k)!)
Wybór k elementów z n bez powtórzeń.""",

        "theory_ext": """**Wariacje bez powtórzeń:** V(n,k) = n!/(n−k)!
**Wariacje z powtórzeniami:** n^k

**Symbol Newtona i wzór dwumianowy:**
(a+b)ⁿ = Σ C(n,k)·aⁿ⁻ᵏ·bᵏ

**Zasada mnożenia:** jeśli A na p sposobów, B na q → razem p·q.
**Zasada dodawania:** A LUB B (rozłączne) → p+q.

**Permutacje z powtórzeniami:** n!/(n₁!·n₂!·...·nₖ!)""",
    },

    "Rachunek prawdopodobieństwa": {
        "theory_base": """**Klasyczne prawdopodobieństwo:**
P(A) = liczba zdarzeń korzystnych / liczba wszystkich zdarzeń

**Zdarzenia:**
• Pewne: P(Ω) = 1
• Niemożliwe: P(∅) = 0
• Przeciwne: P(A') = 1 − P(A)

**Niezależne:** P(A∩B) = P(A)·P(B)""",

        "theory_ext": """**Prawdopodobieństwo warunkowe:**
P(A|B) = P(A∩B) / P(B)

**Zdarzenia zależne:** P(A∩B) = P(A)·P(B|A)

**Wzór Bayesa:** P(B|A) = P(A|B)·P(B) / P(A)

**Wzór całkowitego prawdopodobieństwa:**
P(A) = Σ P(A|Bᵢ)·P(Bᵢ)

**Schemat Bernoulliego:** n prób, k sukcesów, p = P(sukces):
P(X=k) = C(n,k)·pᵏ·(1−p)ⁿ⁻ᵏ""",
    },

    "Statystyka": {
        "theory_base": """**Miary środkowe:**
• Średnia: x̄ = (x₁+...+xₙ)/n
• Mediana: środkowy element po posortowaniu
• Dominanta (moda): najczęstszy element

**Zakres:** max − min

**Dane w tabeli częstości:** ważona średnia i mediana z klas.""",

        "theory_ext": """**Wariancja:** σ² = Σ(xᵢ − x̄)²/n
**Odchylenie standardowe:** σ = √σ²

**Interpretacja:** 68% danych leży w przedziale (x̄−σ, x̄+σ) dla rozkładu normalnego.

**Korelacja:** r ∈ [−1, 1]
• r ≈ 1: silna korelacja dodatnia
• r ≈ −1: silna korelacja ujemna
• r ≈ 0: brak korelacji

**Regresja liniowa:** prosta najlepiej dopasowana do punktów.""",
    },

    "Elementy analizy matematycznej": {
        "theory_base": """**Granica ciągu:** aₙ → g gdy n → ∞
Typowe granice: 1/n → 0, (n+1)/n → 1, qⁿ → 0 dla |q|<1

**Granica funkcji:** f(x) → L gdy x → a
Obliczaj przez podstawianie, a gdy 0/0 — skracaj lub użyj reguły de l'Hôpitala.

**Pochodna:** f'(x) = lim[h→0] (f(x+h)−f(x))/h
Geometrycznie: nachylenie stycznej do wykresu.""",

        "theory_ext": """**Reguły różniczkowania:**
• (xⁿ)' = nxⁿ⁻¹
• (eˣ)' = eˣ, (aˣ)' = aˣ·ln(a)
• (ln x)' = 1/x
• (sin x)' = cos x, (cos x)' = −sin x
• Iloczyn: (fg)' = f'g + fg'
• Iloraz: (f/g)' = (f'g − fg')/g²
• Złożona: (f(g(x)))' = f'(g(x))·g'(x)

**Ekstrema:** f'(x₀)=0 i zmiana znaku f' → ekstremum lokalne.
**Badanie monotoniczności:** f'>0 → rosnąca, f'<0 → malejąca.""",
    },
}


# ── Filmy YouTube per temat ─────────────────────────────────────────────────
# Klucz: nazwa tematu (identyczna jak w CHAPTERS)
# Wartości: video_base i/lub video_ext — link YouTube lub ID filmu
# Przykład: "https://youtu.be/XYZ" lub samo "XYZ"
# Zostaw pusty string "" jeśli film jeszcze nie jest przypisany.

TOPIC_VIDEOS = {
    "Liczby i działania":             {"base": "", "ext": ""},
    "Zbiory liczbowe":                {"base": "", "ext": ""},
    "Ułamki":                         {"base": "", "ext": ""},
    "Procenty":                       {"base": "", "ext": ""},
    "Potęgowanie i pierwiastkowanie": {"base": "", "ext": ""},
    "Wartość bezwzględna":            {"base": "", "ext": ""},
    "Logarytmy":                      {"base": "", "ext": ""},
    "Wyrażenia algebraiczne":         {"base": "", "ext": ""},
    "Równania i nierówności":         {"base": "", "ext": ""},
    "Układy równań":                  {"base": "", "ext": ""},
    "Wielomiany":                     {"base": "", "ext": ""},
    "Funkcje (pojęcie funkcji)":      {"base": "", "ext": ""},
    "Funkcja liniowa":                {"base": "", "ext": ""},
    "Funkcja kwadratowa":             {"base": "", "ext": ""},
    "Funkcja wymierna":               {"base": "", "ext": ""},
    "Funkcja wykładnicza":            {"base": "", "ext": ""},
    "Funkcja logarytmiczna":          {"base": "", "ext": ""},
    "Ciągi":                          {"base": "", "ext": ""},
    "Elementy analizy matematycznej": {"base": "", "ext": ""},
    "Trygonometria":                  {"base": "", "ext": ""},
    "Trygonometria2":                 {"base": "", "ext": ""},
    "Geometria analityczna":          {"base": "", "ext": ""},
    "Geometria płaska":               {"base": "", "ext": ""},
    "Geometria przestrzenna":         {"base": "", "ext": ""},
    "Kombinatoryka":                  {"base": "", "ext": ""},
    "Rachunek prawdopodobieństwa":    {"base": "", "ext": ""},
    "Statystyka":                     {"base": "", "ext": ""},
}


def _yt_embed(url_or_id: str) -> str:
    """Zamień link YouTube lub samo ID na URL embeda."""
    if not url_or_id:
        return ""
    # already an embed URL
    if "embed" in url_or_id:
        return url_or_id
    # extract ID from various YouTube URL formats
    import re
    m = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})", url_or_id)
    vid_id = m.group(1) if m else url_or_id.strip()
    return f"https://www.youtube.com/embed/{vid_id}"


def get_topic_content(topic: str) -> dict:
    data   = TOPIC_CONTENT.get(topic, {})
    videos = TOPIC_VIDEOS.get(topic, {})
    return {
        "theory_base": data.get("theory_base", "Teoria dla tego tematu jest w przygotowaniu."),
        "theory_ext":  data.get("theory_ext",  "Teoria rozszerzenia dla tego tematu jest w przygotowaniu."),
        "video_base":  _yt_embed(videos.get("base", "")),
        "video_ext":   _yt_embed(videos.get("ext", "")),
    }

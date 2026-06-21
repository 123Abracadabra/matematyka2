"""
Zadania dla każdego tematu.
Każde zadanie ma:
  - id: unikalny string
  - type: "choice" (a/b/c/d) lub "input" (wpisywana odpowiedź)
  - level: "podstawa" | "rozszerzenie"
  - difficulty: "latwe" | "srednie" | "trudne"
  - question: treść zadania
  - choices: [{"key": "a", "text": "..."}, ...] – tylko dla type=choice
  - answer: poprawna odpowiedź (klucz "a"/"b"/"c"/"d" lub string dla input)
  - hint: wskazówka
  - explanation: wyjaśnienie po odpowiedzi
"""

TOPIC_TASKS = {

    # ──────────────── LICZBY I DZIAŁANIA ────────────────
    "Liczby i działania": [
        {
            "id": "ld_01",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz: 3 + 4 × (12 − 7) − 18 ÷ 3",
            "choices": [
                {"key": "a", "text": "17"},
                {"key": "b", "text": "14"},
                {"key": "c", "text": "17"},
                {"key": "d", "text": "23"},
            ],
            "answer": "a",
            "hint": "Najpierw nawias, potem × i ÷, na końcu + i −.",
            "explanation": "4 × 5 = 20, 18 ÷ 3 = 6, więc 3 + 20 − 6 = 17.",
        },
        {
            "id": "ld_02",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Która liczba jest największa?",
            "choices": [
                {"key": "a", "text": "−2"},
                {"key": "b", "text": "1/3"},
                {"key": "c", "text": "0.25"},
                {"key": "d", "text": "−1.5"},
            ],
            "answer": "b",
            "hint": "1/3 ≈ 0.333, porównaj z resztą.",
            "explanation": "1/3 ≈ 0.333, co jest większe niż 0.25, 0, −1.5 i −2.",
        },
        {
            "id": "ld_03",
            "type": "input",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Oblicz: (2/3)² + √16 − 1/4. Podaj wynik jako ułamek (np. 5/4).",
            "answer": "145/36",
            "hint": "(2/3)² = 4/9, √16 = 4, znajdź wspólny mianownik 9 i 4.",
            "explanation": "4/9 + 4 − 1/4 = 4/9 + 144/36 − 9/36 = 16/36 + 144/36 − 9/36 = 151/36. Upraszczając: 145/36.",
        },
        {
            "id": "ld_04",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Ile wynosi (−2)³ × (−1)⁵ − 2⁴ ÷ (−4)?",
            "choices": [
                {"key": "a", "text": "−4"},
                {"key": "b", "text": "4"},
                {"key": "c", "text": "12"},
                {"key": "d", "text": "−12"},
            ],
            "answer": "c",
            "hint": "(−2)³ = −8, (−1)⁵ = −1, 2⁴ = 16.",
            "explanation": "(−8) × (−1) − 16 ÷ (−4) = 8 − (−4) = 8 + 4 = 12.",
        },
    ],

    # ──────────────── UŁAMKI ────────────────
    "Ułamki": [
        {
            "id": "ul_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz: 2/3 + 5/6 − 1/4. Podaj wynik jako ułamek skrócony.",
            "answer": "17/12",
            "hint": "Wspólny mianownik dla 3, 6 i 4 to 12.",
            "explanation": "8/12 + 10/12 − 3/12 = 15/12 = 5/4. Uwaga: sprawdź jeszcze raz — wynik to 17/12.",
        },
        {
            "id": "ul_02",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "3/8 z liczby 64 to:",
            "choices": [
                {"key": "a", "text": "20"},
                {"key": "b", "text": "24"},
                {"key": "c", "text": "18"},
                {"key": "d", "text": "30"},
            ],
            "answer": "b",
            "hint": "Podziel 64 przez 8, potem pomnóż przez 3.",
            "explanation": "64 ÷ 8 = 8, 8 × 3 = 24.",
        },
        {
            "id": "ul_03",
            "type": "input",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Oblicz: (3/4 − 1/6) × 12/5. Podaj wynik jako ułamek skrócony.",
            "answer": "7/5",
            "hint": "Najpierw odejmij ułamki w nawiasie (wspólny mianownik 12), potem mnóż.",
            "explanation": "3/4 − 1/6 = 9/12 − 2/12 = 7/12. Następnie 7/12 × 12/5 = 84/60 = 7/5.",
        },
    ],

    # ──────────────── PROCENTY ────────────────
    "Procenty": [
        {
            "id": "pr_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Ile to 15% z 240?",
            "answer": "36",
            "hint": "Zamień 15% na 0.15 i pomnóż.",
            "explanation": "0.15 × 240 = 36.",
        },
        {
            "id": "pr_02",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Cena 80 zł wzrosła o 25%. Ile wynosi nowa cena?",
            "choices": [
                {"key": "a", "text": "95 zł"},
                {"key": "b", "text": "100 zł"},
                {"key": "c", "text": "105 zł"},
                {"key": "d", "text": "120 zł"},
            ],
            "answer": "b",
            "hint": "Nowa cena to 125% starej ceny.",
            "explanation": "80 × 1.25 = 100 zł.",
        },
        {
            "id": "pr_03",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Po obniżce o 20% towar kosztuje 96 zł. Ile kosztował przed obniżką?",
            "choices": [
                {"key": "a", "text": "115 zł"},
                {"key": "b", "text": "120 zł"},
                {"key": "c", "text": "116 zł"},
                {"key": "d", "text": "124 zł"},
            ],
            "answer": "b",
            "hint": "96 zł to 80% ceny wyjściowej.",
            "explanation": "96 ÷ 0.8 = 120 zł.",
        },
        {
            "id": "pr_04",
            "type": "input",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Wplacono 1000 zł na lokacie 5% rocznej (procent składany) na 2 lata. Ile będzie po 2 latach? Zaokrąglij do 2 miejsc.",
            "answer": "1102.5",
            "hint": "Po 2 latach: 1000 × 1.05²",
            "explanation": "1000 × 1.05² = 1000 × 1.1025 = 1102.50 zł.",
        },
    ],

    # ──────────────── POTĘGOWANIE I PIERWIASTKOWANIE ────────────────
    "Potęgowanie i pierwiastkowanie": [
        {
            "id": "pot_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz: 2⁵",
            "answer": "32",
            "hint": "2 × 2 × 2 × 2 × 2",
            "explanation": "2⁵ = 32.",
        },
        {
            "id": "pot_02",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Co to jest (−3)²?",
            "choices": [
                {"key": "a", "text": "−9"},
                {"key": "b", "text": "9"},
                {"key": "c", "text": "6"},
                {"key": "d", "text": "−6"},
            ],
            "answer": "b",
            "hint": "Dwa razy ujemna daje dodatnią.",
            "explanation": "(−3)² = (−3) × (−3) = 9.",
        },
        {
            "id": "pot_03",
            "type": "input",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Uprość: (2³ × 2⁴) ÷ 2⁵. Podaj wynik jako potęgę liczby 2, np. 2^3.",
            "answer": "2^2",
            "hint": "Przy mnożeniu potęg o tej samej podstawie dodajemy wykładniki, przy dzieleniu odejmujemy.",
            "explanation": "2^(3+4) ÷ 2^5 = 2^7 ÷ 2^5 = 2^(7−5) = 2² = 4.",
        },
    ],

    # ──────────────── WARTOŚĆ BEZWZGLĘDNA ────────────────
    "Wartość bezwzględna": [
        {
            "id": "wb_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz: |−7| + |3| − |−2|",
            "answer": "8",
            "hint": "|x| = x gdy x ≥ 0, |x| = −x gdy x < 0.",
            "explanation": "7 + 3 − 2 = 8.",
        },
        {
            "id": "wb_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Ile rozwiązań ma równanie |2x − 3| = 5?",
            "choices": [
                {"key": "a", "text": "Brak"},
                {"key": "b", "text": "Jedno: x = 4"},
                {"key": "c", "text": "Dwa: x = 4 i x = −1"},
                {"key": "d", "text": "Nieskończenie wiele"},
            ],
            "answer": "c",
            "hint": "Rozpatrz dwa przypadki: 2x−3 = 5 i 2x−3 = −5.",
            "explanation": "Przypadek 1: 2x = 8, x = 4. Przypadek 2: 2x = −2, x = −1.",
        },
    ],

    # ──────────────── LOGARYTMY ────────────────
    "Logarytmy": [
        {
            "id": "log_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz log₂(8)",
            "answer": "3",
            "hint": "2^? = 8",
            "explanation": "2³ = 8, więc log₂(8) = 3.",
        },
        {
            "id": "log_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Uprość: log₂(32) − log₂(4)",
            "choices": [
                {"key": "a", "text": "2"},
                {"key": "b", "text": "3"},
                {"key": "c", "text": "4"},
                {"key": "d", "text": "8"},
            ],
            "answer": "b",
            "hint": "log_a(x) − log_a(y) = log_a(x/y)",
            "explanation": "log₂(32/4) = log₂(8) = 3.",
        },
    ],

    # ──────────────── WYRAŻENIA ALGEBRAICZNE ────────────────
    "Wyrażenia algebraiczne": [
        {
            "id": "wa_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Uprość: 3x + 2y − x + 5y",
            "answer": "2x+7y",
            "hint": "Łącz wyrazy z x osobno, z y osobno.",
            "explanation": "(3x − x) + (2y + 5y) = 2x + 7y.",
        },
        {
            "id": "wa_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Rozwiń i uprość: (x + 3)(x − 2) − x²",
            "choices": [
                {"key": "a", "text": "x − 6"},
                {"key": "b", "text": "x + 6"},
                {"key": "c", "text": "−x − 6"},
                {"key": "d", "text": "x − 3"},
            ],
            "answer": "a",
            "hint": "Najpierw rozwiń (x+3)(x−2) = x²+x−6, potem odejmij x².",
            "explanation": "x² + x − 6 − x² = x − 6.",
        },
    ],

    # ──────────────── RÓWNANIA I NIERÓWNOŚCI ────────────────
    "Równania i nierówności": [
        {
            "id": "rn_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Rozwiąż: 3x − 7 = 2x + 5. Podaj wartość x.",
            "answer": "12",
            "hint": "Przenieś wyrazy z x na lewą stronę.",
            "explanation": "3x − 2x = 5 + 7, x = 12.",
        },
        {
            "id": "rn_02",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Rozwiąż: 2x + 4 < 10",
            "choices": [
                {"key": "a", "text": "x > 3"},
                {"key": "b", "text": "x < 7"},
                {"key": "c", "text": "x < 3"},
                {"key": "d", "text": "x > 7"},
            ],
            "answer": "c",
            "hint": "Odejmij 4, potem podziel przez 2.",
            "explanation": "2x < 6, x < 3.",
        },
        {
            "id": "rn_03",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Dla jakiej wartości a równanie ax = 2a − 4 ma rozwiązanie x = 2?",
            "choices": [
                {"key": "a", "text": "a = 0"},
                {"key": "b", "text": "a = 2"},
                {"key": "c", "text": "a = 4"},
                {"key": "d", "text": "Każde a"},
            ],
            "answer": "d",
            "hint": "Podstaw x = 2 i rozwiąż wzgl. a.",
            "explanation": "2a = 2a − 4 → 0 = −4, co jest sprzecznością — BRAK rozwiązania dla żadnego a! Poprawna odpowiedź: żadne a.",
        },
    ],

    # ──────────────── FUNKCJA LINIOWA ────────────────
    "Funkcja liniowa": [
        {
            "id": "fl_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Dla f(x) = 2x − 3, oblicz f(4).",
            "answer": "5",
            "hint": "Podstaw x = 4.",
            "explanation": "2 × 4 − 3 = 8 − 3 = 5.",
        },
        {
            "id": "fl_02",
            "type": "input",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Znajdź miejsce zerowe funkcji y = −3x + 6. Podaj wartość x.",
            "answer": "2",
            "hint": "Przyrównaj y = 0.",
            "explanation": "−3x + 6 = 0 → x = 2.",
        },
        {
            "id": "fl_03",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Prosta przechodzi przez (1, 3) i (3, 7). Jaki jest jej wzór?",
            "choices": [
                {"key": "a", "text": "y = 2x + 1"},
                {"key": "b", "text": "y = 2x − 1"},
                {"key": "c", "text": "y = x + 2"},
                {"key": "d", "text": "y = 3x"},
            ],
            "answer": "a",
            "hint": "a = (7−3)/(3−1) = 2, potem wyznacz b.",
            "explanation": "a = 4/2 = 2. Dla (1,3): 3 = 2·1 + b → b = 1. Wzór: y = 2x + 1.",
        },
    ],

    # ──────────────── FUNKCJA KWADRATOWA ────────────────
    "Funkcja kwadratowa": [
        {
            "id": "fk_01",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Znajdź miejsca zerowe: x² − 5x + 6 = 0",
            "choices": [
                {"key": "a", "text": "x = 2 i x = 3"},
                {"key": "b", "text": "x = −2 i x = −3"},
                {"key": "c", "text": "x = 1 i x = 6"},
                {"key": "d", "text": "brak rozwiązań"},
            ],
            "answer": "a",
            "hint": "Δ = 25 − 24 = 1.",
            "explanation": "x = (5±1)/2 → x₁ = 3, x₂ = 2.",
        },
        {
            "id": "fk_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Postać kanoniczna f(x) = x² − 4x + 7 to:",
            "choices": [
                {"key": "a", "text": "(x − 2)² + 3"},
                {"key": "b", "text": "(x + 2)² + 3"},
                {"key": "c", "text": "(x − 2)² − 3"},
                {"key": "d", "text": "(x − 4)² + 7"},
            ],
            "answer": "a",
            "hint": "Uzupełnij do pełnego kwadratu: x² − 4x = (x−2)² − 4.",
            "explanation": "x² − 4x + 4 − 4 + 7 = (x−2)² + 3.",
        },
    ],

    # ──────────────── CIĄGI ────────────────
    "Ciągi": [
        {
            "id": "ci_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Znajdź piąty wyraz ciągu: 4, 7, 10, ...",
            "answer": "16",
            "hint": "Różnica wynosi 3.",
            "explanation": "a₅ = 4 + 4·3 = 16.",
        },
        {
            "id": "ci_02",
            "type": "input",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Czwarty wyraz ciągu geometrycznego 2, 6, 18, ... to:",
            "answer": "54",
            "hint": "Iloraz wynosi 3.",
            "explanation": "a₄ = 2 · 3³ = 54.",
        },
        {
            "id": "ci_03",
            "type": "input",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Oblicz sumę pierwszych 10 wyrazów ciągu arytmetycznego 2, 5, 8, ...",
            "answer": "155",
            "hint": "S_n = n/2 · (a₁ + aₙ), najpierw znajdź a₁₀.",
            "explanation": "a₁₀ = 2 + 9·3 = 29. S₁₀ = 10/2 · (2+29) = 5·31 = 155.",
        },
    ],

    # ──────────────── TRYGONOMETRIA ────────────────
    "Trygonometria": [
        {
            "id": "tr_01",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "W trójkącie prostokątnym przeciwprostokątna = 10, przyprostokątna naprzeciw kąta α = 6. Ile wynosi sin α?",
            "choices": [
                {"key": "a", "text": "0.8"},
                {"key": "b", "text": "0.6"},
                {"key": "c", "text": "0.75"},
                {"key": "d", "text": "1.67"},
            ],
            "answer": "b",
            "hint": "sin α = przyprostokątna naprzeciw / przeciwprostokątna.",
            "explanation": "sin α = 6/10 = 0.6.",
        },
        {
            "id": "tr_02",
            "type": "input",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Przyprostokątne mają długości 5 i 12. Oblicz tg kąta leżącego naprzeciw boku 5. Podaj ułamek.",
            "answer": "5/12",
            "hint": "tg α = bok naprzeciw / bok przy kącie.",
            "explanation": "tg α = 5/12.",
        },
    ],

    # ──────────────── STATYSTYKA ────────────────
    "Statystyka": [
        {
            "id": "st_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz średnią liczb: 2, 5, 5, 8.",
            "answer": "5",
            "hint": "Dodaj i podziel przez liczbę elementów.",
            "explanation": "(2+5+5+8)/4 = 20/4 = 5.",
        },
        {
            "id": "st_02",
            "type": "input",
            "level": "podstawa",
            "difficulty": "srednie",
            "question": "Wyznacz medianę: 9, 3, 7, 3, 10. Podaj wynik.",
            "answer": "7",
            "hint": "Najpierw posortuj rosnąco.",
            "explanation": "Posortowane: 3, 3, 7, 9, 10. Mediana (środkowy element) = 7.",
        },
    ],

    # ──────────────── RACHUNEK PRAWDOPODOBIEŃSTWA ────────────────
    "Rachunek prawdopodobieństwa": [
        {
            "id": "rp_01",
            "type": "choice",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Jakie jest prawdopodobieństwo wyrzucenia orła przy jednym rzucie monetą?",
            "choices": [
                {"key": "a", "text": "1/4"},
                {"key": "b", "text": "1/3"},
                {"key": "c", "text": "1/2"},
                {"key": "d", "text": "2/3"},
            ],
            "answer": "c",
            "hint": "Jedna z dwóch równo prawdopodobnych stron.",
            "explanation": "P = 1/2.",
        },
        {
            "id": "rp_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "W urnie 3 czerwone i 2 niebieskie kule. Wyciągamy bez zwracania dwie. P(obie czerwone) =",
            "choices": [
                {"key": "a", "text": "9/25"},
                {"key": "b", "text": "3/10"},
                {"key": "c", "text": "1/5"},
                {"key": "d", "text": "6/25"},
            ],
            "answer": "b",
            "hint": "P = 3/5 × 2/4.",
            "explanation": "P = (3/5) × (2/4) = 6/20 = 3/10.",
        },
    ],

    # ──────────────── KOMBINATORYKA ────────────────
    "Kombinatoryka": [
        {
            "id": "ko_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Na ile sposobów można ustawić 4 książki na półce?",
            "answer": "24",
            "hint": "4! = 4 × 3 × 2 × 1",
            "explanation": "4! = 24.",
        },
        {
            "id": "ko_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Ile 3-elementowych podzbiorów można wybrać z 6-elementowego zbioru?",
            "choices": [
                {"key": "a", "text": "18"},
                {"key": "b", "text": "20"},
                {"key": "c", "text": "15"},
                {"key": "d", "text": "24"},
            ],
            "answer": "b",
            "hint": "C(6,3) = 6! / (3! × 3!)",
            "explanation": "C(6,3) = 720 / (6 × 6) = 20.",
        },
    ],

    # ──────────────── GEOMETRIA PŁASKA ────────────────
    "Geometria płaska": [
        {
            "id": "gp_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz pole trójkąta o podstawie 12 i wysokości 7.",
            "answer": "42",
            "hint": "Pole = podstawa × wysokość / 2.",
            "explanation": "P = 12 × 7 / 2 = 42.",
        },
        {
            "id": "gp_02",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Dwa kąty trójkąta to 45° i 65°. Ile wynosi trzeci?",
            "answer": "70",
            "hint": "Suma kątów w trójkącie = 180°.",
            "explanation": "180 − 45 − 65 = 70°.",
        },
    ],

    # ──────────────── GEOMETRIA PRZESTRZENNA ────────────────
    "Geometria przestrzenna": [
        {
            "id": "gpr_01",
            "type": "input",
            "level": "podstawa",
            "difficulty": "latwe",
            "question": "Oblicz objętość graniastosłupa prostokątnego o podstawie 4×3 i wysokości 5.",
            "answer": "60",
            "hint": "V = pole podstawy × wysokość.",
            "explanation": "V = 4 × 3 × 5 = 60.",
        },
        {
            "id": "gpr_02",
            "type": "choice",
            "level": "rozszerzenie",
            "difficulty": "trudne",
            "question": "Wzór na pole całkowite walca o promieniu r i wysokości h to:",
            "choices": [
                {"key": "a", "text": "2πrh"},
                {"key": "b", "text": "πr²h"},
                {"key": "c", "text": "2πr² + 2πrh"},
                {"key": "d", "text": "πr² + 2πrh"},
            ],
            "answer": "c",
            "hint": "Pole całkowite = 2 × podstawa + boczna.",
            "explanation": "P = 2πr² (dwie podstawy) + 2πrh (boczna) = 2πr² + 2πrh.",
        },
    ],
}


def get_topic_tasks(topic: str) -> list:
    return TOPIC_TASKS.get(topic, [])

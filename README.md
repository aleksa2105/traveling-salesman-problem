# Genetski algoritam za problem putujućeg trgovca (TSP)

📌 **Autor**: Ćurčić Aleksa  
🎓 **Fakultet**: Univerzitet u Novom Sadu, Fakultet tehničkih nauka  
📁 **Predmet**: Nelinearno programiranje i evolutivni algoritmi  

---

## 📋 Opis problema

Problem putujućeg trgovca (TSP) podrazumijeva pronalaženje najkraće moguće rute koja obilazi sve date gradove tačno jednom i završava se u početnom gradu.  
Zbog eksplozivnog rasta broja permutacija (n!), koristi se **genetski algoritam** kao heuristički pristup koji omogućava nalaženje dobrih približnih rješenja u razumnom vremenu.

---

## 🧠 Opis rješenja

Algoritam koristi standardne komponente evolutivnih algoritama:

- **Hromozom (jedinka)**: predstavlja jednu putanju (permutaciju gradova)
- **Populacija**: skup jedinki
- **Selekcija**: turnirska selekcija i rulet selekcija
- **Ukrštanje**: PMX (Partially Mapped Crossover) i OX1 (Order Crossover)
- **Mutacija**: displacement metoda
- **Elitizam** i **resetovanje populacije** u slučaju zastoja

---

## ⚙️ Parametri

| Parametar                   | Opis                                                         |
| --------------------------- | ------------------------------------------------------------ |
| `FILE_NAME`                 | Putanja do fajla sa gradovima                                |
| `NUM_GENERATIONS`           | Maksimalan broj generacija                                   |
| `POPULATION_SIZE`           | Broj jedinki u populaciji                                    |
| `TOURNAMENT_SELECTION_SIZE` | Broj učesnika u turniru                                      |
| `MUTATION_CHANCE`           | Vjerovatnoća mutacije djeteta                                |
| `ELITISM_RATE`              | Procenat elitnih jedinki u novoj populaciji                  |
| `CHROMOSOME_MAX_AGE`        | Maksimalna starost jedinke                                   |
| `RESET_RATE`                | Procenat jedinki koje se resetuju prilikom zastoja algoritma |

---

## 🏗️ Struktura koda

- `Chromosome`: predstavlja jednu putanju (hromozom)
- `Population`: upravlja generacijama i jedinkama
- `TournamentSelection` i `RouletteSelection`: selekcione strategije
- `PMX` i `OX1`: operatori ukrštanja
- `Mutate`: displacement mutacija
- `helpers.py`: učitavanje podataka, nasumično generisanje jedinki, izračunavanje udaljenosti itd.

---

## ▶️ Kako pokrenuti

1. Pripremiti `.txt` fajl sa skupom gradova u formatu:

   ```
   CityID x y
   0      22 45
   1      41 65
   ...
   ```

2. Pokrenuti glavni program:

   ```bash
   python3 main.py
   ```

3. Parametri se mogu podesiti unutar fajla `params.py`.

---

## ✅ Rezultati

- Algoritam u većini testova nalazi kvalitetna približna rješenja nakon ograničenog broja generacija.
- Reset mehanizam i starosna granica sprječavaju stagnaciju u lokalnim minimumima.
- Dva operatora ukrštanja omogućavaju poređenje različitih strategija razvoja populacije.

---

## 📌 Napomena

Kod je pisan u edukativne svrhe, uz fokus na čitljivost, proširivost i osnovne mehanizme genetskih algoritama.  
Neki delovi implementacije (npr. heuristička inicijalizacija) su ostavljeni kao potencijalni pravci za proširenje.

---

## 📚 Reference

- Ü. Çölük – *TSP: New Genetic Representations and Operators*, Middle East Technical University.  
  [PDF link](https://user.ceng.metu.edu.tr/~ucoluk/research/publications/tspnew.pdf)

- P. Larrañaga, J.A. Lozano – *Genetic Algorithms for the Travelling Salesman Problem: A Review of Representations and Operators*, Technical Report, University of the Basque Country, 2002.  
  [ResearchGate link](https://www.researchgate.net/profile/Pedro-Larranaga/publication/226665831_Genetic_Algorithms_for_the_Travelling_Salesman_Problem_A_Review_of_Representations_and_Operators/links/55b7b5c808aec0e5f43841d8/Genetic-Algorithms-for-the-Travelling-Salesman-Problem-A-Review-of-Representations-and-Operators.pdf)



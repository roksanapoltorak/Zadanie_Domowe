# Zadanie_Domowe
Zadanie domowe z zajęć relayr Tester School (dzień 5 i 6)

Treść zadania:

Napisać moduł (np. peseltools) zawierający funkcje do operowania na numerze PESEL:
1. Funkcja validate(pesel) zwracająca True jeżeli podany argument jest poprawnym numerem PESEL i False w przeciwnym wypadku.
2. Funkcja extract_personal_data(pesel) zwracająca słownik o kluczach 'birth_date' oraz 'sex'. i odpowiadającym im wartościom: datą urodzenia i płcią ('male', 'female'), dane te mają zostać pobrane z nr PESEL. 
   W przypadku, gdy podany do funkcji extract_personal-data argument nie jest poprawnym numerem PESEL, funkcja ta powinna zgłosić wyjątek ValueError.
   
Dodatkowo napisać przykładowy program, który korzysta z modułu peseltools - na przykład wczytuje PESEL od użytkownika i wyświetla, jakie informacje udało mu się wyciągnąć.

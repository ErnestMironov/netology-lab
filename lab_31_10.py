def hanoi(n, source_peg, aux_peg, target_peg):
    if n == 1:
        print(f"Переместите диск 1 со стержня {source_peg} на стержень {target_peg}")
        return
    # Перемещаем n-1 дисков на вспомогательный стержень
    hanoi(n-1, source_peg, target_peg, aux_peg)
    # Перемещаем n-ый диск на целевой стержень
    print(f"Переместите диск {n} со стержня {source_peg} на стержень {target_peg}")
    # Перемещаем n-1 дисков с вспомогательного стержня на целевой
    hanoi(n-1, aux_peg, source_peg, target_peg)

if __name__ == "__main__":
    n = int(input("Введите количество дисков: "))
    hanoi(n, 'A', 'B', 'C')


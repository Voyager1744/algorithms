def is_transformable(s1, s2):
    """
  Проверяет, можно ли преобразовать строку s1 в строку s2 за счет замены любых двух букв.

  Args:
    s1: Исходная строка.
    s2: Целевая строка.

  Returns:
    True, если строка s1 преобразуема в строку s2, False в противном случае.
  """
    n = len(s1)
    if n != len(s2):
        return False

    for i in range(n):
        if s1[i] != s2[i]:
            for j in range(26):
                if s1[i] == chr(j + ord('a')):
                    s1 = s1.replace(chr(j + ord('a')), s2[i])
                    s1 = s1.replace(s2[i], chr(j + ord('a')))
                    break
            if s1 != s2:
                return False

    return True


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        print("YES" if is_transformable(s1, s2) else "NO")

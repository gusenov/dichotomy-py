def nlr_gen(left, right, parent):
    """
    left и right являются zero-based индексами.
    https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_(NLR)
    """

    # Количество элементов от left до right включительно:
    cnt_from_left_to_right_inclusive = right - left + 1

    # Если элементов всего два:
    if cnt_from_left_to_right_inclusive == 2:
        # Например:
        #  4 5 выдаст 4 и 5.
        yield (left, parent)
        yield (right, left)
        return

    # Определение центрального элемента:
    center_idx = left + cnt_from_left_to_right_inclusive // 2

    # Пример определения центрального элемента для НЕЧЕТНОГО количества элементов:
    # 0 1 2 3 4 >5< 6 7 8 9 10
    # 0 + (10 - 0 + 1) div 2 = 11 div 2 = 5

    # Пример определения центрального элемента для ЧЕТНОГО количества элементов:
    # 0 1 2 3 >4< 5 6 7
    # 0 + (7 - 0 + 1) div 2 = 8 div 2 = 4

    # Пример определения центрального элемента для НЕЧЕТНОГО количества элементов:
    # 5 >6< 7
    # 5 + (7 - 5 + 1) div 2 = 5 + 3 div 2 = 5 + 1 = 6

    # Пример определения центрального элемента для ЧЕТНОГО количества элементов:
    # 4 5 >6< 7
    # 4 + (7 - 4 + 1) div 2 = 4 + 4 div 2 = 4 + 2 = 6

    # Если количество элементов чётное:
    if cnt_from_left_to_right_inclusive % 2 == 0:
        center_idx -= 1

    yield (center_idx, parent)

    # Левая часть:
    if center_idx - 1 == left:
        # Например:
        #  4 >5< 6 7 выдаст 4.
        yield (left, center_idx)
    elif center_idx - 1 > left:
        # Например:
        #  0 1 2 3 4 >5< 6 7 8 9 10 выдаст bin_div_gen(0, 4).
        yield from nlr_gen(left, center_idx - 1, center_idx)

    # Правая часть:
    if center_idx + 1 == right:
        # Например:
        #  4 5 >6< 7 выдаст 7.
        yield (right, center_idx)
    elif center_idx + 1 < right:
        # Например:
        #  0 1 2 3 4 >5< 6 7 8 9 10 выдаст bin_div_gen(6, 10).
        yield from nlr_gen(center_idx + 1, right, center_idx)

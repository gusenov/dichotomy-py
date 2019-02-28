class LevelIterator:
    def __init__(self, bintreelst):  # конструктор.
        self.bintreelst = bintreelst
        self.queue = []
        self.queue.append(0)

    def __next__(self):  # объект является итератором, когда у него есть данный метод.

        if len(self.queue) > 0:
            result_idx = self.queue[0]

            # Получаем индекс родителя в списке.
            # Т.к. индекс zero-based, то для упрощения вычисление добавляем к нему единицу.
            parent_idx = self.queue.pop(0) + 1

            # Для индексов начинающихся с единицы
            # левый потомок узла на позиции n размещается на позиции 2n.
            # Т.к. индексы фактически zero-based, то отнимаем единицу.
            left_child_idx = 2 * parent_idx - 1

            # Для индексов начинающихся с единицы
            # правый потомок узла на позиции n размещается на позиции 2n + 1.
            # Т.к. индексы фактически zero-based, то отнимаем единицу, вследствие чего единица устраняется.
            right_child_idx = 2 * parent_idx

            # Если есть левый потомок, то добавляем его в очередь:
            if left_child_idx < len(self.bintreelst) and \
                    self.bintreelst[left_child_idx] is not None:
                self.queue.append(left_child_idx)

            # Если есть правый потомок, то добавляем его в очередь:
            if right_child_idx < len(self.bintreelst) and \
                    self.bintreelst[right_child_idx] is not None:
                self.queue.append(right_child_idx)

            return (result_idx, self.bintreelst[result_idx])
        else:
            raise StopIteration

    def __iter__(self):
        return self

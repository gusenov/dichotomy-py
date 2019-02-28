class BinaryTreeList(list):
    def __init__(self):
        super(BinaryTreeList, self).__init__()

    def append(self, item):
        super(BinaryTreeList, self).append(item)

    def addnode(self, node, parent):
        if parent is None:
            # Когда список пустой, добавляем на первую (нулевую) позицию корневой элемент:
            if not self:
                self.append(node)
            else:
                self[0] = node
            return

        # Получаем индекс родителя в списке.
        # Т.к. индекс zero-based, то для упрощения вычисление добавляем к нему единицу.
        parent_idx = self.index(parent) + 1
        # Для индексов начинающихся с единицы
        # родитель узла на позиции n размещается на позиции n/2.

        # Для индексов начинающихся с единицы
        # левый потомок узла на позиции n размещается на позиции 2n.
        # Т.к. индексы фактически zero-based, то отнимаем единицу.
        left_child_idx = 2 * parent_idx - 1

        # Для индексов начинающихся с единицы
        # правый потомок узла на позиции n размещается на позиции 2n + 1.
        # Т.к. индексы фактически zero-based, то отнимаем единицу, вследствие чего единица устраняется.
        right_child_idx = 2 * parent_idx

        # Если индекс выходит за границы списка, то расширяем список None-значениями:
        while left_child_idx >= len(self) \
                or right_child_idx >= len(self):
            self.append(None)

        # По возможности, сначала всегда добавляем левого потомка:
        if self[left_child_idx] is None:
            self[left_child_idx] = node

        # Потом правого:
        elif self[right_child_idx] is None:
            self[right_child_idx] = node

# Task 1 #
 - написано функцію reverse(), яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
 - розроблено алгоритм сортування для однозв'язного списку insertion_sort();
 - написано функцію merge_lists(), що об'єднує два відсортовані однозв'язні списки в один відсортований список.

# Task 2 #
 - було написано 2 функції
 - draw_pythagorean_tree() відповідає за розрахунки, які потрібні для виведення дерева і викликає сама себе, тобто має рекурсію
 - draw() яка відповідає за середовище для малювання та викликає draw_pythagorean_tree.

# Task 3 #
 - Взявши алгоритм Дейкстри з коспекту були зроблені зміни для використання бінарної купи

# Task4 # 
  - Код виконує побудову бінарних дерев.
  - Клас Node являє собою вузол дерева, який має посилання на лівих і правих дітей, також кожен вузол має значення, колір і id. 
  - Функція add_edges() відповідає за додавання вузлів і ребер до дерева. Вона має певні параметри, при існуванні вузла, буде цей вузол доданий до графа. Якщо існує ліва дитина вузла, то рекурсивно буде додане ребро і прорахована позиція вузла. Аналогічна ситуація відбувається з правою дитиною вузла.      
  - Функція draw_tree() відповідає за виведення дерева на view port. Спочатку граф ініціалізується, потім зазначається позиція кореневого вузла, а також додаєються вузли, ребра і позиції цих вузлів графа. Додатково додаються фарби і лейбли для виведення графа  
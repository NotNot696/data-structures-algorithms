# 📚 Data Structures & Algorithms in Python

> **یک مجموعه کامل و تمیز از پیاده‌سازی ساختمان‌های داده و الگوریتم‌های مهم به زبان پایتون**

این مخزن شامل پیاده‌سازی‌های **از صفر** و **بدون استفاده از کتابخانه‌های خارجی** (به جز ماژول‌های استاندارد) است. هدف، درک عمیق مفاهیم و تمرین کدنویسی اصولی است.

---

## 🧠 **مباحث پوشش‌داده‌شده**

| دسته‌بندی | مباحث |
|-----------|-------|
| **ساختمان‌های داده پایه** | آرایه داینامیک، لیست پیوندی، استک، صف (عادی، حلقوی، با دو استک، اولویت) |
| **جدول هش** | پیاده‌سازی با روش زنجیره‌ای (Chaining) |
| **درخت‌ها** | درخت باینری، BST، AVL، Trie |
| **هیپ (Heap)** | MaxHeap، MinHeap، عملیات‌های اصلی |
| **گراف** | گراف بدون وزن، گراف وزن‌دار، BFS، DFS، تشخیص دور، دیکسترا، پریم |
| **مرتب‌سازی** | Bubble، Selection، Insertion، Merge، Quick |
| **جستجو** | خطی، دودویی، سه‌گانه |


---

## 📁 **ساختار پروژه**

```
data-structures-algorithms/
│
├── arrays/
│   └── dynamic_array.py
├── linked_lists/
│   └── singly_linked_list.py
├── stacks_queues/
│   ├── stack.py
│   ├── queue.py
│   ├── circular_queue.py
│   └── priority_queue.py
├── hash_tables/
│   └── hash_table.py
├── trees/
│   ├── binary_tree.py
│   ├── bst.py
│   ├── avl_tree.py
│   └── trie.py
├── heaps/
│   ├── max_heap.py
│   └── min_heap.py
├── graphs/
│   ├── graph.py
│   ├── weighted_graph.py
│   ├── dijkstra.py
│   └── prim.py
├── sorting/
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   └── ternary_search.py
├── utils/
│   └── helpers.py
└── tests/
    ├── test_sorting.py
    └── test_searching.py
```

---

## 🚀 **نحوه اجرا**

هر فایل را می‌توانید مستقیم اجرا کنید:

```bash
python sorting/bubble_sort.py
python searching/binary_search.py
python graphs/dijkstra.py
```

برای اجرای تست‌ها:

```bash
python tests/test_sorting.py
python tests/test_searching.py
```

---

## 🧪 **تست‌ها**

تمامی الگوریتم‌ها با استفاده از `assert` تست شده‌اند:

```bash
python tests/test_sorting.py
# ✅ All sorting tests passed!

python tests/test_searching.py
# ✅ All searching tests passed!
```

---

## 👨‍💻 **توسعه دهنده**

[امیرارسلان فرهمند]  
[لینک گیت‌هاب](https://github.com/NotNot696)

---

## 📄 **لایسنس**

MIT
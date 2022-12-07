from data import data, test_data

import time
from bigtree import dict_to_tree, print_tree, postorder_iter

tic = time.perf_counter()

file_tree = {}


full_path = ''
listing = False

for line in data.splitlines():
    # command
    if line.startswith('$ cd'):
        dir_to_go = line.split('$ cd ')[1]
        if dir_to_go == '/':
            full_path = 'root'
        elif dir_to_go == '..':
            full_path = '/'.join(full_path.split('/')[:-1])
            if full_path == '':
                full_path = 'root'
        else:
            full_path += '/' + dir_to_go

        file_tree.update({full_path: {'size': 0}})

    elif line.startswith('$ ls'):
        listing = True
    elif not line.startswith('dir'):
        [file_size, file_name] = line.split(' ')
        file_tree.update({full_path + '/' + file_name: {'size': int(file_size)}})


root = dict_to_tree(file_tree)

for node in postorder_iter(root):
    if node.name != 'root':
        node.parent.size += node.size

total_size = 0
for node in postorder_iter(root):
    if not node.is_leaf and node.size <= 100000:
        total_size += node.size


# print_tree(root, attr_list=["size"])
print(total_size)

toc = time.perf_counter()
print(f"Execution time is {toc - tic:0.4f} seconds")

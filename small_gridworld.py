from __future__ import print_function 
import pprint

grid_size = 4
num_iterations = 10

num_actions = 4
x_actions = [-1, 0, 1, 0]
y_actions = [0, -1, 0, 1]

rewards = [[0, -1, -1, -1], 
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, 0]]

v = [[0., 0., 0., 0.],
    [0., 0., 0., 0.],
    [0., 0., 0., 0.],
    [0., 0., 0., 0.]]

def get_new_pos(old_pos, new_pos, grid_size):
    if new_pos < 0 or new_pos >= grid_size:
        return old_pos
    
    return new_pos
    

equi_prob = 1. / num_actions

phi = [equi_prob] * num_actions

discount_factor = 1.0

def print_v(v, grid_size):
    for row in range(grid_size):

        for col in range(grid_size):
            print('{:.2f} '.format(v[row][col]), end='')
        
            
        print()


for i in range(num_iterations):
    for row in range(grid_size):
        for col in range(grid_size):
            v_sum = 0.

            for a in range(num_actions):
                import ipdb; ipdb.set_trace()
                new_row = get_new_pos(row, row + x_actions[a], grid_size)
                new_col = get_new_pos(col, col + y_actions[a], grid_size)
                v_sum += phi[a] * ( rewards[new_row][new_col] + discount_factor * v[new_row][new_col] ) 
            v[row][col] = v_sum
    print('--')
    print_v(v, grid_size)
    

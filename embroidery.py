def draw_rectangle(width, height, border_color, fill_color, border_width):
    matrix = [[fill_color for i in range(width)] for j in range(height)]
    for my_list in matrix[0:border_width]:
        for index in range(len(my_list)):
            my_list[index] = border_color
    for my_list in matrix[-border_width:]:
        for index in range(len(my_list)):
            my_list[index] = border_color
    for my_list in matrix:
        for index in range(0, border_width):
            my_list[index] = border_color
            my_list[-1 - index] = border_color
    for element in matrix:
        print(str(element).strip("[]").replace(",", " "))


# def draw_triangle(height):
#     matrix = []
#     return matrix


# def draw_christmas_tree(blocks):
#     matrix = []
#     return matrix


# def draw_circle(radius):
#     matrix = []
#     return matrix


# def embroider(matrix, color_scheme):
#     for row in matrix:
#         for cell in row:
#             print(color_scheme[cell], end='')
#         print()
#     print()


# if __name__ == '__main__':
#     color_scheme = {0: ' ', 1: '*', 2: '.'}
#     embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)

draw_rectangle(9, 5, 1, 2, 2)
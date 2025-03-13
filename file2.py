def draw_ascii_tree(height):
    if height < 1:
        return "Height must be at least 1"
    
    tree = ""
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        tree += spaces + stars + '\n'
    
    trunk = ' ' * (height - 1) + '*\n'
    tree += trunk
    return tree

if __name__ == "__main__":
    height = 5
    print(draw_ascii_tree(height))
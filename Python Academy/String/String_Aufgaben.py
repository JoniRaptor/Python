import os
output = 'Das soll in der Mitte stehen'
output_centered = output.center(os.get_terminal_size()[0], '!')
print(output_centered)

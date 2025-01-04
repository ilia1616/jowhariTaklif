'''
    *
   * *
  *   *
 *     *
*********
'''
pat = "   * *\n  *   *\n *     *\n*********"

n = int(input())
final =''

z=0
for i in range(n,0, -1):
    for j in range(4):
        if j == 0:
            final += ((i)* '*********') + (z * '    ') + '\n'
        elif j == 1:
            final += ((i) * ' *     * ') + (z * '    ') + '\n'
        elif j == 2:
            final += ((i) * '  *   *  ') + (z * '    ') + '\n'
        elif j == 3:
            final += ((i) * '   * *   ') + (z * '    ') + '\n'
    z+=1
    

print(((n-1) * '    ') + '    *' , end="")
final = final[::-1]
while ' \n' in final:
    final = final.replace(' \n', '\n')
print(final)
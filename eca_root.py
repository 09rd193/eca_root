# coding: utf-8
import pprint

def onestep(line):
  newline = ''
  for i in range(len(line)):
    x, z = '0', '0'
    if i == 0:
      x, z = '0', line[i + 1]
      if line[i] == '1':
        newline = '1' + newline
    elif i == len(line) - 1:
      x, z = line[i - 1], '0'
    else:
      x, z = line[i - 1], line[i + 1]
    newline += '0' if x == z else '1'
  return newline

def main():
  s = set()
  ans = {}
  for i in range(1, 1000):
    if i in s:
      continue
    s.add(i)
    count = 1
    ans[i] = ','.join((str(i), str(count)))
    b = format(i, 'b')
    for j in range(5):
      b = '0' + b
      b = onestep(b)
      next_i = int(b, 2)
      s.add(next_i)
      count = count + 1
      ans[next_i] = ','.join((str(i), str(count)))
      b = format(next_i, 'b')
  pprint.pprint(ans)




    
if __name__ == '__main__':
  main()
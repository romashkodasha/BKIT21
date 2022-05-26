
import sys
import math

def get_coef(index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            coef_str = input(prompt)
        coef = float(coef_str)
        return coef

def d_positive(result, a, b, c, D):
    sqD = math.sqrt(D)
    sq1 = (-b - sqD) / (2.0 * a)
    sq2 = (-b + sqD) / (2.0 * a)
    if sq1 >= 0.0:
        root1 = -math.sqrt(sq1)
        root2 = math.sqrt(sq1)
        result.append(root1)
        if root1 != root2: result.append(root2)
    if sq2 >= 0.0:
        root3 = -math.sqrt(sq2)
        root4 = math.sqrt(sq2)
        result.append(root3)
        if root3 != root4: result.append(root4)
    return result

def d_zero(result, a, b, c):
    root1 = math.sqrt(-b / (2.0 * a))
    root2 = -math.sqrt(-b / (2.0 * a))
    result.append(root1)
    if root1 != root2: result.append(root2)
    return result

def get_roots(a, b, c):
    result = []
    if a == 0.0:
        if b == 0.0 :
            if c == 0.0: 
                result = [0.0] * 5
                return result
            else: return result
        else:
            sq = -c / b
            if sq>=0:
                root1 = -math.sqrt(sq)
                root2 = math.sqrt(sq)
                result.append(root1)
                if root1 != root2: result.append(root2)
    else:
        D = b * b - 4 * a * c
        if D == 0.0: result = d_zero(result, a, b, c)
        elif D > 0.0: result = d_positive(result, a, b, c, D)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    roots = get_roots(a,b,c)
    if not roots:roots = []
    len_roots = len(roots)
    if len_roots > 1:roots.sort()
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {:.3f}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {:.3f} и {:.3f}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Четыре корня: {:.3f}, {:.3f} и {:.3f}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {:.3f}, {:.3f}, {:.3f} и {:.3f}'.format(roots[0], roots[1], roots[2], roots[3]))
    elif len_roots == 5:
        print('Бесконечное кол-во корней')
    else:
        print('Unexpected result')

if __name__ == "__main__":
    main()
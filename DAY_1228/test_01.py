# ------------------------------------------------------------------------
# [실습 1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해 주세요.
#         +, -, *, /, //, % , **
#         [출력 예시] 10 + 4 = 14
# ------------------------------------------------------------------------

m = int(input('숫자를 입력하세요 : '))
n = int(input('숫자를 입력하세요 : '))

print(f'{m} + {n} = {m + n}')
print(f'{m} - {n} = {m - n}')
print(f'{m} * {n} = {m * n}')
print(f'{m} / {n} = {m / n}')
print(f'{m} // {n} = {m // n}')
print(f'{m} % {n} = {m % n}')
print(f'{m} ** {n} = {m ** n}')
print()
# ------------------------------------------------------------------------
# [실습 2] [실습 1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
#         >, <, >=, <=, ==, !=
#         [출력 예시] 10 > 4   => True
#                   10 == 4  => False
# ------------------------------------------------------------------------

print(f'{m} > {n} => {m > n}')
print(f'{m} < {n} => {m < n}')
print(f'{m} >= {n} => {m >= n}')
print(f'{m} <= {n} => {m <= n}')
print(f'{m} == {n} => {m == n}')
print(f'{m} != {n} => {m != n}')
print()
# ------------------------------------------------------------------------
# [실습 3] [실습 1]에서 입력 받은 숫자 데이터를 활용하여
#         최대값과 최소값을 추가로 입력 받은 후 논리 연산 결과를 출력하세요.
#         [출력 예시] 10 > 4 and 10 > 최대값  => True
#                   10 > 4 and 10 > 최소값 => True
#                   not 10                => False
# ------------------------------------------------------------------------

max_value = int(input('최대값을 입력하세요 : '))
min_value = int(input('최솟값을 입력하세요 : '))

print(f'{m} >= {n} and {m} >= {max_value}  =>  {m >= n and m >= max_value}')
print(f'{m} <= {n} and {m} <= {min_value}  =>  {m <= n and m <= min_value}')
print(f'{m} >= {n} or {m} >= {max_value}  =>  {m >= n or m >= max_value}')
print(f'{m} <= {n} or {m} >= {max_value}  =>  {m <= n or m >= min_value}')
print(f'not {m}  =>  {not m}')
print(f'not {n}  =>  {not n}')
import module_util

print(f"3,000원 --> {module_util.clean_price('3,000원  ')}")

import module_util as util
print(f"3,000원 --> {util.clean_price('3,000원  ')}")

from module_util import BASE_URL,to_code

print(f"to_code-> {to_code(3443)}")
print(f"BASE_URL-->{BASE_URL}")

from module_util import clean_price as cp

print(f"3,000원-->{cp('   3000원  ')}")
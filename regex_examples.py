import re

# url = 'www.medscape.com/v2/657893/article1'
# r = re.findall('\/([0-9]+)',url)
# # print(r.group())
# print(r)

# url = 'www.medscape.com/v2/657895/article1/12386/xyxx/'
# r = re.findall('/.*/([\d]{5})/',url)
# r = re.findall('/([\d]{5,6})/',url)
# r = re.findall('/.*/([\d]{6})/.*/',url)
# r = re.search('/.*/([\d]{6})/.*/([\d]{6})/.*/',url)
# print(r)

dat = '111120221'
s = re.match('^(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])(\d{4})$',dat)
if s:
    print('Valid date')
else:
    print('Invalid date')





import dateparser as dp

def convert_date(stringVal):
	return str(int(round(int(stringVal),-3)))

print dp.parse(convert_date(1390255095))
#dt = dp.parse('1390255095')
#print (dt)

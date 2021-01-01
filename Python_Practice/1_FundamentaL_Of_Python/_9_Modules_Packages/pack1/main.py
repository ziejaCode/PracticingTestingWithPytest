import common.validators
#import common.validators.date
#import common.validators.json

common.validators.json.is_json('werwer')
common.validators.date.is_date('2018-01-23')

print('n\n\***** self ********')
for k in dict(globals()).keys():
    print(k)

print('n\n\***** common ********')
for k in common.__dict__.keys():
    print(k)

print('n\n\***** validators ********')
for k in common.validators.__dict__.keys():
    print(k)
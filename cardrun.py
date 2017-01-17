#!/user/bin/env python
# -*- coding: UTF-8 -*-

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError,TypeError),diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        try:
            ccfile = open('carddata.txt', 'r')
            txns = ccfile.readlines()  #readlines()读取所有数据
        except IOError:
            log.write('no txns this month\n')
            log.close()
    finally:
        ccfile.close()

    # txns = ccfile.readlines()  #readlines()读取所有数据
    # ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result,float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s'% result)
    print '$%.2f (new balance)' % (total)
    log.close()

if __name__ == '__main__':
    main()
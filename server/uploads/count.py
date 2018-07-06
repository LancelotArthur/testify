def count(args):
    try:
        if len(args) != 3:
            raise ParaNumError

        a = int(args[0])
        b = int(args[1])
        c = int(args[2])
        if a == 0 or b == 0 or c == 0:
            raise IncompleteError
        if a < 0 or a > 70 \
            or b < 0 or b > 80 \
                or c < 0 or c > 90:
            raise OutOfRangeError
        sales = 0
        sales += 25 * a + 30 * b + 45 * c
        if sales <= 1000:
            commission = sales * 0.1
        elif sales <= 1800:
            commission = sales * 0.15
        else:
            commission = sales * 0.2
        return str(sales), str(commission)
    except ValueError as e:
        print('ValueError: ', e)
    except IncompleteError as e:
        print('IncompleteError: ', e)
    except OutOfRangeError as e:
        print('OutOfRangeError: ', e)
    except ParaNumError as e:
        print('ParaNumError: ', e)


class IncompleteError(Exception):
    pass


class OutOfRangeError(Exception):
    pass


class ParaNumError(Exception):
    pass

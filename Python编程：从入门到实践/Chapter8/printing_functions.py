def print_models(unprinted_designs, completed_designs):
    """
    模拟打印每个设计，直到没有未打印的为止
    打印完一个后移到已打印列表中
    :param unprinted_designs: 未打印设计
    :param completed_designs: 已打印设计
    :return:None
    """
    while unprinted_designs:
        design = unprinted_designs.pop()

        print("Printing: " + design)
        completed_designs.append(design)

    print(completed_designs)

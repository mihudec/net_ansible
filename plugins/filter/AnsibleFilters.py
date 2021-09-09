from net_templates.filters import BaseFilter, CustomFilters


class FilterModule(object):

    def __init__(self) -> None:
        pass

    def filters(self):
        return CustomFilters().filters()

if __name__ == '__main__':
    f = FilterModule()
    print(f.filters())

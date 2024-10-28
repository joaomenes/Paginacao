from typing import List, Union

class PaginationHelper:
    
    def __init__(self, collection: List[Union[str, int]], items_per_page: int) -> None:
        self.collection = collection
        self.items_per_page = items_per_page
        self.collection_size = len(self.collection)
    
    def item_count(self) -> str:
        return f'O número total de items é {self.collection_size}.'
    
    def page_count(self, return_only_count: bool = False) -> Union[int, str]:
        divided = round(self.collection_size / self.items_per_page)
        if return_only_count:
            return divided
        
        if divided == 0:
            return 'A lista possui 1 página apenas.'
        return f'A lista possui {divided} páginas.'
    
    def page_item_count(self, page_index: int) -> str:
        if page_index < 0 or page_index >= self.page_count(return_only_count=True):
            return 'Página sem items.'

        start_index = page_index * self.items_per_page
        end_index = start_index + self.items_per_page
        total_items = min(self.items_per_page, self.collection_size - start_index)

        return f'Total de items na página {total_items}.'
    
    def page_index(self, item_index: int) -> str:
        if item_index < 0 or item_index >= self.collection_size:
            return 'O item não se encontra na página.'
        return f'O item se encontra na página {item_index // self.items_per_page}.'

# Exemplo de uso
helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 4)
print(helper.item_count())  # O número total de items é 26.
print(helper.page_count(return_only_count=False))  # A lista possui 7 páginas.
print(helper.page_count())  # A lista possui 7 páginas.
print(helper.item_count())  # O número total de items é 26.
print(helper.page_item_count(0))  # Total de items na página 4.
print(helper.page_item_count(1))  # Total de items na página 4.
print(helper.page_item_count(2))  # Total de items na página 4.
print(helper.page_index(5))  # O item se encontra na página 1.
print(helper.page_index(2))  # O item se encontra na página 0.
print(helper.page_index(20))  # O item se encontra na página 5.
print(helper.page_index(-10))  # O item não se encontra na página.

class PaginationHelper:
    
    # O construtor recebe um array de itens e um inteiro indicando
    # quantos itens cabem em uma única página
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.collection_size = len(self.collection)
    
    # retorna o número de itens de toda a coleção
    def item_count(self):
        total = self.collection_size
        return f'O número total da lista é {total}.'
    
    
    # retorna o número de páginas
    def page_count(self, return_only_count=False):
        divided = round(self.collection_size / self.items_per_page )
        if return_only_count:
           return divided
    
        if divided == 0:
            return f'A lista possui 1 página apenas.'
        return f'A lista possui { divided } páginas.'
    
    # retorna o número de itens na página fornecida. page_index é baseado em zero
    # este método deve retornar uma informação  para valores page_index que estão fora do intervalo
    def page_item_count(self, page_index):
        # Verifica se o índice da página é válido
        if page_index < 0 or page_index >= self.page_count(return_only_count=True):
            return 'Página sem items.'

        start_index = page_index * self.items_per_page  # Multiplica pelo número de itens por página
        end_index = start_index + self.items_per_page  # Define o índice final com base nos itens por página
        end = start_index - end_index

        # Retorna o número de itens na página solicitada
        return f'Total de items na página {abs(end)}.' #retornando o valor absoluto
        
    
    # determina em qual página um item de um determinado índice está. Índices baseados em zero.
    # este método deve retornar -1 para valores item_index que estão fora do intervalo
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.collection_size:
            return -1
        return f'O item se encontra na página {item_index // self.items_per_page}.'



helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 4)
print(helper.item_count())
print(helper.page_count(return_only_count=False))
print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))

print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(-10))



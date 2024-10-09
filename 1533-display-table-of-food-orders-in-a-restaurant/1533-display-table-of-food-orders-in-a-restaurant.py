class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        tables = set()
        food_items = set()
        table_orders = defaultdict(lambda: defaultdict(int))

        for _, table_number, food_item in orders:
            tables.add(table_number)
            food_items.add(food_item)
            table_orders[table_number][food_item] += 1
        
        sorted_tables = sorted(tables, key=int)
        sorted_food_items = sorted(food_items)

        result = [['Table'] + sorted_food_items]

        for table in sorted_tables:
            row = [table] + [
                str(table_orders[table].get(food_item, 0)) for food_item in sorted_food_items
            ]
            result.append(row)
        return result

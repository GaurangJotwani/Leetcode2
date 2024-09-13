public class StockSpanner {
    Stack<(int price, int days)> prices;

    public StockSpanner() {
        prices = new Stack<(int price, int days)>();
    }
    
    public int Next(int price) {
        int days = 1;
        while (prices.Count > 0 && price >= prices.Peek().price) {
            days += prices.Peek().days;
            prices.Pop();
        }
        prices.Push((price, days));
        return days;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */
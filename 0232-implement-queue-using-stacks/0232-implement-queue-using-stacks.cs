public class MyQueue {

    Stack<int> front;
    Stack<int> back;
    public MyQueue() {
        front = new Stack<int>();
        back = new Stack<int>();
    }
    
    public void Push(int x) {
        back.Push(x);
    }
    
    public int Pop() {
        var num = 0;
        if (front.Count > 0) {
            num = front.Peek();
            front.Pop();
            return num;
        }
        while (back.Count > 0) {
            num = back.Peek();
            back.Pop();
            front.Push(num);
        }

        num = front.Peek();
        front.Pop();
        return num;
    }
    
    public int Peek() {
        if (front.Count > 0) return front.Peek();
        while (back.Count > 0) {
            var num = back.Peek();
            back.Pop();
            front.Push(num);
        }
        return front.Peek();
    }
    
    public bool Empty() {
        return front.Count == 0 && back.Count == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
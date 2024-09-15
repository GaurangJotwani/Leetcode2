/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
public class NestedIterator {

    private int idx;
    private List<int> res;

    public NestedIterator(IList<NestedInteger> nestedList) {
        res = new List<int>();
        FlattenList(nestedList);
    }

    private void FlattenList(IList<NestedInteger> nestedList) {
        for (int i = 0; i < nestedList.Count; i++) {
            var curr = nestedList[i];
            if (curr.IsInteger()) {
                res.Add(curr.GetInteger());
            }
            else FlattenList(curr.GetList());
        }
        // foreach (var num in res) Console.Write(num + " ");
        // Console.WriteLine();
    }

    public bool HasNext() {
        return idx != res.Count;
    }

    public int Next() {
        return res[idx++];
    }
}

/**
 * Your NestedIterator will be called like this:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.HasNext()) v[f()] = i.Next();
 */
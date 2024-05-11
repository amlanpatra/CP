import java.util.*;

public class Testing {

    public static ArrayList<pair> kNeighbourPoints(ArrayList<pair> points, pair p, int k) {

        if (k > points.size())
            return new ArrayList<pair>(1);

        ArrayList<pair> al = new ArrayList<>();

        for (int i = 0; i < points.size(); i++) {
            int f = Math.abs(p.first - points.get(i).first) + Math.abs(p.second - points.get(i).second);
            pair curr = new pair(f, i); // pair of |x-x'| + |y-y'| and i
            al.add(curr);
        }

        Collections.sort(al, (a, b) -> Integer.compare(a.first, b.first));

        ArrayList<pair> res = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            res.add(points.get(al.get(i).second));
        }

        Collections.sort(res, (a, b) -> Integer.compare(a.first, b.first));

        return res;
    }

    public static void main(String[] args) {
        Integer[][] arr = { { -2, 1 }, { 1, 2 }, { 3, 6 }, { 9, 2 } };
        pair test = new pair(0, 1);
        int k = 5;

        ArrayList<pair> al = new ArrayList<>();

        for (Integer[] i : arr) {
            pair p = new pair(i[0], i[1]);
            al.add(p);
        }

        ArrayList<pair> res = kNeighbourPoints(al, test, k);

        for (pair p : res) {
            System.out.println(p.first + " " + p.second);
        }
    }

}

class pair {
    int first, second;

    pair(int f, int s) {
        this.first = f;
        this.second = s;
    }
}

import java.util.Collections;
import java.util.LinkedList;

/**
 * Definition of Interval:
 * public class Interval {
 * int start, end;
 * Interval(int start, int end) {
 * this.start = start;
 * this.end = end;
 * }
 * }
 */

public class interviewrroom {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    public int minMeetingRooms(List<Interval> intervals) {
        Collections.sort(intervals, (a, b) -> a.start - b.start);
        // for (int i = 0; i < intervals.size(); i++) {
        // System.out.println(intervals.get(i).start + " " + intervals.get(i).end);
        // }

        LinkedList<Interval> ll = new LinkedList<>();

        ll.add(intervals.get(0));

        for (int i = 1; i < intervals.size(); i++) {
            Interval last = ll.getLast();
            Interval comp = intervals.get(i);
            if (last.end <= comp.start) {
                ll.removeLast();
                Interval new_last = new Interval(last.start, Math.max(last.end, comp.end));
                ll.add(new_last);
            } else {
                ll.add(intervals.get(i));
            }
        }
        return ll.size();
    }
}
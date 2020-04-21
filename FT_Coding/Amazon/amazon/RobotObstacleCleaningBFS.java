package dataStructures.treeGraphs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


public class RobotObstacleCleaningBFS {
	
	static class LocationAndDis{
		int x;
		int y;
		int dist;
		public LocationAndDis(int x, int y, int dist) {
			this.x=x;
			this.y=y;
			this.dist=dist;
		}
	}
	int removeObstacle(int numRows, int numColums, List<List<Integer>> lot) {
		Queue<LocationAndDis> queue = new LinkedList<>();
		queue.add(new LocationAndDis(0,0,0));
		int destX = 0;
		int destY = 0;
		boolean[][] visited = new boolean[numRows][numColums];
		for(int i=0;i<numRows;i++) {
			for(int j=0;j<numColums;j++) {
				if(lot.get(i).get(j)==0) {
					visited[i][j]=true;
				}else {
					visited[i][j]=false;
					if(lot.get(i).get(j)==9) {
						destX = i;
						destY = j;
					}
				}
			}
		}
		while(!queue.isEmpty()) {
			LocationAndDis ele = queue.poll();
			if(ele.x==destX && ele.y==destY) {
				return ele.dist;
			}
			boolean topValid = checkIfValid(ele.x-1,ele.y,numRows, numColums);
			boolean downValid = checkIfValid(ele.x+1,ele.y,numRows, numColums);
			boolean leftValid = checkIfValid(ele.x,ele.y-1,numRows, numColums);
			boolean rightValid = checkIfValid(ele.x,ele.y+1,numRows, numColums);
			
			// else enqueue neighbor cells which are not visited
			if(topValid && !visited[ele.x-1][ele.y]) {
				queue.add(new LocationAndDis(ele.x-1, ele.y, ele.dist+1));
			}
			if(downValid && !visited[ele.x+1][ele.y]) {
				queue.add(new LocationAndDis(ele.x+1, ele.y, ele.dist+1));
			}
			if(leftValid && !visited[ele.x][ele.y-1]) {
				queue.add(new LocationAndDis(ele.x, ele.y-1, ele.dist+1));
			}
			if(rightValid && !visited[ele.x][ele.y+1]) {
				queue.add(new LocationAndDis(ele.x, ele.y+1, ele.dist+1));
			}
		}
		return -1;
	}
	private boolean checkIfValid(int i, int j, int numRows, int numColums) {
		if(i>=0 && i<numRows && j>=0 && j<numColums) {
			return true;
		}
		return false;
	}
	
	public static void main(String[] args) {
		List<List<Integer>> inputM = new ArrayList<List<Integer>>();
		List<Integer> list1 = new ArrayList<Integer>();
		list1.add(1);
		list1.add(1);
		list1.add(1);

		list1.add(1);

		List<Integer> list2 = new ArrayList<Integer>();
		list2.add(0);
		list2.add(1);
		list2.add(1);
		list2.add(1);

		List<Integer> list3 = new ArrayList<Integer>();
		list3.add(0);
		list3.add(1);
		list3.add(0);
		list3.add(1);

		List<Integer> list4 = new ArrayList<Integer>();
		list4.add(1);
		list4.add(1);
		list4.add(1);
		list4.add(1);

		List<Integer> list5 = new ArrayList<Integer>();
		list5.add(0);
		list5.add(0);
		list5.add(9);
		list5.add(1);
		inputM.add(list1);
		inputM.add(list2);
		inputM.add(list3);
		inputM.add(list4);
		inputM.add(list5);

		//NEW INPUT
		List<Integer> list11 = new ArrayList<Integer>();
		list11.add(1);
		list11.add(0);
		list11.add(0);

		List<Integer> list12 = new ArrayList<Integer>();
		list12.add(1);
		list12.add(0);
		list12.add(9);

		List<Integer> list13 = new ArrayList<Integer>();
		list13.add(1);
		list13.add(1);
		list13.add(1);


//		inputM.add(list11);
//		inputM.add(list12);
//		inputM.add(list13);

		RobotObstacleCleaningBFS obj = new RobotObstacleCleaningBFS();
		int res = obj.removeObstacle(5, 4, inputM);
		System.out.println(res);
}
}

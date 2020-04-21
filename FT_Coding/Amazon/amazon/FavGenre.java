package dataStructures.Arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public class FavGenre {


	HashMap<String, List<String>> favoriteVideoGenre(int numUsers, 
			HashMap<String, List<String>> userBooksListenedTo, 
			int numGenres,
			HashMap<String, List<String>> bookGenres)
	{
		
		if(numUsers==0 || numGenres==0) return null;


		HashMap<String, String> bookToGenre = new HashMap<>();
		//creating new map
		for(Entry<String, List<String>> entry : bookGenres.entrySet()) {
			for(String book : entry.getValue()) {
				bookToGenre.put(book, entry.getKey());
			}
		}
		
		//iterating over userBookSListenedOut
		for(Entry<String, List<String>> entry : userBooksListenedTo.entrySet()) {
			ArrayList<String> val = new ArrayList<>();
			for(String book: entry.getValue()) {
				val.add(bookToGenre.get(book));
			}
			userBooksListenedTo.put(entry.getKey(), val);
		}
		

		HashMap<String,List<String>> res = new HashMap<>();
		for(Entry<String, List<String>> entry : userBooksListenedTo.entrySet()) {
		HashMap<String, Integer> freqMap = new HashMap<>();	
			for(String genre : entry.getValue()) {
				if(freqMap.containsKey(genre)) {
					freqMap.put(genre, freqMap.get(genre)+1);
				}else {
					freqMap.put(genre, 1);
				}
			}
			List<String> list_fav_genre = findMaxVal(freqMap);
			res.put(entry.getKey(), list_fav_genre);
		}
		
		
		
		return res;
	}
	
	private List<String> findMaxVal(HashMap<String, Integer> map) {
		List<String> list = new ArrayList<>();
		int maxVal = Collections.max(map.values());
		for( Entry<String, Integer> entry : map.entrySet()) {
			if(entry.getValue()==maxVal) {
				list.add(entry.getKey());
			}
		}
		return list;
	}
	
	
	public static void main(String[] args) {

		FavGenre obj = new FavGenre();
		HashMap<String,List<String>> inp1 = new HashMap<>();
		List<String> list = new ArrayList<>();
		list.add("mass");
		list.add("world");
		list.add("stress");
		inp1.put("Fred",list);
		
		List<String> list2 = new ArrayList<>();
		list2.add("happy");
		list2.add("pride");
		inp1.put("Jenie",list2);
		
		List<String> list3 = new ArrayList<>();
		list3.add("alex");
		inp1.put("ronie",list3);
		
		
		HashMap<String,List<String>> inp2 = new HashMap<>();
		List<String> list11 = new ArrayList<>();
		list11.add("mass");
		list11.add("stress");
		inp2.put("horror",list11);
		
		List<String> list12 = new ArrayList<>();
		list12.add("happy");
		inp2.put("comedy",list12);
		
		List<String> list13 = new ArrayList<>();
		list13.add("world");
		list13.add("alex");
		list13.add("pride");
		
		inp2.put("romance",list13);
		
		
		
		
		obj.favoriteVideoGenre(3, inp1, 3,inp2);
	}

}

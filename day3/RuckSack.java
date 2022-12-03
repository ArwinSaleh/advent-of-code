import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

import java.util.Collection;
import java.util.Collections;
import java.util.Set;
import java.util.ArrayList;
import java.lang.Character;
import java.util.HashSet;
import java.util.List;

class RuckSack {
	static int MAX_CHAR = 26;
	static int elvesPerGroup = 3;
	static String alphabetLowerCase = "abcdefghijklmnopqrstuvwxyz";
	static String alphabetUpperCase = alphabetLowerCase.toUpperCase();

	public static void main(String[] args) throws FileNotFoundException {
		File inputFile = new File(args[0]);
		Scanner sc = new Scanner(inputFile);

		// ruckSackPart1(sc);
		ruckSackPart2(sc);
	}

	static void ruckSackPart1(Scanner sc) {
		int sumOfPriorities = 0;
		int numberOfItems, halfNumberOfItems;
		String ruckSackItems;
		char[] compartment1, compartment2;
		while (sc.hasNextLine()) {
			ruckSackItems = sc.nextLine();
			numberOfItems = ruckSackItems.length();
			halfNumberOfItems = numberOfItems / 2;
			compartment1 = ruckSackItems.substring(0, halfNumberOfItems).toCharArray();
			compartment2 = ruckSackItems.substring(halfNumberOfItems, numberOfItems).toCharArray();
			char commonItem = getCommonItem(compartment1, compartment2, halfNumberOfItems);
			sumOfPriorities += getSumOfPriorities(commonItem);
		}
		System.out.println(sumOfPriorities);
	}

	static void ruckSackPart2(Scanner sc) {
		int totalSumOfPriorities = 0;
		String ruckSackItems;
		List<String> currentGroupItems = new ArrayList<String>();

		int elfIdx = 0;
		while (sc.hasNextLine()) {
			if (elfIdx < elvesPerGroup) {
				ruckSackItems = sc.nextLine();
				currentGroupItems.add(ruckSackItems);
				elfIdx++;
			} else {
				char commonItem = findCommonCharsFor(currentGroupItems).iterator().next();
				totalSumOfPriorities += getSumOfPriorities(commonItem);
				currentGroupItems.clear();
				elfIdx = 0;
			}
		}
		char commonItem = findCommonCharsFor(currentGroupItems).iterator().next();
		totalSumOfPriorities += getSumOfPriorities(commonItem);
		System.out.println(totalSumOfPriorities);
	}

	static char getCommonItem(char[] list1, char[] list2, int numElements) {
		HashSet<Character> set_c1 = new HashSet<>();
		HashSet<Character> set_c2 = new HashSet<>();
		for (int i = 0; i < numElements; i++) {
			set_c1.add(list1[i]);
			set_c2.add(list2[i]);
		}
		set_c1.retainAll(set_c2);
		List<Character> commonItems = new ArrayList<Character>(set_c1);
		char commonItem = commonItems.get(0);
		return commonItem;
	}

	static int getSumOfPriorities(char commonItem) {
		int prioritySum = 0;
		int alphabetLowerCaseIndex = alphabetLowerCase.indexOf(commonItem);
		int alphabetUpperCaseIndex = alphabetUpperCase.indexOf(commonItem);

		if (alphabetLowerCaseIndex > -1) {
			prioritySum += alphabetLowerCase.indexOf(commonItem) + 1;
		} else if (alphabetUpperCaseIndex > -1) {
			prioritySum += MAX_CHAR + alphabetUpperCase.indexOf(commonItem) + 1;
		}
		return prioritySum;
	}

	public static Collection<Character> findCommonCharsFor(List<String> strings) {
		if (strings == null || strings.isEmpty()) {
			return Collections.emptyList();
		}
		Set<Character> commonChars = convertStringToSetOfChars(strings.get(0));
		strings.stream().skip(1).forEach(s -> commonChars.retainAll(convertStringToSetOfChars(s)));

		return commonChars;
	}

	private static Set<Character> convertStringToSetOfChars(String string) {
		if (string == null || string.isEmpty()) {
			return Collections.emptySet();
		}
		Set<Character> set = new HashSet<>(string.length() + 10);
		for (char c : string.toCharArray()) {
			set.add(c);
		}
		return set;
	}
}
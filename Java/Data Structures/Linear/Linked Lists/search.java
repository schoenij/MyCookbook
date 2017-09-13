	public static boolean search(Node head, int target) {
		
		Node ptr = head;
		
		while(ptr != null) {
			if(ptr.data == target)
				return true;
			
			ptr = ptr.next;
			
		}
		
		return false;
		
	}

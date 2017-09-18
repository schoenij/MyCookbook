public static Node delete(Node h, int target) {
	
		Node ptr = h;
		Node prev = null;
	
		while(ptr != null) {
			
			if(ptr.data == target) {
				
				if(prev == null) {
					return ptr.next;
				}
				
				prev.next = ptr.next;
				return h;
				
			}
			
			prev = ptr;
			ptr = ptr.next;
			
		}
		
		return h;
		
}

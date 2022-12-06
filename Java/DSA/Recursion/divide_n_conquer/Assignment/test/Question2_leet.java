class Solution {
    public int appendCharacters(String s, String t) {
        int marker = 0;
        for (int i = 0; i < s.length(); i++){
            if (t[marker] == s[i]){
				marker++;
			}
        }
		return t.length() - (marker + 1);
    }
}

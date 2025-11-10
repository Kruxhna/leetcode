from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)

        # If t is empty or longer than s, no valid window can exist
        if not t or len_t > len_s:
            return ""

        # --- Step 1: Create target frequency map for characters in t ---
        # Stores the required counts of characters from t
        target_freq = Counter(t)

        # Number of unique characters in t
        required_unique_chars = len(target_freq)

        # --- Step 2: Initialize sliding window variables ---
        window_freq = {}  # Frequency map for characters in the current window
        formed_unique_chars = 0  # How many unique chars in t are satisfied in window_freq

        # Pointers for the sliding window
        left = 0
        right = 0

        # Variables to store the minimum window length and its start/end indices
        min_len = float('inf')
        min_window_start_idx = 0

        # --- Step 3: Expand the window (right pointer) ---
        while right < len_s:
            char_r = s[right]
            window_freq[char_r] = window_freq.get(char_r, 0) + 1

            # Check if this character helps satisfy a requirement from t
            if char_r in target_freq and window_freq[char_r] == target_freq[char_r]:
                formed_unique_chars += 1

            # --- Step 4: Shrink the window (left pointer) if it's valid ---
            # A window is valid if all required unique characters from t are formed
            while formed_unique_chars == required_unique_chars and left <= right:
                # Update minimum window if current one is smaller
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start_idx = left

                char_l = s[left]

                # If this character was part of the required characters and its count
                # in the window drops below the target, then it means this character
                # is no longer fully satisfied.
                if char_l in target_freq and window_freq[char_l] == target_freq[char_l]:
                    formed_unique_chars -= 1

                # Remove char_l from the window
                window_freq[char_l] -= 1
                if window_freq[char_l] == 0:
                    del window_freq[char_l] # Optional: keep map clean

                # Move left pointer to shrink the window
                left += 1

            # Move right pointer to expand the window
            right += 1

        # --- Step 5: Return the result ---
        # If min_len is still infinity, no valid window was found
        if min_len == float('inf'):
            return ""
        else:
            return s[min_window_start_idx : min_window_start_idx + min_len]